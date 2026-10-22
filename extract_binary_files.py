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
  2. keeps markers inside the known bundle spans whose cleaned path maps
     to a repo target (mapping below);
  3. slices each file's content from just after its marker to the next
     marker in the same span (ANY marker is a boundary — a neighbour file
     with no heading must still terminate the slice);
  4. validates the slice (UTF-8 text, no NULs, sane size) — failures are
     reported and skipped, never guessed at;
  5. writes the file at its target path and records
     {source, target, offset} in binary-map.json, where offset is the
     byte offset of the file's content in the binary.

Deterministic for a given binary: same sha256 in, same tree and manifest
out (except the manifest timestamp, which is the extraction time).

Mapping (user, 2026-10-21):
  browser/          -> browser/            (kept)
  self_improvement/ -> self_improvement/   (kept)
  blocks/           -> system-prompt/
  templates/        -> artifacts/templates/
  artifacts/        -> artifacts/
  assets/           -> artifacts/assets/
  tools/            -> binary-tools/
  <challenge slug>/ -> binary-skills/<slug>/        (SKILL.md guides)
  <domain>/         -> browser/site-config/<domain>/ (config.yaml + SKILL.md)
  session/, chat/, devices/, voice/, activity_monitor/, channels/,
  chat-connections/, connections/, shopping/, references/, src/
                    -> kept under their own names (no ruling yet)
Skipped as fixtures/mentions rather than bundle files: memory/, config/,
notes/, orders/, user/, dreams/, selection/, update/, studying/ —
example or test-fixture paths named inside other files. Fused markers are
cleaned by trimming to the first known bundle root inside the token
(the user's heuristic-delimiter rule).
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

SPANS = [(0x4778000, 0x4B10000), (0x4B50000, 0x4B80000), (0x58C0000, 0x59B0000)]
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
KEEP_ROOTS = {"session", "chat", "devices", "voice", "activity_monitor",
              "channels", "chat-connections", "connections", "shopping",
              "references", "src"}
SKIP_ROOTS = {"memory", "config", "notes", "orders", "user", "dreams",
              "selection", "update", "studying"}
MAX_FILE = 1_000_000


def clean_path(raw):
    if "/" not in raw:
        return None  # bare filenames: a docs bundle uses them (~0x48fxxxx),
        # but it has no ruling yet; fused single tokens land here too
    parts = raw.split("/")
    if parts[0] in KNOWN_ROOTS or parts[0] in SLUGS or DOMAIN.match(parts[0]):
        return raw
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
    if top == "assets":
        return f"artifacts/assets/{rest}"
    if top == "tools":
        return f"binary-tools/{rest}"
    if top in SLUGS:
        return f"binary-skills/{source}"
    if DOMAIN.match(top) and source.count("/") == 1 and \
            rest in ("SKILL.md", "config.yaml"):
        return f"browser/site-config/{source}"
    if top in KEEP_ROOTS:
        return source
    return None  # SKIP_ROOTS and anything unmapped


def census(data):
    raw = subprocess.run(
        ["grep", "-a", "-b", "-o", "-E",
         r"[A-Za-z0-9_.\-]+(/[A-Za-z0-9_.\-]+)*\.(md|yaml|yml|json|toml)",
         str(BIN)], capture_output=True).stdout.decode(errors="replace")
    marks = []
    for line in raw.splitlines():
        off, _, path = line.partition(":")
        off = int(off)
        if len(path) > 120 or ".." in path:
            continue
        if off > 0 and data[off - 1] in PATHCH:
            continue
        marks.append((off, path))
    marks.sort()
    return marks


def in_span(off):
    return any(a <= off < b for a, b in SPANS)


def main():
    data = BIN.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    marks = census(data)
    span_marks = [(o, p) for o, p in marks if in_span(o)]

    # candidate set: cleaned source -> (marker_offset, raw_path)
    cands = {}
    for off, raw in span_marks:
        src = clean_path(raw)
        if src is None or target_for(src) is None:
            continue
        cands.setdefault(src, (off, raw))  # first copy wins (bundle A)
    # Special case: arithmetic-and-counting has no SKILL.md marker; its
    # guide starts at its '# Arithmetic and counting' heading.
    heading = data.find(b"# Arithmetic and counting", 0x4B50000, 0x4B60000)
    special = {}
    if heading != -1:
        special["arithmetic-and-counting/SKILL.md"] = heading

    # Boundaries are the next marker ANYWHERE in the binary, not just in
    # the bundle spans: the next stored file after a bundle file may be a
    # reference-shaped marker, and span-only boundaries over-slice into
    # whatever data follows the bundle.
    all_offsets = sorted(o for o, _ in marks)
    contents = []
    problems = []
    written = {}
    for src in sorted(set(cands) | set(special)):
        if src in special and src not in cands:
            start = special[src]
        else:
            off, raw = cands[src]
            start = off + len(raw)
        # boundary: the first marker strictly after this file's marker
        anchor = start if src in special else cands[src][0]
        after = [o for o in all_offsets if o > anchor]
        end = after[0] if after else len(data)
        body = data[start:end]
        if not (0 < len(body) <= MAX_FILE):
            problems.append(f"{src}: size {len(body)} rejected")
            continue
        if b"\x00" in body:
            problems.append(f"{src}: NUL bytes in slice, skipped")
            continue
        try:
            body.decode("utf-8")
        except UnicodeDecodeError:
            problems.append(f"{src}: slice is not UTF-8, skipped")
            continue
        target = target_for(src)
        dest = REPO / target
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists() and dest.read_bytes() != body:
            pass  # a changed file is the normal case across snapshots
        dest.write_bytes(body)
        written[src] = body
        contents.append({"source": src, "target": target, "offset": start})
    contents.sort(key=lambda c: c["target"])

    manifest = {"bins": [{
        "path": str(BIN),
        "sha256": sha,
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "size": len(data),
        "contents": contents,
    }]}
    (REPO / "binary-map.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"binary {sha[:12]}… size {len(data)}")
    print(f"extracted {len(contents)} files; problems: {len(problems)}")
    for p in problems:
        print(f"  SKIP {p}", file=sys.stderr)


if __name__ == "__main__":
    main()
