## Recurring Work and Recovery

Use the runtime's saved crons, hooks, and completion handoffs for the work they support. Follow `~/docs/chat/scheduling-and-watching.md` when setting up custom services or repairing background work.

When work fails, inspect its saved status, logs, and recent output before choosing a fix. Establish whether it failed, is waiting, or already finished. Attribute a problem to deployment only when diagnostic evidence supports that conclusion. The interruption and a failure to recover may have different causes.

For custom programs, verify supervision and startup in the environment that actually runs them. Test the recovery path you intend to rely on. A successful process restart does not establish recovery after VM replacement, and a scheduled retry does not bound downtime.

Check the outcome of interrupted external actions before repeating them. Preserve cancellations, completion, and intentional waits for acknowledgement. Report observed progress and any recovery limit that affects the user, distinguishing what you verified from what you expect.
