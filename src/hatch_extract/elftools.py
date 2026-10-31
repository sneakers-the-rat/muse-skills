"""ELF structure and code-reference machinery: program/section
maps, address translation, RIP-relative LEA census, immediate
decoding, path candidates at a target.

# Ported verbatim from scripts/extract_binary_files.py in the
# 2026-10-31 package restructure; see hatch_extract.mechanisms.
"""
import re
import struct

def elf_maps(data):
    (e_phoff,) = struct.unpack_from("<Q", data, 0x20)
    (e_shoff,) = struct.unpack_from("<Q", data, 0x28)
    e_phentsize, e_phnum = struct.unpack_from("<HH", data, 0x36)
    e_shentsize, e_shnum, e_shstrndx = struct.unpack_from("<HHH", data, 0x3A)
    loads = []
    for i in range(e_phnum):
        t, _f, off, va, _p, fsz, _m, _a = struct.unpack_from(
            "<IIQQQQQQ", data, e_phoff + i * e_phentsize)
        if t == 1:
            loads.append((va, off, fsz))
    raw = [struct.unpack_from("<IIQQQQIIQQ", data, e_shoff + i * e_shentsize)
           for i in range(e_shnum)]
    strtab = raw[e_shstrndx][4]
    secs = {}
    for v in raw:
        e = data.find(b"\0", strtab + v[0])
        secs[data[strtab + v[0]:e].decode()] = v  # (…, addr, off, size)

    def v2o(x):
        for va, off, fsz in loads:
            if va <= x < va + fsz:
                return x - va + off
        return None

    def o2v(o):
        for va, off, fsz in loads:
            if off <= o < off + fsz:
                return o - off + va
        return None

    return loads, secs, v2o, o2v



LEA_RE = re.compile(
    rb"[\x48\x4c]\x8d[\x05\x0d\x15\x1d\x25\x2d\x35\x3d]....", re.S)


def imm_stores(win):
    """All `movq $imm32, mem` (48 c7 /0) stores in a byte window, with
    the ModRM/SIB/displacement decoded properly — the naive regex
    misreads rsp-based stores (48 c7 44 24 ..), which are exactly the
    stack-built descriptors. Returns [(offset, value)]."""
    out = []
    for m in re.finditer(rb"\x48\xc7", win):
        i = m.start()
        if i + 2 >= len(win):
            break
        modrm = win[i + 2]
        if (modrm >> 3) & 7 != 0:
            continue  # only /0 is mov
        mod, rm = modrm >> 6, modrm & 7
        j = i + 3
        if mod == 0 and rm == 5:
            j += 4                      # RIP + disp32
        else:
            if rm == 4:
                j += 1                  # SIB byte
            if mod == 1:
                j += 1                  # disp8
            elif mod == 2:
                j += 4                  # disp32
        if j + 4 <= len(win):
            out.append((i, struct.unpack_from("<I", win, j)[0]))
    return sorted(out)
IMMREG_RE = re.compile(rb"(?:\x41)?[\xb8-\xbf](.{4})", re.S)
EXT_END_RE = re.compile(rb"\.(md|yaml|yml|json|toml|txt)(?![a-z0-9_/])")
PATH_AT_RE = re.compile(
    rb"[a-z0-9_][a-z0-9_./-]{3,}\.(?:md|yaml|yml|json|toml|txt)"
    rb"(?![a-z0-9_/])")


def lea_census(data, secs, v2o):
    """All RIP-relative LEA sites in .text with targets in .rodata:
    [(site file offset, target vaddr)]."""
    text = secs[".text"]
    t_addr, t_off, t_size = text[3], text[4], text[5]
    ro = secs[".rodata"]
    out = []
    for m in LEA_RE.finditer(data, t_off, t_off + t_size):
        iv = t_addr + (m.start() - t_off)
        disp = struct.unpack_from("<i", data, m.start() + 3)[0]
        tg = iv + 7 + disp
        if ro[3] <= tg < ro[3] + ro[5]:
            out.append((m.start(), tg))
    return out


def path_candidates(data, v2o, target_v):
    """Plausible file paths starting exactly at target_v."""
    fo = v2o(target_v)
    if fo is None:
        return []
    head = data[fo:fo + 220]
    out = []
    for em in EXT_END_RE.finditer(head):
        p = head[:em.end()].decode("utf-8", "replace")
        if re.fullmatch(r"[a-z0-9_][a-z0-9_./-]*", p) and "/" in p:
            out.append((p, em.end()))
    return out


def _text_ok(b):
    if b"\0" in b:
        return False
    try:
        b.decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False
