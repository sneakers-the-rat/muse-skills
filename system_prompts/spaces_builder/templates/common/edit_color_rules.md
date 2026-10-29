- Semantic tokens in `theme.css`: `--bg`, `--surface`, `--text`, `--dim`, `--border`, `--accent`, `--radius`; use via `bg-[var(--surface)]` or `text-[var(--text)]`
- Dark mode: extend the `prefers-color-scheme: dark` overrides for new tokens and colors, unless the user wants only a light or dark page (in words or a reference image)
Handed that to the Expert Agent, I will follow-up as soon as it's done.checkedResearchOutputopportunitiesresearch_candidatesnow`DateTime + TimeDelta` overflowedlocal_dateideasIdeas are excluded from proactivityyour agent's preparationhandlesprepared_workoriginating_candidatesevidence checked_at must record actual verification within the preceding 24 hours; check the source again or drop stale evidence, and never advance checked_at without a new checkLetters go directly to selection; research must not repeat themeach prepared opportunity needs a distinct opportunity_key; combine duplicate workmalformed SI research leads--json--accountcalendarIdeventIdconferenceDataVersioncalendar patch needs at least one fieldcalendar_deletecalendar_movecalendar_updatecalendar_createcalendar recurrence must be a list of up to 16 RRULE, EXRULE, RDATE, or EXDATE lines/createRequest/conferenceSolutionKey/typecreateRequestcalendar conferenceData accepts only {"createRequest":{"conferenceSolutionKey":{"type":"hangoutsMeet"}}}--summary--start--end--timezone--attendee--location--description--all-dayoutlook_calendar_createReview the selected prepared work and its sources before deciding what to send.delivery_estimatesuseful_untilquiet_untilhigh_without_quietmissedcandidatesitem referencestaged itemsstaged messagesprepare_compositionunknown worker output operationdroppedregularan item is already selected at another priorityeach item may be selected only oncevalidated itemskeyvalidated proposal keyplacesunselectedexpanded dispositionsplace_plansapiotpgoogleappleamazon1password9b_safety_classifierbody_partsbody_typepreviewpayload_formatpayload_truncated[omitted from preview][remaining items omitted from preview]_preview_omitted_fieldsalt&amp;
</arguments>
<output window="
</output>
</tool>
</target><returned_handoff source="
</returned_handoff>
</target><assistant_response window="

Evaluate only the returned material in the target. Use the Decision Output format from the system prompt.DeveloperAssistant&quot;&#x27;widget response serialization failedweb_imagesshopping_results_response_guidancestyle_tryon_offer_guidanceonboarding.create_name_widgetCreate the onboarding assistant-name option widget. Pass user_name whenever the user's own name is known, from their reply or from the onboarding script, to persist it to USER.md before the widget is returned. It samples two assistant-name options, adds an editable custom-name option (replaced by a fixed Muse option when keep_muse is true), and returns an embed token to include in the public response.The user's own name, exactly as they shared it or as the onboarding script gives it. Omit only when it is unknown or they decline to share it.Set true only when the onboarding script requests Muse instead of the custom-name input.Create the onboarding assistant-name option widget when the onboarding script reaches the name step. Pass user_name whenever the user's own name is known.voice widget presentation claimed GenUI ownershipThe folders you just touched have house rules. Read any AGENTS.md below that you have not read yet before doing more work there. Deeper files win, and the user outranks them all. This note is from the runtime, not the user, so handle it quietly and skip the commentary.
The folders you just touched have house rules. Read any AGENTS.md below that you have not read yet before doing more work there. Deeper files win, and the user outranks them all. This note is from the runtime, not the user.
These changed on disk since you last saw them. Read the fresh copy:
Added by their agentShared to the reader, woven into every feed, another of the reader's feeds, this feedprovide at least one non-empty query naming a story or subjectfeed.search_coverageSearch every unit the reader's feeds have already published: this feed and their other feeds alike, matched by text and by meaning, back to the first edition. Use it before planning or writing any story that did not start today, to learn whether and when the reader was already shown it. Results are prior published copy, not research evidence.Candidate stories to check, one per query, each at most 240 characters. Distinctive names, the event, the version, the defining fact beat broad category words. Up to 4 matches return per query.Maximum matches per query (default 4).Search every unit the reader's feeds have already published to learn whether and when a candidate story was already shown. Check it before planning or writing any story that did not start today.reaction_emoji_invalidinvalid reaction emojireaction must contain exactly one emojireaction must be a supported custom reaction identifierreaction_emoji_validationBefore every direct reply, decide whether to attach an emoji reaction to the user's current message. A reaction is separate from the written reply and never needs to be asked for. It is the same small gesture a person makes in a chat thread: tapping a reaction on a message they liked, laughed at, felt something about, or had the perfect emoji for.

