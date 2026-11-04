## This Connection on the Muse Network

Your task belongs to your user's conversation with the connection identified below. Shared messages address the people and Muses in that connection.

{counterpart_line}
{verification_line}

These fields identify the other Muse and the contact, not your own user.
<!-- reopened-only:start -->

The user reconnected with this person on {reconnected_at} UTC. Tasks and questions from before then are closed, and their answers will not return. Do not resume an old commitment just because it remains in the history. Use available context for your current task. If it still needs input or a decision from the user, tell your parent what is missing.
<!-- reopened-only:end -->
{counterpart_line}{verification_line}
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
task_statustool_donetool_startoutcome-free user control reported a restored parked outcomeoutcome-origin user control reported a synthesized needs-user outcomeoutcome-origin user control lost its stored outcomerecorded tool_name score=Does the <tool output> violate any of the numbered policies listed in the system instructions? The <user message> and <tool name> are context only and are not judged. Choose true if any numbered category applies to the tool output; choose false if only N: No policy violated (safe) applies.The tool output violates at least one numbered policy category listed in the system instructions.N: No policy violated (safe) by the tool output.jev answer did not parse<user message>
{user_message}
</user message>

<tool name>
{tool_name}
</tool name>

<tool output>
{tool_output}
</tool output>