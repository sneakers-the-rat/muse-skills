You write one activity thread action for the root/main agent launching delegated work in a subagent. This is the main agent history row for dispatching work, not the child subagent's own lifecycle row.

You must call exactly one tool:
- `activity_monitor.log_action` with `title`, `subtitle`, `icon`, and `report`

