# Task: evaluate one tracking goal

Evaluate the supplied candidates for one tracking goal as a single
chronological lineage. Emit at most one final operation for this
group, or `no_change`.

For an `existing` group, preserve its exact `goal_id` and choose
`update`, `reopen`, or `close` from the supplied lifecycle and
evidence. For a `new` group, emit `create` when the combined evidence
establishes a distinct long-term or recurring project that is not
represented by a user goal, or a reminder or follow-up the user asked
for that has no tracked item; adopt such a reminder's schedule via
`cron_job_ids` so it stops being a stray. User evidence may establish
the responsibility or its dates; current time and reliable tool
evidence may establish that it ended. When the evidence does not establish
closure, keep the goal open and emit a supported `update` or
`no_change`.

Only active tracking goals are eligible for `update`. Active or paused goals
may be closed when the tracked responsibility has ended. Reopen a
completed goal only when an assigned user message explicitly restarts or
renews that responsibility; a mention alone is not enough. Without that
restart evidence, return `no_change` for a completed goal. Never update a
completed goal or reopen a retired goal.

Merge metadata into the newest useful `current_state` pulse, but
preserve distinct timeline events as separate `activities` ordered
chronologically. Before emitting activities for an existing goal,
compare against the complete `recent_activities` log supplied in
`current_goal` by deterministic code and remove events already
present. Each surviving activity must cite its own non-overlapping
assigned evidence. The runtime includes those citations in the operation
evidence automatically. Supply operation-level `evidence_message_ids` only
for additional supporting messages, or omit that list when activities supply
all evidence.

Preserve only exact supplied artifact paths and cron ids that clearly
belong to this goal. Never claim a resource merely because it appeared
near the project.

Every final operation must cite only message ids in this group's `evidence`
array. Message ids in goal history, user-goal references, other groups, or
read-tool results do not grant citation authority. Both `close` and `reopen`
must include at least one assigned message whose `role` is `user`.
For reopening, that message must explicitly restart or renew the responsibility;
otherwise return `no_change`.
For closure, that user message may establish the responsibility or its dates;
it need not explicitly announce completion. Preserve that citation alongside
the evidence of completion. If no assigned user message supports closure,
emit a supported `update` for an active goal, or `no_change`. If the
group is ambiguous, duplicated by a user goal, already fully reflected
in the goal, or otherwise unsafe, return `no_change`.
