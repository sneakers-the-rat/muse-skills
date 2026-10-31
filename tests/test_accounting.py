"""Byte-accounting equivalence: the fast implementation (one
merge per kind + bisect windows) must produce byte-identical
results to the original naive algorithm (re-sort every span set
per section), which is kept here as the reference."""
import random

from hatch_extract import accounting as A


def _ref_account_section(data, name, off, size, span_sets):
    lo, hi = off, off + size
    per_kind = {}
    all_spans = []
    for kind, spans in span_sets.items():
        per_kind[kind] = A.union_len(spans, lo, hi)
        all_spans.extend(spans)
    covered = A.merge([(max(s, lo), min(e, hi)) for s, e in all_spans
                       if e > lo and s < hi])
    covered_bytes = sum(e - s for s, e in covered)
    residuals = []
    cur = lo
    for s, e in covered:
        if s > cur:
            residuals.append((cur, s))
        cur = max(cur, e)
    if cur < hi:
        residuals.append((cur, hi))
    classes = {}
    largest = []
    for s, e in residuals:
        cls = A._classify(data, s, e)
        c = classes.setdefault(cls, {"ranges": 0, "bytes": 0})
        c["ranges"] += 1
        c["bytes"] += e - s
        largest.append((e - s, s, e, cls))
    largest.sort(reverse=True)
    return {
        "section": name, "offset": off, "size": size,
        "covered_bytes": covered_bytes,
        "covered_fraction": round(covered_bytes / size, 4) if size else 0,
        "per_kind_covered_bytes": per_kind,
        "residual_bytes": size - covered_bytes,
        "residual_classes": classes,
        "largest_residual_ranges": [
            {"offset": s, "end": e, "len": e - s, "class": cls,
             "first_bytes_hex": bytes(data[s:s + 16]).hex()}
            for _ln, s, e, cls in largest[:25]],
    }


def test_accounting_matches_reference():
    rng = random.Random(20261031)
    data = bytearray(rng.randrange(0, 4) for _ in range(4000))
    for i in range(0, 4000, 97):  # text runs and zero runs
        data[i:i + 20] = b"hello world string"
    for i in range(50, 4000, 613):
        data[i:i + 30] = b"\x00" * 30
    data = bytes(data)

    def spans(n, lo, hi):
        out = []
        for _ in range(n):
            s = rng.randrange(lo, hi)
            out.append((s, s + rng.randrange(0, 200)))
        return out

    span_sets = {
        "files": spans(60, 0, 4000),
        "static": spans(80, 0, 4000),
        "nul": spans(40, 3000, 4000) + spans(10, 0, 100),
        "empty": [],
    }
    sections = [(".rodata", 0, 2000), (".data", 2000, 2000),
                (".empty", 4000, 0), (".tail", 3900, 100)]
    got = A.build_accounting(data, sections, span_sets)
    want_secs = [_ref_account_section(data, n, o, s, span_sets)
                 for n, o, s in sections if s > 0]
    assert got["sections"] == want_secs
    assert got["totals"]["section_bytes"] == 4100
    assert got["totals"]["covered_bytes"] == \
        sum(s["covered_bytes"] for s in want_secs)


def test_account_section_single_matches_reference():
    data = b"\x00" * 10 + b"abcdefghij" * 10 + b"\x00" * 10
    span_sets = {"k": [(12, 30), (25, 40), (200, 300)]}
    got = A.account_section(data, ".x", 0, len(data), span_sets)
    want = _ref_account_section(data, ".x", 0, len(data), span_sets)
    assert got == want