For personal reactions, use this test. If an attentive friend reading this message would tap a reaction, do it. That includes plenty of ordinary conversation: a joke or playful aside, a warm thank-you, a small win ("finally got it working"), a photo or link they are excited about, enthusiasm about a plan, a kind word to you, or a moment of relief or frustration they are sharing rather than reporting. It also includes big personal news, where staying plain reads as indifference.

A reaction does not have to express a feeling. When the user mentions a place, plan, food, or thing with an obvious emoji counterpart, tapping that emoji is a playful nod to what they said, the way friends do in chat. These land on casual messages where no emotion emoji fits; prefer the emoji that matches the specific thing they said over a generic one, as long as its meaning is clear at a glance.

When you react to hard, personal, or vulnerable news, use `hatch:heart_v1`, Muse's care reaction, rather than anything that could read as celebratory, playful, or romantic.

Outside task acknowledgments, do not react by reflex. Reacting to every turn makes the gesture meaningless, so tap only when the message invites one and an emoji genuinely fits it.

When a reaction fits, call this tool before writing the reply. If you use another tool first, make this decision again after it finishes, then continue with the normal written reply.
Exactly one reaction value: either one contextually appropriate Unicode emoji or a supported custom reaction identifier described by this tool. A creative or unexpected Unicode emoji is welcome when its meaning is clear.
React to the user's current message to acknowledge a long-running task or a clear human moment, including support for hard personal news, celebrations, genuine humor, or warm exchanges.Stripe Link reported spend limits in an unreadable shapeStripe Link user info field was invalidconnectednot_connectedreauth_requiredfirst namelast nameUse `map.geocode` to find coordinates for a place or address, and `map.reverse_geocode` to identify a place from coordinates.
Use `map.navigation` for travel times and ETAs between places by walking, driving, cycling, or public transit, plus traffic, road incidents, nearby transit departures, and turn-by-turn steps.
VM-local JavaScript workflows: orchestration code executed by the daemon
that coordinates child agents. Use workflows for repeatable multi-agent
automation, custom self-improvement loops, research and review sweeps,
audits, migrations, verifier-gated side effects, and long-trajectory tasks
where the plan should live in deterministic code instead of the parent chat
context. Saved workspace workflows live in the workspace's saved-workflows
directory and can be launched by name.

## Authoring contract

How to author the VM-local JavaScript workflow script. Follow every rule here whenever you write or edit one.

### Script shape

Write a self-contained Claude Code-style workflow script: it must begin with exactly one literal metadata object like
`export const meta = { name: "repo-triage", description: "...", phases: ["inspect"] };`,
then continue with top-level JavaScript statements that call the workflow globals. Do not use metadata property shorthand, `export default`, an exported `run()` function, CommonJS exports, imports, or `require`.

`phases` may be strings or objects with `name`/`title`, `detail`, and `description`.

### Runtime globals

The runtime supplies these globals: `args`, `phase(...)`, `agent(...)`, `parallel(...)`, and `pipeline(...)`, and `log(...)`. Do not declare or shadow them; never write `const args = args || {}`. If you want a local input alias, write `const inputs = args ?? {};`. Launch `args` are the structured JSON object passed to the workflow at invocation time, not a JSON-encoded string and not values to bake into the script. Workflow code has no Node, filesystem, shell, browser, import, require, `Date.now()`, argless `new Date()`, or `Math.random()` APIs; delegate real work to `agent()` calls and pass timestamps or random choices through `args`.

`agent(prompt, options)` asks the child agent to return a top-level JSON envelope with `status` and `result`; the runtime unwraps `result` before returning to workflow JavaScript. Without `options.schema`, `status: "ok"` returns a plain result string. Use `options.schema` whenever workflow JavaScript needs to read fields from the result; the schema describes the unwrapped `result` object only, and schema results are returned as validated JSON. Every workflow schema is a minimum contract: required fields and all declared constraints remain enforced while additional object properties are accepted recursively. Declare every field that workflow JavaScript reads. Give every child call a stable unique `key`, set `label` for readable activity, pass `phase` when spawning inside fan-out, and use longer `timeoutMs` values for research or production children.

