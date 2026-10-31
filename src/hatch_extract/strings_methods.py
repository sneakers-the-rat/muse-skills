"""General methods for extracting string material from the hatch
binary — the reusable machinery behind the topical curations.

Nothing in this module knows about any topic. A topical curation
supplies its own needles, signature tables, region predicates and
output paths. Manifest plumbing (load/save, Registrar, pruning)
lives in hatch_extract.core and is re-exported here so curation
code written against the old binary_string_methods module works
unchanged.

Ported verbatim from scripts/binary_string_methods.py in the
2026-10-31 package restructure.
"""
import json
import re
import subprocess
from pathlib import Path

from .core import (Registrar, already_done, check_binary,
                   finish_manifest, load_manifest,
                   own_entries, prune_owned, save_manifest)

PRINT_RUN = re.compile(rb"[\x09\x0a\x0d\x20-\x7e]{4,}")


# ---- binary structure -------------------------------------------------

def sections(bin_path):
    """readelf section list: [(name, file_offset, size)]."""
    out = subprocess.run(["readelf", "-S", "-W", str(bin_path)],
                         capture_output=True, text=True,
                         check=True).stdout
    secs = []
    for line in out.splitlines():
        m = re.match(r"\s*\[\s*\d+\]\s+(\S+)\s+(\S+)\s+([0-9a-f]+)\s+"
                     r"([0-9a-f]+)\s+([0-9a-f]+)", line)
        if m:
            secs.append((m.group(1), int(m.group(4), 16),
                         int(m.group(5), 16)))
    return secs


def section_span(secs, name):
    """(offset, size) of one section, or None."""
    return next(((o, s) for n, o, s in secs if n == name), None)


# ---- text windows ------------------------------------------------------

def balanced_json(data, start):
    """Brace-match a JSON object starting at data[start] == '{',
    honouring string literals and escapes. Returns end offset or
    None."""
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


def _is_printable_byte(c):
    return c in (9, 10, 13) or 0x20 <= c <= 0x7E


