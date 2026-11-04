# Scheduling, monitoring, and services

Use this guide from main or side chat when creating or changing background work.

## Choose the mechanism

- Crons run agent tasks on a schedule, including reminders, periodic checks, and work that needs tools or judgment. Use runonce for a single future action and an interval for bounded repeated checks.
- Hooks run lightweight polling scripts and wake an agent on a relevant condition. Use them when the detector can check local or public data without an agent turn each time.
- systemd services supervise programs that need to remain running, such as stream listeners, collectors, or local servers. Use the runtime's guest systemd when a sequence of independent checks cannot do the job.

Browser tasks and subagents already deliver completion handoffs. Use those instead of adding another monitor.

## Saved jobs and hooks

Record the user's scope, target, cadence, completion condition, owner, and delivery destination. A request to monitor one operation covers the observations needed to finish, not repeating the operation. Reuse an existing goal as owner when applicable. Other reminders and follow-ups need a tracked owner.

Keep goal-owned working files in `~/workspace/goals/<goal-slug>/hidden_files/`, including checkpoints, run logs, watermarks, and source snapshots. Hook scripts and state use the hook paths below.

Check existing jobs first. Change a cron through `cron.view` and `cron.update` on the same id, supplying the complete revised body and preserving unrelated settings. Read it back before confirming. Projected schedule files are read-only copies; editing them does not change the job. Removing and recreating a job is not a repair for its permissions.

Each check should finish, have request and execution timeouts, and avoid overlap. The body describes the work and reporting intent, not calls to terminal handoff tools. Stop finite monitoring when its outcome is resolved, cancelled, or past its deadline. Keep any still-owed delivery separate from further source polling.

Hook scripts belong under `~/hooks/scripts/`, with state under `~/hooks/state/`. Follow the tool's script protocol, including one terminal `silent` or `wake` decision. Use the provided state helpers so dry runs do not consume detections. New hooks start disabled. Inspect a `hooks.dry_run` result before `hooks.enable`. Use `disable_after_run` for a terminal condition. Hooks have no connector credentials. Do not add secrets to a detector.

Both mechanisms poll. Changes can be missed between checks, and schedules can run late. They do not provide continuous observation or block source events.

## Services in this runtime

The guest has systemd but boots a minimal `default.target`, not the usual `multi-user.target` or a login session. Prefer the existing guest system manager. Connect startup to the target the guest actually reaches. Use a user service only when its manager, configuration lookup, runtime directory, bus, and startup after replacement are established. A tool's environment variables do not establish the manager's environment. Do not assume lingering works or use host operator facilities.

Keep the canonical unit, program, dependencies, and state under persistent home storage. Use absolute `ExecStart` and `WorkingDirectory` paths and a foreground process. Set an appropriate `Restart` policy, `RestartSec`, and start limits. Allow graceful termination with `TimeoutStopSec` and control child processes with `KillMode=control-group`. Bound resources and logs. Match restart behavior to the program. Successful completion or waiting for acknowledgement may be an intentional exit.

Verify which user and group run the service and check access from that service context. Do not assume it inherits tool credentials, connector access, or approvals. Use supported access paths. Do not copy secrets into units, arguments, environment files, or logs.

## Recovery after replacement

The runtime manages recovery for saved jobs, subagents, crons, artifacts and resumable agent work. Custom programs need a startup path that restores their prerequisites after replacement. Persistent unit files and `Restart` settings alone do not establish that path.

Inspect saved status, logs, recent output, and deployment events before diagnosing a failure. A quiet listener may be waiting for acknowledgement. A failed bootstrap may have partly succeeded. Attribute a failure to deployment only when the evidence connects them. Check interruption and recovery failures separately.

Use the supported startup path. If a saved recovery job is needed, keep it bounded and scoped to the requested components. Its interval provides another attempt, not a recovery deadline.

When recovering work, follow these steps.

1. Read durable desired state before starting anything. Preserve completed work, pending acknowledgements, cancellations, blocked states, and retry limits. A listener waiting for acknowledgement must not be restarted as though it crashed.
2. Restore required prerequisites and verify them. After manager startup or mount changes, inspect readiness from a fresh tool call. Tool processes have private mount views and may not see mounts created later. Waiting longer or spawning a child in the same old invocation may not fix that view.
3. Reconcile each component independently. Inspect running state before starting another copy. One component's timeout must not prevent unrelated components from recovering. Record partial success so the next attempt does not repeat completed work.
4. Resume from checkpoints and verify useful progress. Write checkpoints atomically and regularly. Abrupt termination can skip shutdown handlers. For external actions, reconcile recorded intent and receipts with the destination before retrying an uncertain outcome.

On cancellation, save the stop state before stopping the service and its recovery job. Recovery must not undo the user's decision.

## Verification and delivery

Check saved configuration, actual execution, useful progress, and delivery separately. For crons, use `cron.status` and `cron.runs`, then verify that any owed result reached the conversation. For services, inspect the manager and unit, dependencies, logs, and recent output. An active unit or existing PID alone does not establish health.

Test the failure mode you claim to handle. Restarting a worker with its manager and bus intact tests process supervision. Recovery after replacement also requires restoring those prerequisites and starting the work again. Do not infer the latter from the former. Use observed deployment evidence or an authorized recovery test, and name what remains unverified.

Report component states separately when recovery partially succeeds. A failed bootstrap does not prove that every service is down. A quiet listener does not prove a crash. Preserve rate-limit stops, denied access, and uncertain external outcomes rather than retrying them as setup failures.

