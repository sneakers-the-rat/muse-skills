"""RETIRED 2026-11-01 — compatibility shim (module alias).

The implementation lives in the binary-inspect library as
binary_inspect.extract.paths. This module aliases itself to
that module object, so existing imports (hatch_extract.paths)
and attribute patches behave exactly as they did against the
original single implementation. The original implementation is
preserved beside this file as paths.py.bak-20261101 and in git
history.
"""
import pathlib as _pathlib
import sys as _sys

_BI_SRC = _pathlib.Path.home() / "workspace" / "binary-inspect" / "src"
if str(_BI_SRC) not in _sys.path:
    _sys.path.insert(0, str(_BI_SRC))

import binary_inspect.extract.paths as _impl

_sys.modules[__name__] = _impl