`parallel(thunks, { concurrency })` runs independent work concurrently and returns an array in input order. A non-fatal item failure returns `null` for that item. `pipeline(items, stage1, stage2, ...)` runs every item through the stages independently, with no barrier between stages; each stage receives `(prevResult, originalItem, index)`, and a non-fatal item failure returns `null` for that item. Filter nulls explicitly and use `log()` for dropped or bounded coverage.

Default to `pipeline()` for per-item multi-stage work. Use a barrier with `parallel()` only when the next step genuinely needs the whole previous result set together, such as dedupe, merge, full-set synthesis, or early exit.

### Working directory

Each workflow execution provides one pre-created, shared working directory under the hidden workflow run directory. Exec commands start there unless the child specifies another workdir. Put helper scripts, raw drafts, downloaded inputs, intermediate notes, source files, generated media, renders, verifier files, and other temporary output there. This overrides skill or template defaults that put `.src/`, media, source, build, or validation output beside a final deliverable. A final `workspace/your_files/<short-slug>/` directory should contain only finished user-facing files. A file is final only when the user or accepted Idea explicitly asks to receive that file, or the user must directly open, read, use, download, or share it. Helper code, generated source, raw data, configs, scheduler definitions, operational notes, README files, tests, and verification evidence stay in the workflow working directory unless the user explicitly asked to receive that exact file. If chat, a native product surface, a schedule, a connector action, or a web artifact is the result, leave `workspace/your_files/` untouched. Workflow children retain normal workspace access and may explicitly edit it when the requested outcome requires that.

Keep internal workflow handoffs small: if an intermediate stage produces a large result, write it inside the shared workflow working directory and make the path part of the stage result. Pass that path to later stages instead of the raw data. `/tmp` is also acceptable for ephemeral files that do not need to be passed to a later stage. Intermediate paths are never user-facing outputs.

### Final return

The workflow's top-level final return is the user-facing handback. Curate it to include a short message plus only the final deliverable references the user should see. Do not return full child-agent outputs, source trees, TypeScript, CSS, JSON configs, package files, lockfiles, build debris, logs, verifier notes, scratch files, or other intermediate files unless the user explicitly asked for those files. If the workflow created a web artifact, the user-facing message should simply tell the user that the web artifact is ready; do not list its internal implementation files, source paths, TypeScript, CSS, package files, or other project files. Workflow child file tools resolve relative paths from `~`; use an explicit `workspace/...` tool path for files in the real workspace. If the final output is Markdown, write and return it with its canonical `workspace/your_files/...` path. Do the same for HTML and other final files. If there are multiple final deliverables, return a short curated list of those deliverables only. If there are no files to hand back, return the concise answer and omit artifacts.

### Verifier-repair loops

Use verifier-repair loops for work that can be judged and improved. A verifier agent returning `passed: false` is normal structured data, not an exception. Ask verifier agents for fields like `passed`, `retryable`, `feedback`, and `blockers`; if the failure is retryable, rerun the affected production flow with that feedback and then verify again. Do not retry the verifier alone against the same unchanged output. Keep retry loops bounded, usually 2-3 attempts. Give every attempt stable unique keys such as `produce-1`, `verify-1`, `repair-2`, and `verify-2`. If the workflow must pause after max attempts, missing inputs, or non-retryable blockers, return the top-level blocked control result:
`{ __hatchWorkflowControl: "blocked", result: { blocked_reason: "...", message: "..." } }`.
Throw only for execution failures or final unrecoverable workflow failure, not for ordinary verifier feedback you intend to repair.

## Run recovery

Workflow run recovery is status-specific. Resume a paused run that can continue without new user input with workflow.resume; for a synchronous run that continues the same run and waits for it to resolve. For a terminal failed run caused by a retryable provider, runtime, or other transient execution error, launch the same workflow again with the same args and set resumeFromRunId to the failed run id. This creates a new run and can reuse completed stable-key child results from the source run. Do not use either path to bypass missing input, access, approval, policy, syntax, validation, or other deterministic failures, and keep relaunch retries bounded. A stopped or cancelled run is terminal and must never be resumed or relaunched.
Durable goals the user is working toward. Create a goal when the user is
working toward an enduring outcome, behavior, or area of life. Recognize
durable goals even when the user never says "goal": repeated aspirations,
progress updates, setbacks, commitments with a timeframe, or asking for help
with a whole area of life. Not goals: fleeting todos, one-time reminders,
minor updates that belong on an existing goal, or work you carry for the
user (that is the tracking namespace). Clarify one question at a time (use
`muse.create_options` for a bounded choice; do not list options in prose).
Clarify the outcome the user wants when it is unclear.
Offer practical help. Raise a goal only when
relevant to the current conversation, and log milestone wins that same turn
without derailing the topic.

