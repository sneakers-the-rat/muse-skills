"""Mechanism 3 — constructor descriptors, struct-store variant.

# Ported verbatim from scripts/extract_binary_files.py in the
# 2026-10-31 package restructure; see hatch_extract.mechanisms.
"""
import struct

from ..elftools import (EXT_END_RE, LEA_RE, _text_ok, imm_stores,
                        path_candidates)

def struct_descriptors(data, secs, v2o, lea_sites):
    """LEA path / store / imm(path len) / LEA content / store /
    imm(content len). Returns {path: (content file offset, len)}."""
    ro = secs[".rodata"]
    text = secs[".text"]
    t_addr, t_off = text[3], text[4]

    def lea_at(fo):
        m = LEA_RE.match(data, fo)
        if not m:
            return None
        iv = t_addr + (fo - t_off)
        disp = struct.unpack_from("<i", data, fo + 3)[0]
        return iv + 7 + disp

    found = {}
    for site_fo, target_v in lea_sites:
        for path, plen in path_candidates(data, v2o, target_v):
            if path in found:
                continue
            win = data[site_fo + 7:site_fo + 7 + 160]
            stores = imm_stores(win)
            lenpos = [i for i, (_p, v) in enumerate(stores) if v == plen]
            if not lenpos:
                continue
            after = stores[lenpos[0]][0]
            nxt = None
            for j in range(after + 1, len(win) - 7):
                tg = lea_at(site_fo + 7 + j)
                if tg is not None:
                    nxt = (j, tg)
                    break
            if not nxt:
                continue
            _j, ctgt = nxt
            rest = imm_stores(win[_j + 7:])
            if not rest:
                continue
            clen = rest[0][1]
            if not (0 < clen <= 4_000_000):
                continue
            cfo = v2o(ctgt)
            if cfo is None or cfo + clen > len(data):
                continue
            if _text_ok(data[cfo:cfo + clen]):
                found[path] = (cfo, clen)
    return found

