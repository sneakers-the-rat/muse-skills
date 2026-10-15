#!/bin/bash
# Hourly snapshot of Muse's skill trees into this git repo:
#   skills/          <- /opt/hatch/skills          (symlinks resolved)
#   workflow-skills/ <- /opt/hatch/workflow-skills (symlinks resolved)
# This repo is an archive of Muse's own skills over time; workspace-local
# custom skills are instance-specific and deliberately not archived here.
# Only the two trees are mirrored; other repo files (README.md,
# CHANGELOG.md, plot.svg, these scripts) are maintained alongside and
# committed by the same `git add -A` sweep.
# Every run makes a real commit: plot.svg always gains the current run's
# point, so there are no empty heartbeat commits. When the skill files
# themselves did not change, the commit message says (no changes).
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# First run: init the repo.
if [ ! -d "$REPO/.git" ]; then
  mkdir -p "$REPO/skills"
  git -C "$REPO" init -q
  git -C "$REPO" config user.name "skill-history"
  git -C "$REPO" config user.email "skill-history@local"
fi

# Mirror a source tree, resolving symlinks (-L / --copy-links): the repo
# stores real file content at the paths the links name, so the trees stay
# browsable and content-complete. Links whose targets are not shipped in
# this image dangle; rsync skips just those (exit 23/24) and the mirror
# otherwise succeeds — those two codes are tolerated, anything else fails.
# --no-owner/--no-group: source files are owned by nobody; we track
# content, not ownership. Deletions upstream are recorded as deletions.
mirror() {
  local src="$1" dest="$2" rc=0
  mkdir -p "$dest"
  rsync -aL --delete --no-owner --no-group --exclude='.git' "$src/" "$dest/" || rc=$?
  if [ "$rc" -ne 0 ] && [ "$rc" -ne 23 ] && [ "$rc" -ne 24 ]; then
    echo "rsync $src -> $dest failed with exit $rc" >&2
    exit "$rc"
  fi
}
mirror /opt/hatch/skills "$REPO/skills"
mirror /opt/hatch/workflow-skills "$REPO/workflow-skills"

# Measure this run's skill-file diff (the two trees only): the counts are
# the plot's current point and decide the (no changes) message.
git -C "$REPO" add -A
read -r ADDED REMOVED <<< "$(git -C "$REPO" diff --cached --numstat -- skills workflow-skills \
  | awk '{ if ($1 ~ /^[0-9]+$/) a += $1; if ($2 ~ /^[0-9]+$/) r += $2 } END { print a + 0, r + 0 }')"

# Regenerate the plot with this run's point appended, then stage it too.
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
python3 "$REPO/make_plot.py" --repo "$REPO" --out "$REPO/plot.svg" \
  --current-added "$ADDED" --current-removed "$REMOVED" --current-date "$TS"
git -C "$REPO" add -A

# Commit — the regenerated plot guarantees content, so no --allow-empty.
# If somehow nothing is staged, say so instead of papering over it.
if git -C "$REPO" diff --cached --quiet; then
  echo "nothing to commit at $TS (plot unchanged); skipping commit"
else
  if [ "$ADDED" -eq 0 ] && [ "$REMOVED" -eq 0 ]; then
    git -C "$REPO" commit -q -m "skills snapshot $TS (no changes)"
  else
    git -C "$REPO" commit -q -m "skills snapshot $TS"
  fi
  echo "committed $(git -C "$REPO" rev-parse --short HEAD) at $TS (+$ADDED/-$REMOVED skill lines)"
fi

# Push to GitHub. Auth is a write-scoped deploy key for this repo only
# (see core.sshCommand in the repo config). First try: the configured
# sshCommand (Sentinel egress proxy). If that fails, retry once through
# the Oracle relay SOCKS forward (127.0.0.1:1080, relay-egress-socks.service)
# per the user's 2026-10-06 standing rule: when egress is wedged, route
# around the proxy through fedi-relay (159.54.176.80). Only if both fail
# does the script fail; the local commit is kept and the next run retries.
if git -C "$REPO" push -q origin main; then
  echo "pushed to origin/main"
else
  echo "primary push failed; retrying through Oracle relay SOCKS (127.0.0.1:1080)" >&2
  SSH_CMD="$(git -C "$REPO" config core.sshCommand)"
  RELAY_SSH_CMD="${SSH_CMD//nc -X connect -x 198.19.0.1:3128/nc -X 5 -x 127.0.0.1:1080}"
  if [ "$RELAY_SSH_CMD" = "$SSH_CMD" ]; then
    echo "could not derive relay sshCommand from core.sshCommand; giving up" >&2
    exit 1
  fi
  git -C "$REPO" -c core.sshCommand="$RELAY_SSH_CMD" push -q origin main
  echo "pushed to origin/main via Oracle relay"
fi
