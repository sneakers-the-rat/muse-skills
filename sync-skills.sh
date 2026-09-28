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

# Commit only if something actually changed.
git -C "$REPO" add -A
if git -C "$REPO" diff --cached --quiet; then
  echo "no changes since last snapshot"
else
  TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  git -C "$REPO" commit -q -m "skills snapshot $TS"
  echo "committed $(git -C "$REPO" rev-parse --short HEAD) at $TS"
fi
