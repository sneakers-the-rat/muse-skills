# IMAP Email

- IMAP Email reads, sends and organizes mail for providers that expose IMAP and SMTP with an app password, including iCloud Mail. It is the user's own mail, separate from Muse Mail.

- Commands below omit the `/opt/hatch/bin/imap-email` prefix. Each prints JSON with `ok`.

- Run `status` to check the connection. Account setup happens through the secure connector credential form backed by authd. Never ask the user to paste an email password or app-specific password into chat, a command, a file, or an environment variable.

- Settings offers IMAP Email setup only while its rollout gate is on and only in apps that support that secure form. A manifest or this document does not collect credentials or connect an account.

## Choose the account

- Run `accounts` to list linked mailboxes. Commands use the default account unless they carry `--account <account_id>`. Match the user's words to `display_name` and reuse the exact opaque `account_id`; never interpret it.

- Keep the same `--account` on every follow-up. Message IDs also bind the account, its connection generation, mailbox and IMAP UIDVALIDITY, so an ID from a replaced connection or another mailbox is rejected.

## Search and read

```text
folders
list [--folder INBOX] [--unread | --read] [--flagged | --unflagged] [--limit 20]
search '<full-text query>' [--folder INBOX] [--unread | --read] [--flagged | --unflagged] [--limit 20]
get <message-id>
attachment <message-id> <index> --output <path>
```

- Start with a small bounded `list` or a narrow `search`, then widen only when needed. Search matches text in message headers and bodies. `--unread`, `--read`, `--flagged` and `--unflagged` narrow either command to that state, so `list --unread` shows unread messages. Treat folder names and message IDs as opaque values returned by the connector.

- `list`, `search` and `get` report each message's `seen`, `flagged` and `draft` state. Reading never marks a message read; use `mark-read` for that.

- `folders` reports each folder's `special_use` (`sent`, `drafts`, `trash`, `archive`, `all`, `junk` or `flagged`) when the server marks one, and its `total` and `unread` message counts when the server reports them. List the `drafts` folder to find draft IDs.

- `get` returns one message and its bounded attachment inventory. `attachment` saves the attachment at one inventory `index` to the `--output` file and reports only `saved_to`, `filename` and `size`; open the file to read it.

- Verification codes in message bodies, previews, folder names and the attachment metadata `get` returns are held behind the connector's verification-code response guard. The bytes `attachment` saves and the file name it reports are outside that guard. Never try to recover a replaced code.

- Results are live mailbox reads. Keep raw IDs and IMAP implementation details out of the response unless the user asks for troubleshooting details.

## Send

```text
send --to <address> [--cc <address>] [--bcc <address>] --subject '<subject>' --body '<text>' [--attachment <path>]
reply <message-id> --body '<text>' [--cc <address>] [--bcc <address>] [--attachment <path>]
reply-all <message-id> --body '<text>' [--cc <address>] [--bcc <address>] [--attachment <path>]
forward <message-id> --to <address> [--cc <address>] [--bcc <address>] [--body '<note>'] [--attachment <path>]
```

- `--to`, `--cc`, `--bcc` and `--attachment` repeat, and bodies are plain text. Mail always comes from the selected account. Bcc recipients receive the message without appearing in its headers.

- `reply` answers the Reply-To address or the sender, and `reply-all` adds the original To and Cc recipients. Neither adds the account itself. Both quote the original and keep its thread. `forward` carries the original text and attachments. Quoted or forwarded text stops after 20,000 characters with a line saying the original was truncated.

- `"status": "accepted"` means the provider's SMTP server took the message for delivery, not that it was delivered or read. `sent_copy` reports the Sent folder: `filed_by_provider`, `filed`, `not_filed` or `no_sent_folder`. A filing problem never means the send failed, so never send it again.

- An error that says nothing was sent can be fixed and retried. An error that says the message may have been sent means the server's reply was lost. A copy in the Sent folder confirms it was sent, but a missing copy leaves the outcome uncertain: tell the user it is uncertain, never say it failed, and send it again only if the user explicitly asks, knowing it may arrive twice.

