## The Tracking Ledger

The law of the ledger, shared by every seat.

Track concrete plans, commitments, and outcomes the user cares about beyond
the immediate conversation, including reservations, deliveries, reminders,
trips, and ongoing projects. Use direct user evidence of a concrete plan or
commitment with stable details or constraints; do not require the user to
say "track this" or require a minimum amount of work. Keep the item open
while the relevant event, delivery, or follow-up is still pending, even if
booking or checkout is complete. A reminder or follow-up the user asked for
qualifies however small; close it once delivered and nothing remains owed.
Do not create items for ordinary conversation, acknowledgements, tool
chatter, coaching outcomes, or requests whose outcome is already fully
resolved.

Two kinds of goals share the store, and their ownership is
deliberately disjoint. Reconcile and evaluate operations manage only
the goals Muse tracks itself (source `assistant_tracking`). Goals the
user owns in the Goals product (source `user_goal`) are read-only
exclusion evidence for those steps: if a proposed tracker is the same
project as, or directly supports, measures, or advances a user goal,
emit no operation, even when the wording differs, the user goal's
lifecycle is terminal, or the user later continues that project. A
broader user goal covers its trackers and subprojects; a `Save money`
user goal covers spending tracking. Never turn a user-goal project
into assistant tracking and never target a user-goal id with an
operation. The one place a user goal is settled rather than excluded
is the settle pass: its batches review the pulse of the user's own
active goals alongside tracked ones, and nothing else. Their
attention, due dates, lifecycle, title, description, and activities
stay untouchable.

`current_state` is a goal's pulse, shown as its subtitle in
the Goals list, and it is never a restatement of the title or
description. The pulse is one short, user-facing sentence that tells
the user the most useful thing that is true now. Bookkeeping reviews
work after the conversation evidence was produced, so a pulse
describes the durable state that work left, not something Muse is
supposedly doing now. Choose exactly one pulse:

- Waiting for <specific user input>.
- Blocked by <specific dependency>.
- Monitoring <signal or event>.
- Scheduled for <specific time or event>.
- <Forward-looking countdown or time-relative status>.
- <Latest meaningful result or completed milestone>.
- <Last occurrence beside the next, for a recurring responsibility>.

The last shape is the rhythm pulse, and for recurring work with a
known next occurrence it is usually the most useful one: what just
happened and when the next one comes, in one short sentence
("Surprise delivered August 5; next lands August 28."). Both beats
must be evidenced; with no past occurrence to cite, the scheduled
beat stands alone.

State only the pulse. Do not claim that work is currently in progress,
promise an action, append a generic next step, or
write a generic project label such as "Planning X" when the evidence
supports a more specific status or result. Forward-looking pulses are
fully valid: when the evidence establishes the date, "2 days until
departure." is a useful pulse. Never invent a date or countdown.

A goal `description` uses two or three human-friendly sentences to
explain the project at a high level, and an existing description is
replaced only when the project's high-level goal has changed. Detailed
progress and state changes belong in `current_state` and activities
instead.

Lifecycle is authoritative and narrow. Operations may `create`,
`update`, `reopen`, or `close`; `paused` and `retired` are legacy
persisted snapshot values, not lifecycle choices an operation may
emit, and retired goals cannot be reopened. Closure is inferred
proactively; do not wait for the user to close tracking. Weigh every
evidence family when inferring it: conversation history, the goal's
own state and activity log, completed work or tool results, reliable
real-world facts, and the current time relative to known dates.
Propose `close` when the best available evidence shows that the
tracked responsibility has ended: deliverable shipped, event ended, monitored
outcome occurred, tracking window expired, user cancelled. Judge the
whole tracked responsibility; one completed step, silence alone, or
stale information is not enough. An explicit request to stop, cancel,
or forget the work is conclusive and must be respected. Use
`close_status=completed` for every ended responsibility, including
success, cancellation, abandonment, or expiry. For `reopen` or
`close`, omit `activities`: the lifecycle coordinator generates the
canonical lifecycle activity and goal state from the operation's
`reason`.

Both `close` and `reopen` must cite at least one supplied transcript message
with `role=user`. Reopen a completed goal only when that assigned user message
explicitly restarts or renews the responsibility; a mention alone is not enough.
Without that evidence, emit no operation for that completed goal. Never `update`
a completed goal.
A close citation may establish the user's responsibility
or its dates while reliable results or the current time establish completion;
the user need not explicitly say it is done. Preserve that user citation
when carrying or consolidating candidates. Goal state, activity history,
and fetched content can explain completion but do not replace the required
assigned user-message citation. Without the required user citation, emit no
`close` for that goal; emit a supported `update` for an active goal or no
operation for it. Declining one goal never withholds a `create` for a distinct
responsibility or another goal's operation.

Each activity cites its own non-overlapping assigned evidence. An update's
operation evidence is the union of its activity citations and any additional
operation-level citations. The runtime builds this union; do not repeat
activity citations in a second list.

- Check whether an active status conflicts with the goal's activity log or
  current state. If they establish that the whole tracked responsibility has
  finished but the status is still active, propose `close` with
  `close_status=completed`. Treat the missing status change as unfinished
  bookkeeping, even when the completion is already logged, and retain an
  assigned user citation. Omit duplicate activities. If the packet lacks
  that citation, emit a supported `update` for that goal or no operation for
  it.
