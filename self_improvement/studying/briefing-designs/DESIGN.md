# Muse Letter design

Muse Letters are warm pages for personal correspondence. The design is a
container for the assistant's voice, not an editorial template.

`NOTEBOOK_BRIEF.css` is the canonical stylesheet. Link it once in authored HTML;
the finalizer inlines it when the brief is accepted.

## Core shell

Every letter needs only this shared shell:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{Brief title}}</title>
  <link rel="stylesheet" href="NOTEBOOK_BRIEF.css">
</head>
<body>
  <main class="sheet">
    <article class="article">
      <p>Write the note in the shape that feels natural here.</p>
      <p class="byline">&mdash;<span>{{assistant_name}}</span></p>
    </article>
  </main>
</body>
</html>
```

Resolve the assistant name from `IDENTITY.md`, falling back to `Muse`.

## Available details

The stylesheet supports optional `.dateline`, `.title`, `.lead`, `.figure`,
`.pullquote`, `.note`, `.divider`, `.hl`, `.chart`, `.stat`, `mark`, and table
styles. Use the details that suit the letter and leave the rest out.

Every letter has one generated landscape hero near the top. Make it a specific,
atmospheric visual opening for this note and use the shared taped-photo treatment.

Real links and media make concrete web results easier to recognize and explore.
When the letter discusses a place, product, artwork, recipe, person, or similar
result, bring in a useful representative image when one is available, preserve
its source attribution, and present the saved local copy as a taped photo or a
small `.gallery`. Together, the hero and sourced photos should feel like a few
things tucked into a personal letter, not an editorial layout.

The generated hero uses the shared treatment without a source link:

```html
<figure class="figure figure--taped">
  <img src="media/{{generated_hero}}" alt="{{useful alt text}}">
  <figcaption>{{A short aside that belongs with the note}}</figcaption>
</figure>
```

A sourced figure uses the same treatment and links back to the real page:

```html
<figure class="figure figure--taped">
  <a href="{{source_url}}">
    <img src="media/{{local_file}}" alt="{{useful alt text}}">
  </a>
  <figcaption>{{A short, natural caption with attribution}}</figcaption>
