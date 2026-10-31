"""End-to-end pipeline test on a synthetic ELF64 fixture, plus a
port-fidelity golden: the package's mechanism functions must agree
with the legacy monolith's (imported from its preserved .bak) on
identical input bytes."""
import importlib.util
import json
import pathlib
import struct

import pytest

from hatch_extract.mechanisms.agent_definitions import agent_definitions
from hatch_extract.paths import clean_path
from hatch_extract.pipeline import run_extract

VA = 0x400000
RODATA_OFF = 0x1000

DEF = (b'id = "%s"\nname = "%s"\nmodel = "m"\nprovider = "p"\n'
       b'tool_loading = "all"\ntools = [\n    "do_thing",\n]\n')
FILES = [
    ("session/alpha.md", b"# Alpha\n\nAlpha body text, long enough.\n"),
    ("session/beta.md", b"# Beta\n\nBeta body text follows here.\n"),
    ("session/gamma.md", b"# Gamma\n\nGamma body text follows.\n"),
    ("chat/delta.md", b"# Delta\n\nDelta body text follows here.\n"),
]


def build_fixture(path):
    defs = DEF % (b"alpha_agent", b"Alpha") + \
        b"beta_agent" + DEF % (b"beta_agent", b"Beta")
    bundle = b""
    for p, body in FILES:
        bundle += p.encode() + body
    rodata = defs + bundle
    shstr = b"\x00.rodata\x00.rela.dyn\x00.text\x00.shstrtab\x00"
    names = {".rodata": 1, ".rela.dyn": 9, ".text": 19, ".shstrtab": 25}
    shoff = 64 + 56
    nsec = 5
    shstr_off = shoff + nsec * 64
    total = RODATA_OFF + len(rodata)

    eh = bytearray(64)
    eh[0:4] = b"\x7fELF"
    eh[4] = 2  # 64-bit
    eh[5] = 1  # LE
    eh[6] = 1
    struct.pack_into("<HHIQQQIHHHHHH", eh, 16,
                     2, 0x3E, 1, 0, 64, shoff, 0, 64, 56, 1, 64, nsec, 4)
    ph = struct.pack("<IIQQQQQQ", 1, 5, 0, VA, VA, total, total, 0x1000)

    def sh(name, typ, flags, addr, off, size):
        return struct.pack("<IIQQQQIIQQ", names.get(name, 0), typ,
                           flags, addr, off, size, 0, 0, 1, 0)

    secs = b"".join([
        bytes(64),
        sh(".rodata", 1, 0x2, VA + RODATA_OFF, RODATA_OFF, len(rodata)),
        sh(".rela.dyn", 4, 0x2, VA + shoff, shoff, 0),
        sh(".text", 1, 0x6, VA, 0, 0),
        sh(".shstrtab", 3, 0, 0, shstr_off, len(shstr)),
    ])
    blob = bytes(eh) + ph + secs
    blob += shstr
    blob += b"\x00" * (RODATA_OFF - len(blob))
    blob += rodata
    path.write_bytes(blob)
    return blob


def test_pipeline_on_synthetic_elf(tmp_path):
    fixture = tmp_path / "fakebin"
    build_fixture(fixture)
    repo = tmp_path / "repo"
    repo.mkdir()
    assert run_extract(repo=repo, bin_path=fixture) == 0
    manifest = json.loads((repo / "binary-map.json").read_text())
    binrec = manifest["bins"][0]
    targets = {c["target"] for c in binrec["contents"]}
    for p, _b in FILES:
        root = "binary-skills"
        assert f"{root}/{p}" in targets
    assert binrec["agent_definitions"] == 2
    assert binrec["prose_regions"] >= 1
    assert binrec["referred_spans"] is not None
    assert "binary-strings/referred/INDEX.csv" in targets
    assert "binary-strings/referred/ACCOUNTING.json" in targets
    # THE REGISTRATION RULE: every artifact file the run wrote is
    # registered in the manifest — no sidecar bookkeeping exists.
    on_disk = {f.relative_to(repo).as_posix()
               for root in ("binary-strings", "binary-skills",
                            "system_prompts")
               for f in (repo / root).rglob("*") if f.is_file()}
    assert on_disk <= targets
    # extracted content is byte-faithful
    assert (repo / "binary-skills/session/alpha.md").read_bytes() == \
        FILES[0][1]
    acct = json.loads(
        (repo / "binary-strings/referred/ACCOUNTING.json").read_text())
    ro = next(s for s in acct["sections"] if s["section"] == ".rodata")
    assert ro["covered_bytes"] > 0


def _load_monolith():
    bak = pathlib.Path(__file__).resolve().parent.parent / \
        "scripts" / "extract_binary_files.py.bak-20261031-080942"
    if not bak.exists():
        pytest.skip("legacy monolith .bak not present")
    from importlib.machinery import SourceFileLoader
    spec = importlib.util.spec_from_loader(
        "legacy_monolith", SourceFileLoader("legacy_monolith", str(bak)))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_golden_agent_definitions_match_monolith(tmp_path):
    mono = _load_monolith()
    fixture = tmp_path / "fakebin"
    blob = build_fixture(fixture)
    pkg_found, pkg_problems = agent_definitions(blob)
    mono_found, mono_problems = mono.agent_definitions(blob)
    assert pkg_found == mono_found
    assert pkg_problems == mono_problems


def test_golden_path_policy_matches_monolith():
    mono = _load_monolith()
    samples = ["blocks/agent/core.md", "session/x.md", "README.md",
               "random/thing.md", "are.session/x.md",
               "example.com/SKILL.md", "tools/a/b.json"]
    for s in samples:
        assert clean_path(s) == mono.clean_path(s)


def test_new_mechanism_failure_never_kills_core_run(tmp_path,
                                                    monkeypatch):
    # The live-pipeline rule: mechanisms 7-13 may fail loudly, but
    # the core extraction (what the archive backup depends on)
    # must still complete and write its manifest.
    import hatch_extract.pipeline as pl
    import hatch_extract.mechanisms.bare_prompts as bp

    def boom(*a, **k):
        raise RuntimeError("simulated new-mechanism failure")

    monkeypatch.setattr(bp, "bare_prompts", boom)
    fixture = tmp_path / "fakebin"
    build_fixture(fixture)
    repo = tmp_path / "repo"
    repo.mkdir()
    assert pl.run_extract(repo=repo, bin_path=fixture) == 0
    man = json.loads((repo / "binary-map.json").read_text())
    b0 = man["bins"][0]
    assert b0["agent_definitions"] == 2          # core output landed
    assert b0["referred_spans"] is None          # new keys absent
    assert b0["agent_prompts"] == 0              # puts rolled back
