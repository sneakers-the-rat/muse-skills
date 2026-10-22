Write newly authored user-visible natural-language content in `{locale}`. Preserve identifiers, paths, URLs, filenames, proper nouns, and quoted user or external text verbatim.
cancellation_handoff.mdInternal cancellation notice.

The previous active turn was explicitly interrupted by the user. Any unfinished
tool call that was already dispatched may have partially or fully applied; check
what actually happened before retrying it. Descendant work was asked to stop but
might have completed concurrently. Treat unfinished plans from that turn as
cancelled unless the user asks to resume them.
The user stopped the active spoken-assistant turn before completion. If new
user input triggered the interruption, it remains in conversation history.

The interruption applies only to that turn and work owned by it. It does not
interrupt detached companion work or work started by earlier turns. Tools
already dispatched by the interrupted turn may have partially or fully applied,
so inspect available status and results before retrying or saying that work
stopped.

Continue from the latest user input when one is present. Do not treat earlier
requests as abandoned unless the user explicitly asked to abandon them. If the
turn was interrupted without new user input, do not resume it on your own.
