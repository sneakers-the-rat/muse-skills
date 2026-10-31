import struct

from hatch_extract.mechanisms.bare_prompts import bare_prompts
from hatch_extract.mechanisms.code_literals import literal_extents

BASE = 0x400000


def _v2o(v):
    return v - BASE


def test_literal_extents_finds_lea_plus_imm():
    prompt = b"You must do the thing exactly once and then stop."
    data = bytearray(b"\x00" * 0x400)
    start = 0x100
    data[start:start + len(prompt)] = prompt
    # a lea site at 0x200 whose window carries `mov edx, <len>`
    site = 0x200
    data[site:site + 7] = b"\x48\x8d\x3d\x00\x00\x00\x00"
    data[site + 7] = 0xBA  # mov edx, imm32
    struct.pack_into("<I", data, site + 8, len(prompt))
    ext = literal_extents(bytes(data), _v2o, [(site, BASE + start)])
    assert ext[start] == {len(prompt): 1}


def _defs():
    doc = (b'id = "%s"\nname = "%s"\nmodel = "m"\nprovider = "p"\n'
           b'tool_loading = "all"\ntools = [\n    "%s",\n]\n')
    return {
        "gamma_agent": (0, doc % (b"gamma_agent", b"Gamma Agent",
                                  b"submit_gamma")),
        "delta_agent": (5000, doc % (b"delta_agent", b"Delta Agent",
                                     b"submit_delta")),
    }


def test_bare_prompt_id_abut_carve():
    body = (b"You determine the gamma outcome from the evidence given. "
            b"Always call `submit_gamma` exactly once. Do not return "
            b"prose, only the verdict the evidence supports here.")
    data = bytearray(b"\x00" * 64)
    data += b"gamma_agent" + body
    start = 64 + len("gamma_agent")
    extents = {start: {len(body): 2}}
    carved, dups, problems = bare_prompts(
        bytes(data), _defs(), extents, [], {start + len(body)})
    assert set(carved) == {"gamma_agent"}
    assert carved["gamma_agent"]["body"] == body
    assert carved["gamma_agent"]["rule"] == "id-abut"
    assert problems == []


def test_bare_prompt_placeholder_trim():
    body = (b"Generate the user-facing gamma state from this evidence.\n\n"
            b"Evidence:\n{{evidence_json}}")
    data = bytearray(b"\x00" * 32)
    data += b"somepooljunk" + body + b"\n" + b"nextstring"
    start = 32 + len("somepooljunk")
    extents = {start: {len(body) + 1: 1}}  # code extent includes \n
    carved, _d, _p = bare_prompts(bytes(data), _defs(), extents, [],
                                  {start + len(body) + 1})
    # gamma attribution rides the submit_gamma needle... body has no
    # needle; distinctive-word rule needs 'gamma' — it is in the body
    assert carved.get("gamma_agent", {}).get("body") == body


def test_bare_prompt_skips_covered_extents():
    body = b"You must not carve what a file already covers, ever. " * 3
    data = bytearray(b"\x00" * 16)
    data += b"gamma_agent" + body
    start = 16 + len("gamma_agent")
    extents = {start: {len(body): 1}}
    carved, _d, _p = bare_prompts(
        bytes(data), _defs(), extents,
        [(start, start + len(body))], {start + len(body)})
    assert carved == {}
