#!/usr/bin/env python3
"""SHIM — this file is a compatibility entry point.

The implementation lives in the binary-inspect library
(binary_inspect.extract); this shim preserves the historical CLI so
existing callers (sync-skills.sh, the skills-nightly-checkin cron)
keep working unchanged. The original implementation is preserved
beside this file as extract_binary_files.py.bak-20261031-080942 and in git history.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / "workspace" / "binary-inspect" / "src"))


# Legacy import surface: build_topics.py imported SLUGS from this
# module; keep the commonly used names importable here.
from binary_inspect.extract.paths import *  # noqa: F401,F403
from binary_inspect.extract.paths import (clean_path, split_token, target_for)  # noqa: F401
from binary_inspect.extract.mechanisms.agent_definitions import agent_definitions  # noqa: F401
from binary_inspect.extract.mechanisms.heuristic import census, validate  # noqa: F401
from binary_inspect.extract.elftools import elf_maps, lea_census  # noqa: F401
from binary_inspect.extract.pipeline import run_extract

if __name__ == "__main__":
    sys.exit(run_extract())
