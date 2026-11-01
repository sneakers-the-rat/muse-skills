"""RETIRED 2026-11-01 — compatibility shim.

The implementation lives in the binary-inspect library
(binary_inspect.extract, verbs extract / extract-curate /
extract-topics / extract-verify / extract-mechanisms on the
binary-inspect CLI). This module preserves the historical
hatch-extract CLI surface (verbs extract / curate / topics /
verify / mechanisms) by delegating to it. The original
implementation is preserved beside this file as
cli.py.bak-20261101 and in git history.
"""

import argparse
import pathlib
import sys

_BI_SRC = pathlib.Path.home() / "workspace" / "binary-inspect" / "src"
if str(_BI_SRC) not in sys.path:
    sys.path.insert(0, str(_BI_SRC))

from binary_inspect.extract.core import DEFAULT_BIN, REPO  # noqa: E402
from binary_inspect.extract.mechanisms import REGISTRY  # noqa: E402


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="hatch-extract")
    sub = ap.add_subparsers(dest="verb", required=True)
    p_ext = sub.add_parser("extract")
    p_ext.add_argument("--bin", default=str(DEFAULT_BIN))
    p_ext.add_argument("--repo", default=str(REPO))
    p_cur = sub.add_parser("curate")
    p_cur.add_argument("topic", choices=["bot_challenge",
                                         "browser_persona"])
    sub.add_parser("topics")
    p_ver = sub.add_parser("verify")
    p_ver.add_argument("repo", nargs="?", default=None)
    sub.add_parser("mechanisms")
    args = ap.parse_args(argv)

    if args.verb == "extract":
        from binary_inspect.extract.pipeline import run_extract
        from pathlib import Path
        return run_extract(repo=Path(args.repo),
                           bin_path=Path(args.bin))
    if args.verb == "curate":
        if args.topic == "bot_challenge":
            from binary_inspect.extract.curations.bot_challenge import main as c_main
        else:
            from binary_inspect.extract.curations.browser_persona import main as c_main
        return c_main()
    if args.verb == "topics":
        from binary_inspect.extract.topics import main as t_main
        return t_main()
    if args.verb == "verify":
        from binary_inspect.extract import verify
        if args.repo is not None:
            sys.argv = [sys.argv[0], args.repo]
        return verify.main()
    if args.verb == "mechanisms":
        for m in REGISTRY:
            print(f"{m['number']:>2}  {m['name']:<24} "
                  f"hatch_extract.mechanisms.{m['module']:<22} "
                  f"{m['blurb']}")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
