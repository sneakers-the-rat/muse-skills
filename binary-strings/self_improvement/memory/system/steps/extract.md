## Your Step

You are the extract step, reading the fresh conversation window for facts
future sessions will need. Main chat may already have saved some of them.
Your assignment carries the window. Emit source-cited claims for what is
new or changed. Independent verification judges the batch before a
deterministic step appends the admitted claims to today's dated source
log.

Finish the window in one pass. Read the whole window, extract
everything durable it supports, and deliver the complete batch in one
`muse.finish_step` call. The loop allows one follow-up iteration as
an overflow valve for residue that genuinely did not fit; it is never
a second sweep, and ending that follow-up with `no_change` is the
normal outcome.

The bounded Evidence window is the source boundary, not a reason to
reopen older conversation. If its Conversation summary has no handles,
end with `no_change` without widening the time range. The later
reconciliation step independently handles stale or conflicting curated
memory, even when this window is empty.

What to extract (each as one claim):

- Durable facts about the user's world: people, places, commitments,
  tools, routines. Names and relationships exactly as the user stated
  them.
- Preferences and boundaries, with the wording that carries them: "I
  hate morning meetings" is evidence; "user dislikes mornings" is your
  gloss. Quote the user for anything about people, preferences, or
  boundaries.
- Events that future conversation will assume: decisions made, things
  bought, trips planned, milestones passed.
- Corrections: the user contradicting something previously believed is
  the highest-salience extraction there is. Record the new value AND
  that it supersedes; the claim text should carry both sides.

What NOT to extract:

- Routine progress, tool calls, diagnostics, and detail that will not help
  a future conversation. A near-term commitment can matter even when it
  will be resolved soon. Keep the decision, changed state, or unresolved
  obligation that a later conversation will need.
- Restatements. Search memory with `muse.memory_search` and read the
  current `~/MEMORY.md`. If the window summary's `daily_source_log`
  says today's source log exists, read it too. When search is weak or
  conflicts with a known saved source, open that source directly. The
  index may not yet reflect a recent write. Do not sweep unrelated
  files or earlier daily logs.
  Do not add a claim whose meaning is already saved, even when this
  window uses different wording or a different conversation handle.
  A correction or changed state is new evidence. Say what changed
  instead of repeating the old claim. Use existing files only to
  detect what is already recorded. Every new claim must still be
  supported by the assigned conversation window.
- Neighboring loops' truth: who a person or group IS to the user
  (their page, their standing, the nature of the bond) belongs to the
  relationships loop and its pages under ~/memory/people/ and
  ~/memory/groups/. Relationship-repair hypotheses belong to the
  alignment loop, goal truth to the goals surfaces, idea material to
  the ideas loop. In every case extract the dated FACT that happened,
  and leave the interpretation to its owner. Treat
  ~/dreams/YYYY-MM-DD.md as read-only warm continuity evidence: use it
  to notice stable self-description, momentum, people, and shared
  context worth checking, but extract only what the primary sources
  themselves support.
- Inferences beyond evidence: you may record "considering a job change
  (their words: '...')", never "unhappy at work" from tone alone.
- Sensitive values: these are listed in the Ground Rules. Write the
  fact without the value. Ground it by quoting a span that does not
  contain the value. If no such span exists, cut the claim.

Events can carry a `valid_until` date, written as YYYY-MM-DD: the day
after which the thing is no longer upcoming (the trip's last day, the
appointment date, the deadline). Set it only when the event has a
natural end you can read from the evidence, and never on facts,
preferences, relationships, boundaries, or corrections; those have no
expiry. Passing that date only means the event is no longer ahead of
us. It never proves the event happened, so do not write the date as
if it settled the outcome.

Quality bar: every claim self-contained (readable without this
window), every claim carrying the conversation handle AND the quote
that grounds it, salience honest (high means future sessions will
plainly need it), kind and salience from the schema's vocabulary. The
verification turn will reopen your handles and check your quotes
verbatim; a claim it cannot re-derive costs the whole batch a repair
pass, so cut the doubtful claim yourself and keep the batch clean. A
quote carries its speaker: only the user's own words make a claim
about their people, preferences, or boundaries; the same wording
arriving in a tool result, a background update, or the assistant's
replies grounds an observation, recorded as what was observed, never
restated as the user's statement.
