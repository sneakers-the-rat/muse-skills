#!/usr/bin/env python3
"""
Extract embedded prompt/skill/tool files from the hatch binary into this
repo, and write binary-map.json describing what came from where.

The binary stores bundle files back-to-back in .rodata as
    <relative/path.ext><content><next path><content>...
with no separators and no NUL terminators. This extractor:
  1. censuses every filename marker (.md/.yaml/.yml/.json/.toml) with
     grep -a -b -o, dropping fused markers (a marker whose preceding byte
     is a path character is the tail of a longer token);
  2. splits fused tokens — two paths stored back-to-back with no content
     between them (an empty file followed by the next path) arrive as one
     grep token; they are split where an extension is immediately
     followed by a plausible next path;
  3. clusters markers by offset proximity and keeps only dense "bundle
     clusters" (>= 20 plausible files) — scattered markers are mentions
     of a path inside other files, not embedded files, and are ignored;
  4. slices each file from just after its marker to the next slash-path
     marker anywhere in .rodata (any slash-path marker is a boundary;
     bare filenames are mentions inside content, never boundaries);
  5. validates the slice (UTF-8 text, no NULs, sane size, does not look
     like a list/index fragment or a mid-sentence mention) — failures
     are reported and skipped, never guessed at; a source with several
     occurrences is tried at each occurrence until one validates;
  6. writes the file at its target path and records
     {source, target, offset} in binary-map.json, where offset is the
     byte offset of the file's content in the binary.

Deterministic for a given binary: same sha256 in, same tree and manifest
out (except the manifest timestamp, which is the extraction time).
Bundle-cluster detection replaces fixed offsets, so a binary roll that
moves the bundles does not silently empty the archive; if the bundles
cannot be found at all, the script fails loudly instead of writing an
empty manifest.

Mapping (user, 2026-10-21):
  browser/          -> browser/            (kept)
  self_improvement/ -> self_improvement/   (kept)
  blocks/           -> system-prompt/
  templates/        -> artifacts/templates/
  artifacts/        -> artifacts/
  tools/            -> binary-tools/
  <challenge slug>/ -> binary-skills/<slug>/        (SKILL.md guides)
  <domain>/         -> browser/site-config/<domain>/ (config.yaml + SKILL.md)
  session/, chat/, devices/, voice/, activity_monitor/, channels/,
  chat-connections/, shopping/
                    -> binary-skills/<root>/  (the real multi-file roots)
  anything else     -> binary-etc/<source>  (unsorted; the snapshot hook
                      holds NEW binary-etc files out of the commit and
                      asks the user to classify them — see sync-skills.sh)
Ignored as example/mention paths inside other files: memory/, config/,
notes/, orders/, user/, dreams/, selection/, update/, studying/.
Fused markers are cleaned by trimming to the first known bundle root
inside the token (the user's heuristic-delimiter rule).
"""
import hashlib
import json
import pathlib
import re
import subprocess
import sys
from datetime import datetime, timezone

