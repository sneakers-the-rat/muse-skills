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

SCRIPT_DIR = Path(__file__).resolve().parent
REPO = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
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
            # Link straight at the canonical file, not at this
            # directory's symlink: GitHub renders a symlink as a
            # text blob showing its path, so a link to the symlink
            # costs a manual hop; the direct link clicks through.
            lines.append(f"- [{link_name}](../../{source_rel}) — "
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


def build_browser_persona():
    topic = REPO / "topics" / "browser_persona"
    if topic.exists():
        for p in topic.rglob("*"):
            if p.is_symlink():
                p.unlink()

    groups = {}

    def add(group, link_name, source_rel):
        groups.setdefault(group, []).append((link_name, source_rel))

    bp = "binary-strings/browser/persona"
    add("config", "global-config.yaml", f"{bp}/global-config.yaml")
    add("config", "default.yaml", "binary-etc/default.yaml")
    add("config", "site-personas.yaml", f"{bp}/site-personas.yaml")
    for domain in ("aa.com", "ebay.com", "macys.com"):
        add("config", f"{domain}-config.yaml",
            f"binary-strings/browser/site-config/{domain}/config.yaml")
    add("telemetry", "telemetry-fields.txt",
        f"{bp}/telemetry-fields.txt")
    add("schema", "structs.txt", f"{bp}/structs.txt")
    add("schema", "observed-fingerprint-paths.txt",
        f"{bp}/observed-fingerprint-paths.txt")
    add("implementation", "module-paths.txt", f"{bp}/module-paths.txt")
    add("related", "enums.txt",
        "binary-strings/browser/bot_challenge/enums.txt")

    made = {}
    for group, items in groups.items():
        for link_name, source_rel in items:
            if rel_link(topic / group / link_name, source_rel):
                made.setdefault(group, []).append(
                    (link_name, source_rel))

    (topic / "README.md").write_text(readme_browser_persona(made))
    total = sum(len(v) for v in made.values())
    print(f"topic browser_persona: {total} links in {len(made)} groups")
    return made


def readme_browser_persona(made):
    def index(group, intro):
        items = made.get(group, [])
        if not items:
            return ""
        lines = [f"## {group} ({len(items)})\n", intro, ""]
        for link_name, source_rel in items:
            lines.append(f"- [{link_name}](../../{source_rel}) — "
                         f"`{source_rel}`")
        return "\n".join(lines) + "\n"

    return f"""# browser_persona — the identity the browser presents

A topical view of this archive, regrouping everything recovered
about the browser's persona system as symlinks to the canonical
files. The string material was produced by the browser_persona
topical curation (`scripts/extract_binary_persona.py`); in
`binary-map.json` its entries carry `"topic": "browser_persona"`.

## The story

The browser does not present itself to pages as what it is. It
presents a **persona**: a coherent fabricated machine — operating
system, user-agent platform and high-entropy details, hardware
concurrency, device memory, WebGL renderer, screen size, timezone
and locale — chosen per task and held consistent, because bot
defences cross-examine exactly those surfaces for contradictions.

Personas are organised by **lane**. The embedded global
configuration (`config/default.yaml`) divides the world into
realtime work (chat and side chats) and background work (cron,
proactivity, Spaces), each with its own pool of browsers and its
own default persona: the realtime lane presents Linux, the
background lane presents Windows, and proactivity — always on the
local browser — presents Linux. The whole system is gated by a
kill switch, `hatch_browser_enhanced`: with it off, every lane
falls back to presenting native Linux. Individual sites can pin a
different persona: aa.com, ebay.com and macys.com all present
macOS on the realtime lane (`config/site-personas.yaml`).

Within a lane, the identity a document sees is **derived from a
seed in a scope** (`DocumentPersonaSeedIdentity`: a scope and a
seed id). Seeding is what makes the persona a person rather than a
dice roll — the same scope keeps presenting the same machine,
visit after visit, instead of re-rolling its renderer and screen
size on every page load. Selection, attribution (why this
persona), the operating system and the full parameter set are all
recorded as telemetry (`telemetry/`): a `browser_document_persona_*`
field family covering selection, attribution, config and seed
state, with a status and a reason at every step.

And the system **checks its own story**. A fingerprint probe —
its collector script hashed and versioned — runs in the document
and reads back what the page actually observes on each surface
(`schema/observed-fingerprint-paths.txt`), producing a
`DocumentFingerprintObservation` that lines the seeded identity up
against the observed one. The schema of that observation, and of
the request/egress records it travels with, is in `schema/`. The
implementation is a protocol-level module, `browser_persona/`
(`implementation/`), split into the two halves of the trick:
`native_document.rs` puts the persona into the page, and
`observed_fingerprint.rs` reads back what the page sees.

One honest limit: the collector script itself is not in this
binary. Its output schema is here, and the runtime records the
collector's SHA-256, but the script's text lives elsewhere —
presumably with the browser service that runs it.

The persona is only half of what a site sees; the other half is
the network route, and the same global configuration orders the
egress chain (default first, residential via Oxylabs as fallback)
that the per-site configs can invert and that the bot-challenge
recovery machinery moves between. That story is told in the
bot_challenge topic.

## Index

{index("config", "The configuration layer: the global lane/persona/egress defaults, and the per-site pins that override them.")}
{index("telemetry", "The telemetry field families that record persona selection, seeding and fingerprint probing — the pipeline as the instrumentation names it.")}
{index("schema", "The observation schemas: the persona seed identity, the fingerprint observation, and the exact fingerprint surfaces the probe reads back.")}
{index("implementation", "Where the system lives in the source tree: the browser_persona protocol module.")}
{index("related", "Neighbouring material: the enum/telemetry vocabulary where the persona structs were first spotted.")}
"""


def main():
    build_bot_challenge()
    build_browser_persona()
    return 0


if __name__ == "__main__":
    sys.exit(main())
