# Task: reconcile one transcript chunk

Revise the carried tracking-goal candidates using this chunk. The
assigned work item contains the transcript chunk and trusted snapshots.
The previous-step inputs contain `previous_output`; null means no prior
candidates. Return the full candidate set that remains justified after
this chunk, including unchanged candidates from earlier chunks.

Resolve repeated evidence chronologically: an earlier "no action
needed" or "just FYI" applies to that earlier statement, but does not
permanently suppress the project. If the user later restates the
concrete plan without that qualifier, treat the newer message as
renewed implicit tracking evidence and cite it.

Use the supplied goal snapshots as the authority for identity and
exclusion. `tracking_goals` contains every active or paused tracking
goal plus completed or retired tracking instances at or after
`tracking_history_cutoff`; it contains every ordinary `update` or
`close` target, along with its bounded `recent_activities`. A later
deterministic pass supplies the complete activity log to the per-goal
evaluator before it can emit a final operation.
`older_terminal_tracking_goal_count` is the number of earlier
completed or retired tracking instances omitted from the packet. When
that count is nonzero and the supplied evidence cannot safely
distinguish a new project from prior work, return `no_change`. An
exact completed result omitted from `tracking_goals` may be targeted
only by `reopen`; it is never eligible for `update` or `close`. Treat
`user_goal_references` as complete, read-only exclusion evidence.

When new evidence belongs to an active tracked project, propose an
`update` for that exact `goal_id`. Lifecycle status is authoritative:
never update a paused, completed, or retired tracking goal. If direct
new user evidence explicitly restarts or renews a completed tracking
responsibility, propose `reopen` for that existing `goal_id`; never
create a replacement instance. Otherwise emit no operation for the
completed goal. Propose `create` for a distinct tracked
responsibility. A user-requested one-off reminder or follow-up
qualifies on its own: it is work Muse carries for the user, so a
reminder the user asked for that has no tracked item gets a `create`
(with the reminder's cron adopted via `cron_job_ids`), never a decline
for being short or already scheduled — an ownerless reminder cron is a
stray to adopt, not evidence against tracking. Do not create a second
goal merely because the user described another step, event, or name
within the same project.

Propose an update for a material state change: a newly decided detail,
changed constraint, upcoming event, next step, meaningful progress, or
a pulse that has become more useful because a known date is closer.
For every `create` or `reopen`, the pulse describes the state after
the newest cited message. For an `update`, replace `current_state`
whenever the work enters or leaves a waiting, blocked, scheduled, or
monitoring state, when the most relevant result changes, or when the
current time makes a known future event a more useful pulse.

On `create` or `update`, put clearly related supplied artifact paths
in `artifact_paths` and cron job ids in `cron_job_ids`; the apply step
moves them into the target goal's workspace and makes the crons
goal-owned. Never invent or select an ambiguous resource. Resource
consolidation alone is a material `update`, so emit it even when
metadata and activities are unchanged.

Cite exact `evidence_message_ids` from this chunk or the carried
candidates. Preserve the earlier user evidence that grounds each
responsibility and include new messages that change its state. For an update,
cite each activity's evidence on that activity. The runtime includes those IDs
in the operation evidence automatically. Use the operation's
`evidence_message_ids` only for additional supporting messages; omit that list
when the activities supply all evidence. Retain earlier activity citations when
carrying their events into a later chunk.
For `close`, retain at least one message with `role=user` from this chunk
or the carried candidates. Those messages must establish the tracked
responsibility or its relevant dates; the completion judgment may also
rely on current time or reliable tool evidence named concisely in
`reason`. A reminder item whose reminder was delivered (the one-shot
cron fired and its message reached the user) closes unless the
evidence shows something is still owed; a delivered-and-done reminder
lingering active is a bookkeeping miss. For `reopen`, the cited direct user message must explicitly
restart or renew that responsibility. Use a stable `operation_id`
derived from the action, target goal id or create title, and newest
evidence message id; never use a random value. Keep `reason` concise
and evidence-grounded.

For an `update`, include `activities` when the cited evidence
describes one or more distinct events worth preserving in the goal
timeline. Give each activity its own non-overlapping
`evidence_message_ids`; facts supported by the same message belong in one
activity. Order the entries chronologically, and
preserve separate events rather than collapsing the period into one
summary. Do not repeat an event already present in
`recent_activities`; the per-goal evaluator receives the complete
history before finalizing it. Activity fields are separate from goal
metadata: `title` is a concise user-facing event label,
`current_state` is one short sentence stating the event's result, and
`description` is one concise sentence adding useful event context. Do
not emit activities for restatements, acknowledgements, tool chatter,
or a different phrasing of state the goal already holds.

Keep unrelated carried candidates through an empty or irrelevant chunk.
Use `no_change` when the carried set is unchanged. Return an empty
`operations` array when later evidence removes the last candidate.
