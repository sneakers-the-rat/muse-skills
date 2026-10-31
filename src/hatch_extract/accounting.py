"""Byte accounting: for every section of the binary, how many of
its bytes are (i) inside at least one extracted/referred string
span, (ii) inside a prose region, (iii) in a residual range —
classified by what the residual bytes are. The accounting is the
coverage ledger: it is registered in binary-map.json like every
other artifact, and the manifest's bin record points at it.

Performance note: span sets run to ~10^6 spans. Each kind's union
is merged ONCE per build_accounting call and each section's
overlap is found by bisect over the merged union — never re-sort
a span set per section (the first version did, and a full run
took hours under load instead of minutes).
"""
import bisect
import re

TEXT_RUN8 = re.compile(rb"[^\x00-\x08\x0b\x0c\x0e-\x1f\x7f]{8,}")


def merge(spans):
    out = []
    for s, e in sorted(spans):
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out


def union_len(spans, lo, hi):
    total = 0
    for s, e in merge([(max(s, lo), min(e, hi)) for s, e in spans
                       if e > lo and s < hi]):
        total += e - s
    return total


def _clip(union, starts, lo, hi):
    """The intervals of a merged (sorted, disjoint) union that
    overlap [lo, hi), clipped to the window. `starts` is the
    precomputed list of interval starts for `union`."""
    if not union:
        return []
    i = bisect.bisect_right(starts, lo) - 1
    if i < 0:
        i = 0
    out = []
    while i < len(union):
        s, e = union[i]
        if s >= hi:
            break
        cs, ce = max(s, lo), min(e, hi)
        if ce > cs:
            out.append((cs, ce))
        i += 1
    return out


def _classify(data, s, e):
    blob = bytes(data[s:e])
    if not blob.strip(b"\x00"):
        return "zero padding"
    if TEXT_RUN8.search(blob):
        return "text runs not covered by any reference form"
    return "non-text bytes (numeric/code-adjacent data)"


def _account_window(data, name, off, size, kind_unions, all_union):
    """kind_unions: {kind: (union, starts)}; all_union: (union,
    starts) over every kind. Returns the section's accounting."""
    lo, hi = off, off + size
    per_kind = {}
    for kind, (union, starts) in kind_unions.items():
        per_kind[kind] = sum(e - s for s, e in
                             _clip(union, starts, lo, hi))
    covered = _clip(all_union[0], all_union[1], lo, hi)
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
        cls = _classify(data, s, e)
        c = classes.setdefault(cls, {"ranges": 0, "bytes": 0})
        c["ranges"] += 1
        c["bytes"] += e - s
        largest.append((e - s, s, e, cls))
    largest.sort(reverse=True)
    return {
        "section": name,
        "offset": off,
        "size": size,
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


def account_section(data, name, off, size, span_sets):
    """span_sets: {kind: [(start, end)]} in file offsets.
    Returns the section's accounting dict."""
    kind_unions = {}
    all_spans = []
    for kind, spans in span_sets.items():
        u = merge(spans)
        kind_unions[kind] = (u, [iv[0] for iv in u])
        all_spans.extend(spans)
    au = merge(all_spans)
    return _account_window(data, name, off, size, kind_unions,
                           (au, [iv[0] for iv in au]))


def build_accounting(data, sections, span_sets):
    """sections: [(name, offset, size)] of file-backed sections.
    Returns {"sections": [...], "totals": {...}} — sections with no
    spans and no prose are still listed, with their size."""
    kind_unions = {}
    all_spans = []
    for kind, spans in span_sets.items():
        u = merge(spans)
        kind_unions[kind] = (u, [iv[0] for iv in u])
        all_spans.extend(spans)
    au = merge(all_spans)
    all_union = (au, [iv[0] for iv in au])
    out = []
    tot_size = tot_cov = 0
    for name, off, size in sections:
        if size <= 0:
            continue
        acct = _account_window(data, name, off, size, kind_unions,
                               all_union)
        out.append(acct)
        tot_size += size
        tot_cov += acct["covered_bytes"]
    return {"sections": out,
            "totals": {"section_bytes": tot_size,
                       "covered_bytes": tot_cov,
                       "residual_bytes": tot_size - tot_cov}}
