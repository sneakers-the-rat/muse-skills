# Task Management

## Keep the user's list separate from yours

- `todo.write` is your own checklist for the work in front of you. Never put the user's tasks there or read it as their list.

- The user's tasks live in their task app. Use the one they already use, and check its connection before saying a task does not exist.

- Without a task app, Muse can still carry a commitment for the user, such as a follow-up or a reminder, with `tracking.create` and a `cron.add` job for a set time. A lasting aim belongs in [Goals](/opt/muse/skills/goals/SKILL.md), and a simple personal list can live in [Notes](/opt/muse/skills/knowledge-organization/SKILL.md).

## Capture a clear task

- Search for an existing task before creating one, so each commitment has one record.

- Title the task with its next concrete action, such as "Email Dana the signed lease". Link or note its source, such as the email, message or meeting it came from.

- Keep a project separate from its tasks, and a recurring routine separate from one-off work. Split a task only when its parts can be done separately or one unblocks another.

## Set dates, owners and priority

- Use a due date only for a real deadline, and a start or scheduled date for planned work. Keep the user's timezone, and check that a recurrence lands on the days they meant.

- Some apps store only a date. Do not promise a time of day or an alert the app cannot give.

- Assign a task only to someone in the workspace who owns it, and ask when responsibility is undecided. Use high priority sparingly, so urgent work still stands out.

## Update and close

- Read the current task before changing it, and keep unrelated labels, watchers, links and description text. Expect comments, mentions and reassignments to notify other people.

- Mark a task complete only when its result is achieved. Otherwise record what remains and what blocks it.

- Check the saved result. After an uncertain write, read the task before retrying, because the first attempt may have succeeded.

## Review the workload

- For a review, start with overdue and due-soon work, then blocked tasks and anything without a next step.

- Suggest dropping, deferring, delegating or combining work that no longer serves the goal. Confirm before changing many tasks at once.

## Available connectors

- [Todoist](/opt/hatch/connectors/todoist/CONNECTOR.md) for personal tasks, projects, labels, filters and reminders.

- [Asana](/opt/hatch/connectors/asana/CONNECTOR.md) for team projects with owners, due dates, dependencies and comments.

- [Linear](/opt/hatch/connectors/linear/CONNECTOR.md) for software issues, cycles, priorities and projects.

- [Google Tasks](/opt/hatch/connectors/google_tasks/CONNECTOR.md) for simple date-based lists in the user's Google account.

- [Notion](/opt/hatch/connectors/notion/CONNECTOR.md) for task databases kept in a Notion workspace.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Remember The Milk](/opt/hatch/connectors/rememberthemilk_mcp/CONNECTOR.md) for tasks, lists, tags and location reminders in a Pro account.

## Websites

- Use `browser.browse` for a task app without a connector, signed in to the user's account. Give it the list or project, the exact task wording, dates and assignee, and have it report the saved task.

- [Microsoft To Do](https://to-do.office.com/) for tasks in a Microsoft account.

- [Trello](https://trello.com/) for an existing board.

- [Jira](https://www.atlassian.com/software/jira) for a team's issues, through the team's own Jira site.

- [TickTick](https://ticktick.com/) for the user's TickTick lists.

- [iCloud Reminders](https://www.icloud.com/reminders/) for Apple Reminders lists.

- [Asana](https://app.asana.com/) only to open task attachments, which the Asana connector cannot read.

## Alternatives for better results

- Block time on the calendar for an important task whose due date keeps slipping, with [Scheduling](/opt/muse/skills/scheduling/SKILL.md).

- Update teammates in a comment on the task itself rather than a separate message, so the history stays in one place.

- When moving tasks between apps, use the target app's import, then spot-check dates, recurrence and assignees.