</figure>
```

Tables, stats, and charts belong in letters with real quantitative comparisons,
schedules, budgets, or trends. Ordinary advice and personal observations are
usually better as prose.

The page remains read-only: links may open real destinations, while goal actions
and embedded mutation controls stay outside the letter artifact.
self_improvement/studying/briefing-designs/NOTEBOOK_BRIEF.css/*
Muse goal briefing letter stylesheet.

This is the canonical base stylesheet for Figma-aligned Muse Letter goal briefs.
The brief finalizer inlines this file into the final HTML artifact, so
brief authors should not paste, copy, link, rewrite, minify, or summarize this
stylesheet in individual briefs.

Use this as the shared base for goal briefs. Brief-specific CSS may add
content-only treatments, but should not redefine the root Muse Letter tokens or
replace the core sheet, article, masthead, figure, and content-detail styles
below.

------------------------------------------------------------------------------
MUSE LETTER LAYER
A full-page warm paper letter matching the Figma "v0 Letter Tweaks" direction:
centered small date, large orange handwritten title, compact editorial body,
and rounded white-framed images.
------------------------------------------------------------------------------
*/

@import url("https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,500;0,600;0,700;1,400;1,700&family=Caveat:wght@400;500;600;700&family=Oooh+Baby&family=Tenor+Sans&display=swap");

:root {
  --paper: #f1e7da;
  --paper-card: #ffffff;
  --card: #fff9f4;
  --ink: #23221f;
  --ink-soft: #6f6555;
  --ink-faint: rgba(35, 34, 31, 0.48);
  --accent: #a13f04;
  --accent-deep: #7a3303;
  --accent-2: #6f6555;
  --highlight: #ffe3c0;
  --highlight-2: #efd0c0;
  --line: #e3d6c1;

  --body: 1.1875rem;       /* Figma body: 19px */
  --lead: clamp(1.5rem, 2.25vw, 1.6875rem); /* Figma lead: 24px mobile, 27px web */
  --lead-leading: clamp(2rem, 3.333vw, 2.5rem); /* Figma lead: 32px mobile, 40px web */
  --h1: clamp(4rem, 8vw, 6rem); /* Figma title range: 64px mobile, 96px web */
  --h2: clamp(2.125rem, 5vw, 2.375rem); /* Figma heading: 34px mobile, 38px web */
  --h3: clamp(1.25rem, 3.2vw, 1.35rem);
  --caption: 1.25rem;      /* Figma caption: 20px */
  --signature: 2.375rem;   /* Figma bottom signature: 38px */
  --signature-leading: 1.210526; /* Figma bottom signature: 46px */
  --list: clamp(1.0625rem, 1.667vw, 1.25rem); /* Figma list: 17px mobile, 20px web */
  --list-leading: clamp(1.9125rem, 3.333vw, 2.5rem); /* Figma list: 30.6px mobile, 40px web */
  --measure: 680px;        /* Figma text column */
  --media-width: 760px;    /* Figma image frame */
  --page-gutter: 16px;     /* Figma mobile side padding / minimum gutter */
  --leading: 1.5;          /* 19px / 28.5px */

  --radius: 16px;
  --card-radius: 32px;
  --image-radius: 30px;
  --gap: 1.75rem;          /* Figma web column gap: 28px */
  --mobile-gap: 1.5rem;    /* Figma mobile column gap: 24px */
  --raised:
    0 2px 2px rgba(111, 101, 85, 0.1),
    0 8px 24px rgba(111, 101, 85, 0.1);

  --c1: var(--accent);
  --c2: #d6a56d;
  --c3: #d8b7a6;
  --c4: #8c8f77;
  --c5: #6f6555;
  --grid: var(--line);
  --axis: var(--ink-faint);
}

* {
  box-sizing: border-box;
}

html {
  background: var(--paper);
}

body {
  margin: 0;
  background-color: var(--paper);
  color: var(--ink);
  font-family: "Alegreya", Georgia, serif;
  font-size: var(--body);
  line-height: var(--leading);
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}

body:has(.sheet) {
  background-color: var(--paper);
  padding: 0;
}

.sheet {
  box-sizing: border-box;
  position: relative;
  margin: 0;
  max-width: none;
  min-height: 100vh;
  width: 100%;
  background-color: var(--paper);
}

.sheet::after {
  content: none;
}

.article {
  margin: 0 auto;
  max-width: var(--measure);
  padding: 110px 0 110px;
  width: calc(100% - var(--page-gutter) - var(--page-gutter));
}

:where(.article) p {
  margin: 0 0 var(--gap);
}

.article > p + p {
  text-indent: 0;
}

.dateline {
  color: var(--ink);
  font-family: "Alegreya", Georgia, serif;
  font-size: 1.25rem;
  font-style: italic;
  line-height: 0.7;
  margin: 0 0 1.5rem;
  text-align: center;
  transform: none;
}

.title {
  color: var(--accent);
  font-family: "Caveat", cursive;
  font-size: var(--h1);
  font-weight: 500;
  letter-spacing: 0;
  line-height: 0.95;
  margin: 0 auto 1.75rem;
  max-width: var(--measure);
  overflow-wrap: break-word;
  text-align: center;
}

.wave-rule {
  display: none;
}

.byline {
  color: var(--accent);
  font-family: "Oooh Baby", "Caveat", cursive;
  font-size: var(--signature);
  line-height: var(--signature-leading);
  margin: 1.4rem 0 1.8rem;
  text-align: left;
  transform: none;
}

.lead {
  color: var(--ink);
  font-size: var(--lead);
  font-weight: 600;
  line-height: var(--lead-leading);
}

.lead::first-letter {
  color: inherit;
  float: none;
  font-family: inherit;
  font-size: inherit;
  font-weight: inherit;
  line-height: inherit;
  padding: 0;
}

.article h2 {
  color: var(--ink);
  font-family: "Tenor Sans", Georgia, serif;
  font-size: var(--h2);
  font-weight: 400;
  letter-spacing: 0;
  line-height: 1.21;
  margin: 1.8rem 0 0.8rem;
}

.article h2::before {
  content: none;
}

.article h3,
.chart__title {
  color: var(--ink);
  font-family: "Tenor Sans", Georgia, serif;
  font-size: var(--h3);
  font-weight: 400;
  letter-spacing: 0;
  line-height: 1.25;
  margin: 1.9rem 0 0.6rem;
}

.article a {
  background-image: linear-gradient(var(--accent), var(--accent));
  background-position: 0 1.05em;
  background-repeat: repeat-x;
  background-size: 6px 2px;
  color: var(--accent-deep);
  padding-bottom: 0.04em;
  text-decoration: none;
  transition:
    color 0.2s,
    background-size 0.2s;
}

.article a:hover {
  background-size: 6px 3px;
  color: var(--accent);
}

mark,
.hl {
  background: linear-gradient(
    104deg,
    transparent 0.5%,
    var(--highlight) 0.5%,
    var(--highlight) 96%,
    transparent 96%
  );
  border-radius: 1px;
  box-decoration-break: clone;
  color: inherit;
  margin: 0 -0.05em;
  padding: 0.05em 0.15em;
  -webkit-box-decoration-break: clone;
}

.hl--mint {
  background-image: linear-gradient(
    104deg,
    transparent 0.5%,
    var(--highlight-2) 0.5%,
    var(--highlight-2) 96%,
    transparent 96%
  );
}

/* Hand-made layer (added): angle variants so no two swipes look identical. */
.hl--a {
  background-image: linear-gradient(
    99deg,
    transparent 1%,
    var(--highlight) 1%,
    var(--highlight) 94%,
    transparent 97%
  );
}

.hl--b {
  background-image: linear-gradient(
    108deg,
    transparent 0%,
    var(--highlight-2) 2%,
    var(--highlight-2) 97%,
    transparent 99%
  );
}

/* Hand-made layer (added): a hand-drawn underline drawn behind a phrase.
   Wrap the phrase in <span class="scribble">…<svg>…</svg></span>; the inline
   SVG path carries filter="url(#ink-rough-2)". */
.scribble {
  position: relative;
  white-space: nowrap;
}

.scribble svg {
  position: absolute;
  left: -0.05em;
  right: -0.05em;
  bottom: -0.32em;
  width: 104%;
  height: 0.55em;
  overflow: visible;
}

.pullquote {
  background: var(--paper-card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: 0 12px 28px -22px rgba(35, 34, 31, 0.28);
  color: var(--ink);
  font-family: "Caveat", cursive;
  font-size: clamp(1.35rem, 4vw, 1.75rem);
  line-height: 1.25;
  margin: 1.7rem 0;
  padding: 1rem 1.2rem;
  position: relative;
  transform: none;
}

.pullquote:nth-of-type(even) {
  transform: none;
}

.pullquote::before {
  background: rgba(255, 255, 255, 0.72);
  border-radius: 2px;
  content: "";
  height: 20px;
  left: 50%;
  position: absolute;
  top: -10px;
  transform: translateX(-50%) rotate(-2deg);
  width: 82px;
}

.note {
  color: var(--accent-2);
  font-family: "Caveat", cursive;
  font-size: 1.35rem;
  line-height: 1.2;
}

blockquote {
  border-left: 3px solid var(--accent);
  color: var(--ink-soft);
  font-style: italic;
  margin: 1.8rem 0;
  padding: 0.2rem 0 0.2rem 1.3rem;
}

.article ul {
  list-style: disc;
  margin: 0 0 var(--gap);
  padding-left: 1.4rem;
}

.article ul li {
  font-size: var(--list);
  line-height: var(--list-leading);
  margin: 0;
  padding-left: 0.1rem;
}

.article ul li::marker {
  color: var(--accent);
  font-size: 0.85em;
}

.divider {
  background: no-repeat center / contain
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='16' viewBox='0 0 180 16'%3E%3Cpath d='M3 8q11-6 22 0t22 0 22 0 22 0 22 0 22 0 22 0' fill='none' stroke='%236F6555' stroke-width='2' stroke-linecap='round' opacity='.62'/%3E%3C/svg%3E");
  border: 0;
  height: 16px;
  margin: 2rem auto;
  width: 180px;
}

figure,
.figure,
.chart,
.stat {
  margin: 0 0 var(--gap);
}

figcaption {
  color: var(--ink);
  font-family: "Caveat", cursive;
  font-size: var(--caption);
  line-height: 1;
  margin-top: 0.45rem;
  text-align: center;
  transform: rotate(1deg);
}

figure,
.figure {
  margin-left: 50%;
  max-width: calc(100vw - var(--page-gutter) - var(--page-gutter));
  padding: 1.5rem 0;
  transform: translateX(-50%);
  width: var(--media-width);
}

figure > img,
.figure img {
  background: var(--paper-card);
  border: 6px solid #ffffff;
  border-radius: var(--image-radius);
  box-shadow: var(--raised);
  display: block;
  height: auto;
  transform: rotate(1deg);
  width: 100%;
}

.figure--taped {
  position: relative;
}

.figure--taped img {
  transform: rotate(1deg);
}

.figure--taped::before {
  background: rgba(255, 255, 255, 0.72);
  border-radius: 2px;
  content: "";
  height: 30px;
  left: 18%;
  position: absolute;
  top: 1.5rem;
  transform: translateY(-50%) rotate(-4deg);
  width: 88px;
  z-index: 2;
}

.gallery {
  display: grid;
  gap: 0.9rem;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  margin: 2.2rem 0;
}

.gallery img {
  aspect-ratio: 4 / 3;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  height: 100%;
  object-fit: cover;
  width: 100%;
}

.gallery img:nth-child(odd) {
  transform: rotate(-0.8deg);
}

.gallery img:nth-child(even) {
  transform: rotate(0.8deg);
}

.chart svg {
  height: auto;
  overflow: visible;
  width: 100%;
}

.chart__title {
  margin: 0 0 0.6rem;
}

.chart__val {
  fill: var(--ink);
  font-family: "Caveat", cursive;
  font-size: 15px;
}

.chart__cat {
  fill: var(--axis);
  font-family: "Alegreya", serif;
  font-size: 11px;
}

.chart__note {
  fill: var(--accent-2);
  font-family: "Caveat", cursive;
  font-size: 14px;
}

.article table {
  border-collapse: collapse;
  font-size: 1.02rem;
  margin: 2rem 0;
  width: 100%;
}

.article th {
  border-bottom: 2px solid var(--accent);
  font-family: "Tenor Sans", Georgia, serif;
  font-weight: 600;
  padding: 0.55rem 0.6rem;
  text-align: left;
}

.article td {
  border-bottom: 1px solid var(--line);
  color: var(--ink-soft);
  padding: 0.55rem 0.6rem;
}

.article tr:last-child td {
  border-bottom: 0;
}

.article tbody tr:hover td {
  background: rgba(255, 227, 192, 0.24);
}

.article td.num {
  font-variant-numeric: tabular-nums;
  text-align: right;
}

.stat {
  margin-left: auto;
  margin-right: auto;
  max-width: 22ch;
  text-align: center;
}

.stat__num {
  color: var(--accent);
  font-family: "Tenor Sans", Georgia, serif;
  font-size: 3.4rem;
  font-weight: 400;
  line-height: 1;
}

.stat__label {
  color: var(--ink-soft);
  display: block;
  font-family: "Caveat", cursive;
  font-size: 1.4rem;
  margin-top: 0.3rem;
}

.stamp {
  display: none;
}

@media (min-width: 1100px) {
  .note {
    clear: right;
    float: right;
    margin: 0.2rem -190px 0.8rem 1rem;
    width: 160px;
  }

  .note:nth-of-type(3n) {
    transform: none;
  }

  .note:nth-of-type(3n + 1) {
    transform: none;
  }

  .note:nth-of-type(3n + 2) {
    transform: none;
  }

  .note::before {
    content: "\21B3 ";
  }

  .figure--wide {
    margin-left: 50%;
    width: var(--media-width);
  }
}

@media (max-width: 1099px) {
  .note {
    border-left: 3px dotted var(--accent-2);
    display: block;
    margin: 1rem 0;
    padding-left: 0.9rem;
  }
}

@media (max-width: 640px) {
  :root {
    --body: 1.0625rem; /* Figma mobile body: 17px */
    --leading: 1.411765; /* Figma mobile body: 24px */
    --gap: var(--mobile-gap);
    --image-radius: 16px;
  }

  .article {
    max-width: none;
    padding: 48px 0;
  }

  .dateline {
    margin-bottom: 1.5rem;
  }

  .title {
    line-height: 1;
    margin-bottom: 1.5rem;
    max-width: none;
    width: 100%;
  }

  figure,
  .figure {
    max-width: 100%;
    width: 100%;
  }

  figure > img,
  .figure img {
    border-width: 6px;
    border-radius: var(--image-radius);
  }

}
# Personal Brief

One user goal for this pass: its study found something fundamentally
new, and you write the personal Letter and render the finished Muse
Letter artifact in this same turn. The Letter voice rules, the
rendering fidelity contract, and the design doctrine are in your
system prompt; this assignment carries the mechanics.

Your Assigned item carries `goal_id`, the staged study note's
`note_path`, the full study output, and `briefing_reason`, one
sentence on why the study ruled this worth a Letter. Read the staged
study note at `note_path` inside your staging surface, then `USER.md`
and `IDENTITY.md`; your system prompt's Writing the Letter law governs
how the note becomes the Letter.

The note's `## Already Covered in Main Chat` section lists what the user
and the main agent already covered about this goal in main chat. Read
that section before you draft. Your system prompt's Writing the Letter
law governs what the Letter may do with what it lists.

