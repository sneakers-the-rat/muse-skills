"""Mechanism 12 — NUL-terminated strings (reference form e):
FFI-facing C strings are delimited by their terminator, not by a
length. Enumerate every printable run of >= MIN_LEN bytes closed
by a NUL in the given sections, validating UTF-8 like every other
string class. The span excludes the terminator.

Implementation note: the run pattern must NOT carry the \\x00
requirement itself. With the terminator inside the regex, every
unterminated run of L allowed bytes costs O(L^2) backtracking
(the engine retries at every offset of the run) — .rodata holds
megabyte-scale non-string blobs, and that shape took minutes-to-
hours on the live binary. Finding maximal runs is linear; the
terminator is then a one-byte check after each run. The match
set is identical: a NUL-terminated string is exactly a maximal
allowed-class run immediately followed by a NUL.
"""
import re

MIN_LEN = 4
RUN = re.compile(rb"[\x09\x0a\x0d\x20-\x7e\x80-\xff]{%d,}" % MIN_LEN)


def nul_strings(data, spans):
    """spans: [(section_offset, section_size)]. Returns
    [{offset, len, refs, form}] with refs=1 per occurrence."""
    out = []
    for off, size in spans:
        region = bytes(data[off:off + size])
        for m in RUN.finditer(region):
            end = m.end()
            if end >= len(region) or region[end] != 0:
                continue  # not closed by a NUL inside the section
            blob = m.group(0)
            try:
                blob.decode("utf-8")
            except UnicodeDecodeError:
                continue
            out.append({"offset": off + m.start(), "len": len(blob),
                        "refs": 1, "form": "NUL-terminated C string"})
    return out
