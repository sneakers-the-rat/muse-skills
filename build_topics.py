#!/usr/bin/env python3
"""Build the topical views under topics/.

The archive's extractions sort by kind — embedded files by what
they are, curated strings by the curation that produced them — so
one subject scatters across several trees. A topic directory
regroups everything about one subject as SYMLINKS to the canonical
files, with a README that tells the subject's story in prose and
indexes the links. Nothing in a topic directory is a copy: the
content lives at the link targets, and the links are rebuilt from
the current archive on every sync, so a topic view can never go
stale — a source that disappears simply drops out of the index.

Topics here are hand-chosen groupings (which files belong to a
subject is a judgement, not a derivation), one builder per topic
below. The bot_challenge topic gathers the files produced by the
bot_challenge curation in extract_binary_strings.py — the entries
marked "topic": "bot_challenge" in binary-map.json — plus the
challenge guides and browser instructions the generic file
extraction recovered.
"""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from extract_binary_files import SLUGS  # the challenge-guide slugs


def rel_link(link_path, source_rel):
    """Create link_path as a relative symlink to REPO/source_rel.
    Returns True if the source exists and the link was made."""
    src = REPO / source_rel
    if not src.exists():
        return False
    target = Path(*([".."] * len(link_path.parent.relative_to(REPO)
                                .parts)), source_rel)
    link_path.parent.mkdir(parents=True, exist_ok=True)
    if link_path.is_symlink() or link_path.exists():
        link_path.unlink()
    link_path.symlink_to(target)
    return True


def build_bot_challenge():
    topic = REPO / "topics" / "bot_challenge"
    # start clean: this builder owns every symlink in the topic dir
    # (and its README); real files someone placed here are left alone
    if topic.exists():
        for p in topic.rglob("*"):
            if p.is_symlink():
                p.unlink()

    groups = {}   # group -> [(link_name, source_rel, blurb)]

    def add(group, link_name, source_rel, blurb=""):
        groups.setdefault(group, []).append(
            (link_name, source_rel, blurb))

    for slug in sorted(SLUGS):
        add("skill", f"{slug}.md", f"binary-skills/{slug}/SKILL.md")
    for name in ("bot_checks.md", "challenges.md"):
        add("browser-instructions", name,
            f"binary-strings/browser/instructions/{name}")
    for name in ("bot_challenge.assess.json", "bot_challenge.guide.json",
                 "bot_challenge.recover.json",
                 "browser.bot_challenge.json"):
        add("tools", name, f"binary-strings/tools/{name}")
    add("prompts", "roles.txt",
        "binary-strings/browser/bot_challenge/roles.txt")
    add("prompts", "classifier.txt",
        "binary-strings/browser/bot_challenge/classifier.txt")
    sites_dir = REPO / "binary-strings/browser/bot_challenge/sites"
    if sites_dir.is_dir():
        for f in sorted(sites_dir.iterdir()):
            if f.is_file():
                add("sites", f.name,
                    f"binary-strings/browser/bot_challenge/sites/"
                    f"{f.name}")
    add("reference", "enums.txt",
        "binary-strings/browser/bot_challenge/enums.txt")
    add("reference", "dispatch-fragments.txt",
        "binary-strings/browser/bot_challenge/dispatch-fragments.txt")
    add("reference", "errors.csv", "binary-strings/browser/errors.csv")

    made = {}
    for group, items in groups.items():
        for link_name, source_rel, _blurb in items:
            if rel_link(topic / group / link_name, source_rel):
                made.setdefault(group, []).append(
                    (link_name, source_rel))

    (topic / "README.md").write_text(readme_bot_challenge(made))
    total = sum(len(v) for v in made.values())
    print(f"topic bot_challenge: {total} links in {len(made)} groups")
    return made


def readme_bot_challenge(made):
    def index(group, intro):
        items = made.get(group, [])
        if not items:
            return ""
        lines = [f"## {group} ({len(items)})\n", intro, ""]
        for link_name, source_rel in items:
            lines.append(f"- [{link_name}]({group}/{link_name}) — "
                         f"`{source_rel}`")
        return "\n".join(lines) + "\n"

    return f"""# bot_challenge — the browser's bot-challenge machinery

A topical view of this archive. The extractions sort by kind —
embedded files by what they are, curated strings by the curation
that produced them — so one subject scatters across several trees.
This directory regroups everything about one subject, the browser
agent's bot-challenge machinery, as symlinks to the canonical
files, so the topic reads in one place. Nothing here is a copy:
follow a link to the real file, and edit it there. The string
material below was produced by the bot_challenge topical curation
(`extract_binary_strings.py`); in `binary-map.json` its entries
carry `"topic": "bot_challenge"`, which is what distinguishes a
topical curation from the generic file extraction's entries.

## The story

When the browser agent meets a CAPTCHA or a bot wall, it does not
improvise. A classifier — the Browser Task Tagger, whose prompt is
in `prompts/classifier.txt` — first decides what the page is: a
solvable challenge, a hard bot block, an ordinary page, and so on.
If it is a challenge, the work hands off to a dedicated specialist
role, `browser_bot_challenge`, whose registry entry is in
`prompts/roles.txt`. The specialist takes over the tab with a small
toolset of its own (`tools/`): `bot_challenge.assess` reads the
challenge's state and classifies the block, `bot_challenge.guide`
fetches the handling guide for that challenge type,
`browser.bot_challenge` performs the actions inside the challenge,
and `bot_challenge.recover` reloads the page or replaces the
environment when an attempt is spent.

The guides the specialist fetches are the per-challenge-type
playbooks in `skill/` — one for each challenge family, from
image grids and sliders to press-and-hold and waiting rooms. The
browser agent's own standing instructions for recognising checks
and challenges, and for conducting the handoff, are in
`browser-instructions/`. What varies by site — how a given site's
bot detection behaves and what has worked there — is recorded in
`sites/`, one note per site, split out of the full site guides.
`reference/` holds the surrounding vocabulary: the Browser* enum
and telemetry names, the dispatch-string fragments that name the
tool outside the main string pool, and the browser error lexicon
the regions yielded.

## Index

{index("skill", "The per-challenge-type handling guides — the playbooks `bot_challenge.guide` serves to the specialist.")}
{index("browser-instructions", "The browser agent's own embedded instructions about bot checks and challenges: when a page is a challenge, and how the handoff to the specialist works.")}
{index("tools", "The tool definitions: the specialist's three tools, and the browser tool through which it acts inside a challenge.")}
{index("prompts", "The prose that steers the machinery: the specialist's role-registry entry, and the Task Tagger classifier prompt that routes pages to it.")}
{index("sites", "Per-site bot-detection notes, split out of the site guides — what each site's defences do and what the guide says about them.")}
{index("reference", "Supporting vocabulary: enum/telemetry names, dispatch fragments, and the browser error lexicon.")}
"""


def main():
    build_bot_challenge()
    return 0


if __name__ == "__main__":
    sys.exit(main())