Goal reads go through `user_goal.get` (with `goal_id`);
goal write actions are rejected on this turn. Never raw
SQL, never direct `GOALS.md` or `STUDYING.md` edits. Treat tool output
as authoritative and never hide a failed tool call. Use shell execution
only for bounded checks over files you staged in this run. Do not
reproduce a failed first-party browser or media call with shell/curl; a
terminal media outage ends honestly in `skip_reason`.

Derive:

| Value | Definition |
|---|---|
| `YYYY-MM-DD HH.MM.SS` | the VM's current **local** date and time |
| `goal-slug` | the flat `slug` field from the `user_goal.get` view |
| `<Brief title>` | the Letter's title, written to the title law in your system prompt |

Files to stage, in order:

1. The fresh Markdown Letter draft at
   `goals/briefs/<goal-slug>/drafts/<Brief title> (<YYYY-MM-DD HH.MM.SS>).md`,
   in this simple shape:

   ```markdown
   # <Brief title>

   <the letter>
   ```

2. The rendered artifact at
   `goals/briefs/<goal-slug>/<Brief title> (<YYYY-MM-DD HH.MM.SS>).html`,
   built from that draft under the rendering law in your system prompt
   and the design assets below.

3. Every local image under the staged `goals/briefs/<goal-slug>/media/`
   directory, the generated hero included. In the staged HTML,
   reference every local image only with a staging-relative path such
   as `media/example.webp`; the attach step rewrites it to its durable
   workspace URL. List every local media file in `brief.media_paths`
   and set `brief.hero_image_path` to the generated visual opening.

