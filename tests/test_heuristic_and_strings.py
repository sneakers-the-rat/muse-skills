import pathlib

from hatch_extract.mechanisms.heuristic import find_heuristic, validate
from hatch_extract.strings_methods import (balanced_json, split_section,
                                           window_run)


def test_validate_rules():
    assert validate(b"# Title\n\nBody.\n", True) is None
    assert validate(b"", True) is not None
    assert validate(b"has\x00nul", True) is not None
    assert validate(b"mid sentence start", True) is not None


def _bundle_file(tmp_path):
    files = [
        ("session/alpha.md", b"# Alpha\n\nAlpha body text, long enough.\n"),
        ("session/beta.md", b"# Beta\n\nBeta body text follows here.\n"),
        ("session/gamma.md", b"# Gamma\n\nGamma body text follows.\n"),
        ("chat/delta.md", b"# Delta\n\nDelta body text follows here.\n"),
    ]
    blob = b""
    for path, body in files:
        blob += path.encode() + body
    # pad so census offsets sit inside one small span, then a fake
    # ELF-ish tail the heuristic never reaches (bundle ends the file)
    p = tmp_path / "fakebin"
    p.write_bytes(blob)
    return p, dict(files)


def test_find_heuristic_small_table(tmp_path):
    p, files = _bundle_file(tmp_path)
    data = p.read_bytes()
    found_h, problems, marks, bundle, cands = find_heuristic(data, p)
    assert set(found_h) == set(files)
    for src, (_off, body) in found_h.items():
        assert body == files[src]


def test_balanced_json():
    blob = b'xx{"type": "object", "properties": {"a": {"x": "}"}}}yy'
    end = balanced_json(blob, 2)
    assert blob[2:end].endswith(b"}}")
    assert balanced_json(b"{unclosed", 0) is None


def test_window_run_and_split_section():
    blob = b"\x00\x01" + b"printable run of text here" + b"\x00"
    start, win = window_run(blob, 10, span=100)
    assert win == b"printable run of text here"
    md = b"# A\n\n## Bot detection\n\nnotes\n\n## Other\n\nx\n"
    assert split_section(md, b"## Bot detection") == \
        b"## Bot detection\n\nnotes\n\n"
