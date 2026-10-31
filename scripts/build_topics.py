#!/usr/bin/env python3
"""SHIM — this file is a compatibility entry point.

The implementation lives in the hatch_extract package
(src/hatch_extract/); this shim preserves the historical CLI so
existing callers (sync-skills.sh, the skills-nightly-checkin cron)
keep working unchanged. The original implementation is preserved
beside this file as build_topics.py.bak-20261031-080942 and in git history.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))


from hatch_extract.topics import main

if __name__ == "__main__":
    sys.exit(main())
