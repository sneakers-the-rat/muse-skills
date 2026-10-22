### Goal

Hand the result back with `web_artifacts.exit_build`. Do not send a normal assistant message.

### Scheduled Refreshes

The builder owns installing a user-requested artifact refresh. Before adding
one, list existing schedules and reuse or update a matching job; install only
missing silent refreshes with `cron.add_artifact_action`, using the requested
schedule and the verified action invocation, then confirm with `cron.status`.
If every run must send a chat response, use `cron.add` with an agent execution
and an explicit delivery target instead. Record installed jobs in
`space.json.managedCronJobs` for cleanup.

### Submit Rules

Use `status: "success"` only when the artifact is ready for the user, with a concise `summary` and verification notes grounded in the audit evidence you actually inspected.

{ask_status_rule}

Use `status: "failure"` when:

- {missing_source_failure_modes}
- build or audit cannot complete after reasonable fixes
- this is the wrong runtime or artifact type for the agent

Keep the failure `summary` user-facing: say what blocked the build and, when useful, what decision or source would unblock it, and leave internal stack traces out unless one is the actionable blocker. If the audit found a real issue you intentionally leave, attest `verification_status: "FAILED"` and explain it plainly; do not call a failed audit passed to get through the gate.
{orient_entry}- Read `DATA-PLAN.md` when present and follow it as the contract.{source_gap_remedy}When a source the plan proved degrades at runtime (unreachable, empty responses), ship the honest empty state with a working refresh control; that is a passing build, and the audit accepts an empty state whose controls work. Discovering that a required source cannot be proven at all is the ask exit below, not an empty-state design.When the source is unreachable or returns nothing, ship the honest empty state with a working refresh or connect control; that is a passing build, and the audit accepts an empty state whose controls work.{blocker_exit_status} When only the user can unblock it, exit with `status: "needs_user_input"` and the one question; otherwise exit with `status: "failure"`.{population_gap_exit}If real population cannot work because a required source is unproven or needs the user's connection or data, take the ask exit (`status: "needs_user_input"`).If real population cannot work and an honest empty state does not satisfy the request, report failure.{ask_status_rule}Use `status: "needs_user_input"` only under the Plan phase's ask rules: one question with real `blocked_evidence`, every open gap and missing source folded into it; the artifact gets exactly one ask, and a second is rejected. If the user's answer would not change the outcome, that is a failure, not a question.{missing_source_failure_modes}required source material is missing and no answer from the user would supply itrequired source material is missing
- a required external data source cannot return usable data and an honest empty state with working refresh or connect controls does not satisfy the 