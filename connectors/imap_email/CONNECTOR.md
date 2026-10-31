# IMAP Email

- IMAP Email reads mail from providers that expose IMAP, including iCloud Mail. This first version cannot send, delete, move, mark, or draft messages.

- Run `/opt/hatch/bin/imap-email status` to check the connection. Account setup happens through the secure connector credential form backed by authd. Never ask the user to paste an email password or app-specific password into chat, a command, a file, or an environment variable.

- The connector is hidden from Settings until the companion client supports that secure form. A manifest or this document does not collect credentials or connect an account.

## Choose the account

- Run `accounts` to list linked mailboxes. Commands use the default account unless they carry `--account <account_id>`. Match the user's words to `display_name` and reuse the exact opaque `account_id`; never interpret it.

- Keep the same `--account` on every follow-up. Message IDs also bind the account, its connection generation, mailbox and IMAP UIDVALIDITY, so an ID from a replaced connection or another mailbox is rejected.

## Search and read

```text
folders
list [--folder INBOX] [--limit 20]
search '<full-text query>' [--folder INBOX] [--limit 20]
get <message-id>
```

- Start with a small bounded `list` or a narrow `search`, then widen only when needed. Search matches text in message headers and bodies. Treat folder names and message IDs as opaque values returned by the connector.

- `get` returns one message and its bounded attachment inventory. Attachment download is not available in this version.

- Verification codes in message bodies, previews, folder names and attachment metadata are held behind the connector's verification-code response guard. Never try to recover a replaced code.

- Results are live mailbox reads. Keep raw IDs and IMAP implementation details out of the response unless the user asks for troubleshooting details.

## Connection setup

- For iCloud Mail, the user enters their iCloud Mail email address and an app-specific password generated at account.apple.com under Sign-In and Security. Apple requires two-factor authentication before it can generate an app-specific password.

- IMAP server settings are discovered and validated by the trusted setup path. A usable SMTP endpoint may also be retained for a later sending release, but SMTP is not required or authenticated by this read-only version.

- Setup sends the email address and password directly from the secure client form to authd over the authenticated Noise path. The agent never receives the password. Authd validates the connection before adding its account record. To replace a password, unlink that account and connect it again.

## Limits

- One invocation returns at most 100 messages. A message is capped at 25 MiB.

- This version has no OAuth setup, background sync, push/IDLE, POP3, sending, mailbox changes, private-network mail servers, or TLS certificate bypass.

## Related skills

- Use `muse.skill_search` to find other skills and `muse.connector_search` to find other connectors.
