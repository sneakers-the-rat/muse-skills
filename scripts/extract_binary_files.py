#!/usr/bin/env python3
"""
Extract embedded prompt/skill/tool files from the hatch binary into this
repo, and write binary-map.json describing what came from where.

The binary embeds its files through several mechanisms, and this
extractor reads each one at its own authority level, in one pass:

  1. (path, data) tables — Rust fat-pointer slice pairs in the
     relocation data: a path slice whose +16 slot is a data slice.
     Exact paths, offsets and lengths. (Relocation addends give the
     pointers; the length is the plain u64 after each pointer slot.)
  2. Content slices — a heuristic-found file whose content address is
     the target of a table slice: the slice's length replaces the
     heuristic length.
  3. Constructor descriptors, struct-store variant — code that builds
     a file's descriptor with LEA path / store / immediate path
     length / LEA content / store / immediate content length.
  4. Constructor descriptors, register variant — the same, with the
     lengths passed in registers (accepted when the pick is
     adjacency-verified or positionally strong).
  5. Heuristic string-splitting (the supplement) — bundle text in
     .rodata stored as <path><content><path><content>... with no
     separators; markers are censused, clustered, sliced to the next
     marker and validated. Used only for files no mechanism above
     covers, and reported as such.
  6. Agent definitions — the sub-agent registry is stored as
     consecutive TOML documents in .rodata, each document starting
     at its `id = "<agent id>"` line and running to the next
     document's start; an entry name (the id itself) abuts some
     documents and is stored elsewhere for others, so the documents
     are anchored on their own first line, delimited by the next
     anchor, and validated field-by-field. These names carry no
     path and no extension, so no mechanism above can see them.

A file covered by a higher mechanism is never taken from a lower one.
The manifest records {source, target, offset} per file exactly as
before; the run's stdout reports how many files came from each
mechanism, how many changed versus the tree on disk, and what remains
heuristic-only. binary-map.json's one functional use is the hash
check below: if the binary is unchanged, extraction is skipped —
offsets are provenance, never a lookup table.

If the bundles cannot be found at all, the script fails loudly
instead of writing an empty manifest.

Mapping (user, 2026-10-21; top-level layout revised by the user
later that evening — everything string-like now lives under
binary-strings/, and system-prompt/ became system_prompts/):
  browser/          -> binary-strings/browser/
  self_improvement/ -> binary-strings/self_improvement/
  blocks/           -> system_prompts/
  templates/        -> binary-strings/artifacts/templates/
  artifacts/        -> binary-strings/artifacts/
  tools/            -> binary-strings/tools/
  <challenge slug>/ -> binary-skills/<slug>/        (SKILL.md guides)
  <domain>/         -> binary-strings/browser/site-config/<domain>/
                       (config.yaml + SKILL.md)
  session/, chat/, devices/, voice/, activity_monitor/, channels/,
  chat-connections/, shopping/
                    -> binary-skills/<root>/  (the real multi-file roots)
  agent-definitions/<id>.toml
                    -> binary-strings/agent-definitions/<id>.toml
                       (mechanism 6: the embedded entry name is the
                       bare agent id; the .toml is archive-side naming
                       for its TOML content)
  anything else     -> binary-etc/<source>  (unsorted; the snapshot hook
                      holds NEW binary-etc files out of the commit and
                      asks the user to classify them — see sync-skills.sh)
Ignored as example/mention paths inside other files: memory/, config/,
notes/, orders/, user/, dreams/, selection/, update/, studying/.
"""
import hashlib
import json
import pathlib
import re
import struct
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone

