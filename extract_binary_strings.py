#!/usr/bin/env python3
"""Extract curated binary strings (things with no filename) into
binary-strings/ and register them in binary-map.json.

Sibling of extract_binary_files.py, which handles embedded FILES (a
path marker + content). This script handles the other kind of embedded
text: string material that has no filename of its own —

  binary-strings/tools/<tool>.json     tool definitions from the
                                       binary's tool catalog, split
                                       by tool name
  binary-strings/browser/errors.csv    browser error strings, one row
                                       per string: offset,string
  binary-strings/browser/bot_challenge/  everything else recovered
                                       about the bot_challenge tool:
                                       role registry, enum vocabulary,
                                       the task-tagger classifier,
                                       dispatch-string fragments, and
                                       per-site bot-detection notes
                                       split out of the site guides

These are MANUAL CURATIONS, not an exhaustive dump of the binary's
strings: each file is produced by a stated match (a needle, a pattern,
a section of another extracted file), strings may repeat across files,
and grouping is topical. Every file created is registered in
binary-map.json under the same bin as the file extraction, as a
contents entry whose "match" field (instead of "source") says what
was matched, with the byte offset it was found at. Offsets are
provenance, exactly as in the file manifest.

Hash rule, same as the file extractor: if the binary's SHA-256 differs
from binary-map.json, this script refuses (run extract_binary_files.py
first); if its own entries are already registered and present on disk,
it does nothing.
"""
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
from pathlib import Path

BIN = Path("/opt/hatch/bin/hatch")
REPO = Path(__file__).resolve().parent
ROOT = REPO / "binary-strings"

PRINT_RUN = re.compile(rb"[\x09\x0a\x0d\x20-\x7e]{4,}")
ERROR_RE = re.compile(
    r"(error|fail|unavailable|invalid|not found|denied|refus|unable|"
    r"could not|cannot|missing|expired|blocked|no guide|not loaded)",
    re.I)


def sections():
    out = subprocess.run(["readelf", "-S", "-W", str(BIN)],
                         capture_output=True, text=True, check=True).stdout
    secs = []
    for line in out.splitlines():
        m = re.match(r"\s*\[\s*\d+\]\s+(\S+)\s+(\S+)\s+([0-9a-f]+)\s+"
                     r"([0-9a-f]+)\s+([0-9a-f]+)", line)
        if m:
            secs.append((m.group(1), int(m.group(4), 16),
                         int(m.group(5), 16)))
    return secs


def balanced_json(data, start):
    """Brace-match a JSON object starting at data[start] == '{',
    honouring string literals and escapes. Returns end offset or None."""
    depth = 0
    i = start
    in_str = False
    esc = False
    while i < len(data) and i < start + 300_000:
        c = data[i]
        if in_str:
            if esc:
                esc = False
            elif c == 0x5C:
                esc = True
            elif c == 0x22:
                in_str = False
        else:
            if c == 0x22:
                in_str = True
            elif c == 0x7B:
                depth += 1
            elif c == 0x7D:
                depth -= 1
                if depth == 0:
                    return i + 1
        i += 1
    return None


