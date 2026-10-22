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

## skill (20)

The per-challenge-type handling guides — the playbooks `bot_challenge.guide` serves to the specialist.

- [arithmetic-and-counting.md](skill/arithmetic-and-counting.md) — `binary-skills/arithmetic-and-counting/SKILL.md`
- [audio-challenge.md](skill/audio-challenge.md) — `binary-skills/audio-challenge/SKILL.md`
- [automatic-check.md](skill/automatic-check.md) — `binary-skills/automatic-check/SKILL.md`
- [block-page.md](skill/block-page.md) — `binary-skills/block-page/SKILL.md`
- [game-puzzle.md](skill/game-puzzle.md) — `binary-skills/game-puzzle/SKILL.md`
- [icon-order.md](skill/icon-order.md) — `binary-skills/icon-order/SKILL.md`
- [image-click.md](skill/image-click.md) — `binary-skills/image-click/SKILL.md`
- [image-grid.md](skill/image-grid.md) — `binary-skills/image-grid/SKILL.md`
- [network-block.md](skill/network-block.md) — `binary-skills/network-block/SKILL.md`
- [page-load-failure.md](skill/page-load-failure.md) — `binary-skills/page-load-failure/SKILL.md`
- [path-drawing.md](skill/path-drawing.md) — `binary-skills/path-drawing/SKILL.md`
- [press-and-hold.md](skill/press-and-hold.md) — `binary-skills/press-and-hold/SKILL.md`
- [rotation-puzzle.md](skill/rotation-puzzle.md) — `binary-skills/rotation-puzzle/SKILL.md`
- [sign-in-check.md](skill/sign-in-check.md) — `binary-skills/sign-in-check/SKILL.md`
- [slider-puzzle.md](skill/slider-puzzle.md) — `binary-skills/slider-puzzle/SKILL.md`
- [soft-block.md](skill/soft-block.md) — `binary-skills/soft-block/SKILL.md`
- [start-gate.md](skill/start-gate.md) — `binary-skills/start-gate/SKILL.md`
- [text-captcha.md](skill/text-captcha.md) — `binary-skills/text-captcha/SKILL.md`
- [verification-checkbox.md](skill/verification-checkbox.md) — `binary-skills/verification-checkbox/SKILL.md`
- [waiting-room.md](skill/waiting-room.md) — `binary-skills/waiting-room/SKILL.md`

## browser-instructions (2)

The browser agent's own embedded instructions about bot checks and challenges: when a page is a challenge, and how the handoff to the specialist works.

- [bot_checks.md](browser-instructions/bot_checks.md) — `binary-strings/browser/instructions/bot_checks.md`
- [challenges.md](browser-instructions/challenges.md) — `binary-strings/browser/instructions/challenges.md`

## tools (4)

The tool definitions: the specialist's three tools, and the browser tool through which it acts inside a challenge.

- [bot_challenge.assess.json](tools/bot_challenge.assess.json) — `binary-strings/tools/bot_challenge.assess.json`
- [bot_challenge.guide.json](tools/bot_challenge.guide.json) — `binary-strings/tools/bot_challenge.guide.json`
- [bot_challenge.recover.json](tools/bot_challenge.recover.json) — `binary-strings/tools/bot_challenge.recover.json`
- [browser.bot_challenge.json](tools/browser.bot_challenge.json) — `binary-strings/tools/browser.bot_challenge.json`

## prompts (2)

The prose that steers the machinery: the specialist's role-registry entry, and the Task Tagger classifier prompt that routes pages to it.

- [roles.txt](prompts/roles.txt) — `binary-strings/browser/bot_challenge/roles.txt`
- [classifier.txt](prompts/classifier.txt) — `binary-strings/browser/bot_challenge/classifier.txt`

## sites (60)

Per-site bot-detection notes, split out of the site guides — what each site's defences do and what the guide says about them.

