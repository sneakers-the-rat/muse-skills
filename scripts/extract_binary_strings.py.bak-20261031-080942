#!/usr/bin/env python3
"""The bot_challenge TOPICAL curation of binary strings.

This script is one topic's curation, not a general extractor. All
the general machinery lives in binary_string_methods.py; this file
holds only what is specific to the bot_challenge topic — its
needles, its tool-signature table, its region choices, its output
paths — and calls the general methods with them. To investigate a
new topic, write a sibling curation the same way, with its own
TOPIC name.

What this curation produces, under binary-strings/:

  tools/<tool>.json        the bot_challenge and browser tool
                           definitions from the binary's tool
                           catalog, split by tool name
  browser/errors.csv       browser error strings, one offset,string
                           row per string, from the browser/guide/
                           catalog regions
  browser/bot_challenge/   everything else recovered about the
                           bot_challenge machinery: the specialist
                           role registry, the Browser* enum
                           vocabulary, the Browser Task Tagger
                           classifier prompt, dispatch-string
                           fragments from the constant sections,
                           and per-site bot-detection notes split
                           out of the site guides

These are MANUAL CURATIONS, not an exhaustive dump of the binary's
strings: each file is produced by a stated match (a needle, a
pattern, a section of another extracted file), strings may repeat
across files, and grouping is topical.

Every file created is registered in binary-map.json under the same
bin as the file extraction, as a contents entry whose "match" field
(instead of "source") says what was matched, with the byte offset it
was found at — and whose "topic" field names this curation,
"bot_challenge". That is how the manifest tells topical curations
apart from extract_binary_files.py's generic, exhaustive entries.
Offsets are provenance, exactly as in the file manifest.

Hash rule, same as the file extractor: if the binary's SHA-256
differs from binary-map.json, this script refuses (run
extract_binary_files.py first); if this topic's entries are already
registered and present on disk, it does nothing.
"""
import csv
import hashlib
import io
import json
import re
import sys
from pathlib import Path

import binary_string_methods as M

BIN = Path("/opt/hatch/bin/hatch")
REPO = Path(__file__).resolve().parent.parent
ROOT = REPO / "binary-strings"
TOPIC = "bot_challenge"
BC = "binary-strings/browser/bot_challenge"

ERROR_RE = re.compile(
    r"(error|fail|unavailable|invalid|not found|denied|refus|unable|"
    r"could not|missing|expired|blocked|no guide|not loaded)",
    re.I)

GUIDE_SLUGS = {
    "arithmetic-and-counting", "audio-challenge", "automatic-check",
    "block-page", "game-puzzle", "icon-order", "image-click",
    "image-grid", "network-block", "page-load-failure", "path-drawing",
    "press-and-hold", "rotation-puzzle", "sign-in-check",
    "slider-puzzle", "soft-block", "start-gate", "text-captcha",
    "verification-checkbox", "waiting-room",
}


def identify(obj, blob, desc):
    """This topic's signature table for catalog entries whose gap
    label is not the tool's name: property names and enum values are
    distinctive."""
    props = set(obj.get("properties", {}).keys())
    if props == {"guide"}:
        return "bot_challenge.guide"
    if props == {"tab", "instruction"}:
        return "browser.bot_challenge"
    if b"reload_page" in blob:
        return "bot_challenge.recover"
    if b"environment_error" in blob:
        return "bot_challenge.assess"
    if desc.startswith("Read the current page in a tab"):
        return "browser.observe"
    if desc.startswith("Perform a short sequence of actions"):
        return "browser.act"
    if desc.startswith("Upload granted files"):
        return "browser.files"
    return None


