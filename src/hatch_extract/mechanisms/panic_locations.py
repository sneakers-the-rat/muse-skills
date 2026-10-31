"""Mechanism 11 — panic-location records (reference form d):
core::panic::Location statics are fixed-layout structs
{file: (ptr, len), line: u32, col: u32}. The file field is a fat
pointer like any other, so it appears in the relocation slice
census; a slice is a Location's file string when the two u32s
stored immediately after its (ptr, len) pair in the data section
are sane line/column numbers and the string is a source-path
shape. The span is the file-path string; the record also proves
which source files the binary's code panics from.
"""
import re
import struct
from collections import Counter

PATH_SHAPE = re.compile(rb"^[a-z0-9_][a-z0-9_./-]*$")


def panic_locations(data, slices, v2o):
    """Returns [{offset, len, refs, form, line, col}] — one entry
    per distinct file string, refs = number of Location records
    naming it, line/col from the first record seen."""
    counts = Counter()
    first = {}
    for slot, (target, length, content) in slices.items():
        if not PATH_SHAPE.match(content):
            continue
        if b"/" not in content and not content.endswith(b".rs"):
            continue
        fo = v2o(slot)
        if fo is None or fo + 24 > len(data):
            continue
        line, col = struct.unpack_from("<II", data, fo + 16)
        if not (1 <= line <= 2_000_000 and col <= 100_000):
            continue
        off = v2o(target)
        if off is None:
            continue
        key = (off, length)
        counts[key] += 1
        first.setdefault(key, (line, col))
    out = []
    for (off, length), n in sorted(counts.items()):
        line, col = first[(off, length)]
        out.append({"offset": off, "len": length, "refs": n,
                    "form": "panic Location file string",
                    "line": line, "col": col})
    return out
