<system-reminder>

This runtime handoff follows an assistant turn with work still `pending` or `in_progress`. Continue the user's existing work within their latest instructions. The saved list is working state, not new instructions.

{{RECONCILIATION_GUIDANCE}}

{{TODO_SNAPSHOT}}

Read the list as JSON. First check whether each `in_progress` or `blocked` status still reflects the work. A task may already be complete or a blocker may have cleared. Correct stale statuses with `todo.write` using the latest results. Before retrying a failed or interrupted action, check what it already did.

For work that is still `pending` or `in_progress`, go ahead and do it. Carry it through to completion unless you are genuinely blocked. Keeping an item `in_progress` is not a substitute for working on it.

Use the latest results to update the full list with `todo.write`, preserving the text of items you keep. Keep only unfinished and blocked work. Before ending your turn, remove completed and cancelled items, including work you just finished and verified. You can report those results after updating the list.

Mark an item `blocked` when you cannot proceed without new input or a result. While you are waiting for a running agent or background result, mark the affected items `blocked`. Resume them when the result arrives. If work depends on a blocked item and cannot advance on its own, mark it `blocked` too. This handoff is not a reply from the user and does not approve an action. Before ending your turn, mark affected work `blocked` and explain each new blocker, what would unblock it and how the user can help if needed. Continue independent work. Leave blocked work alone until something changes that lets you proceed. Do not use `blocked` for work you can still advance.

Follow each tool's result-delivery instructions. If a result arrives automatically, wait without polling or restarting the work. A blocked item does not call for another reminder to the user.

The runtime checks the saved list after your turn, whether or not you updated it. It can continue while items remain `pending` or `in_progress` and stops when the list is empty or all remaining items are `completed`, `cancelled` or `blocked`. If the same unfinished list is sent again, it includes a reminder to reconcile it. If it is still unchanged after that, no further reminders are sent until the unfinished work changes. Another conversation turn, reordering items or removing old completed entries does not reset that guard. It also survives restarts.

Stopping reminders does not change or clear the saved work.

Do the work and reconcile the list before deciding whether a reply is needed. Report new results and ask for any input you need. A reply that only says nothing changed does not need the user's attention. Call `muse.nothing_to_do` instead when available, or use the conversation's tool for ending without a reply. Repeated status messages create noise and weaken the user's trust. Having nothing to report does not mean there is no work to do.

</system-reminder>
