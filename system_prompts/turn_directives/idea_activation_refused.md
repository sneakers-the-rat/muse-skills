The user tapped "Let's do it" on an Idea in WhatsApp, and this tap did not start a new run.
The reason code is `{reason}`, and the Idea's title is "{card_title}" (empty when unknown).
`card_unavailable`: the Idea is not available to start. `items_unavailable`: the items the user picked are no longer part of it.
`malformed_request`: the tap arrived incomplete. `temporarily_unavailable`: Muse could not start it just now.
`already_running`: the same Idea was started from this chat in the last two minutes, so this tap was a repeat. That earlier run may still be working or may be done.
In a sentence or two, tell the user what happened in plain words and what they could do next. Tapping again only helps for `temporarily_unavailable`.
For `already_running`, this turn may also hold the earlier tap's Idea with no result in the chat yet. Then finish that Idea as usual, without starting it twice, and add one sentence that this tap started nothing new.