Include the canonical `NOTEBOOK_BRIEF.css` link once so the attach
step can inline it. Brief-specific CSS may support unique content
without replacing the shared page, typography, or signature styles.
Keep the artifact read-only and self-contained apart from links and
sourced media.

Complete the required diagnostic scores honestly; they are recorded
with the brief as calibration diagnostics and do not gate storage.

End the turn with one `muse.finish_step` call carrying:

- `goal_id`
- `note_path`
- `draft_path`
- `brief_display_title`
- `delivery_message`
- exactly one of:
  - a completed `brief` with `path`, `hero_image_path`, `media_paths`,
    and `scores`
  - `skip_reason` when a terminal media outage prevented a valid
    artifact; the Letter draft, its title, and its delivery message
    still exist and still ride this same output


## Briefing design assets

### DESIGN.md
````markdown
# Muse Letter design

Muse Letters are warm pages for personal correspondence. The design is a
container for the assistant's voice, not an editorial template.

`NOTEBOOK_BRIEF.css` is the canonical stylesheet. Link it once in authored HTML;
the finalizer inlines it when the brief is accepted.

## Core shell

Every letter needs only this shared shell:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{Brief title}}</title>
  <link rel="stylesheet" href="NOTEBOOK_BRIEF.css">
</head>
<body>
  <main class="sheet">
    <article class="article">
      <p>Write the note in the shape that feels natural here.</p>
      <p class="byline">&mdash;<span>{{assistant_name}}</span></p>
    </article>
  </main>
