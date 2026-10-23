#!/usr/bin/env python3
"""Content census for the skills archive — the nightly check-in's evidence.

Usage: verify_archive.py [repo_root]   (default: the repo this file lives in)

Verifies the archive against the LIVE trees, not against the sync's own
model of them:

1. CONNECTORS: every live /opt/hatch/connectors/<name> directory is
   present under <repo>/connectors/<name>, the relative file sets are
   identical, every archived file is a real file (never a symlink), and
   every file's sha256 matches the live file.
2. SKILL LINKS, for skills/ and workflow-skills/:
   - A live source symlink that resolves into a connector MUST appear in
     the archive as a relative symlink that resolves INSIDE the checkout
     to <repo>/connectors/... and to content that exists.
   - An archived symlink stored verbatim (absolute target) is allowed
     ONLY as dangling data: the live source has the identical link at the
     same path and its target does not ship in this image.
   - Anything else — an absolute link whose target ships, a link that
     resolves inside the checkout to somewhere other than connectors/,
     a connector link missing from the archive — is a failure.

Prints one VERIFY line per section and a final "VERIFY RESULT: PASS" or
"VERIFY RESULT: FAIL (n failures)" with one FAIL line per problem.
Exit code 0 on PASS, 1 on FAIL.
"""
import hashlib
import os
import sys

LIVE_CONN = "/opt/hatch/connectors"
TREES = [("skills", "/opt/hatch/skills"), ("workflow-skills", "/opt/hatch/workflow-skills")]

failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL: " + msg)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def file_set(root):
    out = {}
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            p = os.path.join(dirpath, name)
            out[os.path.relpath(p, root)] = p
    return out


def check_connectors(repo):
    live_names = sorted(d for d in os.listdir(LIVE_CONN)
                          if os.path.isdir(os.path.join(LIVE_CONN, d)))
    repo_conn = os.path.join(repo, "connectors")
    repo_names = sorted(d for d in os.listdir(repo_conn)
                          if os.path.isdir(os.path.join(repo_conn, d))
                          and not os.path.islink(os.path.join(repo_conn, d))) \
        if os.path.isdir(repo_conn) else []
    for name in live_names:
        if name not in repo_names:
            fail(f"connectors/{name}: live connector missing from archive")
    for name in repo_names:
        if name not in live_names:
            fail(f"connectors/{name}: archived but no longer shipped live")
    total_files = 0
    ok = 0
    for name in live_names:
        if name not in repo_names:
            continue
        live_files = file_set(os.path.join(LIVE_CONN, name))
        repo_files = file_set(os.path.join(repo_conn, name))
        if set(live_files) != set(repo_files):
            missing = sorted(set(live_files) - set(repo_files))
            extra = sorted(set(repo_files) - set(live_files))
            if missing:
                fail(f"connectors/{name}: {len(missing)} live files missing from archive, e.g. {missing[0]}")
            if extra:
                fail(f"connectors/{name}: {len(extra)} archived files not shipped live, e.g. {extra[0]}")
        for rel, live_path in live_files.items():
            repo_path = repo_files.get(rel)
            if repo_path is None:
                continue
            total_files += 1
            if os.path.islink(repo_path):
                fail(f"connectors/{name}/{rel}: stored as a symlink, not real content")
            elif sha256(live_path) != sha256(repo_path):
                fail(f"connectors/{name}/{rel}: content differs from live (sha256 mismatch)")
            else:
                ok += 1
    print(f"VERIFY connectors: {len(repo_names)}/{len(live_names)} connectors present, "
          f"{ok}/{total_files} files hash-identical")


def resolve_within(link_path, target):
    """Absolute-normalized path a symlink points at, resolved lexically."""
    if os.path.isabs(target):
        return os.path.normpath(target)
    return os.path.normpath(os.path.join(os.path.dirname(link_path), target))


