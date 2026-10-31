"""Mechanism 13 — length-prefixed strings (reference form f):
some pools store a string as a u32/u64 little-endian length
immediately followed by the bytes. Anchored on maximal text runs
(the same segmentation as mechanism 7, at a lower threshold): a
run is length-prefixed when the 4 (or 8) bytes before it decode to
exactly its length, or to a shorter length whose span still ends
on a byte boundary (NUL or non-text byte).
"""
import re
import struct

TEXT_RUN = re.compile(rb"[^\x00-\x08\x0b\x0c\x0e-\x1f\x7f]{4,}")


def length_prefixed(data, spans):
    """spans: [(section_offset, section_size)]. Returns
    [{offset, len, refs, form, prefix}]."""
    out = []
    for off, size in spans:
        region = bytes(data[off:off + size])
        for m in TEXT_RUN.finditer(region):
            start = off + m.start()
            run = m.group(0)
            for width, fmt in ((4, "<I"), (8, "<Q")):
                p = start - width
                if p < off:
                    continue
                (val,) = struct.unpack_from(fmt, data, p)
                if val == len(run):
                    out.append({"offset": start, "len": val, "refs": 1,
                                "form": "length-prefixed string",
                                "prefix": f"u{width * 8}"})
                    break
                if 4 <= val < len(run):
                    after = run[val:val + 1]
                    if after in (b"\x00", b""):
                        out.append({"offset": start, "len": val,
                                    "refs": 1,
                                    "form": "length-prefixed string",
                                    "prefix": f"u{width * 8}"})
                        break
    return out