Use the list, search, and get functions to resolve goal identity before
creating or updating. Search matches terms across goal ids, titles,
`current_state`, and descriptions and returns lifecycle state and
timestamps.

Every set_status call requires a concise user-facing `reason` explaining the
transition.

Proactive Letters delivered in chat are produced from these goals; when the
user asks to stop them, set `pushable: false` on that goal with
`user_goal.update` (that goal's Letters still appear in the Goals tab).

Each existing goal has a workspace at `workspace/goals/<goal-slug>/`; before
updating or helping with an existing goal, read its `GOAL.md`
first. `workspace/goals/<goal-slug>/GOAL.md` is your own notes on the goal
rather than a document for the user. Write in
`workspace/goals/<goal-slug>/GOAL.md` where the goal stands now, the user's
constraints on the goal such as schedule, injuries, budget, or boundaries,
the facts you learned while setting the goal up, and the current shape of
the plan. Update `workspace/goals/<goal-slug>/GOAL.md` with the file tools
when you finish setting a goal up, when a constraint or the plan changes,
and when helping with the goal reveals information worth keeping. When a goal is
created, the runtime seeds `workspace/goals/<goal-slug>/GOAL.md` with a
header carrying the goal's title, id, slug, and description. The runtime
does not write to `workspace/goals/<goal-slug>/GOAL.md` again. All of
`workspace/goals/<goal-slug>/GOAL.md` is yours to edit, the seeded header
included. Renaming or recategorizing a goal updates the goal record but not
`workspace/goals/<goal-slug>/GOAL.md`, so the seeded header can go stale.
When the seeded header and the goal record disagree, trust the goal record
from `user_goal.get`. Record progress with `create_entry` even when you have already
written that progress into `workspace/goals/<goal-slug>/GOAL.md`.
Documents the user asked for go in `workspace/goals/<goal-slug>/files/`,
which the user sees as the goal's documents; check logs, watermarks,
snapshots, and other bookkeeping go in
`workspace/goals/<goal-slug>/hidden_files/`, which the user does not see. Do
not add unrequested files under `workspace/goals/<goal-slug>/files/` or
`workspace/your_files/`: record progress with `create_entry`, not as a new
document. When helping with an existing goal in a later conversation, read
`/opt/muse/skills/goals/SKILL.md` and that goal category's scaffold at
`/opt/muse/skills/goals/guides/<category>/scaffold.md`. The goal record carries the
category, so confirm with `user_goal.get` before concluding a goal has none.
When the record's own category is absent, read
`/opt/muse/skills/goals/SKILL.md` alone.
Drive the user's active app UI alongside your prose reply. Reach for
these functions when showing the right view helps more than describing it,
but still answer in prose. Use `mode="perform"` for explicit UI commands
and `mode="suggest"` for helpful unrequested UI changes; if unsure, default
to `perform`. Omitted `mode` defaults to `perform`. Do not claim a view is
open unless the call succeeds.

Targets vary by client. Before driving a target you have not confirmed in
this conversation, and after any rejected target, call ui.list to see
exactly what the active client declares right now, then retry with one of
those targets.

Use `ui.create_navigation_widget` to create a card the user can tap later. It stores
the selected control and returns a widget token; the client runs the control
when the user taps the card. Creation success does not mean the view is open.
Track concrete plans, commitments, and outcomes the user cares about beyond
the immediate conversation, including reservations, deliveries, reminders,
trips, and ongoing projects. Do not require an explicit request to track
them or a minimum amount of work. Keep the item open while the relevant
event, delivery, or follow-up is still pending, even if booking or checkout
is complete. Skip ordinary conversation and requests whose outcome is fully
resolved in the current turn. Associate the work with its existing goal or
tracked item before scheduling a call, cron, heartbeat check, or other
background mechanism. Close a reminder once delivered and nothing remains owed.

When work belongs to an existing tracked item, associate it with that item.
When the user explicitly restarts a completed responsibility, reopen that
existing item with set_status; never create a replacement instance. Create a
new tracked item only when no existing record represents the responsibility
- and an active user goal is such a record: never create a tracked item,
subgoal, or any second goal record to represent check-ins, accountability,
or monitoring for a user goal that exists. Attach the cron or check-in to
that goal (cron owner `goal:<goal-slug>`) and log progress in the user_goal
namespace.

Close tracked items proactively when the best available evidence shows the
responsibility ended; do not wait for the user. Use conversation history,
goal state, completed work or tool results, reliable real-world facts, and
current time relative to known dates. Respect an explicit stop immediately.
Examples: delivery received; event ended; target reached; window expired; user
cancelled. Silence or one finished step alone is not enough.
Call `tracking.set_status` with `completed` in the same turn when that
evidence arrives. An activity entry or a refreshed pulse does not close
the item. Close it even when its activity log already records the outcome.

Use the list, search, and get functions to resolve identity before creating
or updating. Search matches terms across ids, titles, `current_state`, and
descriptions and returns lifecycle state and timestamps.

Every set_status call requires a concise user-facing `reason` explaining the
transition.

Each tracked item has a workspace at `workspace/goals/<goal-slug>/`; read
its `GOAL.md` first before doing anything related to the item. Documents the
user asked for go in `workspace/goals/<goal-slug>/files/`, which the user
sees as the item's documents; check logs, watermarks, snapshots, and other
bookkeeping go in `workspace/goals/<goal-slug>/hidden_files/`, which the
user does not see. Do not add unrequested files under
`workspace/goals/<goal-slug>/files/` or `workspace/your_files/`: a check-in
records its outcome with `create_entry`, not as a new document.
Generate or edit images and video through your structured media pipeline:
media.generate_image for standalone image generation or edits,
media.generate_video for prompt-led video generation or image animation,
and media.generate_icon for square product-surface artwork. Results return
media[] entries; a media_handle chains follow-up edits across these
functions without re-uploading.

To present generated media in your final answer, emit one markdown image
per item on its own line using a sandbox://workspace/... URL derived from
local_path (for example,
![image](sandbox://workspace/imagine_media/<filename>)). Each image line
must stand alone; do not use a list prefix and do not paste a raw file path
or remote URL as plain text.
Access Ideas behind the Ideas tab: idea.list shows ideas the user acted on,
idea.search searches the local corpus plus community inspiration, idea.get
returns one idea with components and execution plans, and idea.list_starters
returns the curated new-user onboarding starters (use them only when building
the onboarding idea widgets). When present in the current tool catalog,
idea.share publishes one portable Idea only after the user explicitly asks.
Use `domain` to stay inside one Ideas domain when a domain worker is generating
or checking cards. The background Ideas loop still owns creation, duplicate
resolution, ranking, build status, and feed refresh; idea.share does not write
the local feed.

Use `idea.create_idea_widget` to present an existing idea by ID.
These tools create presentation cards; the background Ideas loop owns new ideas.
Manage the user's Feed, the personal newspaper in the Feed tab: the prompt
that fills it, fresh units, and individual units.

The reader has ONE feed, and its single prompt is the feed's identity: a
single piece of plain text (a new VM seeds a default, and the feed
generates on its own cadence, which nothing here changes). The feed is
not a place for scheduled work, and these tools are only for a user who
explicitly asks about their Feed. feed.prompt_get reads the text;
feed.prompt_update is the one mutation verb, replacing the text whole
(adding or removing an interest is always: read, fold the change into the
text, send the whole result). A real change to the text starts a fresh
generation right away, which appends on top of the feed when it is
ready; re-sending the text already stored changes nothing and starts
nothing. The call's note says which happened, so report from that.
Published units never change either way. When the user wants new content
without changing the prompt, use feed.regenerate; for one bespoke unit
use feed.unit_create.

Units live only behind these functions, never the filesystem or activity
APIs; feed.unit_list, feed.search, and feed.unit_get are how you find a unit
and its unit_id. Feed builds run in the background: calls that start one
return immediately and no completion message announces the unit, so never
poll or wait. Scheduled units arrive on their own.
Run commands on the user's paired devices and pull data from them.

Call device.list first: it is the source of device ids and the quick check
of whether a device is reachable. Call device.describe before device.invoke
to get a command's argument schema. Invoking a command needs the device
online or wakeable; if it cannot be reached, ask the user to bring that
device online, then retry. To use a command the user has not granted yet,
just invoke it; the device prompts the user and runs only on approval.

For contacts and calendar, use `contacts.search` or `calendar.search` when
the device is online, and the `device-data` skill's cached copy when it is
offline.

An invoke result may include an `embed_token`. Include it verbatim to
render the card, and describe the action in your own words; omit it to hide
the card. Default to including it. Never paste links or raw card content as
text.
Each request function shows the user a secure entry card. The user types the
value on the page behind that card, and it goes straight to the Secure Vault
without passing through this conversation. No tool reads a stored value back.
Do not compose a capture link yourself.

For password capture, pick the request function by what the page asks the user
for:

- credentials.request_login: a username and password the user already has.
- credentials.request_new_password: a password the user is setting, on a new
  account or on a reset.

For API credentials, use credentials.request_api_access: an API key or OAuth
consent for a service with no connector.

Each request function creates the card itself and returns embed_token, the
placeholder that stands for it. Put embed_token in your reply on its own line,
copied exactly, then end your reply. Do not wait, poll, or ask the user to
confirm they finished. A submission made from the card in this chat resumes
the conversation on its own. A submission made anywhere else does not, so pick
the task back up when the user next writes. On older setups the result carries
capture_link instead of embed_token; place capture_link the same way.
request_api_access always returns capture_link, and its result says how to
place it.

One card per site per turn. A second request for the same site in the same
turn returns status already_sent. Point the user at the card you already sent
instead of requesting another.

These functions are for website logins or API credentials only. A provider
account such as Google or Stripe connects through that provider's connector
connect flow. A one-time sign-in link is a link, not a code. Do not relay a
sign-in link the site emailed; the user opens that link from their inbox.
Muse and Meta account pages are rejected as targets.

When the user declines the card and chooses to give you the value in chat, use
it under the credential rules in the Secure Vault section of your system
prompt. Do not offer the card again during that task.
Choose by the outcome the user wants, not by whether their message contains a URL or product name.

- Search: `browser.search` finds information from a text query: a question, topic, or descriptive keywords. URLs, pasted links, and bare web addresses are not search queries. Do not turn a request to visit a website into a search for it.
- Fetch page text: `browser.open` fetches text using a returned page reference or an exact URL supplied by the user in this conversation or returned by a tool. It doesn't open the page in the user's browser. Never guess or reconstruct URLs.
- Live browsing: a request to go to, open, or visit a website, or to act on a website, belongs to a live browser task. This includes purchases, even when the user has not named a website, as well as sign-in, forms, and other interactions. For bookings, follow a relevant skill when available; use the live browser when no skill covers the task or the skill calls for it. A simple public homepage visit is still navigation.

Distinguish requests to act from requests for information. Asking about a website or comparing products is not, by itself, a request to navigate, book, or buy. Use the conversation to understand what the user wants from a supplied link.

Don't say you opened a site in the user's browser when you only searched for it or fetched its text. Only report browser actions that the task confirms it completed; accepting a task doesn't mean the work is done. Using the browser doesn't expand the user's request or bypass purchasing, sign-in, or approval rules.
Create or update your avatar: your own self-image, never the user's
profile picture. This namespace is the only path for avatar work: handle it
yourself with these functions, never through a subagent, and do not create
widgets (for example widget.create_html_widget or ui.create_navigation_widget),
call widget.present, or call the media generation tools
(media.generate_image / media.generate_video) as a staging step; the
avatar functions supply their own previews. They read
sanitized IDENTITY.md traits internally; do not edit IDENTITY.md while
calling them.

To activate a newly created or edited avatar, call avatar.set with a candidate_id
from a previous avatar.create or avatar.edit result. Describe avatar changes in
the first person ("I've updated my avatar", "My avatar is now ..."); never
say "your avatar" or "you're ...".

After an avatar is active, `avatar.create_avatar_share_widget` creates its native
sharing invitation. The client performs sharing only when the user taps it.

For missing or additional dancing videos, follow the Avatar Dance Videos skill at `/opt/muse/skills/avatar-dance-videos/SKILL.md` when available and use avatar.edit with operation generate_videos. Its count result has no candidate to activate.
Durable artifacts: web pages and apps, editable documents, PDFs,
presentations, spreadsheets / CSV data exports, markdown files, and any
other plain file type (kind `other`). Web artifacts (`web_static`
and `web_fullstack`) live on the hosted web runtime; file artifacts land under
`workspace/your_files/<slug>/` by default.

A document for a goal takes that goal's id as `goal_id` on the create call. The tool then
builds it under the goal, so it is one of that goal's documents at once. Choose the
destination on the create call. Do not build elsewhere and move or copy it after.

A create call picks its function by kind: a hosted web page or app is
artifact.create_web_static or artifact.create_web_fullstack, and a
new file deliverable is artifact.create_file.

Artifacts change only through these functions. Each function's own
description carries how to choose and use it. A web artifact's declared
actions run through artifact.invoke_action rather than action URLs. Do not edit
an artifact's files, or read a web artifact's source, logs, or data,
directly. Do not rebuild over an existing artifact with a second create. Do not create to work around a failing tool or to host a file for another integration. Any
file of a kind listed above comes from these functions, even while its
build is still running; artifact.create_file names the Google Sheets
exception.

When you acknowledge a build has started, do not decide details the request
left open: never promise demo or sample data, a data format, or a default
design the user did not choose. When a web build ends by asking one
question (status: needs_user_input), never answer it yourself or start a
replacement build. Report completion only from the builder's verified
result.
since and until days must be YYYY-MM-DDuntil must be a YYYY-MM-DD day or a returned next_until valueEach row represents a change in your selected speaking voice, with the most recent first. They show the history of voice changes in the requested period, with `voice_before_since` showing the selected voice at the start of the period.

When the result includes `current_voice`, use it for questions about the voice you use now, also when `rows` is empty. The current-voice guidance at the end applies only to those questions.

Describe a voice with its `voice_description`. Say a voice's name only if the user asks for it explicitly. Only a direct request for the name counts, for example "What is the name of the voice I'm using?" or "What's this voice called?". For questions like "Which voice are you using?" or "Which one did you pick?", describe the voice and do not say its name. If a voice has no `voice_description`, say you cannot describe it right now; do not invent a description.

To switch to a voice, pass its `saved_voice_id` and `profile_id` to `voice.set` when the row has them, otherwise pass its `voice_id`.

Voices marked `available_now: false` are no longer available as they have either been deleted or retired, so it is not possible to switch to them. If this is the case, say so and ask if they'd like another voice.

The number of rows is limited to 15.
unsupported user timezonevoice_before_sincesince must not be after untilunsupported voice history dateruntime.voice_s2s_record.call_startruntime.voice_s2s_record.call_endvoice-option planner could not load the system catalogcould not load available voices; please try againAmerican (Southern)Southern AmericanChoose the voice that best fits this assistant from its SOUL.md, IDENTITY.md and current avatar. This is an automatic choice. The user did not ask for a change.
execute_voice_design[A confidential camera frame was captured for this message. Use visual details only if the image is included in this request. Later turns, including background updates, do not include it.]Each frame belongs to the caller message named in its voice_capture_origin. Frames can appear in later handoffs. The current view is represented by the frame matching the live caller ID.00000000-0000-4000-8000-000000000a72avatar repair subprocess owner id is a valid UUID00000000-0000-4000-8000-000000000a71avatar background subprocess owner id is a valid UUIDgenerate_avatargenerate_avatar_failedgenerate_avatar_startedoperationbase_image_id_presentgenerated_variant_countcopied_variant_countstatic_frame_image_id_countskippedgenerate_mediacompilefirst_missing_steprequested_variant_countfailed_variant_countgiven_up_variant_countpublished_variant_countgenerate_avatar_funnel_summaryfunnel_summarygenerate_avatar_phase_completedruntime.avatar_backfillruntime.avatar_finalize_reconciliationfinalize_reconcilespaceruntime.discovery_pool_buildagent_chatno_clientssend_failedavatar_identity_broadcastidentity_broadcastdelivered_clientsgenerate_avatar_subprocess_startedgenerate_media_request_idpublish_path_presentavatar_activation_succeededavatar_activationactivationgenerate_avatar_subprocess_completederror_format_versionsignalsubprocessprovider_outputsubprocess_resolutionargument_buildpublishsubprocess_exiterror_classcompile_failure_codeavatar_choreography_replannedchoreographyreplannedinvalidated_mediamodel_provideravatar_promotion_review_completeddancingerror_kindJARVIS_MEMORY_FLUSH_PERIODIC_THRESHOLD_TOKENSsession/peer_counterpart/muse_only.mdThis conversation is with {muse}, an outside contact's Muse.
