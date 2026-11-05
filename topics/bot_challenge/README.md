# bot_challenge — the browser's bot-challenge machinery

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


## browser-instructions (2)

The browser agent's own embedded instructions about bot checks and challenges: when a page is a challenge, and how the handoff to the specialist works.

- [bot_checks.md](../../binary-strings/browser/instructions/bot_checks.md) — `binary-strings/browser/instructions/bot_checks.md`
- [challenges.md](../../binary-strings/browser/instructions/challenges.md) — `binary-strings/browser/instructions/challenges.md`

## tools (4)

The tool definitions: the specialist's three tools, and the browser tool through which it acts inside a challenge.

- [bot_challenge.assess.json](../../binary-strings/tools/bot_challenge.assess.json) — `binary-strings/tools/bot_challenge.assess.json`
- [bot_challenge.guide.json](../../binary-strings/tools/bot_challenge.guide.json) — `binary-strings/tools/bot_challenge.guide.json`
- [bot_challenge.recover.json](../../binary-strings/tools/bot_challenge.recover.json) — `binary-strings/tools/bot_challenge.recover.json`
- [browser.bot_challenge.json](../../binary-strings/tools/browser.bot_challenge.json) — `binary-strings/tools/browser.bot_challenge.json`

## prompts (2)

The prose that steers the machinery: the specialist's role-registry entry, and the Task Tagger classifier prompt that routes pages to it.

- [roles.txt](../../binary-strings/browser/bot_challenge/roles.txt) — `binary-strings/browser/bot_challenge/roles.txt`
- [classifier.txt](../../binary-strings/browser/bot_challenge/classifier.txt) — `binary-strings/browser/bot_challenge/classifier.txt`


## reference (3)

Supporting vocabulary: enum/telemetry names, dispatch fragments, and the browser error lexicon.

- [enums.txt](../../binary-strings/browser/bot_challenge/enums.txt) — `binary-strings/browser/bot_challenge/enums.txt`
- [dispatch-fragments.txt](../../binary-strings/browser/bot_challenge/dispatch-fragments.txt) — `binary-strings/browser/bot_challenge/dispatch-fragments.txt`
- [errors.csv](../../binary-strings/browser/errors.csv) — `binary-strings/browser/errors.csv`

