"""Mechanism 4 — constructor descriptors, register variant, plus
the family's two recovery passes: the floating-arrangement
(general) reader and the jump-table matcher arms.

# Ported verbatim from scripts/extract_binary_files.py in the
# 2026-10-31 package restructure; see hatch_extract.mechanisms.
"""
import re
import struct

from ..elftools import (IMMREG_RE, LEA_RE, PATH_AT_RE, _text_ok,
                        imm_stores, path_candidates)

def register_descriptors(data, secs, v2o, lea_sites, covered, starts):
    """Register-length variant. Tiered picks: immediates after the
    content LEA beat earlier ones; an end landing exactly on the next
    path (adjacency) beats a merely decodable span. Only adjacency or
    after-the-LEA picks are returned. Overlap guard: a pick whose span
    contains another file's canonical start (from `starts`) is a
    bundle-registration span, not a file — rejected.
    {path: (content offset, len)}"""
    import bisect
    starts = sorted(starts)
    found = {}
    for site_fo, target_v in lea_sites:
        cands = path_candidates(data, v2o, target_v)
        if not cands:
            continue
        path, plen = cands[0]
        if path in covered or path in found:
            continue
        win = data[site_fo:site_fo + 240]
        leas = []
        for lm in LEA_RE.finditer(win):
            iv = secs[".text"][3] + (site_fo + lm.start()
                                     - secs[".text"][4])
            disp = struct.unpack_from("<i", data,
                                      site_fo + lm.start() + 3)[0]
            leas.append((lm.start(), iv + 7 + disp))
        imms = [(im.start(), struct.unpack("<I", im.group(1))[0])
                for im in IMMREG_RE.finditer(win)]
        if plen not in [v for _p, v in imms]:
            continue
        for rel, tg in leas[1:]:
            if tg == target_v:
                continue
            cfo = v2o(tg)
            if cfo is None:
                continue
            picks = []
            for pos, val in imms:
                if val == plen or not (0 < val <= 4_000_000):
                    continue
                if cfo + val > len(data):
                    continue
                k = bisect.bisect_right(starts, cfo)
                if k < len(starts) and starts[k] < cfo + val:
                    continue  # span swallows another file's start
                if not _text_ok(data[cfo:cfo + val]):
                    continue
                adj = bool(PATH_AT_RE.match(data, cfo + val))
                tier = (0 if pos > rel else 2) + (0 if adj else 1)
                picks.append((tier, pos, val))
            if picks:
                picks.sort()
                tier, _pos, val = picks[0]
                if tier <= 1:
                    found[path] = (cfo, val)
                break
    return found



def general_descriptors(data, secs, v2o, o2v, lea_sites, targets, starts):
    """Floating-arrangement descriptor reader: for each target path
    (path -> heuristic content file offset), examine its path-LEA
    sites' windows without assuming an instruction arrangement.
    Collect LEA targets and immediate constants (register loads and
    properly decoded stores); accept a constant as the content
    length only if the content at the known offset is valid text and
    its end lands exactly on a known file start. This covers the
    stack-built and cmov-pair registrations the rigid shapes miss.
    Returns {path: (content file offset, length)}."""
    text = secs[".text"]
    t_addr, t_off = text[3], text[4]

    def leas_in(win_start, win):
        out = set()
        for m in LEA_RE.finditer(win):
            fo = win_start + m.start()
            iv = t_addr + (fo - t_off)
            disp = struct.unpack_from("<i", win, m.start() + 3)[0]
            out.add(iv + 7 + disp)
        return out

    def imms_in(win):
        vals = [v for _p, v in imm_stores(win) if 0 < v <= 4_000_000]
        for m in IMMREG_RE.finditer(win):
            v = struct.unpack("<I", m.group(1))[0]
            if 0 < v <= 4_000_000:
                vals.append(v)
        return vals

    by_target = {}
    for fo, tg in lea_sites:
        by_target.setdefault(tg, []).append(fo)
    found = {}
    for src, cfo in targets.items():
        po = data.find(src.encode())
        if po == -1:
            continue
        pv = o2v(po)
        cv = o2v(cfo)
        for site in by_target.get(pv, []):
            ws = max(t_off, site - 256)
            win = data[ws:site + 1024]
            if cv not in leas_in(ws, win):
                continue
            cands = {v for v in imms_in(win)
                     if v != len(src) and cfo + v in starts
                     and _text_ok(data[cfo:cfo + v])}
            if len(cands) == 1:
                found[src] = (cfo, cands.pop())
                break
    return found



def matcher_descriptors(data, secs, v2o, wanted):
    """Jump-table matcher arms: each arm loads (path -> rdi,
    path length -> esi, content -> rdx, content length -> ecx) and
    jumps to a common store. For every lea-rdi site whose target is a
    wanted path, walk backwards a short window collecting the arm's
    other values; accept only on exact validation: esi == path
    length and content == path + path length (bundle adjacency) and
    the content is valid text. Returns {path: (content offset, len)}.
    """
    text = secs[".text"]
    t_addr, t_off = text[3], text[4]
    lea_rdi = re.compile(rb"\x48\x8d\x3d....", re.S)
    lea_rdx = re.compile(rb"\x48\x8d\x15....", re.S)
    mov_esi = re.compile(rb"\xbe(.{4})", re.S)
    mov_ecx = re.compile(rb"\xb9(.{4})", re.S)

    def lea_tgt(fo):
        iv = t_addr + (fo - t_off)
        disp = struct.unpack_from("<i", data, fo + 3)[0]
        return iv + 7 + disp

    found = {}
    for m in lea_rdi.finditer(data, t_off, t_off + text[5]):
        site = m.start()
        tgt = lea_tgt(site)
        fo = v2o(tgt)
        if fo is None:
            continue
        cands = path_candidates(data, v2o, tgt)
        if not cands:
            continue
        path, plen = cands[0]
        if path not in wanted or path in found:
            continue
        win_start = max(t_off, site - 56)
        win = data[win_start:site]
        esi = mov_esi.findall(win)
        ecx = mov_ecx.findall(win)
        rdxs = [lea_tgt(win_start + mm.start())
                for mm in lea_rdx.finditer(win)]
        if not esi or not ecx or not rdxs:
            continue
        if struct.unpack("<I", esi[-1])[0] != plen:
            continue
        clen = struct.unpack("<I", ecx[-1])[0]
        cfo = v2o(rdxs[-1])
        if cfo is None or cfo != fo + plen:
            continue
        if not (0 < clen <= 4_000_000):
            continue
        if _text_ok(data[cfo:cfo + clen]):
            found[path] = (cfo, clen)
    return found

