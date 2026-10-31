"""hatch-extract CLI: a thin wrapper over the library, shaped like
binary-inspect's CLI (one tool, verbs over one binary).

Verbs:
  extract            run the full extraction pipeline (mechanisms 1-13)
  curate <topic>     run a topical string curation (bot_challenge,
                     browser_persona)
  topics             rebuild the topical views under topics/
  verify [repo]      the archive content census (verify_archive)
  mechanisms         list the mechanism registry
"""

import argparse
import sys

from .core import DEFAULT_BIN, REPO
from .mechanisms import REGISTRY


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
        from .pipeline import run_extract
        from pathlib import Path
        return run_extract(repo=Path(args.repo),
                           bin_path=Path(args.bin))
    if args.verb == "curate":
        if args.topic == "bot_challenge":
            from .curations.bot_challenge import main as c_main
        else:
            from .curations.browser_persona import main as c_main
        return c_main()
    if args.verb == "topics":
        from .topics import main as t_main
        return t_main()
    if args.verb == "verify":
        from . import verify
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
