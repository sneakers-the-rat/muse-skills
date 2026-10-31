"""Mechanism 6 — agent definitions: the sub-agent registry is
stored as consecutive TOML documents in .rodata, each anchored on
its own `id = "<agent id>"` first line, delimited by the next
anchor, and validated field-by-field.

# Ported verbatim from scripts/extract_binary_files.py in the
# 2026-10-31 package restructure; see hatch_extract.mechanisms.
"""
import re

from ..paths import MAX_FILE

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
