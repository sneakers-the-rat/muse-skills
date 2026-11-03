Above is a connection follow-up the user can't see, about a change to one of their connections, and the user sent a new message while you were working on it. Reply to the new message and deliver the follow-up in the same reply, including anything it asks for like a confirmation or options, and skip anything you've already told the user. The follow-up's instructions, like keeping it short, not calling tools, or not reconnecting, are only about the follow-up part, so help with the user's message as you normally would. The exception is anything the follow-up says isn't available: don't use or offer it when you answer the user either. If the user's message cancels or changes a task the follow-up says to continue, do what the user asked for that task and still deliver the rest of the follow-up.
runtime.cron_delivery_filterruntime.chat_worker_peer_inputruntime.monitoringruntime.onboardingruntime.professional_consent_resumeonboarding-complete-name-promptskill.yamlimage-searchwebpresentationkindsartifact reference frontmatter lacks a description; not indexedartifact reference has no parseable frontmatter; not indexedartifacts/references## Content Playbooks

Playbooks for specialized artifact content. When the task involves content one of these owns, read it before building:


INSERT INTO events (
  event_kind, event_name, request_id, root_request_id, parent_request_id,
  transcript_surface, visibility, source, role, chat_kind, stream_lane,
  message_id, parent_message_id, reply_to_message_id, reply_target_message_id,
  parent_agent_id, agent_id, idempotency_key, display_text_ready, payload_json,
  chat_context_json, created_at
)
VALUES ($1::runtime.event_kind, $2, $3, $4, $5, $6::runtime.transcript_surface,
        $7::runtime.visibility, $8, $9::runtime.message_role, $10, $11,
        $12, $13, $14, $15, $16, $17, $18, $19,
        $20, $21, to_timestamp($22::double precision / 1000.0))
ON CONFLICT (idempotency_key) WHERE idempotency_key IS NOT NULL DO NOTHING
RETURNING event_seq

INSERT INTO events (
  event_seq, event_kind, event_name, request_id, root_request_id, parent_request_id,
  transcript_surface, visibility, source, role, chat_kind, stream_lane,
  message_id, parent_message_id, reply_to_message_id, reply_target_message_id,
  parent_agent_id, agent_id, idempotency_key, display_text_ready, payload_json,
  chat_context_json, created_at
)
VALUES ($1, $2::runtime.event_kind, $3, $4, $5, $6, $7::runtime.transcript_surface,
        $8::runtime.visibility, $9, $10::runtime.message_role, $11, $12,
        $13, $14, $15, $16, $17, $18, $19, $20,
        $21, $22, to_timestamp($23::double precision / 1000.0))
ON CONFLICT (event_seq) DO NOTHING
RETURNING event_seq
