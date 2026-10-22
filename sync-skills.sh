#!/bin/bash
# Hourly snapshot of Muse's skill trees into this git repo:
#   skills/          <- /opt/hatch/skills          (symlinks resolved)
#   workflow-skills/ <- /opt/hatch/workflow-skills (symlinks resolved)
#   docs/            <- ~/docs                     (symlinks resolved;
#                       added 2026-10-20 at the user's request, so the
#                       product docs are versioned alongside the skills)
#   connectors/      <- the /opt/hatch/connectors directories that NO
#                       symlink in /opt/hatch/skills resolves into — the
#                       connectors with no skill surface. Computed fresh
#                       every run, never a hard-coded list: the moment a
#                       connector gains a skill symlink it is archived
#                       through skills/ instead and drops out of here.
#   binary trees     <- extracted from the hatch binary itself by
#                       extract_binary_files.py (system-prompt/,
#                       binary-skills/, binary-tools/, binary-etc/,
#                       browser/, self_improvement/, artifacts/ plus
#                       binary-map.json, the provenance manifest — which
#                       binary, and the byte offset each file came from).
#                       New files landing in binary-etc/ are UNSORTED:
#                       they are held out of the commit (updates to
#                       already-versioned binary-etc files still commit)
#                       and reported on stdout as BINARY_ETC_UNVERSIONED
#                       lines, so the calling hook can ask the user to
#                       classify them.
# This repo is an archive of Muse's own skills over time; workspace-local
# custom skills are instance-specific and deliberately not archived here.
# Only these trees are mirrored or extracted; other repo files
# (README.md, CHANGELOG.md, plot.svg, these scripts) are maintained
# alongside and committed by the same `git add -A` sweep.
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
# --ignore-errors: without it, rsync skips the whole deletion phase when
# any file errors — and the permanently dangling links error every run,
# which would silently stop upstream deletions from ever being recorded.
# --no-owner/--no-group: source files are owned by nobody; we track
# content, not ownership. Deletions upstream are recorded as deletions.
#
# A dangling link is DATA, not an error to scrub (user, 2026-10-15): it
# records that the skill references a file this image doesn't ship. So
# after the content mirror, archive_links recreates every dangling
# source symlink as a symlink at the same path, and removes archive
# symlinks the source no longer backs (the link was deleted upstream, or
# its target shipped and rsync -L now stores the content instead). The
# invariant is: a symlink exists in the archive ONLY where the source
# link dangles — never as a substitute for content that resolves.
archive_links() {
  local src="$1" dest="$2" p rel
  while IFS= read -r -d '' p; do
    rel="${p#$dest/}"
    if [ ! -L "$src/$rel" ] || [ -e "$src/$rel" ]; then rm -f "$p"; fi
  done < <(find "$dest" -type l -print0)
  while IFS= read -r -d '' p; do
    rel="${p#$src/}"
    if [ ! -e "$p" ]; then
      mkdir -p "$dest/$(dirname "$rel")"
      ln -sfn "$(readlink "$p")" "$dest/$rel"
    fi
  done < <(find "$src" -type l -print0)
}

mirror() {
  local src="$1" dest="$2" rc=0
  mkdir -p "$dest"
  rsync -aL --delete --ignore-errors --no-owner --no-group --exclude='.git' "$src/" "$dest/" || rc=$?
  if [ "$rc" -ne 0 ] && [ "$rc" -ne 23 ] && [ "$rc" -ne 24 ]; then
    echo "rsync $src -> $dest failed with exit $rc" >&2
    exit "$rc"
  fi
  archive_links "$src" "$dest"
}
mirror /opt/hatch/skills "$REPO/skills"
mirror /opt/hatch/workflow-skills "$REPO/workflow-skills"
mirror "$HOME/docs" "$REPO/docs"

# Connectors with no skill surface. A connector directory is covered when
# at least one symlink in /opt/hatch/skills resolves to the directory
# itself or to a path inside it; every other connector is mirrored into
# connectors/<name>/ under the same rules as the skill trees. Archive
# directories whose connector has since gained a skill symlink (or has
# vanished upstream) are pruned, so connectors/ always holds exactly the
# currently-unlinked set — computed here, never listed by hand.
SKILL_TARGETS=()
while IFS= read -r l; do
  t="$(readlink -f "$l" 2>/dev/null)" && [ -n "$t" ] && SKILL_TARGETS+=("$t")
