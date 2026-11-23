"""Tests for scripts/extract_mac_strings.py — the pure functions
(spec-fragment parsing, catalog parsing, fragment assignment, string
extraction) plus the flat-layout contract: the dump goes directly
under mac-app/ with NO version directory, and the app version lives
as metadata in mac-app-map.json. The full dump is also exercised by
running the script itself against the banked app; these tests pin
the fragment/catalog logic that decides the tool-prompts categories,
in the same plain-pytest style as the rest of tests/."""
import hashlib
import importlib.util
import json
import pathlib

SCRIPT = (pathlib.Path(__file__).resolve().parent.parent
          / "scripts" / "extract_mac_strings.py")
spec = importlib.util.spec_from_file_location("extract_mac_strings", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

SPEC_TEXT = """# header comment
# Long set: 1; short set: 2.

## One-line complete specs

Do the thing with files.read now.

Short spec for computer.control.

## Long spec / guidance fragments (>=200 chars)

""" + ("Long guidance for files.read and computer.control. " * 5).strip() + "\n"

CATALOG = """# catalog header

agent.status
chat.stream
client.invoke
computer.control
files.de
files.read

## files.* family (attested by substring census)
files.copy
files.get_tags
files.read
files.update_tags
"""


def test_parse_spec_descriptions_splits_sets():
    short, long = mod.parse_spec_descriptions(SPEC_TEXT)
    assert len(short) == 2
    assert len(long) == 1
    assert short[0].startswith("Do the thing")
    assert len(long[0]) >= 200


def test_parse_command_catalog_device_vs_gateway():
    device, gateway = mod.parse_command_catalog(CATALOG)
    # gateway/plumbing and chat.* are not device commands
    assert "agent.status" in gateway
    assert "chat.stream" in gateway
    assert "client.invoke" in gateway
    # truncated 8-char artifact is dropped; family names are kept whole
    assert "files.de" not in device
    assert "files.get_tags" in device
    assert "files.update_tags" in device
    # prose-only commands are added
    assert "screen.snap" in device
    assert "files.delete" in device
    assert "computer.control" in device


def test_assign_fragments_and_status():
    short, long = mod.parse_spec_descriptions(SPEC_TEXT)
    device, _ = mod.parse_command_catalog(CATALOG)
    per = mod.assign_fragments(device, short, long)
    assert mod.command_status(per["files.read"]) == "described_long"
    assert mod.command_status(per["computer.control"]) == "described_long"
    assert mod.command_status(per["files.copy"]) == "name_only"


def test_strings_of_ascii_and_utf16():
    data = b"\x00hello world\x00\x00" + "utf16 string here".encode("utf-16-le")
    strs = mod.strings_of(data)
    assert "hello world" in strs
    assert "utf16 string here" in strs


def test_prompt_like_filter():
    long_instruction = ("You must always check the observation before "
                        "you answer the user and never skip this step "
                        "when the tool result is incomplete today.")
    assert mod.prompt_like([long_instruction, "short"]) == [long_instruction]


def _fake_inputs(tmp_path, version="9.9"):
    """Minimal banked-version fixture: app copy + analysis artifacts
    with just enough content for a full dump."""
    app_dir = tmp_path / "analysis" / version / "work" / "Muse.app"
    for rel in mod.BINARIES.values():
        p = app_dir / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b"\x00hello world test string\x00" * 4)
    analysis_dir = tmp_path / "analysis" / version
    (analysis_dir / "spec-descriptions.txt").write_text(SPEC_TEXT)
    (analysis_dir / "command-catalog.txt").write_text(CATALOG)
    (analysis_dir / "urls.txt").write_text("# urls\n\nhttps://example.com/\n")
    (analysis_dir / "entitlements.txt").write_text("entitlements body\n")
    (analysis_dir / "info-plist-summary.txt").write_text("plist body\n")
    (analysis_dir / "keyword-hits.txt").write_text("keyword body\n")
    (analysis_dir / "objc-main.json").write_text(json.dumps(
        {"evidence": "test",
         "slices": [{"arch": "arm64", "method": "test", "cryptid": 0,
                     "counts": {}}]}))
    names_dir = analysis_dir / "objc-names"
    names_dir.mkdir(exist_ok=True)
    for name in ("classes", "protocols", "selectors", "swift-reflstr"):
        (names_dir / f"{name}.arm64.txt").write_text("Foo\nBar\n")
    return app_dir, analysis_dir


def test_dump_app_writes_flat_tree_no_version_dir(tmp_path, monkeypatch):
    out_root = tmp_path / "mac-app"
    monkeypatch.setattr(mod, "OUT_ROOT", out_root)
    app_dir, analysis_dir = _fake_inputs(tmp_path)
    manifest = {"bundle_id": "com.example.test", "build": "42",
                "team_id": "TEAM", "minimum_macos": "15.0"}
    files, _census, _tools = mod.dump_app(
        "9.9", app_dir, analysis_dir, "0" * 64, manifest)
    # flat: categories sit directly under mac-app/, no 9.9/ level
    assert (out_root / "strings" / "Muse.strings.txt").is_file()
    assert (out_root / "tool-prompts" / "tools-manifest.json").is_file()
    assert not (out_root / "9.9").exists()
    assert files  # something was dumped
    assert all(not k.startswith("9.9/") for k in files)
    assert "strings/census.json" in files


def test_main_records_version_as_manifest_metadata(tmp_path, monkeypatch):
    version = "9.9"
    app_dir, analysis_dir = _fake_inputs(tmp_path, version)
    vdir = tmp_path / "archive" / "versions" / version
    vdir.mkdir(parents=True)
    dmg_bytes = b"fake dmg bytes"
    (vdir / "app.dmg").write_bytes(dmg_bytes)
    (vdir / "manifest.json").write_text(json.dumps({
        "sha256": hashlib.sha256(dmg_bytes).hexdigest(),
        "bundle_id": "com.example.test", "build": "42",
        "team_id": "TEAM"}))
    monkeypatch.setattr(mod, "ARCHIVE", tmp_path / "archive")
    monkeypatch.setattr(mod, "ANALYSIS_ROOT", tmp_path / "analysis")
    monkeypatch.setattr(mod, "OUT_ROOT", tmp_path / "mac-app")
    map_path = tmp_path / "mac-app-map.json"
    monkeypatch.setattr(mod, "MAP_PATH", map_path)

    assert mod.main([]) == 0
    mmap = json.loads(map_path.read_text())
    # version is metadata on the single flat manifest, not a key/dir
    assert mmap["version"] == version
    assert mmap["build"] == "42"
    assert mmap["bundle_id"] == "com.example.test"
    assert mmap["dmg_sha256"] == hashlib.sha256(dmg_bytes).hexdigest()
    assert all(not k.startswith(version + "/") for k in mmap["files"])
    assert (tmp_path / "mac-app" / "command-catalog.txt").is_file()
    # hash gate: a second plain run skips and leaves the map untouched
    before = map_path.read_bytes()
    assert mod.main([]) == 0
    assert map_path.read_bytes() == before
