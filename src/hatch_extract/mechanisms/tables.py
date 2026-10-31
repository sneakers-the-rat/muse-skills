"""Mechanism 1 — (path, data) tables: Rust fat-pointer slice
pairs in the relocation data. Also builds the full slice census
every other mechanism consults (slices, by_target, pairs).

# Ported verbatim from scripts/extract_binary_files.py in the
# 2026-10-31 package restructure; see hatch_extract.mechanisms.
"""
import re
import struct

PATH_SLICE_RE = re.compile(
    rb"^[a-z0-9_][a-z0-9_./-]*\.(md|yaml|yml|json|toml|txt)$")


def build_slices(data, secs, v2o):
    """Fat-pointer slices from R_X86_64_RELATIVE relocations: pointer =
    addend, length = u64 stored after the slot. Returns (slices,
    by_target, pairs): slices slot -> (target vaddr, len, content);
    by_target target vaddr -> {lengths}; pairs path -> (data target
    vaddr, data len) for (path @ slot, data @ slot+16)."""
    ro = secs[".rodata"]
    ro_addr, ro_size = ro[3], ro[5]
    rela = secs[".rela.dyn"]
    slices = {}
    for i in range(rela[5] // 24):
        slot, r_info, add = struct.unpack_from(
            "<QQq", data, rela[4] + i * 24)
        if r_info & 0xFFFFFFFF != 8 or not (ro_addr <= add
                                            < ro_addr + ro_size):
            continue
        fo = v2o(slot)
        if fo is None or fo + 16 > len(data):
            continue
        (ln,) = struct.unpack_from("<Q", data, fo + 8)
        if not (0 < ln <= 4_000_000):
            continue
        tfo = v2o(add)
        if tfo is None or tfo + ln > len(data):
            continue
        content = data[tfo:tfo + ln]
        if b"\0" in content:
            continue
        try:
            content.decode("utf-8")
        except UnicodeDecodeError:
            continue
        slices[slot] = (add, ln, content)
    by_target = {}
    for t, ln, _c in slices.values():
        by_target.setdefault(t, set()).add(ln)
    pairs = {}
    for s, (t, ln, c) in slices.items():
        if ln < 250 and PATH_SLICE_RE.match(c) and (s + 16) in slices:
            dt, dln, dc = slices[s + 16]
            if not PATH_SLICE_RE.match(dc):
                pairs[c.decode()] = (dt, dln)
    return slices, by_target, pairs