def window_run(data, pos, span=1600):
    """The maximal printable run containing pos, centred-trimmed."""
    start = pos
    while start > 0 and (data[start - 1] in (9, 10, 13)
                         or 0x20 <= data[start - 1] <= 0x7E):
        start -= 1
    end = pos
    while end < len(data) and (data[end] in (9, 10, 13)
                               or 0x20 <= data[end] <= 0x7E):
        end += 1
    if end - start > span:
        mid = (start + end) // 2
        start = max(start, mid - span // 2)
        end = min(end, start + span)
    return start, data[start:end]


def main():
    data = BIN.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    manifest_path = REPO / "binary-map.json"
    if not manifest_path.exists():
        print("binary-map.json missing; run extract_binary_files.py first",
              file=sys.stderr)
        return 1
    manifest = json.loads(manifest_path.read_text())
    binrec = manifest["bins"][0]
    if binrec["sha256"] != sha:
        print("binary differs from binary-map.json; run "
              "extract_binary_files.py first", file=sys.stderr)
        return 1
    old_entries = [c for c in binrec["contents"] if "match" in c]
    if old_entries and all((REPO / c["target"]).exists()
                            for c in old_entries):
        print(f"binary unchanged ({sha[:12]}…); strings extraction skipped")
        return 0

    secs = sections()
    ro = next((o, s) for n, o, s in secs if n == ".rodata")
    entries = []          # manifest contents entries for created files
    produced = set()      # repo-relative targets created this run

    def register(match, target, offset):
        entries.append({"match": match, "target": target,
                        "offset": offset})
        produced.add(target)

    def write(target, blob):
        p = REPO / target
        p.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(blob, str):
            blob = blob.encode()
        p.write_bytes(blob)

    # ---- tool definitions, split by tool name -------------------------
    tool_hits = {}
    for m in re.finditer(rb'"name":\s*"((?:browser|bot_challenge)'
                         rb'\.[a-z0-9_.]+)"', data):
        tool_hits.setdefault(m.group(1).decode(), []).append(m.start())
    tools_done = 0
    catalog_offsets = []
    for name, offs in sorted(tool_hits.items()):
        blob = None
        obj_off = None
        for off in offs:
            brace = data.rfind(b"{", off - 16, off)
            if brace < 0:
                continue
            end = balanced_json(data, brace)
            if end is None:
                continue
            try:
                json.loads(data[brace:end])
            except ValueError:
                continue
            blob = data[brace:end]
            obj_off = brace
            break
        if blob is not None:
            target = f"binary-strings/tools/{name}.json"
            write(target, blob)
            register(f'tool definition "name":"{name}"', target, obj_off)
            catalog_offsets.append(obj_off)
            tools_done += 1
        else:
            off = offs[0]
            start, win = window_run(data, off, 2400)
            target = f"binary-strings/tools/{name}.txt"
            write(target, win)
            register(f'tool definition window for "name":"{name}"',
                     target, start)
            catalog_offsets.append(off)
            tools_done += 1

    # ---- browser error strings ----------------------------------------
    # Regions: every extracted browser/ file's span, the challenge
    # guides' spans, and the tool-catalog region around the tool defs.
    regions = []
    for c in binrec["contents"]:
        if "source" not in c:
            continue
        f = REPO / c["target"]
        if not f.exists():
            continue
        size = f.stat().st_size
        if c["target"].startswith("browser/") or (
                c["target"].startswith("binary-skills/")
                and "/" in c["source"]
                and c["source"].split("/")[0] in GUIDE_SLUGS):
            regions.append((c["offset"], c["offset"] + size))
    if catalog_offsets:
        regions.append((min(catalog_offsets) - 0x2000,
                        max(catalog_offsets) + 0x8000))
    regions.sort()

    def in_regions(pos):
        for a, b in regions:
            if a <= pos < b:
                return True
            if pos < a:
                return False
        return False

    seen = {}
    for m in PRINT_RUN.finditer(data, ro[0], ro[0] + ro[1]):
        if not in_regions(m.start()):
            continue
        for line in m.group().split(b"\n"):
            s = line.strip().decode("utf-8", "replace")
            if not (12 <= len(s) <= 400) or " " not in s:
                continue
            if not ERROR_RE.search(s):
                continue
            off = m.start() + m.group().find(line)
            if s not in seen or off < seen[s]:
                seen[s] = off
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["offset", "string"])
    for s, off in sorted(seen.items(), key=lambda kv: kv[1]):
        w.writerow([off, s])
    write("binary-strings/browser/errors.csv", buf.getvalue())
    first_off = min(seen.values()) if seen else ro[0]
    register("error-lexicon strings within browser/guide/catalog regions",
             "binary-strings/browser/errors.csv", first_off)

    # ---- bot_challenge curations ---------------------------------------
    bc = "binary-strings/browser/bot_challenge"

    # role registry window
    best = None
    for m in re.finditer(rb'"browser_bot_challenge"', data):
        start, win = window_run(data, m.start(), 1800)
        if b'"tools"' in win or b"tools" in win:
            best = (start, win)
            break
    if best:
        write(f"{bc}/roles.txt", best[1])
        register('role registry entry "browser_bot_challenge"',
                 f"{bc}/roles.txt", best[0])

    # enum / telemetry vocabulary windows
    parts = []
    first = None
    for needle in [b"BrowserFailureClass", b"BrowserBlockClass",
                   b"BrowserSpecialistEnding", b"BrowserHandoffOutcome",
                   b"captcha_reference_invalid"]:
        m = re.search(re.escape(needle), data)
        if not m:
            continue
        start, win = window_run(data, m.start(), 700)
        parts.append(b"# " + needle + b"\n" + win)
        if first is None:
            first = start
    if parts:
        write(f"{bc}/enums.txt", b"\n\n".join(parts))
        register("Browser* enum/telemetry vocabulary windows",
                 f"{bc}/enums.txt", first)

    # Browser Task Tagger classifier prompt
    for m in re.finditer(rb"Task Tagger", data):
        start, win = window_run(data, m.start(), 3200)
        if b"captcha" in win and (b"challenge_loop" in win
                                  or b"hard_bot_block" in win):
            write(f"{bc}/classifier.txt", win)
            register("Browser Task Tagger classifier prompt",
                     f"{bc}/classifier.txt", start)
            break

    # dispatch-string fragments outside the main .rodata pool
    frag_lines = []
    first = None
    for name, o, s in secs:
        if "cst" not in name:
            continue
        for m in re.finditer(rb"bot_challenge", data[o:o + s]):
            pos = o + m.start()
            ctx = data[pos:pos + 24].hex()
            frag_lines.append(f"{name}\t0x{pos:x}\t{ctx}")
            if first is None:
                first = pos
    if frag_lines:
        write(f"{bc}/dispatch-fragments.txt",
              "\n".join(frag_lines) + "\n")
        register("bot_challenge fragments in constant-string sections",
                 f"{bc}/dispatch-fragments.txt", first)

    # per-site bot-detection notes, split out of the site guides
    sites = 0
    for c in binrec["contents"]:
        if "source" not in c:
            continue
        t = c["target"]
        if not (t.startswith("browser/site-config/")
                and t.endswith("/SKILL.md")):
            continue
        f = REPO / t
        if not f.exists():
            continue
        blob = f.read_bytes()
        idx = blob.find(b"## Bot detection")
        if idx < 0:
            continue
        end = blob.find(b"\n## ", idx + 1)
        section = blob[idx:] if end < 0 else blob[idx:end + 1]
        if len(section) < 40:
            continue
        domain = t.split("/")[2]
        target = f"{bc}/sites/{domain}.md"
        write(target, section)
        register(f"'## Bot detection' section of {c['source']}",
                 target, c["offset"] + idx)
        sites += 1

    # ---- prune stale curations, update the manifest --------------------
    for f in sorted(ROOT.rglob("*"), reverse=True) if ROOT.exists() else []:
        rel = f.relative_to(REPO).as_posix()
        if f.is_file() and rel not in produced:
            f.unlink()
        elif f.is_dir() and not any(f.iterdir()):
            f.rmdir()
    keep = [c for c in binrec["contents"] if "source" in c]
    binrec["contents"] = sorted(keep + entries,
                                 key=lambda c: c["target"])
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"tools: {tools_done}; error strings: {len(seen)}; "
          f"site notes: {sites}; curation files: {len(entries)}")
    return 0


GUIDE_SLUGS = {
    "arithmetic-and-counting", "audio-challenge", "automatic-check",
    "block-page", "game-puzzle", "icon-order", "image-click",
    "image-grid", "network-block", "page-load-failure", "path-drawing",
    "press-and-hold", "rotation-puzzle", "sign-in-check",
    "slider-puzzle", "soft-block", "start-gate", "text-captcha",
    "verification-checkbox", "waiting-room",
}

if __name__ == "__main__":
    sys.exit(main())
