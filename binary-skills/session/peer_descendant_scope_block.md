## This Connection on the Muse Network

Your task belongs to your user's conversation with the connection identified below. Shared messages address the people and Muses in that connection.

{counterpart_line}
{verification_line}

These fields identify the other Muse and the contact, not your own user.
<!-- reopened-only:start -->

The user reconnected with this person on {reconnected_at} UTC. Tasks and questions from before then are closed, and their answers will not return. Do not resume an old commitment just because it remains in the history. Use available context for your current task. If it still needs input or a decision from the user, tell your parent what is missing.
<!-- reopened-only:end -->
{counterpart_line}{verification_line}skill.yamlimage-searchkindsartifact reference frontmatter lacks a description; not indexedartifact reference has no parseable frontmatter; not indexedartifacts/references## Content Playbooks

Playbooks for specialized artifact content. When the task involves content one of these owns, read it before building:


)
SELECT
  e.event_seq AS seq,
  (extract(epoch from e.created_at) * 1000)::bigint AS occurred_at_ms,
  e.created_at::text AS occurred_at_utc,
  e.request_id,
  e.event_name,
  coalesce(e.role::text, m.role::text, 'system') AS role,
  e.source,
  e.transcript_surface::text AS transcript_surface,
  coalesce(e.message_id, m.message_id, '') AS message_id,
  e.agent_id,
  e.parent_agent_id,
  m.body AS display_text
FROM selected_events e
LEFT JOIN messages m ON m.event_seq = e.event_seq
ORDER BY e.event_seq ASCoverflow when multiplying duration by 