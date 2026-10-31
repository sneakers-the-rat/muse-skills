"""Mechanism 12 equivalence + performance: the linear maximal-run
implementation must match the original terminator-anchored regex
on every input, and must not blow up on megabyte-scale
unterminated runs (the original's O(L^2) backtracking shape)."""
import re
import time

from hatch_extract.mechanisms.nul_strings import MIN_LEN, nul_strings

OLD = re.compile(rb"[\x09\x0a\x0d\x20-\x7e\x80-\xff]{%d,}\x00" % MIN_LEN)


def _ref(data, spans):
    out = []
    for off, size in spans:
        region = bytes(data[off:off + size])
        for m in OLD.finditer(region):
            blob = m.group(0)[:-1]
            try:
                blob.decode("utf-8")
            except UnicodeDecodeError:
                continue
            out.append({"offset": off + m.start(), "len": len(blob),
                        "refs": 1, "form": "NUL-terminated C string"})
    return out


def test_nul_strings_matches_reference():
    blob = (b"hello\x00short\x00"
            b"\xff\xfe\xfdnot utf8\x00"          # invalid UTF-8 run
            b"ab\x01cdef\x00"                    # run split by \x01
            b"xy\x00"                            # below MIN_LEN
            b"long enough string here\x00"
            b"unterminated tail no nul at all")
    got = nul_strings(blob, [(0, len(blob))])
    want = _ref(blob, [(0, len(blob))])
    assert got == want
    texts = {(g["offset"], g["len"]) for g in got}
    assert any(blob[o:o + ln] == b"hello" for o, ln in texts)
    assert any(blob[o:o + ln] == b"cdef" for o, ln in texts)
    assert any(blob[o:o + ln] == b"long enough string here"
               for o, ln in texts)


def test_nul_strings_no_blowup_on_unterminated_blob():
    # 2 MB of class bytes with no terminator anywhere: the old
    # regex burned O(L^2) here. The whole thing is also ONE
    # maximal run, so a trailing word inside it is not a separate
    # string — both implementations agree it yields nothing.
    blob = b"\x80" * 2_000_000 + b"tail"
    t0 = time.time()
    got = nul_strings(blob, [(0, len(blob))])
    assert time.time() - t0 < 10
    assert got == []
    # and a long genuinely-terminated string still lands whole
    blob2 = b"A" * 100_000 + b"\x00"
    assert nul_strings(blob2, [(0, len(blob2))]) == [
        {"offset": 0, "len": 100_000, "refs": 1,
         "form": "NUL-terminated C string"}]