- [affirm.com.md](sites/affirm.com.md) — `binary-strings/browser/bot_challenge/sites/affirm.com.md`
- [amazon.com.md](sites/amazon.com.md) — `binary-strings/browser/bot_challenge/sites/amazon.com.md`
- [apple.com.md](sites/apple.com.md) — `binary-strings/browser/bot_challenge/sites/apple.com.md`
- [baidu.com.md](sites/baidu.com.md) — `binary-strings/browser/bot_challenge/sites/baidu.com.md`
- [bestbuy.com.md](sites/bestbuy.com.md) — `binary-strings/browser/bot_challenge/sites/bestbuy.com.md`
- [bing.com.md](sites/bing.com.md) — `binary-strings/browser/bot_challenge/sites/bing.com.md`
- [booking.com.md](sites/booking.com.md) — `binary-strings/browser/bot_challenge/sites/booking.com.md`
- [cdninstagram.com.md](sites/cdninstagram.com.md) — `binary-strings/browser/bot_challenge/sites/cdninstagram.com.md`
- [chatgpt.com.md](sites/chatgpt.com.md) — `binary-strings/browser/bot_challenge/sites/chatgpt.com.md`
- [cloudflare.com.md](sites/cloudflare.com.md) — `binary-strings/browser/bot_challenge/sites/cloudflare.com.md`
- [costco.com.md](sites/costco.com.md) — `binary-strings/browser/bot_challenge/sites/costco.com.md`
- [craigslist.org.md](sites/craigslist.org.md) — `binary-strings/browser/bot_challenge/sites/craigslist.org.md`
- [duckduckgo.com.md](sites/duckduckgo.com.md) — `binary-strings/browser/bot_challenge/sites/duckduckgo.com.md`
- [ebay.com.md](sites/ebay.com.md) — `binary-strings/browser/bot_challenge/sites/ebay.com.md`
- [expedia.com.md](sites/expedia.com.md) — `binary-strings/browser/bot_challenge/sites/expedia.com.md`
- [facebook.com.md](sites/facebook.com.md) — `binary-strings/browser/bot_challenge/sites/facebook.com.md`
- [fbcdn.net.md](sites/fbcdn.net.md) — `binary-strings/browser/bot_challenge/sites/fbcdn.net.md`
- [google.com.md](sites/google.com.md) — `binary-strings/browser/bot_challenge/sites/google.com.md`
- [googlevideo.com.md](sites/googlevideo.com.md) — `binary-strings/browser/bot_challenge/sites/googlevideo.com.md`
- [grab.com.md](sites/grab.com.md) — `binary-strings/browser/bot_challenge/sites/grab.com.md`
- [greenhouse.io.md](sites/greenhouse.io.md) — `binary-strings/browser/bot_challenge/sites/greenhouse.io.md`
- [homedepot.com.md](sites/homedepot.com.md) — `binary-strings/browser/bot_challenge/sites/homedepot.com.md`
- [icloud.com.md](sites/icloud.com.md) — `binary-strings/browser/bot_challenge/sites/icloud.com.md`
- [indeed.com.md](sites/indeed.com.md) — `binary-strings/browser/bot_challenge/sites/indeed.com.md`
- [instacart.com.md](sites/instacart.com.md) — `binary-strings/browser/bot_challenge/sites/instacart.com.md`
- [instagram.com.md](sites/instagram.com.md) — `binary-strings/browser/bot_challenge/sites/instagram.com.md`
- [jd.com.md](sites/jd.com.md) — `binary-strings/browser/bot_challenge/sites/jd.com.md`
- [klaviyo.com.md](sites/klaviyo.com.md) — `binary-strings/browser/bot_challenge/sites/klaviyo.com.md`
- [linkedin.com.md](sites/linkedin.com.md) — `binary-strings/browser/bot_challenge/sites/linkedin.com.md`
- [loblaws.ca.md](sites/loblaws.ca.md) — `binary-strings/browser/bot_challenge/sites/loblaws.ca.md`
- [microsoft.com.md](sites/microsoft.com.md) — `binary-strings/browser/bot_challenge/sites/microsoft.com.md`
- [naver.com.md](sites/naver.com.md) — `binary-strings/browser/bot_challenge/sites/naver.com.md`
- [offerup.com.md](sites/offerup.com.md) — `binary-strings/browser/bot_challenge/sites/offerup.com.md`
- [openai.com.md](sites/openai.com.md) — `binary-strings/browser/bot_challenge/sites/openai.com.md`
- [paypal.com.md](sites/paypal.com.md) — `binary-strings/browser/bot_challenge/sites/paypal.com.md`
- [pinimg.com.md](sites/pinimg.com.md) — `binary-strings/browser/bot_challenge/sites/pinimg.com.md`
- [pinterest.com.md](sites/pinterest.com.md) — `binary-strings/browser/bot_challenge/sites/pinterest.com.md`
- [qualtrics.com.md](sites/qualtrics.com.md) — `binary-strings/browser/bot_challenge/sites/qualtrics.com.md`
- [rakuten.co.jp.md](sites/rakuten.co.jp.md) — `binary-strings/browser/bot_challenge/sites/rakuten.co.jp.md`
- [reddit.com.md](sites/reddit.com.md) — `binary-strings/browser/bot_challenge/sites/reddit.com.md`
- [resy.com.md](sites/resy.com.md) — `binary-strings/browser/bot_challenge/sites/resy.com.md`
- [shop.app.md](sites/shop.app.md) — `binary-strings/browser/bot_challenge/sites/shop.app.md`
- [shopback.com.md](sites/shopback.com.md) — `binary-strings/browser/bot_challenge/sites/shopback.com.md`
- [shopify.com.md](sites/shopify.com.md) — `binary-strings/browser/bot_challenge/sites/shopify.com.md`
- [snapchat.com.md](sites/snapchat.com.md) — `binary-strings/browser/bot_challenge/sites/snapchat.com.md`
- [starbucks.com.md](sites/starbucks.com.md) — `binary-strings/browser/bot_challenge/sites/starbucks.com.md`
- [stripe.com.md](sites/stripe.com.md) — `binary-strings/browser/bot_challenge/sites/stripe.com.md`
- [target.com.md](sites/target.com.md) — `binary-strings/browser/bot_challenge/sites/target.com.md`
- [temu.com.md](sites/temu.com.md) — `binary-strings/browser/bot_challenge/sites/temu.com.md`
- [tiktok.com.md](sites/tiktok.com.md) — `binary-strings/browser/bot_challenge/sites/tiktok.com.md`
- [tradingview.com.md](sites/tradingview.com.md) — `binary-strings/browser/bot_challenge/sites/tradingview.com.md`
- [turo.com.md](sites/turo.com.md) — `binary-strings/browser/bot_challenge/sites/turo.com.md`
- [twimg.com.md](sites/twimg.com.md) — `binary-strings/browser/bot_challenge/sites/twimg.com.md`
- [united.com.md](sites/united.com.md) — `binary-strings/browser/bot_challenge/sites/united.com.md`
- [walmart.com.md](sites/walmart.com.md) — `binary-strings/browser/bot_challenge/sites/walmart.com.md`
- [x.com.md](sites/x.com.md) — `binary-strings/browser/bot_challenge/sites/x.com.md`
- [yahoo.co.jp.md](sites/yahoo.co.jp.md) — `binary-strings/browser/bot_challenge/sites/yahoo.co.jp.md`
- [yahoo.com.md](sites/yahoo.com.md) — `binary-strings/browser/bot_challenge/sites/yahoo.com.md`
- [youtube.com.md](sites/youtube.com.md) — `binary-strings/browser/bot_challenge/sites/youtube.com.md`
- [zillow.com.md](sites/zillow.com.md) — `binary-strings/browser/bot_challenge/sites/zillow.com.md`

## reference (3)

Supporting vocabulary: enum/telemetry names, dispatch fragments, and the browser error lexicon.

- [enums.txt](reference/enums.txt) — `binary-strings/browser/bot_challenge/enums.txt`
- [dispatch-fragments.txt](reference/dispatch-fragments.txt) — `binary-strings/browser/bot_challenge/dispatch-fragments.txt`
- [errors.csv](reference/errors.csv) — `binary-strings/browser/errors.csv`

