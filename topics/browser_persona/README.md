# browser_persona — the identity the browser presents

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


## telemetry (1)

The telemetry field families that record persona selection, seeding and fingerprint probing — the pipeline as the instrumentation names it.

- [telemetry-fields.txt](../../binary-strings/browser/persona/telemetry-fields.txt) — `binary-strings/browser/persona/telemetry-fields.txt`

## schema (2)

The observation schemas: the persona seed identity, the fingerprint observation, and the exact fingerprint surfaces the probe reads back.

- [structs.txt](../../binary-strings/browser/persona/structs.txt) — `binary-strings/browser/persona/structs.txt`
- [observed-fingerprint-paths.txt](../../binary-strings/browser/persona/observed-fingerprint-paths.txt) — `binary-strings/browser/persona/observed-fingerprint-paths.txt`

## implementation (1)

Where the system lives in the source tree: the browser_persona protocol module.

- [module-paths.txt](../../binary-strings/browser/persona/module-paths.txt) — `binary-strings/browser/persona/module-paths.txt`

## related (1)

Neighbouring material: the enum/telemetry vocabulary where the persona structs were first spotted.

- [enums.txt](../../binary-strings/browser/bot_challenge/enums.txt) — `binary-strings/browser/bot_challenge/enums.txt`

