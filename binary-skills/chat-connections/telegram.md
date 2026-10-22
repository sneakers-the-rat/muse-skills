# Telegram side chats

Each Telegram conversation is one durable side chat in Muse. Replies and tasks
scheduled from that conversation return to the same chat. The chat UUID is its
identity; Telegram addresses and topics are private transport details.

## Connect and disconnect

Start with `chat.connection_status` with `provider: telegram`. A linked
connection reports `running`, which says whether its poll worker is alive.
Linked alone does not prove delivery is working. Status never returns a
pairing bearer or an app chat link for Telegram.

For a requested connection when `unlinked` or `link_pending`, offer:

[Connect Telegram](https://agent.meta.ai/connect/channel?service=telegram&intent=connect)

The app collects and validates the bot token securely. Never request a token in
chat, invent a pairing link, or call backend linking endpoints through a shell.
If already linked, say so. If unavailable, explain the temporary failure and do
not offer a link. A pending link needs completion in the app.

For an explicit disconnect request from the user's own Muse chat, inspect
status and call `chat.disconnect` with `provider: telegram`. Clarify ambiguous
intent before disconnecting. Provider-origin turns and background work cannot
change connection settings or disconnect themselves. Disconnect retains history.
Replacing the bot revokes the previous bot's grants and delivery authority.

## Preferences

Use `chat.configure_connection({"provider":"telegram"})` to read preferences.
Pass `settings` to update a partial object; omitted fields retain their values.
The daemon commits settings before publishing the live snapshot. No restart or
workspace configuration-file edit is required.

| Setting | Meaning |
|---|---|
| `access_mode` | `allowlist` only |
| `allow_chat_ids` | Complete array of allowed native Telegram numeric chat IDs |
| `group_policy` | `allowlist` or null for the default; `deny` or `disabled` blocks groups |
| `require_mention` | Require a mention in groups |
| `mention_patterns` | Additional mention patterns |
| `groups` | Rules keyed by native Telegram group ID |
| `direct` | Rules keyed by native Telegram DM ID |
| `poll_interval_ms` | Poll interval, 1–60000 ms; runtime minimums still apply |
| `request_timeout_secs` | Request timeout, 1–300 seconds |
| `parse_mode` | `HTML`, `Markdown`, `MarkdownV2`, or empty for plain text |
| `media_mode` | `ignore`, `placeholder`, or `download` |
| `reaction_mode` | `off`, `log_only`, or `bot_message_turns` |
| `outbound_media_enabled` | Enable outbound media |
| `typing_indicator_enabled` | Enable typing indicators |
| `streaming_replies_enabled` | Enable live reply updates |
| `connected_ack_enabled` | Retained preference; linking does not send an acknowledgement |

`groups.<native_id>` accepts `enabled` and `topics.<topic_id>.enabled`.
`direct.<native_id>` also accepts `require_topic`. Objects merge recursively;
null removes a group, DM, or topic override. Arrays replace completely: read the
existing allowlist before adding a user-authorized entry to preserve other
grants. Linking, credentials, the primary linked recipient, and global
connection enablement belong to the secure connection flow.

Disable all group replies:

```json
{"provider":"telegram","settings":{"group_policy":"deny"}}
```

Disable one topic without changing other rules:

```json
{"provider":"telegram","settings":{"groups":{"-1001234567890":{"topics":{"42":{"enabled":false}}}}}}
```

These are transport preferences, not chat routing selectors. Native IDs must
never be passed to chat tools or scheduling as a chat UUID. Ask for a known
native group ID when configuring admission; do not promise to discover it from
updates or logs during ordinary chat.

## Admission and group visibility

Inbound traffic requires a connected, running provider, an allowed native chat
ID, applicable group policy, mention rules, and enabled group/topic rules.
The coarse allowlist admits the chat; topic enablement is checked afterward.
A group grant never makes that group the recipient of an unaddressed message.

Telegram Privacy Mode limits messages bots receive. To receive all group
messages, the owner can disable privacy mode with BotFather `/setprivacy` or
make the bot a group admin. After changing privacy mode, remove and re-add the
bot to apply it. `/setjoingroups` controls whether the bot can join groups.

## Media and reactions

Inbound photos and static stickers can become image inputs. Documents, audio,
video, and voice can become file inputs. Animated/video stickers remain
placeholders. Outbound stickers and photo/video media groups are supported.
Reactions use the originating chat and current admission policy; a reaction
cannot select another chat or revive revoked authority.

For missing replies, read `running` before changing tokens or permissions. A
stopped worker needs runtime investigation. Then check the allowlist, group
policy, mentions, topic rules, and Telegram privacy mode. For a DM with
`require_topic`, verify its topic is present. Inspect media and reaction
preferences when those features are disabled. Never redirect a failed reply
to main chat or another provider conversation.
