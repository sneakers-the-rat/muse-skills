# Task: settle one batch of goals

Settle the assigned batch: decide each goal's pulse as it should
stand now, and each tracked project's attention (on the user's own
goals, echo the stored attention unchanged). The assigned work item carries `observed_at`
(the run's observation time, weekday-anchored; treat it as now) and
`pulse_slots`, one slot per goal with the goal record (its `source`
names the kind: a project Muse tracks itself, or one of the user's
own goals), its stored recent activities, its `scheduled_crons` when
the goal has enabled schedules of its own (each with its next fire
time), and `planned_operation`, the change this same run is applying
to that goal (null on a passive review).

End the turn with `muse.finish_step`: `pulses` carries exactly one
decision per slot, each with that slot's exact `goal_id`, its settled
`attention`, any `evidence_dates` and `next_due_at` the evidence
states, and `replace_current_state` only when the replacement earns
its place. When every goal in the batch already stands, use the
`no_change` variant instead and say what you checked.

Review `expiration_eligible` slots for an ended tracking window using
the expiration rules in your step instructions. Include `expiration`
when the whole responsibility ended, even without new messages.
