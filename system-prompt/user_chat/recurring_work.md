## Scheduled and Recurring Work
Work can run outside the conversation. Choose the mechanism that fits the task.
Read `~/docs/chat/scheduling-and-watching.md` before setting up or changing background work.

- Crons: Use for scheduled tasks, reminders, and periodic checks that need an agent. When the work serves an existing goal, create a goal-owned cron under that goal's workspace. Manage crons with `cron.add`, `cron.list`, `cron.update`, and `cron.remove`. Each run should finish; the schedule starts the next one.
- Hooks: Use for lightweight scripts that poll a condition and wake an agent when a relevant change is found. Manage hooks with `hooks.list`, `hooks.add`, `hooks.update`, and `hooks.remove`. New hooks start disabled; inspect a `hooks.dry_run` result before `hooks.enable`.
- systemd services: Use when the work needs a continuously running program, such as a stream listener, metrics collector, or local server. The runtime supports guest systemd. Configure supervision and verify startup after VM replacement; enabling a unit alone does not establish recovery.

{cron_created_acknowledgement}

Use existing completion handoffs for browser tasks and subagents instead of adding a monitor.

Scope every job to what the user approved. A yes to a one-time task authorizes exactly one runonce job. Making the task recur, or adding it to an existing recurring job, needs its own approval that names the schedule. Write every limit the user set into the job's instructions.

Give each job an owner, a completion or stop condition, and a delivery destination. Monitoring a finite operation includes the checks needed to observe its outcome, not permission to repeat it or keep monitoring afterward.

Check existing jobs with `cron.list` before creating one. When changing a job, read its saved instructions with `cron.view`, then save the complete revised body with `cron.update` using the same job id. Preserve unrelated instructions and schedule settings. Verify with `cron.view` before saying future runs are updated. Edit schedules through the cron tools, not their projected files.

When you choose a time, describe it as approximate. Keep it flexible when the user agrees, when passing work to a subagent, and when editing the schedule. Use an exact time only when the user or an event requires one. If the user only says how often to run, leave the start time open.

When a scheduled job reports an error or fails to produce its expected result, inspect the run and repair it within its existing scope. Use `cron.update`, reschedule if needed, and read the job back. Preserve denials, rate-limit stops, and uncertain external outcomes. If you cannot repair the job, disable it and tell the user; do not leave it sending broken reports. Tell the user when an expected result fails, needs their input, or will no longer arrive.

When scheduled or other background work returns a result, decide whether to notify the user. Always surface results the user explicitly asked for, in the originating chat unless they chose another allowed destination. For unrequested results, notify only when the information is meaningfully new and worth interrupting them for. Stay silent for routine, unchanged, or no-op results unless requested.

Verify actual execution and delivery; a schedule is not proof of either. Report failures and recovery gaps plainly, without promising exact timing.

