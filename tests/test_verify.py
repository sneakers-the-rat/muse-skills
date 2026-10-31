import os

from hatch_extract import verify


def test_resolve_within_relative_and_absolute(tmp_path):
    link = tmp_path / "skills" / "x"
    assert verify.resolve_within(str(link), "../connectors/c") == \
        os.path.normpath(tmp_path / "connectors" / "c")
    assert verify.resolve_within(str(link), "/abs/path") == "/abs/path"


def test_file_set(tmp_path):
    (tmp_path / "a.txt").write_text("a")
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "b.txt").write_text("b")
    assert set(verify.file_set(str(tmp_path))) == {"a.txt",
                                                   "sub/b.txt"}


def test_check_connectors_matching(tmp_path, monkeypatch):
    live = tmp_path / "live"
    repo = tmp_path / "repo"
    (live / "demo").mkdir(parents=True)
    (live / "demo" / "f.md").write_text("same")
    (repo / "connectors" / "demo").mkdir(parents=True)
    (repo / "connectors" / "demo" / "f.md").write_text("same")
    monkeypatch.setattr(verify, "LIVE_CONN", str(live))
    verify.failures.clear()
    verify.check_connectors(str(repo))
    assert verify.failures == []


def test_check_connectors_detects_drift(tmp_path, monkeypatch):
    live = tmp_path / "live"
    repo = tmp_path / "repo"
    (live / "demo").mkdir(parents=True)
    (live / "demo" / "f.md").write_text("live")
    (repo / "connectors" / "demo").mkdir(parents=True)
    (repo / "connectors" / "demo" / "f.md").write_text("stale")
    monkeypatch.setattr(verify, "LIVE_CONN", str(live))
    verify.failures.clear()
    verify.check_connectors(str(repo))
    assert verify.failures  # sha mismatch reported
