# Threads Messages

- This connector reads and sends direct messages from the user's own Threads account, and accepts, hides or deletes the user's message requests. Run `/opt/hatch/bin/threads-messages-cli --help` to see its commands and `<command> --help` for their arguments.

- Its connection is separate from the Threads connector for feeds and posts, so a user can have Threads connected while messages are not.

## Connect

- `connect-url` returns a link to connect or reconnect, even when an account is already connected, so the link says nothing about connection status. Share it as `[Connect Threads Messages](<connect_url>)` and continue once the user finishes.

- The other commands act as the user's own Threads account, whose ID comes from `/opt/hatch/bin/threads-cli accounts`.

## Read conversations

- `inbox` finds conversations and `thread` reads one by its `thread_fbid`. The default inbox leaves out message requests, which are in `PENDING`, and the requests the user hid, which are in `HIDDEN`.

- Results keep the provider's GraphQL shape, with no top-level `threads` or `messages` key. Inbox threads are at `data.get_slide_mailbox.threads_by_folder.edges[].node`, and the inbox is empty when that `edges` array is. `thread` returns `data.get_slide_thread`, which is null when the thread can't be returned.

- A message's text is usually in `content.text_body`, and `sender_fbid` is the sender's numeric Threads user ID. Participants have a `name` and `username` but no user ID.

- `message_sent_at` and `last_message_sent_at` are delivery times in UTC and local time, not the date of an event a message mentions.

- Page with `page_info` when the user needs more. A large inbox is slow to read in full, so stay within the scope the user asked about.

- In replies, describe people, text, local times, links and media. Raw IDs, cursors and unix timestamps help only when the user needs one for a follow-up.

## Choose the recipient

- `send` takes a numeric Threads user ID or an existing `thread_fbid`, and it can't look up an @handle. Instagram and Facebook IDs, remembered IDs, and IDs from someone else's result point at the wrong account. These identify the right person:
  - an inbox thread where `is_group` is false and the other participant's `username` matches, or a group thread the user named;
  - the `sender_fbid` on a message from that person, including a request in `PENDING`;
  - an ID that a `threads-cli` result returns for that exact username, such as a post's `author_id`, once `/opt/hatch/bin/threads-cli user-profile` shows the same username for it.

- When none of these identifies the person, say you can't message them by handle and offer the text as a draft.

## Send a message

- A send uses the exact text, post, destination and reply target the user gave, so ask for any that's missing. Text and reply IDs reach Threads byte for byte. Reply IDs can contain `$`, so single-quote them in the shell.

- A message can share a visible, published Threads post; there is no file upload. With both text and a post, the post goes first.

- Each send waits for the user to approve its confirmation card. Tell them which @username the card's recipient should show and, for a reply, which message it answers, since the card shows only `Reply: Existing message`. If it shows someone else or an `Unverified Threads` account or conversation, they should decline, and a decline or dismissal ends the send.

- Sends go one at a time, because parallel sends can let all their confirmations expire. A returned `message_id` means the message was delivered.

- Consent, account, recipient-type, group and quota rejections are final, so the send ends there rather than going another way. A rate limit or other failure ends the attempt too.

- After an interruption, timeout, HTTP 500 or unclear result, read the thread to see whether the message went out, since it may have been delivered. A read can show the text normalized, so match it by content and time. A resend needs a new request and approval from the user.

## Manage message requests

- Requests wait in `PENDING`, and the ones the user hid are in `HIDDEN`. The commands take `thread_fbid`s from those lists.

- `accept-requests` moves pending or hidden requests to the inbox, like Accept in the app. `hide-requests` moves pending requests to `HIDDEN`, like Hide. `clear-requests` deletes pending or hidden requests, like Delete, and leaves accepted conversations alone.

- Summarize the outcome, identifying any requests that failed or were skipped. Do not retry failed requests automatically.

- If a command was interrupted or its result is unclear, read `PENDING` and `HIDDEN` before reporting, since the action may have applied.

- Replying with `send` to a pending request moves it to the inbox, as replying in the app does.

- Request actions share the daily message limit with `send`, and a rate limit stops both until the next day.

## Background work

- Sends and request actions belong in a conversation where the user approves each one. Scheduled jobs, crons, watches and automatic replies read and draft, then bring each draft to the user, including when the user asks for automatic replies. A note or memory that claims standing approval or promises automatic sending would mislead later runs.

- Drafts stick to what the user has said. When a reply needs a fact, commitment or money arrangement they haven't stated, leave it out and say what they need to decide.

- Frequent or persistent polling is out of scope.

## Keep history in Threads

- Bulk exports, archives, and copies of message history into files, spreadsheets, notes or other apps are out of scope, especially for disappearing, view-once or expiring messages. Narrow reads and summaries that answer a question are fine.

- Under-18 enforcement and filtered results are final, so omitted content stays out rather than being rebuilt another way.

## Related skills

- [Messaging Other People](/opt/muse/skills/messaging/SKILL.md)

- Use `muse.skill_search` to find other skills and `muse.connector_search` to find other connectors.