def main():
    data = BIN.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    manifest = M.load_manifest(REPO)
    if manifest is None:
        print("binary-map.json missing; run extract_binary_files.py "
              "first", file=sys.stderr)
        return 1
    binrec = manifest["bins"][0]
    if not M.check_binary(binrec, sha):
        print("binary differs from binary-map.json; run "
              "extract_binary_files.py first", file=sys.stderr)
        return 1
    if M.already_done(binrec, REPO, TOPIC):
        print(f"binary unchanged ({sha[:12]}…); {TOPIC} curation "
              "skipped")
        return 0

    secs = M.sections(BIN)
    ro = M.section_span(secs, ".rodata")
    reg = M.Registrar(REPO, TOPIC)

    # ---- tool definitions, split by tool name ----------------------
    tools_done = 0
    catalog_offsets = []
    for name, desc, obj, s_off in M.catalog_tool_defs(
            data, identify,
            strip_labels=("checked-in browser tool schema",),
            label_pattern=r"((?:browser|bot_challenge)\.[a-z_]+)"):
        if name:
            fname = name
            match = f'tool definition strings for "{name}"'
        else:
            fname = f"unidentified-{s_off:x}"
            match = f"tool definition strings at 0x{s_off:x} " \
                    "(unidentified)"
        target = f"binary-strings/tools/{fname}.json"
        doc = {"name": name, "description": desc, "input_schema": obj}
        reg.write_and_register(match, target, s_off,
                               json.dumps(doc, indent=2) + "\n")
        catalog_offsets.append(s_off)
        tools_done += 1

    # ---- browser error strings --------------------------------------
    # Regions: every extracted browser/ file's span, the challenge
    # guides' spans, and the tool-catalog region around the tool defs.
    def region_pred(c):
        return c["target"].startswith("binary-strings/browser/") or (
            c["target"].startswith("binary-skills/")
            and c["source"].split("/")[0] in GUIDE_SLUGS)

    regions = M.manifest_spans(binrec["contents"], REPO, region_pred)
    if catalog_offsets:
        regions.append((min(catalog_offsets) - 0x2000,
                        max(catalog_offsets) + 0x8000))
        regions.sort()
    seen = M.error_lexicon(data, ro, regions, ERROR_RE)
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["offset", "string"])
    for s, off in sorted(seen.items(), key=lambda kv: kv[1]):
        w.writerow([off, s])
    first_off = min(seen.values()) if seen else ro[0]
    reg.write_and_register(
        "error-lexicon strings within browser/guide/catalog regions",
        "binary-strings/browser/errors.csv", first_off, buf.getvalue())

    # ---- the specialist role registry --------------------------------
    best = M.anchored_window(
        data, [b'id = "browser_bot_challenge"',
               b'"browser_bot_challenge"'],
        back=100, span=1500, require=(b"tools",))
    if best:
        reg.write_and_register('role registry entry '
                               '"browser_bot_challenge"',
                               f"{BC}/roles.txt", best[0], best[1])

    # ---- enum / telemetry vocabulary windows --------------------------
    parts = []
    first = None
    for needle in [b"BrowserFailureClass", b"BrowserBlockClass",
                   b"BrowserSpecialistEnding", b"BrowserHandoffOutcome",
                   b"captcha_reference_invalid"]:
        i = data.find(needle)
        if i < 0:
            continue
        start, win = M.window_run(data, i, 700)
        parts.append(b"# " + needle + b"\n" + win)
        if first is None:
            first = start
    if parts:
        reg.write_and_register("Browser* enum/telemetry vocabulary "
                               "windows", f"{BC}/enums.txt", first,
                               b"\n\n".join(parts))

    # ---- Browser Task Tagger classifier prompt ------------------------
    # Not a delimited string in the binary: the prompt's prose sits in
    # a densely packed literal cluster (schema field names and the
    # input format template fused at its head, worked examples at its
    # tail), no (ptr,len) slice covers it, and code LEAs target its
    # pieces individually. So the honest extract is the WHOLE cluster
    # (span far above its ~4.7 KB), not a centred cut of it — an
    # earlier 3,200-byte window silently truncated the prompt at
    # both ends.
    for m in re.finditer(rb"Task Tagger", data):
        start, win = M.window_run(data, m.start(), 16384)
        if b"captcha" in win and (b"challenge_loop" in win
                                  or b"hard_bot_block" in win):
            reg.write_and_register(
                "Browser Task Tagger classifier prompt (full "
                "literal-cluster window extract; the prompt is not "
                "a delimited string in the binary)",
                f"{BC}/classifier.txt", start, win)
            break

    # ---- dispatch-string fragments outside the main .rodata pool ------
    frag_lines, first = M.cst_fragments(data, secs, b"bot_challenge")
    if frag_lines:
        reg.write_and_register(
            "bot_challenge fragments in constant-string sections",
            f"{BC}/dispatch-fragments.txt", first,
            "\n".join(frag_lines) + "\n")

    # ---- per-site bot-detection notes, split out of the site guides ---
    sites = 0
    for c in binrec["contents"]:
        if "source" not in c:
            continue
        t = c["target"]
        if not (t.startswith("binary-strings/browser/site-config/")
                and t.endswith("/SKILL.md")):
            continue
        f = REPO / t
        if not f.exists():
            continue
        blob = f.read_bytes()
        section = M.split_section(blob, b"## Bot detection")
        if section is None or len(section) < 40:
            continue
        idx = blob.find(b"## Bot detection")
        domain = t.split("/")[3]
        target = f"{BC}/sites/{domain}.md"
        reg.write_and_register(
            f"'## Bot detection' section of {c['source']}",
            target, c["offset"] + idx, section)
        sites += 1

    # ---- prune this curation's stale outputs, update the manifest ---
    owned = []
    bc_dir = ROOT / "browser" / "bot_challenge"
    if bc_dir.exists():
        owned += [p for p in bc_dir.rglob("*") if p.is_file()]
    owned.append(ROOT / "browser" / "errors.csv")
    owned += list((ROOT / "tools").glob("*.json"))
    M.prune_owned(REPO, owned, reg.produced)
    M.finish_manifest(manifest, binrec, TOPIC, reg.entries)
    M.save_manifest(REPO, manifest)
    print(f"tools: {tools_done}; error strings: {len(seen)}; "
          f"site notes: {sites}; curation files: {len(reg.entries)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
