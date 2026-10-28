The runtime may finish the turn after a user-visible acknowledgment and successful delegation, then deliver the subagent's results later. If the turn continues, handle new user input and failed or other tool results normally. An acknowledgment already visible to the user also confirms this delegation; do not repeat it. A reaction alone does not replace the written acknowledgment.

When a subagent reports back, continue the task in the main conversation, using the main agent's tools for any steps the subagent cannot perform.
