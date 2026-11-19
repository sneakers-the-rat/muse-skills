Your previous review did not satisfy the decision contract. Nothing has been sent. Review the same evidence and call `submit_connection_review` once with a corrected decision.

Include `draft_approval_required`. Set it to `true` only when the user reserved approval of the final wording, and use an ask decision unless denying the send. Ordinary ask-first rules leave it `false`.

Use `ask_owner` for an unsatisfied condition in a cited rule, or `ask_user` for a private detail the user has not agreed to share. This applies regardless of who started the exchange. An `allow` needs covering rule IDs or an authenticated user request. Otherwise it is held for private review.

If permission comes from a listed owner message, cite its `owner_message_ids` from the supplied list. This includes authenticated messages to their own Muse marked `owner_chat`. Cite only instructions that cover this content and recipient. Other messages are context, not permission.

Keep details the user asked you to share. Remove other personal details the task does not need, even if they seem harmless. Use `text` for a complete useful revision. Preserve wording the user asked to send exactly, and judge unchanged attachments and shared items too.

`nothing_shared` covers replies with no private disclosure, including ordinary coordination, without a saved rule or explicit request. Explain why the reply fits and respect restrictions and confidences. Files, images and shared resources cannot use it. Cite only stored rule IDs, each once.
