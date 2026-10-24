<browser_status as_of="{as_of}" tasks="{task_count}" note="Replaces earlier browser status. Act only on what the user's message asks.">
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
New work: browser.browse with task_id "new".
Update: browser.browse with the task's task_id.
Answer: browser.browse with the task's task_id, answer_to set to the question ID, and your answer in task.
Stop: browser.windows close with the task's task_id.
</browser_status>
