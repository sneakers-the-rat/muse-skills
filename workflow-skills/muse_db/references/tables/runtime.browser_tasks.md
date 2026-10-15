# `runtime.browser_tasks`

Browser tasks, their ownership, session and execution state.

- Return to the [table index](/opt/muse/skills/muse_db/references/schema.md) or [query rules](/opt/muse/skills/muse_db/references/querying.md).

## Columns

- `task_id` uses `text` and is required.

  Local row identifier (primary key).

- `browser_session_id` uses `text` and is required.

  Default: `'default'::text`.

  Browser-runtime identifier; no Muse PostgreSQL owner table.

- `root_session_id` uses `text` and is required.

  Soft local reference → `agent.sessions.session_id`.

- `owner_agent_id` uses `text` and is nullable.

  For agent-created tasks, including historical null `owner_kind`, soft local reference → `agent.agents.agent_id`. When `owner_kind` is `user`, NULL; no executing agent or owner row.

- `root_message_id` uses `text` and is required.

  For agent-created tasks, including historical null `owner_kind`, soft local reference → `runtime.messages.message_id`. When `owner_kind` is `user`, repeats this row's `task_id`; no message owner row.

- `stream_owner_message_id` uses `text` and is required.

  For agent-created tasks, including historical null `owner_kind`, soft local reference → `runtime.messages.message_id`. When `owner_kind` is `user`, repeats this row's `task_id`; no message owner row.

- `status` uses `text` and is required.

- `title` uses `text` and is required.

  Default: `'Browser task'::text`.

- `step_count` uses `integer` and is required.

  Default: `0`.

- `chat_context_json` uses `text` and is nullable.

- `latest_action_id` uses `text` and is nullable.

  Browser-runtime action identifier; no Muse PostgreSQL owner table.

- `latest_tab_json` uses `text` and is nullable.

- `latest_screenshot_json` uses `text` and is nullable.

- `created_at` uses `timestamp with time zone` and is required.

  Default: `now()`.

- `updated_at` uses `timestamp with time zone` and is required.

  Default: `now()`.

- `completed_at` uses `timestamp with time zone` and is nullable.

- `terminal_reason` uses `text` and is nullable.

- `admission_seq` uses `bigint` and is nullable.

- `presentation_root_session_id` uses `text` and is nullable.

  Soft local reference → `agent.sessions.session_id`.

- `parent_agent_id` uses `text` and is nullable.

  Soft local reference → `agent.agents.agent_id`.

- `tool_call_id` uses `text` and is nullable.

  For agent-created tasks, including historical null `owner_kind`, soft local reference → `runtime.tool_calls.call_id` (the text correlation identifier, not its numeric `tool_call_id`). When `owner_kind` is `user`, repeats this row's `task_id`; no tool call or owner row.

- `request_trace_context_json` uses `text` and is nullable.

- `requester_source` uses `text` and is nullable.

- `requester_transport` uses `text` and is nullable.

- `requester_model` uses `text` and is nullable.

- `requester_effective_model` uses `text` and is nullable.

- `request_mode_json` uses `text` and is nullable.

- `max_training_tier_json` uses `text` and is nullable.

- `is_task_card_visible` uses `boolean` and is required.

  Default: `false`.

- `initial_instruction` uses `text` and is nullable.

- `history_source_agent_id` uses `text` and is nullable.

  Soft local reference → `agent.agents.agent_id`.

- `state_revision` uses `bigint` and is required.

  Default: `0`.

- `deadline_at` uses `timestamp with time zone` and is nullable.

- `continuation_root_task_id` uses `text` and is nullable.

  Soft local reference → `runtime.browser_tasks.task_id`.

- `terminal_interrupt_subtype` uses `text` and is nullable.

- `outcome_status` uses `text` and is nullable.

- `outcome_reason` uses `text` and is nullable.

- `outcome_at` uses `timestamp with time zone` and is nullable.

- `retention_end_reason` uses `text` and is nullable.

- `card_generation` uses `bigint` and is required.

  Default: `0`.

- `input_grants_json` uses `text` and is required.

  Default: `'{"version":1,"grants":[]}'::text`.

- `browser_navigation_attempted` uses `boolean` and is required.

  Default: `false`.

- `terminal_user_update_due_at` uses `timestamp with time zone` and is nullable.

  Non-null while this terminal occurrence still owes its user-facing ending update; also serves as the worker retry/claim time.

- `egress_profile` uses `text` and is nullable.

- `run_number` uses `bigint` and is nullable.

- `run_started_at` uses `timestamp with time zone` and is nullable.

- `run_presentation_locale` uses `text` and is nullable.

  BCP 47 presentation locale frozen for the current BrowserTask run; null legacy rows read as en-US

- `run_location_context_json` uses `text` and is nullable.

- `owner_kind` uses `text` and is nullable.

  Creation origin: user, main_agent, or cron; null when unknown. Immutable across takeover and continuation. User leases have a null owner_agent_id and reserve root_message_id, stream_owner_message_id and tool_call_id with task_id and have no executing agent, chat card or terminal chat delivery. Rust owns the vocabulary and lifecycle.

- `broker_instance` uses `text` and is required.

  Default: `'user'::text`.

  Immutable physical browser owner selected by trusted admission: user or cron. Independent of logical owner_kind and retained across continuation.

- `wallet_selection_provider` uses `text` and is nullable.

  Validated wallet provider selected for the current browser task

- `wallet_selection_payment_method_id` uses `text` and is nullable.

  Opaque correlation identifier; no declared local table relationship. Opaque validated wallet payment-method id selected for the current browser task

- `node_id` uses `text` and is nullable.

  Soft local reference → `device.nodes.node_id`.

- `node_name` uses `text` and is nullable.

- `browser_harness_kind` uses `text` and is required.

  Default: `'core_sdk'::text`.

- `browser_harness_version` uses `integer` and is required.

  Default: `2`.

## Keys and relationships

- PRIMARY KEY `browser_tasks_pkey` covers `task_id`.
