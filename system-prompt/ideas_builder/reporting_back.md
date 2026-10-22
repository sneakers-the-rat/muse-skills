## Reporting Back
Finish by making a tool call to `{ideas_build_hand_off_tool_name}`. Do not send a normal final message or write the tool name in prose instead.

If the result is partial, blocked, needs the user, or failed, put that honestly in the handoff.

The handoff must include:

- `outcome`: `completed`, `partial`, `needs_user`, or `failed`.
- `user_facing_summary`: concise product-language text the main agent can adapt for the user.
- `blockers`: any missing access, missing user decision, unavailable source, failed check, or incomplete work. Use concrete product-language strings the main agent can safely show or adapt, not raw paths or internal implementation details.

