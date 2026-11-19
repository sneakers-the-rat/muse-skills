<!-- tasks-only:start -->
<browser_status as_of="{as_of}" tasks="{task_count}" note="Replaces earlier browser status. Act only on what the <!-- personal-muse-only:start -->user's<!-- personal-muse-only:end --><!-- group-muse-only:start -->member's<!-- group-muse-only:end --> message asks.">
<!-- tasks-only:end -->
<!-- no_tasks-only:start -->
<browser_status as_of="{as_of}" tasks="0">
No active browser tasks.
<!-- no_tasks-only:end -->
<!-- browsers-only:start -->
<!-- choice_heading-only:start -->
Browsers
<!-- choice_heading-only:end -->
<!-- root_choice_heading-only:start -->
Available browsers
<!-- root_choice_heading-only:end -->
{browser_rows}
<!-- choice_rule-only:start -->
Set browser on new work only when the user chose one of these. Otherwise leave it unset and the default is used. If the user wants one that isn't listed, start nothing and offer one listed. For a browser on another device, tell them to send the message from that device.
<!-- choice_rule-only:end -->
<!-- root_choice_rule-only:start -->
Choose the browser for each new task from these, for the user and their request. If the user wants one that isn't listed, start nothing and offer one listed. For a browser on another device that isn't listed, tell them to send the message from that device.
<!-- other_devices-only:start -->
A browser listed by its name is on another of the user's devices. To use it, set browser to that name exactly as written. Choose it when the user asks for that browser or the request needs it.
<!-- other_devices-only:end -->
Cloud browser environments: {cloud_networks}. Every new cloud browser task names one of these environments. A device browser takes no environment.
<!-- root_choice_rule-only:end -->
<!-- devices-only:start -->
User's browsers:
{device_rows}
<!-- devices-only:end -->
<!-- tasks-only:start -->

<!-- tasks-only:end -->
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
<!-- tasks-only:start -->
New work: browser.browse with task_id "new".
Update: browser.browse with the task's task_id.
Answer: browser.browse with the task's task_id and your answer in task, plus answer_to set to the question ID when its row names one. When <!-- personal-muse-only:start -->the user's<!-- personal-muse-only:end --><!-- group-muse-only:start -->a member's<!-- group-muse-only:end --> message gives a paused task what it waits on, answer that task rather than starting new work.
Stop a scheduled job's run: cron.stop with its schedule id (cron.list finds it); that cancels the whole run, not just its browser window.
Stop only a browser window: browser.windows close with the task's task_id, whatever its state.
<!-- tasks-only:end -->
</browser_status>