def check_tree(repo, tree, live_root, live_conn_names):
    repo_root = os.path.join(repo, tree)
    repo_links = {}
    for dirpath, dirnames, filenames in os.walk(repo_root):
        for name in dirnames + filenames:
            p = os.path.join(dirpath, name)
            if os.path.islink(p):
                repo_links[os.path.relpath(p, repo_root)] = p
    live_links = {}
    for dirpath, dirnames, filenames in os.walk(live_root):
        for name in dirnames + filenames:
            p = os.path.join(dirpath, name)
            if os.path.islink(p):
                live_links[os.path.relpath(p, live_root)] = p

    def live_resolved(p):
        return os.path.realpath(p)

    def into_connector(resolved):
        # A link "into a connector" only counts when the connector it
        # names actually ships in this image. A link naming a connector
        # this image does not ship dangles live, and is data (below).
        if not resolved.startswith(LIVE_CONN + "/"):
            return False
        return resolved[len(LIVE_CONN) + 1:].split("/")[0] in live_conn_names

    n_conn_links = 0
    n_data_links = 0
    # Forward: every live connector link must be archived as an
    # in-checkout relative link into connectors/.
    for rel, lp in sorted(live_links.items()):
        if not into_connector(live_resolved(lp)):
            continue
        rp = repo_links.get(rel)
        if rp is None:
            fail(f"{tree}/{rel}: live connector link missing from archive")
            continue
        target = os.readlink(rp)
        if os.path.isabs(target):
            fail(f"{tree}/{rel}: archived as ABSOLUTE link -> {target} "
                 f"(points at the live image, not the backup)")
            continue
        resolved = resolve_within(rp, target)
        conn_root = os.path.join(repo, "connectors")
        if not (resolved == conn_root or resolved.startswith(conn_root + "/")):
            fail(f"{tree}/{rel}: link -> {target} resolves outside the repo connectors/ tree")
        elif not os.path.exists(resolved):
            fail(f"{tree}/{rel}: link -> {target} does not resolve within the checkout")
        else:
            n_conn_links += 1
    # Backward: every archived link must be justified — either a connector
    # link (checked above) or verbatim dangling data from the source.
    for rel, rp in sorted(repo_links.items()):
        lp = live_links.get(rel)
        if lp is not None and into_connector(live_resolved(lp)):
            continue  # connector link, checked above
        target = os.readlink(rp)
        if lp is not None and os.readlink(lp) == target and not os.path.exists(lp):
            n_data_links += 1  # verbatim dangling source link: data
            continue
        resolved = resolve_within(rp, target)
        if os.path.exists(resolved) and resolved.startswith(repo + "/"):
            fail(f"{tree}/{rel}: content stored as a link -> {target} instead of real content")
        elif os.path.isabs(target) and os.path.exists(target):
            fail(f"{tree}/{rel}: absolute link -> {target} whose target SHIPS in this image; "
                 f"content must be archived, not linked")
        elif lp is None:
            fail(f"{tree}/{rel}: archive link with no live source link backing it")
        else:
            fail(f"{tree}/{rel}: archive link -> {target} differs from live source link -> {os.readlink(lp)}")
    print(f"VERIFY {tree} links: {n_conn_links} connector links resolve in-checkout, "
          f"{n_data_links} dangling data links, {len(repo_links)} archive links total")


def main():
    repo = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else \
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not os.path.isdir(os.path.join(repo, ".git")) and len(sys.argv) <= 1:
        print(f"FAIL: {repo} does not look like the archive repo")
        return 1
    check_connectors(repo)
    live_conn_names = {d for d in os.listdir(LIVE_CONN)
                       if os.path.isdir(os.path.join(LIVE_CONN, d))}
    for tree, live_root in TREES:
        check_tree(repo, tree, live_root, live_conn_names)
    if failures:
        print(f"VERIFY RESULT: FAIL ({len(failures)} failures)")
        return 1
    print("VERIFY RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
