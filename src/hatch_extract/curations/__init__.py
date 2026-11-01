"""RETIRED 2026-11-01 — compatibility shim.

The implementation lives in the binary-inspect library as
binary_inspect.extract.curations; this module re-exports it so
existing imports (hatch_extract.curations) keep working unchanged.
The original implementation is preserved beside this file as
__init__.py.bak-20261101 and in git history.
"""
import pathlib as _pathlib
import sys as _sys

_BI_SRC = _pathlib.Path.home() / "workspace" / "binary-inspect" / "src"
if str(_BI_SRC) not in _sys.path:
    _sys.path.insert(0, str(_BI_SRC))

import binary_inspect.extract.curations as _impl

for _k, _v in _impl.__dict__.items():
    if _k not in ("__name__", "__package__", "__loader__", "__spec__",
                  "__file__", "__cached__", "__builtins__", "__doc__",
                  "__path__"):
        globals()[_k] = _v
del _k, _v, _impl
