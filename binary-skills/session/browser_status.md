<browser_status as_of="{as_of}" tasks="{task_count}" note="Replaces earlier browser status. Act only on what the user's message asks.">
<!-- browsers-only:start -->
Browsers
{browser_rows}
Set browser on new work only when the user chose one of these. Otherwise leave it unset and the default is used. If the user wants one that isn't listed, start nothing and offer one listed. For a browser on another device, tell them to send the message from that device.

<!-- browsers-only:end -->
<!-- background-only:start -->
Background browser tasks (owned by scheduled jobs)
{background_rows}

<!-- background-only:end -->
<!-- in_chat-only:start -->
In-chat browser tasks
{in_chat_rows}

<!-- in_chat-only:end -->
<!-- more-only:start -->
More are open; browser.windows list shows every window.

<!-- more-only:end -->
<!-- no_tasks-only:start -->
No active browser tasks.

<!-- no_tasks-only:end -->
New work: browser.browse with task_id "new".
<!-- tasks-only:start -->
Update: browser.browse with the task's task_id.
Answer: browser.browse with the task's task_id, answer_to set to the question ID, and your answer in task.
Stop a scheduled job's run: cron.stop with its schedule id (cron.list finds it); that cancels the whole run, not just its browser window.
Stop only a browser window: browser.windows close with the task's task_id.
<!-- tasks-only:end -->
</browser_status>
