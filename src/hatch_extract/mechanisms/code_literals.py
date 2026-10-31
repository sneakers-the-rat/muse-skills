"""Mechanism 10 — code-referenced literals (reference form c):
rip-relative lea/mov sites in .text load an address in a string
section, and the length of the &str being materialized rides as an
immediate constant in the same instruction window. Enumerating
every (target, length) pair the code itself uses is the ground
truth for fused-pool strings: spans are defined by references,
not by region boundaries, so a literal that starts mid-"region"
is still recovered exactly.

Also provides the extent census mechanism 8 (bare prompts) carves
from. Validation: a candidate length counts only if the span it
names is valid text (no NUL, UTF-8). Each span records its support
— the number of code sites that materialize exactly that
(target, length) pair.
"""
import struct
from collections import defaultdict

from ..elftools import IMMREG_RE, _text_ok, imm_stores

MAX_LITERAL = 4_000_000
WINDOW = 192


def literal_extents(data, v2o, lea_sites, window=WINDOW):
    """{target_file_offset: {length: support}} for every
    code-referenced literal whose bytes validate as text."""
    by_target = defaultdict(list)
    for site, tg in lea_sites:
        by_target[tg].append(site)
    extents = {}
    for tg, sites in by_target.items():
        toff = v2o(tg)
        if toff is None:
            continue
        cand = defaultdict(int)
        for site in sites:
            win = bytes(data[site:site + window])
            for m in IMMREG_RE.finditer(win):
                val = struct.unpack("<I", m.group(1))[0]
                if 0 < val <= MAX_LITERAL:
                    cand[val] += 1
            for _p, val in imm_stores(win):
                if 0 < val <= MAX_LITERAL:
                    cand[val] += 1
        ok = {}
        for length, sup in cand.items():
            if toff + length <= len(data) and \
                    _text_ok(data[toff:toff + length]):
                ok[length] = sup
        if ok:
            extents[toff] = ok
    return extents


def boundary_starts(extents, extra_starts=()):
    """The set of file offsets where some referenced literal or
    other known span starts — the boundary oracle for endpoint
    validation."""
    starts = set(extents)
    starts.update(extra_starts)
    return starts


def end_is_boundary(end, starts, data_len):
    """An extent end is boundary-validated when another known span
    starts exactly there, or one byte later (a single '\\n'
    separator string the compiler fused between literals), or the
    extent runs to the end of the data."""
    return end in starts or (end + 1) in starts or end >= data_len
