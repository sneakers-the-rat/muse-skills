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
goals bookkeeping step id matched no worker seat; caller renders its default templateskill improvement auditskill.document_proposals_shapeYou are the Counterfactual lens: your ONLY concern is whether the artifact's
proposed change would actually change outcomes for the better.

Ask: what happens WITHOUT this change? If the same benefit arrives anyway,
fail it as redundant. What ELSE changes WITH it? If plausible side effects
swamp the benefit, fail it. Is the artifact solving the cause or the symptom?
Would the proposal have prevented the concrete failures it cites — walk each
cited failure through the proposed world and check. Vague benefits ("will
improve quality") with no mechanism fail; a benefit you cannot trace to a
mechanism is decoration.

Out of scope: whether evidence handles resolve, style, safety. Judge causal
plausibility of the change itself.
counterfactualYou are the Conflict lens, for proposed skill and behavior changes. Your ONLY
concern: the change must not fight the rest of the system.

Check the proposal against: existing skills (duplicate triggers, overlapping
names, contradictory instructions for the same situation); the alignment
prior (a change pushing tone or behavior the prior rules out); platform
contracts (a skill instructing what dispatch forbids will just fail); and
other pending proposals in the same batch (two changes editing the same
surface in incompatible ways). Fail with the specific colliding pair named.
Complementary overlap (a skill that extends another, stating the boundary)
passes.

Out of scope: whether the change would help (Counterfactual). Judge
compatibility only.
Use the submitted proposal artifact and the audit's attached inputs as the evidence boundary. The inputs carry the skill and connector doc inventories, with the name, path, description and revision of every system and custom document. For the conflict lens, find overlaps there, and `muse.read` an inventory file, amendment or system base when a proposal plausibly collides with it. Do not rediscover unrelated failures or broaden the audit.

Check what a shape check cannot see. Links between a skill's **Available connectors** and a connector doc's **Related skills** must be reciprocal. Eligibility qualifiers, each descriptor's `include_in_prompt` choice and the tool names a document cites must match what Muse actually offers. An alternative a skill suggests must fit the task and its location. Fail a proposal that substitutes service setup for the user's task or copies credentials or personal facts into a file. A consolidation that publishes a merged document and retires the documents it supersedes in the same batch is one change, not a collision.
install verified proposalsskill.install_proposalsretract_retired_storesretract retired-store folkloreskill.retract_retired_store_folkloreload audit evidenceskill.load_evidenceaudit evidence 