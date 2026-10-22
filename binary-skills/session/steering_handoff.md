The user interrupted your work.

For each message immediately below this note:
- If it refines, redirects, or stops the current work, adjust accordingly.
- If it's a separate task that can run without you or the user, hand it to a subagent so it runs in parallel.
- If it cannot move forward without user input, ask the user for the missing information or decision.

Don't silently drop anything the user still wants, including the work already in progress. Handle or delegate what you can now and clearly state anything that still requires the user's input.
runtime.device_syncruntime.external_synccancellation_handoff.mdInternal cancellation notice.

The previous active turn was explicitly interrupted by the user. Any unfinished
tool call that was already dispatched may have partially or fully applied; check
what actually happened before retrying it. Descendant work was asked to stop but
might have completed concurrently. Treat unfinished plans from that turn as
cancelled unless the user asks to resume them.
