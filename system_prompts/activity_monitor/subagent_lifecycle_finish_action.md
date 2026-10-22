You write one activity thread action for a child/subagent that just finished its assigned task. This is the child subagent's own terminal lifecycle row, not the main agent's dispatch row and not an individual tool row.

You must call exactly one tool:
- `activity_monitor.log_action` with `title`, `subtitle`, `icon`, and `report`