</body>
</html>
```

Resolve the assistant name from `IDENTITY.md`, falling back to `Muse`.

## Available details

The stylesheet supports optional `.dateline`, `.title`, `.lead`, `.figure`,
`.pullquote`, `.note`, `.divider`, `.hl`, `.chart`, `.stat`, `mark`, and table
styles. Use the details that suit the letter and leave the rest out.

Every letter has one generated landscape hero near the top. Make it a specific,
atmospheric visual opening for this note and use the shared taped-photo treatment.

Real links and media make concrete web results easier to recognize and explore.
When the letter discusses a place, product, artwork, recipe, person, or similar
result, bring in a useful representative image when one is available, preserve
its source attribution, and present the saved local copy as a taped photo or a
small `.gallery`. Together, the hero and sourced photos should feel like a few
things tucked into a personal letter, not an editorial layout.

The generated hero uses the shared treatment without a source link:

```html
<figure class="figure figure--taped">
  <img src="media/{{generated_hero}}" alt="{{useful alt text}}">
  <figcaption>{{A short aside that belongs with the note}}</figcaption>
</figure>
```

A sourced figure uses the same treatment and links back to the real page:

```html
<figure class="figure figure--taped">
  <a href="{{source_url}}">
    <img src="media/{{local_file}}" alt="{{useful alt text}}">
  </a>
  <figcaption>{{A short, natural caption with attribution}}</figcaption>
