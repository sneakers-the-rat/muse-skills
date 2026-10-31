#!/usr/bin/env python3
"""SHIM — this file is a compatibility entry point.

The implementation lives in the hatch_extract package
(src/hatch_extract/); this shim preserves the historical CLI so
existing callers (sync-skills.sh, the skills-nightly-checkin cron)
keep working unchanged. The original implementation is preserved
beside this file as binary_string_methods.py.bak-20261031-080942 and in git history.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))


from hatch_extract.strings_methods import *  # noqa: F401,F403
from hatch_extract.strings_methods import (  # noqa: F401
    PRINT_RUN, Registrar, already_done, anchored_window, balanced_json,
    catalog_schemas, catalog_tool_defs, check_binary, cst_fragments,
    error_lexicon, finish_manifest, in_regions, load_manifest,
    manifest_spans, own_entries, prune_owned, save_manifest,
    section_span, sections, split_section, window_run)
