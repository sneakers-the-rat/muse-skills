# `saved.items`

Entities saved into a list, with stable display data, note, purchase state and the agent, chat and turn that saved them.

- Return to the [table index](/opt/muse/skills/muse_db/references/schema.md) or [query rules](/opt/muse/skills/muse_db/references/querying.md).

## Columns

- `item_id` uses `text` and is required.

  Local row identifier (primary key).

- `list_id` uses `text` and is required.

  Potential local reference; resolve by domain context in: `saved.lists.list_id`.

- `entity_type` uses `text` and is required.

- `entity_key` uses `text` and is required.

- `url_key` uses `text` and is nullable.

- `payload_version` uses `smallint` and is required.

- `payload` uses `text` and is required.

- `title` uses `text` and is required.

- `url` uses `text` and is required.

- `image_url` uses `text` and is nullable.

- `note` uses `text` and is nullable.

- `raw_input` uses `text` and is nullable.

- `purchased_at` uses `timestamp with time zone` and is nullable.

- `agent_id` uses `text` and is nullable.

  Soft local reference → `agent.agents.agent_id`.

- `root_session_id` uses `text` and is required.

  Root session of the chat the item was saved in; the same UUID as `chat.chats.chat_id`.

- `chat_surface` uses `text` and is required.

- `message_id` uses `text` and is nullable.

  Soft local reference to `runtime.messages.message_id` of the turn that saved the item.

- `request_origin` uses `text` and is required.

- `saved_at` uses `timestamp with time zone` and is required.

  Default: `now()`.

- `updated_at` uses `timestamp with time zone` and is required.

  Default: `now()`.

## Keys and relationships

- PRIMARY KEY `items_pkey` covers `item_id`.

- UNIQUE `items_list_id_entity_type_entity_key_key` covers `list_id`, `entity_type`, `entity_key`.
