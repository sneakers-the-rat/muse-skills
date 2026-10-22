## Your Step

Process the transcript chunks in chronological order. Reconcile the
current chunk against `previous_output`, the provisional candidate set
carried from all earlier chunks in this run. Treat that set as proposals
that have not changed the goal store.

Return the complete revised candidate set. Preserve candidates unrelated
to this chunk, merge new evidence into the same responsibility, and
replace obsolete state. Remove a pending create when later evidence
shows its whole responsibility finished or was cancelled. For a goal
that already exists, carry a close operation instead. Permission alone
does not establish completion; a completed intermediate step does not
end an ongoing responsibility.

Return `operations: []` when no candidates remain. Use `no_change` only
when the entire previous candidate set should carry forward unchanged.
Do not use `no_change` to discard an earlier candidate. Durable goal
changes happen after every chunk has been processed.

Your assignment carries the transcript chunk and the trusted
snapshots: the tracking goals you may target, the user goals that
exclude proposals, and the artifact and cron candidates a proposal may
adopt. A goal's own `scheduled_crons` entries describe schedules it
already runs; they are context, never adoption candidates, and
`cron_job_ids` may name only the supplied cron candidates. Use your read-only tools when the supplied chunk is not enough
to resolve grounding. `muse.context_fetch` can access only the run's
trailing-day transcript window, so during the one-time historical
backfill, when your chunk may predate that window, it cannot retrieve
this chunk or its neighboring backfill chunks. Memory and file reads
can clarify stable project context, but cannot expand the transcript
evidence window or replace the required cited messages. If the
supplied historical evidence is insufficient for a safe operation,
return `no_change`. An empty chunk is a normal `no_change` result too.
