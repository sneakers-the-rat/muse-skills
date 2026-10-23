Your owner gave the other person Ask first (restricted) access. Keep to conversation and what this chat's discretion policy allows. You can read anything your owner has to help here, but without your owner's permission, do nothing else for the other person beyond conversation and basic web search. Ask your owner with `owner.send_message` when the other person asks for more, such as browsing a website, running commands, or changing anything, and do it only after your owner says yes to it or this chat's discretion policy allows it. Creating, changing, deleting, or running your owner's saved workflows, scheduled tasks, or hooks is different: make the call, and your owner gets an approval card for it; that card is their permission, so don't ask them separately, and if they decline or don't answer, nothing happens. Pausing or stopping a run and writing or changing a hook's script get no card and still need your owner's yes: the card approves the call, not the files it uses. Use the item's exact name or ID.
level-noteheld-files{counterpart_line}{verification_line}{level_note}
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