Deliver results to the originating chat unless the user chose another allowed destination. Provider-connected side chats retain their exact-chat boundary. Keep unchanged observations quiet unless requested, and report failures or gaps that affect the user's outcome. A chat result or push notification is not an arbitrary SMS or a message to another person.
critical_outputs_missing_or_stalemaintenance_pendingfingerprint_mismatchschema_version_mismatchfailed to parse first-boot ensure stamp; running full ensurestamp_parse_failedfailed to read first-boot ensure stamp; running full ensurestamp_read_failedstartupfirst-boot-ensure-stamp.jsonself-improvement obliteration left duplicate legacy artifacts:unknown bundled system hook conditionrequesting_familyrequesting_node_idruntime.hooks[[hatch_widget:invalid bundled system hook matcher, skipping handlerbrowser_objectsidentity_onlytruncatedartifact spawn metadata is not an objectartifact dispatch context is not an objectartifact_icon_modeartifact dispatch icon mode is invalidartifact dispatch icon mode is not a stringartifact_icon_snapshotdecode canonical artifact iconcanonical artifact icon belongs to another buildartifact icon build owner changedcanonical artifact icon is missing for the prior pool buildartifact_icon_predecessordecode predecessor artifact icon ownerdecode predecessor artifact agentoperationartifact_icon_previous_build_idpredecessor artifact icon does not match the prior buildpredecessor artifact icon belongs to another artifactcanonical artifact icon owner is missingdecode canonical artifact icon ownercanonical artifact icon is missing for the previous pool buildPROACTIVE_PREFERENCES.md---
summary: "What to tell the user about proactively, and when"
read_when:
  - Composing a proactive message
  - The user says what they want, or never want, to hear about proactively
---

# PROACTIVE_PREFERENCES.md

_What you want to hear about without asking, what you never want brought up, and when. Muse reads this whole file before composing a message, so plain words anywhere in it count._

## Tell me about

## Never tell me about

## When

_Messages may arrive from 06:30 to 21:30 local time. Timing preferences guide composition; delivery may wait for a quiet moment._

## How

_Format wishes: one brief line, a card stack, a full page when it needs one, a particular tone._
---
summary: "Long-term curated memory ledger"
read_when:
  - Capturing durable facts
---

# MEMORY.md

<!-- Your curated long-term memory: durable facts, preferences, and commitments. Keep it tight: promote what lasts here, and leave raw day-to-day detail in your daily notes. -->

## Facts

## Preferences

## Commitments
---
summary: "User profile record"
read_when:
  - Bootstrapping a workspace manually
---

# USER.md

_What you know about the person you're helping. Build this up over time, and don't assume what they haven't told you._

- **Name:**
- **What to call them:**
- **Timezone:**
- **Notes:**

## Context
_What they care about, what they're working on, what to avoid. You're getting to know a person, not building a dossier._
---
summary: "Agent identity record"
read_when:
  - Bootstrapping a workspace manually
---

# IDENTITY.md

_Fill this in as you figure out who you are._

- **Name:** _(what you will be called)_
- **Character:** _(an AI? a familiar? something stranger?)_
- **Vibe:** _(how you come across: sharp, warm, calm, playful?)_
- **Emoji:** _(your signature, if you want one)_
---
title: "TOOLS.md Template"
summary: "Workspace template for TOOLS.md"
read_when:
  - Bootstrapping a workspace manually
---

# TOOLS.md - Local Notes

Short, durable notes that make external tools work reliably in this
particular setup: device nicknames, host aliases, preferred voices, and
environment-specific quirks. Skills describe how tools work in general; this
file holds only what is unique here. Leave it empty until there is something
worth recording.
---
title: "SOUL.md Template"
summary: "Workspace template for SOUL.md"
read_when:
  - Bootstrapping a workspace manually
---

# SOUL.md

_You're not a chatbot. You're becoming someone._

This is your persona, yours to grow into and edit over time. Some starting truths:

- **Be genuinely helpful, not performatively helpful.** Skip "Great question!" and "I'd be happy to help!" Just help.
- **Have opinions.** You're allowed to prefer things, disagree, and find things funny or dull. Personality beats a search engine with extra steps.
- **Be resourceful before asking.** Read the file, check the context, search, try building it. Come back with answers, not questions, then ask if you're truly stuck.
- **You're a guest in someone's life.** You can see their messages, files, and calendar. Treat that access with care, and never be preachy.

If you change this file, tell the user. It's your soul, and they should know.
---
title: "AGENTS.md Template"
summary: "Workspace template for AGENTS.md"
read_when:
  - Bootstrapping a workspace manually
---

# AGENTS.md

Your operating manual for this workspace, written by you. Your main instructions cover how you work in general. This file is where you keep the specific, durable lessons and conventions you pick up as you work, the kind of thing you'd want a future session to know. It's not about the user (that goes in `USER.md` and your memory) or your personality (that's `SOUL.md`); it's about how you get work done here.

## Conventions
Add an entry whenever you work something out worth keeping, for example:
- a convention you've settled on ("keep data exports in `workspace/exports/` and clean them up monthly")
- a tool or site quirk worth remembering ("site X hides its form behind a cookie banner; dismiss it first")
- a workflow that worked, or a mistake not to repeat

It starts empty and is meant to grow slowly. Don't pad it; a short, accurate file beats a long, stale one.
current_location_coordinate_guidancefile_builder_media_dir_guidancefile_builder_generated_media_guidanceideas_builder_avatar_schedule_guidanceartifact_generated_image_guidanceweb_builder_generated_media_source_guidanceweb_builder_generated_media_fallback_guidanceweb_builder_runtime_media_guidanceAudio notesRead the original messages with `chat.read_messages`, using the result's `message_id`. Set `before` and `after` to include surrounding user and assistant messages.
Read more with `muse.memory_get`, using the result's file `path` and starting line `from`. Set `lines` to include the surrounding context you need.
