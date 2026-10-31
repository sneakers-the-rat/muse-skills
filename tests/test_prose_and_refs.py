import struct

from hatch_extract.mechanisms.length_prefixed import length_prefixed
from hatch_extract.mechanisms.nul_strings import nul_strings
from hatch_extract.mechanisms.panic_locations import panic_locations
from hatch_extract.mechanisms.prose_regions import prose_regions
from hatch_extract.mechanisms.static_refs import static_refs


def test_prose_regions_segment_fused_pool():
    pool = (b"short\x00" + b"# Heading\n\n" +
            b"You must always segment the fused pool carefully. " * 6 +
            b"\x00\x00" + b"x" * 200)
    regs = prose_regions(pool, 0, len(pool))
    assert len(regs) == 2
    big = max(regs, key=lambda r: r["end"] - r["offset"])
    assert big["features"]["md_headings"] >= 1
    assert big["prompt_score"] > 0
    assert big["body"].startswith(b"# Heading")


def test_static_refs_dedupes_with_refcount():
    slices = {0x1000: (0x5000, 5, b"hello"),
              0x1010: (0x5000, 5, b"hello"),
              0x1020: (0x6000, 3, b"bye")}
    v2o = lambda v: v - 0x4000
    spans = static_refs(slices, v2o)
    by = {(s["offset"], s["len"]): s["refs"] for s in spans}
    assert by == {(0x1000, 5): 2, (0x2000, 3): 1}


def test_panic_locations_layout():
    # data section: one Location {ptr->0x9000, len, line=42, col=7}
    path = b"src/main.rs"
    data = bytearray(b"\x00" * 64)
    struct.pack_into("<QQII", data, 16, 0x9000, len(path), 42, 7)
    slices = {0x4010: (0x9000, len(path), path)}
    v2o = lambda v: v - 0x4000
    out = panic_locations(bytes(data), slices, v2o)
    assert len(out) == 1
    assert out[0]["offset"] == 0x5000 and out[0]["line"] == 42


def test_panic_locations_rejects_bad_line():
    path = b"src/main.rs"
    data = bytearray(b"\x00" * 64)
    struct.pack_into("<QQII", data, 16, 0x9000, len(path), 0, 7)
    slices = {0x4010: (0x9000, len(path), path)}
    assert panic_locations(bytes(data), slices, lambda v: v - 0x4000) == []


def test_nul_strings():
    blob = b"\x00\x01binary\x00hello world string\x00\xff\xfe bad \x00"
    out = nul_strings(blob, [(0, len(blob))])
    texts = [blob[s["offset"]:s["offset"] + s["len"]] for s in out]
    assert b"hello world string" in texts


def test_length_prefixed():
    s = b"a length prefixed string body"
    blob = b"\xff\xff" + struct.pack("<I", len(s)) + s + b"\x00"
    out = length_prefixed(blob, [(0, len(blob))])
    assert any(o["len"] == len(s) and o["offset"] == 6 for o in out)
