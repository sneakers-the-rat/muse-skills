"""Live-binary golden: when the live binary is the build the
pre-restructure archive was extracted from (the baseline recorded
by the prompt-census promotion), the package's mechanism 6 must
reproduce the archived agent definitions byte-for-byte. Skips
when the binary has rolled or the baseline is absent."""
import hashlib
import json
import pathlib

import pytest

from hatch_extract.core import DEFAULT_BIN, REPO, Binary
from hatch_extract.mechanisms.agent_definitions import agent_definitions

BASELINE = pathlib.Path(
    "/home/hatch/workspace/your_files/agent-prompt-census/promotion/"
    "baseline-archive.json")


@pytest.mark.skipif(not BASELINE.exists(), reason="no baseline recorded")
def test_agent_definitions_reproduce_archive():
    base = json.loads(BASELINE.read_text())
    b = Binary(DEFAULT_BIN)
    if b.sha256() != base["binary_sha256"]:
        pytest.skip("live binary has rolled past the baseline build")
    found, problems = agent_definitions(b.data)
    assert problems == []
    assert len(found) == base["agent_definitions"] == 87
    for aid, (_off, body) in found.items():
        target = f"binary-strings/agent-definitions/{aid}.toml"
        assert hashlib.sha256(body).hexdigest() == \
            base["hashes"][target]
    b.close()


@pytest.mark.skipif(not DEFAULT_BIN.exists(), reason="no live binary")
def test_live_binary_map_targets_exist():
    m = json.loads((REPO / "binary-map.json").read_text())
    for c in m["bins"][0]["contents"]:
        assert (REPO / c["target"]).exists(), c["target"]
