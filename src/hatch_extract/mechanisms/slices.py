"""Mechanism 2 — content slices: a heuristic-found file whose
content address is the target of a relocation slice gets the
slice's authoritative length (confirming or correcting the
heuristic length).

Ported from the merge loop of scripts/extract_binary_files.py in
the 2026-10-31 package restructure.
"""
from ..elftools import _text_ok


def confirm_slices(found, put, by_target, data, o2v):
    """For every file found so far, if its content address is a
    slice target: when the found length is among the slice lengths
    the file is confirmed at slice authority; when there is exactly
    one slice length and the re-sliced bytes are valid text, the
    length is corrected to the slice's."""
    for s, (cs, body, _v) in list(found.items()):
        v = o2v(cs)
        if v is not None and v in by_target:
            lens = by_target[v]
            if len(body) in lens:
                put(s, cs, body, "slice")
            elif len(lens) == 1:
                nl = next(iter(lens))
                nb = data[cs:cs + nl]
                if _text_ok(nb):
                    put(s, cs, nb, "slice")
