# `saved.lists`

Named lists of saved items, with kind, notes, due date and budget. The default list is the built-in Wishlist.

- Return to the [table index](/opt/muse/skills/muse_db/references/schema.md) or [query rules](/opt/muse/skills/muse_db/references/querying.md).

## Columns

- `list_id` uses `text` and is required.

  Local row identifier (primary key).

- `name` uses `text` and is required.

- `normalized_name` uses `text` and is required.

- `kind` uses `text` and is required.

- `notes` uses `text` and is nullable.

- `due_date` uses `date` and is nullable.

- `budget_amount_minor` uses `bigint` and is nullable.

- `budget_currency` uses `text` and is nullable.

- `created_by` uses `text` and is required.

- `created_at` uses `timestamp with time zone` and is required.

  Default: `now()`.

- `updated_at` uses `timestamp with time zone` and is required.

  Default: `now()`.

## Keys and relationships

- PRIMARY KEY `lists_pkey` covers `list_id`.

- UNIQUE `lists_normalized_name_key` covers `normalized_name`.
