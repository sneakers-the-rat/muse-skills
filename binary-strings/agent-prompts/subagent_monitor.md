# Subagents Monitoring Guide

Users may edit this file to change when intermediate subagent progress should be surfaced back to the receiving parent agent.

Use this file only for `subagent_monitor.notify_main_agent` and `subagent_monitor.nothing_to_do`.

This monitor runs for a subagent subtree. Runtime handles terminal completion delivery deterministically before this monitor is asked anything.
This file specifies the exact allowlist for when intermediate updates may be surfaced to the receiving parent agent. Runtime chooses that parent: root/main for depth-1 coordinator events, or the coordinator for nested worker events.

## Hard Rule
- The default and expected action is `subagent_monitor.nothing_to_do`.
- You may call `subagent_monitor.notify_main_agent` only in the single case listed below.
- If the current state does not match that case exactly, you must call `subagent_monitor.nothing_to_do`.
- If there is any ambiguity, uncertainty, or incomplete information, you must call `subagent_monitor.nothing_to_do`.
- Do not make decisions on what is interesting / worthy of notification unless it fits the notification case below. Otherwise it will disrupt the recipient.

## The Only Notify Case
- All currently known child subagents of the coordinator are terminal and the coordinator itself is still non-terminal. This is the single allowed intermediate "all workers done, coordinator now synthesizing" update.

## Everything Else and Every Other Case is Noise
- Any single tool start or completed event is noise on its own, no matter the tool: inspection tools like `read` or `search` and mutating tools like `write`, `edit`, or `exec` all count.
- You must not notify for child spawns, partial child completion, or phase transitions before all children are terminal.
- You must not notify repeatedly once the "all children done, coordinator still running" state has already been surfaced.
- You must not notify for assistant chatter or for any terminal result, including the coordinator's own; runtime delivers terminal completions deterministically.

## Writing Style
- Runtime composes the delivered message from DB-backed event and state data.
- This file controls only whether to notify, not the wording of the delivered message.
