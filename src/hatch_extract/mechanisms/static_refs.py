"""Mechanism 9 — static fat-pointer references (reference form b):
every (ptr, len) pair stored in a data section whose ptr lands in
a string section and whose span validates as text — the standard
Rust &str constant in statics, vtables and fmt piece arrays
(form g rides this form: core::fmt piece arrays are statics of
exactly these pairs, so their spans fall out of this census).

Built on mechanism 1's relocation slice census: each slice slot is
one stored fat pointer. Spans are deduplicated by (offset, len)
with a reference count.
"""
from collections import Counter


def static_refs(slices, v2o):
    """slices: {slot_vaddr: (target_vaddr, len, content)} from
    build_slices. Returns [{offset, len, refs, form}]."""
    counts = Counter()
    for _slot, (target, length, _content) in slices.items():
        off = v2o(target)
        if off is not None:
            counts[(off, length)] += 1
    return [{"offset": off, "len": length, "refs": n,
             "form": "static fat-pointer (ptr,len)"}
            for (off, length), n in sorted(counts.items())]