REPO = pathlib.Path(__file__).resolve().parent
BIN = pathlib.Path("/opt/hatch/bin/hatch")
PATHCH = set(b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_./-")
EXTS = (".md", ".yaml", ".yml", ".json", ".toml")

KNOWN_ROOTS = {"blocks", "browser", "session", "self_improvement",
               "templates", "tools", "artifacts", "channels", "devices",
               "connections", "memory", "notes", "voice", "docs",
               "references", "assets", "chat-connections", "dreams",
               "orders", "selection", "shopping", "studying", "config",
               "src", "user", "update", "chat", "activity_monitor"}
SLUGS = {"arithmetic-and-counting", "audio-challenge", "automatic-check",
         "block-page", "game-puzzle", "icon-order", "image-click",
         "image-grid", "network-block", "page-load-failure", "path-drawing",
         "press-and-hold", "rotation-puzzle", "sign-in-check",
         "slider-puzzle", "soft-block", "start-gate", "text-captcha",
         "verification-checkbox", "waiting-room"}
DOMAIN = re.compile(r"^[a-z0-9\-]+(\.[a-z0-9\-]+)+$")
SKILL_ROOTS = {"session", "chat", "devices", "voice", "activity_monitor",
               "channels", "chat-connections", "shopping"}
SKIP_ROOTS = {"memory", "config", "notes", "orders", "user", "dreams",
              "selection", "update", "studying"}
MAX_FILE = 1_000_000
CLUSTER_GAP = 0x20000
MIN_CLUSTER_FILES = 20


def clean_path(raw):
    if "/" not in raw:
        return None  # bare filenames are mentions, not bundle files
    parts = raw.split("/")
    # a final component carrying two extensions is two fused names
    # ('a.mdvoice_chat_delegate.md'); the stored entry is the first name
    last = parts[-1]
    for ext in EXTS:
        i = last.find(ext)
        if i != -1 and any(e in last[i + len(ext):] for e in EXTS):
            parts[-1] = last[:i + len(ext)]
            raw = "/".join(parts)
            break
    if parts[0] in KNOWN_ROOTS or parts[0] in SLUGS:
        return raw
    if DOMAIN.match(parts[0]) and len(parts) == 2 and \
            parts[1] in ("SKILL.md", "config.yaml"):
        return raw
    # fused prefix ending in a known root as a suffix of the first
    # component ('are.session/x.md' -> 'session/x.md'): the root name is
    # the delimiter (the user's heuristic)
    for root in sorted(KNOWN_ROOTS, key=len, reverse=True):
        if parts[0].endswith(root) and len(parts[0]) > len(root):
            return "/".join([root] + parts[1:])
    for i in range(1, len(parts) - 1):
        if parts[i] in KNOWN_ROOTS:
            return "/".join(parts[i:])
    return None


def target_for(source):
    top, _, rest = source.partition("/")
    if top == "browser":
        return source
    if top == "self_improvement":
        return source
    if top == "blocks":
        return f"system-prompt/{rest}"
    if top == "templates":
        return f"artifacts/templates/{rest}"
    if top == "artifacts":
        return source
    if top == "tools":
        return f"binary-tools/{rest}"
    if top in SLUGS:
        return f"binary-skills/{source}"
    if DOMAIN.match(top) and source.count("/") == 1 and \
            rest in ("SKILL.md", "config.yaml"):
        return f"browser/site-config/{source}"
    if top in SKILL_ROOTS:
        return f"binary-skills/{source}"
    if top in SKIP_ROOTS:
        return None
    return f"binary-etc/{source}"


def split_token(tok):
    """Split a fused grep token into sub-paths. A split point is an
    extension end immediately followed by a plausible next path start
    (known root, guide slug, or domain component, each followed by '/').
    Returns [(local_start, subpath, is_last)]."""
    out = []
    pos = 0
    while pos < len(tok):
        # earliest extension end at or after pos
        end = None
        for ext in EXTS:
            i = tok.find(ext, pos)
            if i != -1 and (end is None or i + len(ext) < end[0]):
                end = (i + len(ext), ext)
        if end is None:
            out.append((pos, tok[pos:], True))
            break
        e = end[0]
        rest = tok[e:]
        nxt = None
        if rest:
            head = rest.split("/", 1)[0]
            if "/" in rest and (head in KNOWN_ROOTS or head in SLUGS
                                or DOMAIN.match(head)):
                nxt = e
        if nxt is None:
            out.append((pos, tok[pos:], True))
            break
        out.append((pos, tok[pos:e], False))
        pos = e
    return out


def census(data):
    raw = subprocess.run(
        ["grep", "-a", "-b", "-o", "-E",
         r"[A-Za-z0-9_.\-]+(/[A-Za-z0-9_.\-]+)*\.(md|yaml|yml|json|toml)",
         str(BIN)], capture_output=True).stdout.decode(errors="replace")
    marks = []  # (offset, path, content_start, is_last_in_token)
    for line in raw.splitlines():
        off, _, tok = line.partition(":")
        off = int(off)
        if len(tok) > 200 or ".." in tok:
            continue
        if off > 0 and data[off - 1] in PATHCH:
            continue
        for local, sub, is_last in split_token(tok):
            marks.append((off + local, sub, off + len(tok) if is_last
                          else off + local + len(sub), is_last))
    marks.sort()
    return marks


def rodata_range():
    out = subprocess.run(["readelf", "-S", "-W", str(BIN)],
                         capture_output=True).stdout.decode(errors="replace")
    for line in out.splitlines():
        parts = line.split()
        # [Nr] Name Type Address Offset Size ...
        if len(parts) >= 6 and parts[1] == ".rodata":
            try:
                off = int(parts[4], 16)
                size = int(parts[5], 16)
                return off, off + size
            except ValueError:
                pass
    return 0, BIN.stat().st_size


def validate(body, is_last):
    """Return None if the slice looks like a stored file, else a reason."""
    if len(body) == 0:
        return None if not is_last else "empty slice"
    if len(body) > MAX_FILE:
        return f"size {len(body)} rejected"
    if b"\x00" in body:
        return "NUL bytes in slice"
    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError:
        return "slice is not UTF-8"
    if text.startswith('"') or text.startswith("` -"):
        return "list/index fragment, not a file"
    if text[0].islower() and not re.match(r"^[a-z_]+:", text):
        return "starts mid-sentence (a mention, not a file start)"
    return None


def main():
    data = BIN.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    # Provenance is one-way: binary-map.json is a record of where files
    # came from, never a lookup table — its offsets are not read back.
    # Its one functional use is this hash check: if the binary is the
    # one the manifest records, the embedded strings cannot have
    # changed, so extraction is skipped (unless a recorded target file
    # has gone missing from the tree, which forces a fresh run).
    manifest_path = REPO / "binary-map.json"
    if manifest_path.exists():
        try:
            old = json.loads(manifest_path.read_text())
            oldbin = old["bins"][0]
            if oldbin["sha256"] == sha and all(
                    (REPO / c["target"]).exists()
                    for c in oldbin["contents"]):
                print(f"binary unchanged ({sha[:12]}…); extraction skipped")
                return 0
        except (ValueError, KeyError, IndexError, TypeError):
            pass  # a malformed manifest is just re-created below
    marks = census(data)
    r0, r1 = rodata_range()
    rod = [m for m in marks if r0 <= m[0] < r1]
    slash_offsets = sorted(m[0] for m in rod if "/" in m[1])

    # bundle clusters: dense runs of slash-path markers
    clusters = []
    for m in rod:
        if "/" not in m[1]:
            continue
        if clusters and m[0] - clusters[-1][-1][0] <= CLUSTER_GAP:
            clusters[-1].append(m)
        else:
            clusters.append([m])
    bundle = []
    for cl in clusters:
        plausible = {clean_path(p) for _, p, _, _ in cl}
        plausible = {p for p in plausible
                     if p is not None and target_for(p) is not None}
        # A cluster is a bundle if it is dense overall, or if it is a
        # small single-root table (e.g. the activity_monitor fragments):
        # >= 4 plausible files, >= 3 of them under one root, tight span.
        from collections import Counter
        roots = Counter(p.split("/")[0] for p in plausible)
        dense = len(plausible) >= MIN_CLUSTER_FILES
        small_table = (len(plausible) >= 4 and roots and
                       max(roots.values()) >= 3 and
                       cl[-1][0] - cl[0][0] <= 0x100000)
        if dense or small_table:
            bundle.extend(cl)
    if not bundle:
        print("ERROR: no bundle clusters found — binary layout changed; "
              "refusing to write an empty extraction", file=sys.stderr)
        return 1

    # candidates: cleaned source -> [occurrences]
    cands = {}
    for off, raw, cstart, is_last in bundle:
        src = clean_path(raw)
        if src is None or target_for(src) is None:
            continue
        cands.setdefault(src, []).append((off, cstart, is_last))

    def boundary_after(anchor):
        after = [o for o in slash_offsets if o > anchor]
        return after[0] if after else len(data)

    contents = []
    problems = []
    for src in sorted(cands):
        done = False
        for off, cstart, is_last in cands[src]:
            end = cstart if not is_last else boundary_after(off)
            body = data[cstart:end]
            why = validate(body, is_last)
            if why is not None:
                continue
            target = target_for(src)
            dest = REPO / target
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(body)
            contents.append({"source": src, "target": target,
                             "offset": cstart})
            done = True
            break
        if not done:
            problems.append(src)

    # Special case: arithmetic-and-counting has no SKILL.md marker; its
    # guide starts at its '# Arithmetic and counting' heading, inside the
    # guide cluster (the cluster holding the other guide slugs).
    src = "arithmetic-and-counting/SKILL.md"
    if src not in {c["source"] for c in contents}:
        guide = [m for m in bundle if clean_path(m[1]) in
                 {f"{s}/SKILL.md" for s in SLUGS}]
        if guide:
            lo = min(m[0] for m in guide) - CLUSTER_GAP
            hi = max(m[0] for m in guide) + CLUSTER_GAP
            h = data.find(b"# Arithmetic and counting", lo, hi)
            if h != -1:
                body = data[h:boundary_after(h)]
                if validate(body, True) is None:
                    target = target_for(src)
                    dest = REPO / target
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(body)
                    contents.append({"source": src, "target": target,
                                     "offset": h})
    contents.sort(key=lambda c: c["target"])

    # Prune stale outputs: a file under a managed root that this run did
    # not produce is a file the binary no longer embeds (or an artefact
    # of an older extractor layout) — remove it so the archive records
    # the deletion instead of keeping a stale copy forever.
    MANAGED_ROOTS = ["system-prompt", "binary-skills", "binary-tools",
                     "binary-etc", "browser", "self_improvement",
                     "artifacts"]
    keep = {c["target"] for c in contents}
    pruned = 0
    for root in MANAGED_ROOTS:
        base = REPO / root
        if not base.is_dir():
            continue
        for f in sorted(base.rglob("*"), reverse=True):
            rel = f.relative_to(REPO).as_posix()
            if f.is_file() and rel not in keep:
                f.unlink()
                pruned += 1
            elif f.is_dir() and not any(f.iterdir()):
                f.rmdir()
    if pruned:
        print(f"pruned {pruned} stale extracted files")

    manifest = {"bins": [{
        "path": str(BIN),
        "sha256": sha,
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "size": len(data),
        "contents": contents,
    }]}
    (REPO / "binary-map.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"binary {sha[:12]}… size {len(data)}")
    print(f"extracted {len(contents)} files; skipped {len(problems)}")
    for p in problems:
        print(f"  SKIP {p}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