done < <(find /opt/hatch/skills -type l -print)
mkdir -p "$REPO/connectors"
UNLINKED=()
for c in /opt/hatch/connectors/*/; do
  name="$(basename "$c")"
  covered=0
  for t in ${SKILL_TARGETS[@]+"${SKILL_TARGETS[@]}"}; do
    case "$t" in
      "${c%/}"|"${c%/}/"*) covered=1; break ;;
    esac
  done
  if [ "$covered" -eq 0 ]; then
    UNLINKED+=("$name")
    mirror "${c%/}" "$REPO/connectors/$name"
  fi
done
for d in "$REPO/connectors"/*/; do
  [ -d "$d" ] || continue
  name="$(basename "$d")"
  keep=0
  for u in ${UNLINKED[@]+"${UNLINKED[@]}"}; do
    if [ "$u" = "$name" ]; then keep=1; break; fi
  done
  if [ "$keep" -eq 0 ]; then rm -rf "$d"; fi
done

# Binary extraction: pull the embedded prompt/skill/tool files out of
# the hatch binary into their repo trees and refresh binary-map.json.
# A failure here fails the whole snapshot (set -e), so a binary roll
# that breaks extraction is reported, never silently archived around.
python3 "$REPO/extract_binary_files.py"
python3 "$REPO/extract_binary_strings.py"

# binary-etc/ holds extracted files the user has not sorted yet. Updates
# to files already versioned there commit as usual, but a NEW file there
# is held out of the commit until the user classifies it (ignore it,
# commit it as-is, or say where it sorts). Held-out paths are printed as
# BINARY_ETC_UNVERSIONED lines for the calling hook to surface.
NEW_ETC=()
while IFS= read -r p; do
  [ -n "$p" ] && NEW_ETC+=("$p")
done < <(git -C "$REPO" ls-files --others --exclude-standard -- binary-etc)
for p in ${NEW_ETC[@]+"${NEW_ETC[@]}"}; do
  echo "BINARY_ETC_UNVERSIONED $p"
done

# Stage everything, then unstage the held-out binary-etc paths.
stage_all() {
  git -C "$REPO" add -A
  if [ "${#NEW_ETC[@]}" -gt 0 ]; then
    git -C "$REPO" reset -q -- "${NEW_ETC[@]}"
  fi
}

# Measure this run's skill-file diff (the two skill trees only): the
# counts are the plot's current point. Separate connectors, docs and
# binary-extraction counts keep a change in only one of those trees
# from being labelled (no changes).
stage_all
read -r ADDED REMOVED <<< "$(git -C "$REPO" diff --cached --numstat -- skills workflow-skills \
  | awk '{ if ($1 ~ /^[0-9]+$/) a += $1; if ($2 ~ /^[0-9]+$/) r += $2 } END { print a + 0, r + 0 }')"
read -r CONN_ADDED CONN_REMOVED <<< "$(git -C "$REPO" diff --cached --numstat -- connectors \
  | awk '{ if ($1 ~ /^[0-9]+$/) a += $1; if ($2 ~ /^[0-9]+$/) r += $2 } END { print a + 0, r + 0 }')"
read -r DOCS_ADDED DOCS_REMOVED <<< "$(git -C "$REPO" diff --cached --numstat -- docs \
  | awk '{ if ($1 ~ /^[0-9]+$/) a += $1; if ($2 ~ /^[0-9]+$/) r += $2 } END { print a + 0, r + 0 }')"
read -r BIN_ADDED BIN_REMOVED <<< "$(git -C "$REPO" diff --cached --numstat -- system-prompt binary-skills binary-tools binary-etc binary-strings browser self_improvement artifacts binary-map.json \
  | awk '{ if ($1 ~ /^[0-9]+$/) a += $1; if ($2 ~ /^[0-9]+$/) r += $2 } END { print a + 0, r + 0 }')"

# Regenerate the plot with this run's point appended, then stage it too.
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
python3 "$REPO/make_plot.py" --repo "$REPO" --out "$REPO/plot.svg" \
  --current-added "$ADDED" --current-removed "$REMOVED" --current-date "$TS"
stage_all

# Commit — the regenerated plot guarantees content, so no --allow-empty.
# If somehow nothing is staged, say so instead of papering over it.
if git -C "$REPO" diff --cached --quiet; then
  echo "nothing to commit at $TS (plot unchanged); skipping commit"
else
  if [ "$ADDED" -eq 0 ] && [ "$REMOVED" -eq 0 ] && [ "$CONN_ADDED" -eq 0 ] && [ "$CONN_REMOVED" -eq 0 ] && [ "$DOCS_ADDED" -eq 0 ] && [ "$DOCS_REMOVED" -eq 0 ] && [ "$BIN_ADDED" -eq 0 ] && [ "$BIN_REMOVED" -eq 0 ]; then
    git -C "$REPO" commit -q -m "skills snapshot $TS (no changes)"
  else
    git -C "$REPO" commit -q -m "skills snapshot $TS"
  fi
  echo "committed $(git -C "$REPO" rev-parse --short HEAD) at $TS (+$ADDED/-$REMOVED skill lines, +$CONN_ADDED/-$CONN_REMOVED connector lines, +$DOCS_ADDED/-$DOCS_REMOVED docs lines, +$BIN_ADDED/-$BIN_REMOVED binary lines)"
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
