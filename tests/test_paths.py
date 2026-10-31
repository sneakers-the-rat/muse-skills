from hatch_extract.paths import clean_path, split_token, target_for


def test_clean_path_accepts_bundle_paths():
    assert clean_path("blocks/agent/core.md") == "blocks/agent/core.md"
    assert clean_path("session/peer_guidelines.md") == \
        "session/peer_guidelines.md"


def test_clean_path_rejects_bare_and_foreign():
    assert clean_path("README.md") is None  # no slash: a mention
    assert clean_path("random/thing.md") is None


def test_clean_path_unfuses_prefix():
    assert clean_path("are.session/x.md") == "session/x.md"


def test_target_for_roots():
    assert target_for("blocks/agent/core.md") == \
        "system_prompts/agent/core.md"
    assert target_for("browser/system.md") == \
        "binary-strings/browser/system.md"
    assert target_for("agent-definitions/x.toml") == \
        "binary-strings/agent-definitions/x.toml"
    assert target_for("memory/notes.md") is None  # SKIP_ROOTS


def test_target_for_new_subtrees():
    assert target_for("agent-prompts/a.md") == \
        "binary-strings/agent-prompts/a.md"
    assert target_for("prose-regions/region-00000001.txt") == \
        "binary-strings/prose-regions/region-00000001.txt"


def test_split_token_splits_fused_paths():
    parts = split_token("blocks/a.mdtemplates/b.yaml")
    assert parts[0][1] == "blocks/a.md"
    assert parts[1][1] == "templates/b.yaml"
    assert parts[1][2] is True
