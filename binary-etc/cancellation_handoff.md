Internal cancellation notice.

The previous active turn was explicitly interrupted by the user. Any unfinished
tool call that was already dispatched may have partially or fully applied; check
what actually happened before retrying it. Descendant work was asked to stop but
might have completed concurrently. Treat unfinished plans from that turn as
cancelled unless the user asks to resume them.