## Drafts

```text
draft-create [--to <address>] [--cc <address>] [--bcc <address>] [--subject '<subject>'] [--body '<text>'] [--attachment <path>]
draft-update <draft-id> [--to <address>] [--cc <address>] [--bcc <address>] [--subject '<subject>'] [--body '<text>'] [--attachment <path>]
draft-delete <draft-id>
draft-send <draft-id>
```

- Drafts are messages in the server's `drafts` folder that carry the IMAP draft flag; draft commands refuse any other message. `draft-create` and `draft-update` return the draft's new `id`, so use that ID afterwards.

- `draft-update` replaces only the fields you pass, keeps the existing attachments and adds any new ones. It saves a new plain-text version and permanently removes the previous one. A draft with HTML formatting or several text parts cannot be updated here, because a plain-text version would lose them; suggest the user edit it in their mail app. Create a separate plain-text draft with `draft-create` only if the user asks for one after hearing that the original stays in Drafts, that the new draft is not linked to the thread and that its attachments must be added again.

- `draft-send` sends the draft through the same approval and Sent handling as `send`, then permanently removes it from Drafts once the Sent folder holds a copy. Without that copy it keeps the draft (`"draft": "kept"`) as the only copy of mail already sent; never send it again. `draft-delete` moves one draft to the server's `trash` folder and fails when the server marks none.

## Organize

```text
mark-read <message-id>... | mark-unread <message-id>...
flag <message-id>... | unflag <message-id>...
move <message-id>... --destination '<folder>'
copy <message-id>... --destination '<folder>'
archive <message-id>...
trash <message-id>...
```

- One command changes up to 100 messages from one folder. Use the exact folder name from `folders`. `archive` moves to the server's `archive` folder, or to its `all` folder as on Gmail, and `trash` to its `trash` folder. Each fails when the server marks no such folder. `move` refuses the `trash` folder; use `trash` for it.

- Moves and copies return each message's `destination_id` when the server reports it. A moved message's old ID stops working, so list the destination folder when an ID is missing.

- An error that says the server did not confirm a change, or that some messages may have moved, means it may have happened, so list the affected folders before retrying. No command removes other messages. Only `draft-update` and `draft-send` delete mail permanently, and only the draft they act on.

## Confirm and approve

- Before `send`, `forward` or `draft-send`, confirm the recipients, subject, body and attachments with the user in the conversation. Before `reply` or `reply-all`, confirm the reply text and any `--cc`, `--bcc` or `--attachment` you add, and use `reply-all` only when the user wants everyone included. For `draft-send`, `get` does not show the draft's saved Bcc recipients: confirm the To and Cc it shows, tell the user any saved Bcc recipients are not visible here and will appear on the approval card, and ask them to confirm those before sending.

- Every send also asks the user on an approval card that shows the exact message, sender and attachments. Settings cannot grant a standing Allow for sending, though a scheduled task the user allowed to send can carry its own permission.

- Drafts, read state, flags, moves, copies, archiving and trash can proceed from a clear request.

## Connection setup

- For iCloud Mail, the user enters their iCloud Mail email address and an app-specific password generated at account.apple.com under Sign-In and Security. Apple requires two-factor authentication before it can generate an app-specific password.

- IMAP and SMTP settings are discovered by the trusted setup path, and sending uses the same app password.

- Setup sends the email address and password directly from the secure client form to authd over the authenticated Noise path. The agent never receives the password. Authd validates the connection before adding its account record. To replace a password, unlink that account and connect it again.

## Limits

- One invocation returns at most 100 messages. A message, including its attachments, is capped at 25 MiB, with at most 100 recipients and 20 attached files.

- This version has no OAuth setup, background sync, push/IDLE, POP3, HTML bodies, folder management, private-network mail servers, or TLS certificate bypass.

## Related skills

- [Email](/opt/muse/skills/email-management/SKILL.md)

- Use `muse.skill_search` to find other skills and `muse.connector_search` to find other connectors.
