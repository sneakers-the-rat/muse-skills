#!/bin/bash
# Hourly snapshot of /opt/hatch/skills into this git repo.
# Tracks how skill prompts/configs change over time; only deltas are stored.
# Safe to run as often as you like — commits only when content changed.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="/opt/hatch/skills"
DEST="$REPO/skills"

# First run: init the repo.
if [ ! -d "$REPO/.git" ]; then
  mkdir -p "$DEST"
  git -C "$REPO" init -q
  git -C "$REPO" config user.name "skill-history"
  git -C "$REPO" config user.email "skill-history@local"
fi

# Mirror the source tree (deletions upstream are recorded as deletions).
# --no-owner/--no-group: source files are owned by nobody; we track content, not ownership.
mkdir -p "$DEST"
rsync -a --delete --no-owner --no-group --exclude='.git' "$SRC/" "$DEST/"

# Always commit — an empty commit is a heartbeat proving the script ran
# and the copy is fresh. Empty commits store no new objects.
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
git -C "$REPO" add -A
if git -C "$REPO" diff --cached --quiet; then
  git -C "$REPO" commit -q --allow-empty -m "skills snapshot $TS (no changes)"
  echo "heartbeat $(git -C "$REPO" rev-parse --short HEAD) at $TS (no changes)"
else
  git -C "$REPO" commit -q -m "skills snapshot $TS"
  echo "committed $(git -C "$REPO" rev-parse --short HEAD) at $TS"
fi

# Push to GitHub. Auth is a write-scoped deploy key for this repo only
# (see core.sshCommand in the repo config). A failed push fails the
# script so the scheduled run reports it; the local commit is kept and
# the next run retries.
git -C "$REPO" push -q origin main
echo "pushed to origin/main"