</figure>
```

Tables, stats, and charts belong in letters with real quantitative comparisons,
schedules, budgets, or trends. Ordinary advice and personal observations are
usually better as prose.

The page remains read-only: links may open real destinations, while goal actions
and embedded mutation controls stay outside the letter artifact.

````

### NOTEBOOK_BRIEF.css
````css
/*
Muse goal briefing letter stylesheet.

This is the canonical base stylesheet for Figma-aligned Muse Letter goal briefs.
The brief finalizer inlines this file into the final HTML artifact, so
brief authors should not paste, copy, link, rewrite, minify, or summarize this
stylesheet in individual briefs.

Use this as the shared base for goal briefs. Brief-specific CSS may add
content-only treatments, but should not redefine the root Muse Letter tokens or
replace the core sheet, article, masthead, figure, and content-detail styles
below.

------------------------------------------------------------------------------
MUSE LETTER LAYER
A full-page warm paper letter matching the Figma "v0 Letter Tweaks" direction:
centered small date, large orange handwritten title, compact editorial body,
and rounded white-framed images.
------------------------------------------------------------------------------
*/

@import url("https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,500;0,600;0,700;1,400;1,700&family=Caveat:wght@400;500;600;700&family=Oooh+Baby&family=Tenor+Sans&display=swap");

:root {
  --paper: #f1e7da;
  --paper-card: #ffffff;
  --card: #fff9f4;
  --ink: #23221f;
  --ink-soft: #6f6555;
  --ink-faint: rgba(35, 34, 31, 0.48);
  --accent: #a13f04;
  --accent-deep: #7a3303;
  --accent-2: #6f6555;
  --highlight: #ffe3c0;
  --highlight-2: #efd0c0;
  --line: #e3d6c1;

  --body: 1.1875rem;       /* Figma body: 19px */
  --lead: clamp(1.5rem, 2.25vw, 1.6875rem); /* Figma lead: 24px mobile, 27px web */
  --lead-leading: clamp(2rem, 3.333vw, 2.5rem); /* Figma lead: 32px mobile, 40px web */
  --h1: clamp(4rem, 8vw, 6rem); /* Figma title range: 64px mobile, 96px web */
  --h2: clamp(2.125rem, 5vw, 2.375rem); /* Figma heading: 34px mobile, 38px web */
  --h3: clamp(1.25rem, 3.2vw, 1.35rem);
  --caption: 1.25rem;      /* Figma caption: 20px */
  --signature: 2.375rem;   /* Figma bottom signature: 38px */
  --signature-leading: 1.210526; /* Figma bottom signature: 46px */
  --list: clamp(1.0625rem, 1.667vw, 1.25rem); /* Figma list: 17px mobile, 20px web */
  --list-leading: clamp(1.9125rem, 3.333vw, 2.5rem); /* Figma list: 30.6px mobile, 40px web */
  --measure: 680px;        /* Figma text column */
  --media-width: 760px;    /* Figma image frame */
  --page-gutter: 16px;     /* Figma mobile side padding / minimum gutter */
  --leading: 1.5;          /* 19px / 28.5px */

  --radius: 16px;
  --card-radius: 32px;
  --image-radius: 30px;
  --gap: 1.75rem;          /* Figma web column gap: 28px */
  --mobile-gap: 1.5rem;    /* Figma mobile column gap: 24px */
  --raised:
    0 2px 2px rgba(111, 101, 85, 0.1),
    0 8px 24px rgba(111, 101, 85, 0.1);

  --c1: var(--accent);
  --c2: #d6a56d;
  --c3: #d8b7a6;
  --c4: #8c8f77;
  --c5: #6f6555;
  --grid: var(--line);
  --axis: var(--ink-faint);
}

* {
  box-sizing: border-box;
}

html {
  background: var(--paper);
}

body {
  margin: 0;
  background-color: var(--paper);
  color: var(--ink);
  font-family: "Alegreya", Georgia, serif;
  font-size: var(--body);
  line-height: var(--leading);
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}

body:has(.sheet) {
  background-color: var(--paper);
  padding: 0;
}

.sheet {
  box-sizing: border-box;
  position: relative;
  margin: 0;
  max-width: none;
  min-height: 100vh;
  width: 100%;
  background-color: var(--paper);
}

.sheet::after {
  content: none;
}

.article {
  margin: 0 auto;
  max-width: var(--measure);
  padding: 110px 0 110px;
  width: calc(100% - var(--page-gutter) - var(--page-gutter));
}

:where(.article) p {
  margin: 0 0 var(--gap);
}

.article > p + p {
  text-indent: 0;
}

.dateline {
  color: var(--ink);
  font-family: "Alegreya", Georgia, serif;
  font-size: 1.25rem;
  font-style: italic;
  line-height: 0.7;
  margin: 0 0 1.5rem;
  text-align: center;
  transform: none;
}

.title {
  color: var(--accent);
  font-family: "Caveat", cursive;
  font-size: var(--h1);
  font-weight: 500;
  letter-spacing: 0;
  line-height: 0.95;
  margin: 0 auto 1.75rem;
  max-width: var(--measure);
  overflow-wrap: break-word;
  text-align: center;
}

.wave-rule {
  display: none;
}

.byline {
  color: var(--accent);
  font-family: "Oooh Baby", "Caveat", cursive;
  font-size: var(--signature);
  line-height: var(--signature-leading);
  margin: 1.4rem 0 1.8rem;
  text-align: left;
  transform: none;
}

.lead {
  color: var(--ink);
  font-size: var(--lead);
  font-weight: 600;
  line-height: var(--lead-leading);
}

.lead::first-letter {
  color: inherit;
  float: none;
  font-family: inherit;
  font-size: inherit;
  font-weight: inherit;
  line-height: inherit;
  padding: 0;
}

.article h2 {
  color: var(--ink);
  font-family: "Tenor Sans", Georgia, serif;
  font-size: var(--h2);
  font-weight: 400;
  letter-spacing: 0;
  line-height: 1.21;
  margin: 1.8rem 0 0.8rem;
}

.article h2::before {
  content: none;
}

.article h3,
.chart__title {
  color: var(--ink);
  font-family: "Tenor Sans", Georgia, serif;
  font-size: var(--h3);
  font-weight: 400;
  letter-spacing: 0;
  line-height: 1.25;
  margin: 1.9rem 0 0.6rem;
}

.article a {
  background-image: linear-gradient(var(--accent), var(--accent));
  background-position: 0 1.05em;
  background-repeat: repeat-x;
  background-size: 6px 2px;
  color: var(--accent-deep);
  padding-bottom: 0.04em;
  text-decoration: none;
  transition:
    color 0.2s,
    background-size 0.2s;
}

.article a:hover {
  background-size: 6px 3px;
  color: var(--accent);
}

mark,
.hl {
  background: linear-gradient(
    104deg,
    transparent 0.5%,
    var(--highlight) 0.5%,
    var(--highlight) 96%,
    transparent 96%
  );
  border-radius: 1px;
  box-decoration-break: clone;
  color: inherit;
  margin: 0 -0.05em;
  padding: 0.05em 0.15em;
  -webkit-box-decoration-break: clone;
}

.hl--mint {
  background-image: linear-gradient(
    104deg,
    transparent 0.5%,
    var(--highlight-2) 0.5%,
    var(--highlight-2) 96%,
    transparent 96%
  );
}

/* Hand-made layer (added): angle variants so no two swipes look identical. */
.hl--a {
  background-image: linear-gradient(
    99deg,
    transparent 1%,
    var(--highlight) 1%,
    var(--highlight) 94%,
    transparent 97%
  );
}

.hl--b {
  background-image: linear-gradient(
    108deg,
    transparent 0%,
    var(--highlight-2) 2%,
    var(--highlight-2) 97%,
    transparent 99%
  );
}

/* Hand-made layer (added): a hand-drawn underline drawn behind a phrase.
   Wrap the phrase in <span class="scribble">…<svg>…</svg></span>; the inline
   SVG path carries filter="url(#ink-rough-2)". */
.scribble {
  position: relative;
  white-space: nowrap;
}

.scribble svg {
  position: absolute;
  left: -0.05em;
  right: -0.05em;
  bottom: -0.32em;
  width: 104%;
  height: 0.55em;
  overflow: visible;
}

.pullquote {
  background: var(--paper-card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: 0 12px 28px -22px rgba(35, 34, 31, 0.28);
  color: var(--ink);
  font-family: "Caveat", cursive;
  font-size: clamp(1.35rem, 4vw, 1.75rem);
  line-height: 1.25;
  margin: 1.7rem 0;
  padding: 1rem 1.2rem;
  position: relative;
  transform: none;
}

.pullquote:nth-of-type(even) {
  transform: none;
}

.pullquote::before {
  background: rgba(255, 255, 255, 0.72);
  border-radius: 2px;
  content: "";
  height: 20px;
  left: 50%;
  position: absolute;
  top: -10px;
  transform: translateX(-50%) rotate(-2deg);
  width: 82px;
}

.note {
  color: var(--accent-2);
  font-family: "Caveat", cursive;
  font-size: 1.35rem;
  line-height: 1.2;
}

blockquote {
  border-left: 3px solid var(--accent);
  color: var(--ink-soft);
  font-style: italic;
  margin: 1.8rem 0;
  padding: 0.2rem 0 0.2rem 1.3rem;
}

.article ul {
  list-style: disc;
  margin: 0 0 var(--gap);
  padding-left: 1.4rem;
}

.article ul li {
  font-size: var(--list);
  line-height: var(--list-leading);
  margin: 0;
  padding-left: 0.1rem;
}

.article ul li::marker {
  color: var(--accent);
  font-size: 0.85em;
}

.divider {
  background: no-repeat center / contain
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='16' viewBox='0 0 180 16'%3E%3Cpath d='M3 8q11-6 22 0t22 0 22 0 22 0 22 0 22 0 22 0' fill='none' stroke='%236F6555' stroke-width='2' stroke-linecap='round' opacity='.62'/%3E%3C/svg%3E");
  border: 0;
  height: 16px;
  margin: 2rem auto;
  width: 180px;
}

figure,
.figure,
.chart,
.stat {
  margin: 0 0 var(--gap);
}

figcaption {
  color: var(--ink);
  font-family: "Caveat", cursive;
  font-size: var(--caption);
  line-height: 1;
  margin-top: 0.45rem;
  text-align: center;
  transform: rotate(1deg);
}

figure,
.figure {
  margin-left: 50%;
  max-width: calc(100vw - var(--page-gutter) - var(--page-gutter));
  padding: 1.5rem 0;
  transform: translateX(-50%);
  width: var(--media-width);
}

figure > img,
.figure img {
  background: var(--paper-card);
  border: 6px solid #ffffff;
  border-radius: var(--image-radius);
  box-shadow: var(--raised);
  display: block;
  height: auto;
  transform: rotate(1deg);
  width: 100%;
}

.figure--taped {
  position: relative;
}

.figure--taped img {
  transform: rotate(1deg);
}

.figure--taped::before {
  background: rgba(255, 255, 255, 0.72);
  border-radius: 2px;
  content: "";
  height: 30px;
  left: 18%;
  position: absolute;
  top: 1.5rem;
  transform: translateY(-50%) rotate(-4deg);
  width: 88px;
  z-index: 2;
}

.gallery {
  display: grid;
  gap: 0.9rem;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  margin: 2.2rem 0;
}

.gallery img {
  aspect-ratio: 4 / 3;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  height: 100%;
  object-fit: cover;
  width: 100%;
}

.gallery img:nth-child(odd) {
  transform: rotate(-0.8deg);
}

.gallery img:nth-child(even) {
  transform: rotate(0.8deg);
}

.chart svg {
  height: auto;
  overflow: visible;
  width: 100%;
}

.chart__title {
  margin: 0 0 0.6rem;
}

.chart__val {
  fill: var(--ink);
  font-family: "Caveat", cursive;
  font-size: 15px;
}

.chart__cat {
  fill: var(--axis);
  font-family: "Alegreya", serif;
  font-size: 11px;
}

.chart__note {
  fill: var(--accent-2);
  font-family: "Caveat", cursive;
  font-size: 14px;
}

.article table {
  border-collapse: collapse;
  font-size: 1.02rem;
  margin: 2rem 0;
  width: 100%;
}

.article th {
  border-bottom: 2px solid var(--accent);
  font-family: "Tenor Sans", Georgia, serif;
  font-weight: 600;
  padding: 0.55rem 0.6rem;
  text-align: left;
}

.article td {
  border-bottom: 1px solid var(--line);
  color: var(--ink-soft);
  padding: 0.55rem 0.6rem;
}

.article tr:last-child td {
  border-bottom: 0;
}

.article tbody tr:hover td {
  background: rgba(255, 227, 192, 0.24);
}

.article td.num {
  font-variant-numeric: tabular-nums;
  text-align: right;
}

.stat {
  margin-left: auto;
  margin-right: auto;
  max-width: 22ch;
  text-align: center;
}

.stat__num {
  color: var(--accent);
  font-family: "Tenor Sans", Georgia, serif;
  font-size: 3.4rem;
  font-weight: 400;
  line-height: 1;
}

.stat__label {
  color: var(--ink-soft);
  display: block;
  font-family: "Caveat", cursive;
  font-size: 1.4rem;
  margin-top: 0.3rem;
}

.stamp {
  display: none;
}

@media (min-width: 1100px) {
  .note {
    clear: right;
    float: right;
    margin: 0.2rem -190px 0.8rem 1rem;
    width: 160px;
  }

  .note:nth-of-type(3n) {
    transform: none;
  }

  .note:nth-of-type(3n + 1) {
    transform: none;
  }

  .note:nth-of-type(3n + 2) {
    transform: none;
  }

  .note::before {
    content: "\21B3 ";
  }

  .figure--wide {
    margin-left: 50%;
    width: var(--media-width);
  }
}

@media (max-width: 1099px) {
  .note {
    border-left: 3px dotted var(--accent-2);
    display: block;
    margin: 1rem 0;
    padding-left: 0.9rem;
  }
}

@media (max-width: 640px) {
  :root {
    --body: 1.0625rem; /* Figma mobile body: 17px */
    --leading: 1.411765; /* Figma mobile body: 24px */
    --gap: var(--mobile-gap);
    --image-radius: 16px;
  }

  .article {
    max-width: none;
    padding: 48px 0;
  }

  .dateline {
    margin-bottom: 1.5rem;
  }

  .title {
    line-height: 1;
    margin-bottom: 1.5rem;
    max-width: none;
    width: 100%;
  }

  figure,
  .figure {
    max-width: 100%;
    width: 100%;
  }

  figure > img,
  .figure img {
    border-width: 6px;
    border-radius: var(--image-radius);
  }

}

````