def window_run(data, pos, span=1600):
    """The maximal printable run containing pos, centred-trimmed to
    span bytes. Returns (start_offset, window_bytes)."""
    start = pos
    while start > 0 and _is_printable_byte(data[start - 1]):
        start -= 1
    end = pos
    while end < len(data) and _is_printable_byte(data[end]):
        end += 1
    if end - start > span:
        mid = (start + end) // 2
        start = max(start, mid - span // 2)
        end = min(end, start + span)
    return start, data[start:end]


def anchored_window(data, needles, back=100, span=1500, require=()):
    """Window anchored at a needle occurrence: walk back to the start
    of the printable run containing it, then take span bytes from at
    most `back` bytes before the needle — for registry-style blocks
    whose run is far longer than the window, where centred trimming
    would lose the needle itself. Tries each needle in order and
    each occurrence in order, accepting the first window that
    contains every byte string in require. Returns (start, window)
    or None."""
    for needle in needles:
        for m in re.finditer(re.escape(needle), data):
            rs = m.start()
            while rs > 0 and _is_printable_byte(data[rs - 1]):
                rs -= 1
            start = max(rs, m.start() - back)
            win = data[start:start + span]
            if all(r in win for r in require):
                return start, win
    return None


# ---- the tool catalog ---------------------------------------------------
# Catalog format: consecutive strings — [label][description][schema
# JSON] — back to back, the label abutting the description. Schemas
# are pretty-printed object schemas; brace-match each one and read
# the name off the text gap since the previous schema.

def catalog_schemas(data):
    """Every pretty-printed object schema in the binary:
    [(start, end, parsed_obj)], sorted by start."""
    schemas = []
    for m in re.finditer(rb'\{\n  "type": "object",', data):
        end = balanced_json(data, m.start())
        if end is None:
            continue
        try:
            obj = json.loads(data[m.start():end])
        except ValueError:
            continue
        if obj.get("type") == "object" and "properties" in obj:
            schemas.append((m.start(), end, obj))
    schemas.sort()
    return schemas


def catalog_tool_defs(data, identify, strip_labels=(),
                      label_pattern=None):
    """Split the tool catalog into per-tool definitions.

    identify(obj, blob, desc) -> tool name or None: the curation's
    signature table, consulted when the text gap's label is not
    itself a tool name. strip_labels are label tags that precede the
    real text in the gap (stripped before parsing). label_pattern is
    the curation's regex for a tool name at the start of the gap
    text (one capture group).

    Yields (name_or_None, description, schema_obj, schema_offset).
    """
    prev_end = None
    for s_off, s_end, obj in catalog_schemas(data):
        blob = data[s_off:s_end]
        desc = ""
        label = None
        if prev_end is not None and s_off - prev_end < 30000:
            gap = data[prev_end:s_off].decode("utf-8", "replace")
            desc = gap.strip("\n")
            for tag in strip_labels:
                if desc.startswith(tag):
                    label = tag
                    desc = desc[len(tag):]
            if label_pattern:
                m = re.match(label_pattern, desc)
                if m:
                    label = m.group(1)
                    desc = desc[m.end():]
            desc = desc.strip()
        prev_end = s_end
        name = label if label and "." in label else identify(
            obj, blob, desc)
        yield name, desc, obj, s_off


# ---- regions and lexicons ----------------------------------------------

def manifest_spans(contents, repo, pred):
    """Byte spans of extracted files whose manifest entry satisfies
    pred(entry) — (offset, offset + on-disk size), from the manifest
    offset and the extracted file's size. Sorted."""
    spans = []
    for c in contents:
        if "source" not in c or not pred(c):
            continue
        f = repo / c["target"]
        if not f.exists():
            continue
        spans.append((c["offset"], c["offset"] + f.stat().st_size))
    spans.sort()
    return spans


def in_regions(regions, pos):
    """regions must be sorted (manifest_spans and padded catalog
    spans are)."""
    for a, b in regions:
        if a <= pos < b:
            return True
        if pos < a:
            return False
    return False


def error_lexicon(data, ro_span, regions, pattern,
                  min_len=12, max_len=400):
    """Error-lexicon strings within the given byte regions of
    .rodata: printable runs split into lines, lines whose stripped
    text has a space, is min_len..max_len long and matches pattern.
    Returns {string: offset} with the offset of the STRIPPED string
    (the raw line's offset plus its leading-whitespace width) —
    the recorded offset must byte-match the stored string."""
    seen = {}
    ro_off, ro_size = ro_span
    for m in PRINT_RUN.finditer(data, ro_off, ro_off + ro_size):
        if not in_regions(regions, m.start()):
            continue
        pos = m.start()
        for line in m.group().split(b"\n"):
            line_off = pos
            pos += len(line) + 1
            s = line.strip().decode("utf-8", "replace")
            if not (min_len <= len(s) <= max_len) or " " not in s:
                continue
            if not pattern.search(s):
                continue
            off = line_off + (len(line) - len(line.lstrip()))
            if s not in seen or off < seen[s]:
                seen[s] = off
    return seen


def cst_fragments(data, secs, needle):
    """Occurrences of needle in the constant-string sections
    (.rodata.cst*): lines of 'section\\t0xoffset\\thex-context'.
    Returns (lines, first_offset_or_None)."""
    lines = []
    first = None
    for name, o, s in secs:
        if "cst" not in name:
            continue
        for m in re.finditer(re.escape(needle), data[o:o + s]):
            pos = o + m.start()
            ctx = data[pos:pos + 24].hex()
            lines.append(f"{name}\t0x{pos:x}\t{ctx}")
            if first is None:
                first = pos
    return lines, first


def split_section(blob, heading):
    """The section of a markdown blob starting at heading, up to the
    next same-level heading ('\\n## ') or the end. None if absent."""
    idx = blob.find(heading)
    if idx < 0:
        return None
    end = blob.find(b"\n## ", idx + 1)
    return blob[idx:] if end < 0 else blob[idx:end + 1]


