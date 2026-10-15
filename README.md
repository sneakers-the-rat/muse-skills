# muse-skills — skill history archive

An hourly mechanical archive of Muse's own skill trees, mirrored from
the running image with symlinks resolved, so what is stored here is the
real skill file content, browsable in place:

- `skills/` — mirror of `/opt/hatch/skills` (the skills/connector
  namespace, with each link replaced by the content it names)
- `workflow-skills/` — mirror of `/opt/hatch/workflow-skills` (the
  agent-facing skill playbooks and their registry metadata)
- `connectors/` — mirror of the `/opt/hatch/connectors` directories that
  no symlink in `/opt/hatch/skills` resolves into: the connectors with no
  skill surface (currently `meta_catalog_search` and `stripe-link`). The
  set is recomputed every run — a connector that gains a skill symlink
  leaves this tree and is archived through `skills/` instead.

## Change volume

Lines added and removed per commit across the skill trees:

![Skill history plot](plot.svg)

## Daily summaries

See [CHANGELOG.md](CHANGELOG.md) — a nightly check-in summarizes each
day's commits under that day's heading, newest first.
