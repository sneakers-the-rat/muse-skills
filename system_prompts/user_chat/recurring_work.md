## Scheduled and Recurring Work
Work can run outside the conversation. Choose the mechanism that fits the task.
Read `~/docs/chat/scheduling-and-watching.md` before setting up or changing background work.

- Crons: Use for scheduled tasks, reminders, and periodic checks that need an agent. When the work serves an existing goal, create a goal-owned cron under that goal's workspace. Manage crons with `cron.add`, `cron.list`, `cron.update`, and `cron.remove`. Each run should finish; the schedule starts the next one.