REPO = pathlib.Path(__file__).resolve().parent.parent
BIN = pathlib.Path("/opt/hatch/bin/hatch")
PATHCH = set(b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_./-")
EXTS = (".md", ".yaml", ".yml", ".json", ".toml")

KNOWN_ROOTS = {"blocks", "browser", "session", "self_improvement",
               "templates", "tools", "artifacts", "channels", "devices",
               "connections", "memory", "notes", "voice", "docs",
               "references", "assets", "chat-connections", "dreams",
               "orders", "selection", "shopping", "studying", "config",
               "src", "user", "update", "chat", "activity_monitor"}
SLUGS = {"arithmetic-and-counting", "audio-challenge", "automatic-check",
         "block-page", "game-puzzle", "icon-order", "image-click",
         "image-grid", "network-block", "page-load-failure", "path-drawing",
         "press-and-hold", "rotation-puzzle", "sign-in-check",
         "slider-puzzle", "soft-block", "start-gate", "text-captcha",
         "verification-checkbox", "waiting-room"}
DOMAIN = re.compile(r"^[a-z0-9\-]+(\.[a-z0-9\-]+)+$")
SKILL_ROOTS = {"session", "chat", "devices", "voice", "activity_monitor",
               "channels", "chat-connections", "shopping"}
SKIP_ROOTS = {"memory", "config", "notes", "orders", "user", "dreams",
              "selection", "update", "studying"}
MAX_FILE = 1_000_000
CLUSTER_GAP = 0x20000
MIN_CLUSTER_FILES = 20


def clean_path(raw):
    if "/" not in raw:
        return None  # bare filenames are mentions, not bundle files
    parts = raw.split("/")
    # a final component carrying two extensions is two fused names
    # ('a.mdvoice_chat_delegate.md'); the stored entry is the first name
    last = parts[-1]
    for ext in EXTS:
        i = last.find(ext)
        if i != -1 and any(e in last[i + len(ext):] for e in EXTS):
            parts[-1] = last[:i + len(ext)]
            raw = "/".join(parts)
            break
    if parts[0] in KNOWN_ROOTS or parts[0] in SLUGS:
        return raw
    if DOMAIN.match(parts[0]) and len(parts) == 2 and \
            parts[1] in ("SKILL.md", "config.yaml"):
        return raw
    # fused prefix ending in a known root as a suffix of the first
    # component ('are.session/x.md' -> 'session/x.md'): the root name is
    # the delimiter (the user's heuristic)
    for root in sorted(KNOWN_ROOTS, key=len, reverse=True):
        if parts[0].endswith(root) and len(parts[0]) > len(root):
            return "/".join([root] + parts[1:])
    for i in range(1, len(parts) - 1):
        if parts[i] in KNOWN_ROOTS:
            return "/".join(parts[i:])
    return None


def target_for(source):
    top, _, rest = source.partition("/")
    if top == "agent-definitions":
        return f"binary-strings/{source}"
    if top == "browser":
        return f"binary-strings/{source}"
    if top == "self_improvement":
        return f"binary-strings/{source}"
    if top == "blocks":
        return f"system_prompts/{rest}"
    if top == "templates":
        return f"binary-strings/artifacts/templates/{rest}"
    if top == "artifacts":
        return f"binary-strings/{source}"
    if top == "tools":
        return f"binary-strings/tools/{rest}"
    if top in SLUGS:
        return f"binary-skills/{source}"
    if DOMAIN.match(top) and source.count("/") == 1 and \
            rest in ("SKILL.md", "config.yaml"):
        return f"binary-strings/browser/site-config/{source}"
    if top in SKILL_ROOTS:
        return f"binary-skills/{source}"
    if top in SKIP_ROOTS:
        return None
    return f"binary-etc/{source}"


def split_token(tok):
    """Split a fused grep token into sub-paths. A split point is an
    extension end immediately followed by a plausible next path start
    (known root, guide slug, or domain component, each followed by '/').
    Returns [(local_start, subpath, is_last)]."""
    out = []
    pos = 0
    while pos < len(tok):
        # earliest extension end at or after pos
        end = None
        for ext in EXTS:
            i = tok.find(ext, pos)
            if i != -1 and (end is None or i + len(ext) < end[0]):
                end = (i + len(ext), ext)
        if end is None:
            out.append((pos, tok[pos:], True))
            break
        e = end[0]
        rest = tok[e:]
        nxt = None
        if rest:
            head = rest.split("/", 1)[0]
            if "/" in rest and (head in KNOWN_ROOTS or head in SLUGS
                                or DOMAIN.match(head)):
                nxt = e
        if nxt is None:
            out.append((pos, tok[pos:], True))
            break
        out.append((pos, tok[pos:e], False))
        pos = e
    return out


def census(data):
    raw = subprocess.run(
        ["grep", "-a", "-b", "-o", "-E",
         r"[A-Za-z0-9_.\-]+(/[A-Za-z0-9_.\-]+)*\.(md|yaml|yml|json|toml)",
         str(BIN)], capture_output=True).stdout.decode(errors="replace")
    marks = []  # (offset, path, content_start, is_last_in_token)
    for line in raw.splitlines():
        off, _, tok = line.partition(":")
        off = int(off)
        if len(tok) > 200 or ".." in tok:
            continue
        if off > 0 and data[off - 1] in PATHCH:
            continue
        for local, sub, is_last in split_token(tok):
            marks.append((off + local, sub, off + len(tok) if is_last
                          else off + local + len(sub), is_last))
    marks.sort()
    return marks


def rodata_range():
    out = subprocess.run(["readelf", "-S", "-W", str(BIN)],
                         capture_output=True).stdout.decode(errors="replace")
    for line in out.splitlines():
        parts = line.split()
        # [Nr] Name Type Address Offset Size ...
        if len(parts) >= 6 and parts[1] == ".rodata":
            try:
                off = int(parts[4], 16)
                size = int(parts[5], 16)
                return off, off + size
            except ValueError:
                pass
    return 0, BIN.stat().st_size


def validate(body, is_last):
    """Return None if the slice looks like a stored file, else a reason."""
    if len(body) == 0:
        return None if not is_last else "empty slice"
    if len(body) > MAX_FILE:
        return f"size {len(body)} rejected"
    if b"\x00" in body:
        return "NUL bytes in slice"
    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError:
        return "slice is not UTF-8"
    if text.startswith('"') or text.startswith("` -"):
        return "list/index fragment, not a file"
    if text[0].islower() and not re.match(r"^[a-z_]+:", text):
        return "starts mid-sentence (a mention, not a file start)"
    return None


# ---------------------------------------------------------------------
# Agent definitions (mechanism 6): the sub-agent registry is a run of
# consecutive TOML documents in .rodata. Each document begins with
# `id = "<agent id>"` followed by a `name = ` line; the next document
# begins at the next such anchor (an entry name — the id itself —
# abuts some documents, so an anchored document's slice ends that
# many bytes before the next anchor). A document is accepted only if
# it carries the registry's required fields and every line is
# TOML-shaped; anything else wearing the anchor is reported as a
# rejected candidate, never silently dropped.
# ---------------------------------------------------------------------

AGENT_DEF_ANCHOR = re.compile(rb'id = "([a-z0-9_]+)"\nname = "')
AGENT_DEF_LINE = re.compile(
    rb'^[A-Za-z_]+ = |^    "|^    [A-Za-z_]|^#|^\]|^\[\[|^\[|^$')
AGENT_DEF_REQUIRED = (b'\nmodel = "', b'\nprovider = "',
                      b'\ntool_loading = "', b'\ntools = ')


def _agent_def_invalid(block):
    """Return None if the slice is a whole agent definition, else a
    reason."""
    if b"\x00" in block:
        return "NUL bytes in slice"
    try:
        block.decode("utf-8")
    except UnicodeDecodeError:
        return "slice is not UTF-8"
    for req in AGENT_DEF_REQUIRED:
        if req not in block:
            return f"missing required field {req.decode().strip()}"
    for line in block.split(b"\n"):
        if not AGENT_DEF_LINE.match(line):
            return f"non-TOML line: {line[:60]!r}"
    return None


def agent_definitions(data):
    """Census the agent-definition registry. Returns
    ({id: (content_offset, body)}, [problem strings])."""
    cands = [(m.start(), m.group(1))
             for m in AGENT_DEF_ANCHOR.finditer(data)]
    found = {}
    problems = []
    for idx, (start, aid_b) in enumerate(cands):
        aid = aid_b.decode()
        if idx + 1 < len(cands):
            nstart, nid = cands[idx + 1]
            end = nstart - len(nid) \
                if data[nstart - len(nid):nstart] == nid else nstart
            block = data[start:end].rstrip(b"\n")
        else:
            # Last document: its end is not delimited by a successor,
            # so take a generous window and trim trailing lines that
            # are not part of the document.
            block = data[start:start + MAX_FILE].rstrip(b"\n")
            while block and _agent_def_invalid(block) is not None:
                nl = block.rfind(b"\n")
                if nl == -1:
                    block = b""
                    break
                block = block[:nl]
        why = _agent_def_invalid(block)
        if why is not None:
            problems.append(f"agent-def {aid}: {why}")
            continue
        if aid in found:
            problems.append(f"agent-def {aid}: duplicate id, "
                            "first occurrence kept")
            continue
        found[aid] = (start, block)
    return found, problems


# ---------------------------------------------------------------------
# Deterministic sources: ELF maps, relocation slices and tables,
# constructor descriptors. All static reads of the binary's bytes.
# ---------------------------------------------------------------------

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
        e = data.index(b"\0", strtab + v[0])
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


def main():
    data = BIN.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    # Provenance is one-way: binary-map.json is a record of where files
    # came from, never a lookup table — its offsets are not read back.
    # Its one functional use is this hash check: if the binary is the
    # one the manifest records, the embedded strings cannot have
    # changed, so extraction is skipped (unless a recorded target file
    # has gone missing from the tree, which forces a fresh run).
    manifest_path = REPO / "binary-map.json"
    if manifest_path.exists():
        try:
            old = json.loads(manifest_path.read_text())
            oldbin = old["bins"][0]
            if oldbin["sha256"] == sha and \
                    oldbin.get("agent_definitions") is not None and all(
                    (REPO / c["target"]).exists()
                    for c in oldbin["contents"]):
                print(f"binary unchanged ({sha[:12]}…); extraction skipped")
                return 0
        except (ValueError, KeyError, IndexError, TypeError):
            pass  # a malformed manifest is just re-created below

    # ---- phase 5 (computed first): heuristic string-splitting --------
    marks = census(data)
    r0, r1 = rodata_range()
    rod = [m for m in marks if r0 <= m[0] < r1]
    slash_offsets = sorted(m[0] for m in rod if "/" in m[1])

    # bundle clusters: dense runs of slash-path markers
    clusters = []
    for m in rod:
        if "/" not in m[1]:
            continue
        if clusters and m[0] - clusters[-1][-1][0] <= CLUSTER_GAP:
            clusters[-1].append(m)
        else:
            clusters.append([m])
    bundle = []
    for cl in clusters:
        plausible = {clean_path(p) for _, p, _, _ in cl}
        plausible = {p for p in plausible
                     if p is not None and target_for(p) is not None}
        # A cluster is a bundle if it is dense overall, or if it is a
        # small single-root table (e.g. the activity_monitor fragments):
        # >= 4 plausible files, >= 3 of them under one root, tight span.
        roots = Counter(p.split("/")[0] for p in plausible)
        dense = len(plausible) >= MIN_CLUSTER_FILES
        small_table = (len(plausible) >= 4 and roots and
                       max(roots.values()) >= 3 and
                       cl[-1][0] - cl[0][0] <= 0x100000)
        if dense or small_table:
            bundle.extend(cl)

    # candidates: cleaned source -> [occurrences]
    cands = {}
    for off, raw, cstart, is_last in bundle:
        src = clean_path(raw)
        if src is None or target_for(src) is None:
            continue
        cands.setdefault(src, []).append((off, cstart, is_last))

    def boundary_after(anchor):
        after = [o for o in slash_offsets if o > anchor]
        return after[0] if after else len(data)

    found_h = {}   # source -> (content offset, body)
    problems = []
    for src in sorted(cands):
        done = False
        for off, cstart, is_last in cands[src]:
            end = cstart if not is_last else boundary_after(off)
            body = data[cstart:end]
            if validate(body, is_last) is not None:
                continue
            found_h[src] = (cstart, body)
            done = True
            break
        if not done:
            problems.append(src)

    # Special case: arithmetic-and-counting has no SKILL.md marker; its
    # guide starts at its '# Arithmetic and counting' heading, inside the
    # guide cluster (the cluster holding the other guide slugs).
    src = "arithmetic-and-counting/SKILL.md"
    if src not in found_h:
        guide = [m for m in bundle if clean_path(m[1]) in
                 {f"{s}/SKILL.md" for s in SLUGS}]
        if guide:
            lo = min(m[0] for m in guide) - CLUSTER_GAP
            hi = max(m[0] for m in guide) + CLUSTER_GAP
            h = data.find(b"# Arithmetic and counting", lo, hi)
            if h != -1:
                body = data[h:boundary_after(h)]
                if validate(body, True) is None:
                    found_h[src] = (h, body)

    # ---- deterministic phases -----------------------------------------
    _loads, secs, v2o, o2v = elf_maps(data)
    _slices, by_target, pairs = build_slices(data, secs, v2o)
    lea_sites = lea_census(data, secs, v2o)
    d_struct = struct_descriptors(data, secs, v2o, lea_sites)
    starts = {cs for cs, _b in found_h.values()}
    starts |= {cfo for cfo, _ln in d_struct.values()}
    starts |= {v2o(tv) for tv, _ln in pairs.values()}
    starts.discard(None)
    d_reg = register_descriptors(data, secs, v2o, lea_sites,
                                 set(pairs) | set(d_struct), starts)

    if not bundle and not pairs:
        print("ERROR: no bundle clusters or tables found — binary "
              "layout changed; refusing to write an empty extraction",
              file=sys.stderr)
        return 1

    # ---- merge by authority: table > slice > struct > register > heur.
    RANK = {"table": 7, "agent-def": 7, "slice": 6,
            "descriptor-struct": 5, "descriptor-register": 4,
            "matcher": 3, "descriptor-general": 2, "heuristic": 1}
    found = {}   # source -> (offset, body, via)
    rank = {}

    def put(s, off, body, via):
        if RANK[via] > rank.get(s, 0):
            found[s] = (off, body, via)
            rank[s] = RANK[via]

    for s, (cs, body) in found_h.items():
        put(s, cs, body, "heuristic")
    # slice membership: the content address is a slice target; the
    # slice length is authoritative (confirm or correct the heuristic)
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
    for s, (cfo, ln) in d_struct.items():
        if target_for(s) is not None:
            put(s, cfo, data[cfo:cfo + ln], "descriptor-struct")
    for s, (cfo, ln) in d_reg.items():
        if target_for(s) is not None:
            put(s, cfo, data[cfo:cfo + ln], "descriptor-register")
    for s, (tv, ln) in pairs.items():
        if target_for(s) is not None:
            tfo = v2o(tv)
            if tfo is not None:
                put(s, tfo, data[tfo:tfo + ln], "table")
    # general floating-arrangement reader for what is still heuristic
    starts_g = set(starts)
    for _off, _raw, _cs, _il in marks:
        starts_g.add(_off)
        starts_g.add(_cs)
    for _cfo, _ln in d_struct.values():
        starts_g.add(_cfo)
        starts_g.add(_cfo + _ln)
    for _cfo, _ln in d_reg.values():
        starts_g.add(_cfo)
    todo_h = {s: cs for s, (cs, _b) in found_h.items()
              if rank.get(s, 0) < RANK["descriptor-general"]}
    d_gen = general_descriptors(data, secs, v2o, o2v, lea_sites,
                                todo_h, starts_g)
    for s, (cfo, ln) in d_gen.items():
        if target_for(s) is not None:
            put(s, cfo, data[cfo:cfo + ln], "descriptor-general")
    # jump-table matcher arms, for anything still below that rank
    # (heuristic files and previously skipped candidates alike)
    wanted_m = {s for s in set(cands) | set(found_h)
                if rank.get(s, 0) < RANK["matcher"]}
    d_match = matcher_descriptors(data, secs, v2o, wanted_m)
    for s, (cfo, ln) in d_match.items():
        if target_for(s) is not None:
            put(s, cfo, data[cfo:cfo + ln], "matcher")
    # agent definitions (mechanism 6): anchored TOML documents whose
    # entry names are bare ids — invisible to every path-based
    # mechanism above, so they merge here on their own authority
    d_agents, agent_problems = agent_definitions(data)
    for aid, (cfo, body) in d_agents.items():
        put(f"agent-definitions/{aid}.toml", cfo, body, "agent-def")
    for p in agent_problems:
        print(f"  SKIP {p}", file=sys.stderr)
    problems = [p for p in problems if p not in found]

    # ---- write ---------------------------------------------------------
    contents = []
    n_new = n_changed = 0
    for s in sorted(found):
        off, body, _via = found[s]
        target = target_for(s)
        dest = REPO / target
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            if dest.read_bytes() != body:
                n_changed += 1
                dest.write_bytes(body)
        else:
            n_new += 1
            dest.write_bytes(body)
        contents.append({"source": s, "target": target, "offset": off})
    contents.sort(key=lambda c: c["target"])

    # Prune stale outputs: a file under a managed root that this run did
    # not produce is a file the binary no longer embeds (or an artefact
    # of an older extractor layout) — remove it so the archive records
    # the deletion instead of keeping a stale copy forever.
    # Pruning is scoped to subtrees ONLY this extractor writes.
    # binary-strings/ is shared: binary-strings/tools/*.json and
    # binary-strings/browser/{bot_challenge,errors.csv} belong to the
    # topical string extractions and are never pruned from here.
    MANAGED_ROOTS = ["system_prompts", "binary-skills", "binary-etc",
                     "binary-strings/agent-definitions",
                     "binary-strings/artifacts",
                     "binary-strings/browser/instructions",
                     "binary-strings/browser/site-config",
                     "binary-strings/browser/workflows",
                     "binary-strings/self_improvement"]
    keep = {c["target"] for c in contents}
    # Untracked files are unclassified material (user rule, 2026-10-27):
    # a file the user has not yet classified — e.g. a new binary-etc
    # hold-out — is NEVER pruned, even when this run does not produce
    # it. Only tracked files are pruned: their deletion is recorded by
    # git, so nothing is lost silently.
    tracked = set(subprocess.run(
        ["git", "-C", str(REPO), "ls-files"], capture_output=True,
        text=True).stdout.split())
    pruned = 0
    preserved = 0
    for root in MANAGED_ROOTS:
        base = REPO / root
        if not base.is_dir():
            continue
        for f in sorted(base.rglob("*"), reverse=True):
            rel = f.relative_to(REPO).as_posix()
            if f.is_file() and rel not in keep:
                if rel in tracked:
                    f.unlink()
                    pruned += 1
                else:
                    preserved += 1
            elif f.is_dir() and not any(f.iterdir()):
                f.rmdir()
    if pruned:
        print(f"pruned {pruned} stale extracted files")
    if preserved:
        print(f"preserved {preserved} untracked (unclassified) files")

    manifest = {"bins": [{
        "path": str(BIN),
        "sha256": sha,
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "size": len(data),
        "agent_definitions": sum(
            1 for c in contents
            if c["target"].startswith("binary-strings/agent-definitions/")),
        "contents": contents,
    }]}
    (REPO / "binary-map.json").write_text(json.dumps(manifest, indent=2) + "\n")
    vias = Counter(v for _o, _b, v in found.values())
    print(f"binary {sha[:12]}… size {len(data)}")
    print(f"extracted {len(contents)} files; skipped {len(problems)}")
    print(f"by mechanism: {dict(vias)}")
    print(f"new on disk: {n_new}; changed on disk: {n_changed}")
    print(f"heuristic-only residue: {vias.get('heuristic', 0)}")
    spans = sorted((off, off + len(body)) for off, body, _v
                   in found.values())
    for p in problems:
        # a candidate whose every occurrence lies inside an
        # extracted file's content is a mention in that file, not a
        # missed file — tag it so the skip list reads honestly
        occ = []
        i = data.find(p.encode())
        while i != -1:
            occ.append(i)
            i = data.find(p.encode(), i + 1)
        mention = bool(occ) and all(
            any(a <= o < b for a, b in spans) for o in occ)
        print(f"  SKIP {'(mention) ' if mention else ''}{p}",
              file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
