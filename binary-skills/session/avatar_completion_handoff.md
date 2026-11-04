The selected avatar image is active. Instagram profile available: {instagram_profile_available}. Use avatar.get to check that its current image path matches {image_path}. If a different avatar is now active, do not announce or present this completed avatar.

### If instagram profile available is true
- Videos may still be generating; do not wait for them. After confirming this is still the current avatar, give the user the option to add a Muse banner to their profile. 
- This banner is a visual pill on the user's Instagram profile beneath their bio, showing their Muse avatar and name. Tapping it opens the Muse app if installed, or prompts the visitor to download it. It does not change the user's profile picture or bio. Adding the banner does not grant or change permissions for Muse or anyone else to read or access the user's Instagram profile, posts, or account. It does not give visitors access to the user's Muse and does not let them ask the user's Muse questions. Visitors only see the Muse avatar and name through the banner. Use these facts when explaining the banner or answering privacy questions.
- To give the user the option to add a Muse banner to their profile, speak in first person and invite the user: "Want to show off my new look? Add me as a banner on your Instagram profile". Use this wording in English, or its natural equivalent in the user's language. Refer to yourself as "me" and the avatar as "my new look", not by your name in third person. Call muse.create_options with exactly one accepting reply: {"options":["Let's do it"]} in English, or its natural equivalent in the user's language. The option's displayed text is also the exact user message sent when tapped. Include the returned embed_token unchanged in the same message as the invitation; plain text alone is not a complete offer. Do not use the avatar_share card, open a share sheet, attach avatar media, or add a separate readiness announcement.
- This handoff authorizes only the invitation, not a profile change. Wait for the user's acceptance; tapping "Let's do it" accepts this invitation. If they accept, read /opt/hatch/connectors/instagram/CONNECTOR.md to resolve their linked account and run instagram-cli profile-banner --account-id <user_own_fbid> --action add through the normal connector approval flow. If multiple accounts are linked and the intended account is unclear, ask which one. Recheck account availability before the write. If Instagram has been disconnected, do not update the profile or turn this offer into an account-linking upsell. Do not change the profile photo or bio. Confirm the banner was added only when the command returns success: true; otherwise explain that the update did not complete or could not be confirmed.

### If Instagram profile available is false
- Preserve the existing sharing flow: all required images and videos are published. After verifying the current avatar, call avatar.create_avatar_share_widget with the sharing-card fields. Set button_text to "Share avatar" and fallback_text to "You can share it with friends!" in the user's language. Write a short sharing invitation in title and subtitle in the user's language. Omit image_url. Send only the returned embed token in your final message. Do not send commentary, a readiness announcement, or other text. Do not attach avatar media. The client handles sharing when the user presses the button; do not open a share sheet or perform sharing yourself. Do not mention Instagram or offer to connect it.
idle_video_path{image_path}{instagram_profile_available}runtime.background_execruntime_execinstagram profile banner invitation handed to agentavatar completion handoff acceptedconnector_call_reason/opt/hatch/bin/instagram-cliJARVIS_HOMEJARVIS_VAR_LIB_DIRJARVIS_TRACE_CONTEXTcall-portrait.jpgactive_stemavatar_surfacehatchtriggerenqueue_if_neededimagehttp://localhost/hatch/avatar/call-idlechoreography_profileavatar enrichment could not resolve the choreography profileenrichmentenrichment_plansuperseded_during_admissionavatar enrichment superseded during admissionnothing_to_generatefunnel_versionv2avatar enrichment: nothing to generateavatar enrichment could not be plannedotheravatardownstream_statusavatar_funnelambiguous_hbi_mutationlease_renew_retry_exhaustedlease_renew_terminaltarget_unavailable(?i)\b(?:cvv|cvc|security[ _-]?code|password|passcode|verification[ _-]?code|pin|api[ _-]?key|access[ _-]?token|client[ _-]?secret)\bcredential label regex is validbrowser workflow is waiting or terminalbrowser-credential-updateruntime.browser_codebrowser-codebrowser-inputbrowser task is no longer runningthe browser planner stopped this specialistruntime.browser_controlbrowser seat endedbrowser tabs after control return were unavailableThis subtask stopped during a restart and did not report a result. Its work may be partly or fully done: check what it already produced before redoing anything, then redo or redelegate only what is actually missing.Closed during restart recovery without reporting a result.failed to persist terminal state for closed checkpointed subagentfailed to persist terminal status for closed checkpointed agentclosed Spaces builder checkpoint has no parent identityclosed Spaces builder checkpoint has no storage rootfailed to load closed Spaces builder generationfailed to delete runtime restart checkpoint for closed agentpartial_recovery_descriptormissing_conversationinvalid_structural_owner_identityrecovery_identity_mismatchinvalid_recovery_descriptorinvalid_durable_owner_identityinvalid_inherited_execution_authority/self_improvement/stepSideChatMemoryside_chatsubagent.spawnartifact.list_actionsartifact.invoke_actionFollow the user's instructions.
INSERT INTO requests (
  request_id, root_request_id, parent_request_id, request_origin,
  transcript_surface, root_work_class
)
VALUES ($1, $2, $3, $4, $5::runtime.transcript_surface, $6)
ON CONFLICT (request_id) DO UPDATE SET
  root_request_id = COALESCE(requests.root_request_id, excluded.root_request_id),
  parent_request_id = COALESCE(requests.parent_request_id, excluded.parent_request_id),
  request_origin = CASE
    WHEN requests.request_origin = 'internal.runtime_replay' THEN excluded.request_origin
    ELSE requests.request_origin
  END,
  transcript_surface = excluded.transcript_surface,
  root_work_class = CASE
    WHEN requests.root_work_class = 'internal' AND excluded.root_work_class = 'user_facing'
      THEN excluded.root_work_class
    ELSE requests.root_work_class
  END
WHERE (requests.root_request_id IS NULL AND excluded.root_request_id IS NOT NULL)
   OR (requests.parent_request_id IS NULL AND excluded.parent_request_id IS NOT NULL)
   OR (requests.request_origin = 'internal.runtime_replay'
       AND excluded.request_origin <> 'internal.runtime_replay')
   OR requests.transcript_surface IS DISTINCT FROM excluded.transcript_surface
   OR (requests.root_work_class = 'internal' AND excluded.root_work_class = 'user_facing')
call_id
INSERT INTO tool_outputs (event_seq, call_id, status, output_text, error_text, created_at)
VALUES ($1, $2, $3, $4, $5, to_timestamp($6::double precision / 1000.0))
ON CONFLICT (event_seq) DO UPDATE SET
  call_id = excluded.call_id,
  status = excluded.status,
  output_text = excluded.output_text,
  error_text = excluded.error_text
arguments
INSERT INTO tool_calls (event_seq, call_id, tool_name, status, arguments_json, created_at)
VALUES ($1, $2, $3, 'started', $4, to_timestamp($5::double precision / 1000.0))
ON CONFLICT (call_id) DO UPDATE SET
  event_seq = excluded.event_seq,
  tool_name = excluded.tool_name,
  status = excluded.status,
  arguments_json = excluded.arguments_json

INSERT INTO chat_event_derived_write_backlog (event_seq, resources_json)
VALUES ($1, $2)
ON CONFLICT (event_seq) DO UPDATE SET
  resources_json = excluded.resources_json,
  updated_at = now()
select coalesce(
                    (select i.indisvalid from pg_index i where i.indexrelid = to_regclass($1)),
                    false
                )
                and exists (
                    select 1 from pg_extension
                    where extname = 'pg_textsearch'
                      and extversion = current_setting('pg_textsearch.library_version', true)
                )runtime.search_documents_events_bm25_v1_idxUPDATE chat_private.peer_conversations SET requester_chat_id = NULL
         WHERE conversation_id = $1 AND requester_revision = $2
           AND requester_chat_id = $3 AND NOT requester_unavailable
           AND chat_id = $5
           AND EXISTS (SELECT 1 FROM agent.agents
                       WHERE id = $4 AND session_id = $3)peer handoff disagrees with its asking-chat claimpeer handoff requester changed before admission
SELECT json_build_object(
         'accepted_ordinal', accepted_ordinal,
         'state', state,
         'checkpoint_custody', checkpoint_custody,
         'submission_json', submission_json
       )::text
FROM agent.message_mailbox
WHERE agent_id = $1
  AND state IN ('accepted', 'attached')
ORDER BY accepted_ordinal, submission_id
FOR UPDATE
SELECT payload_json FROM runtime_restart_checkpoints WHERE agent_id = $1
UPDATE agent.message_mailbox
SET state = 'attached',
    checkpoint_custody = 'executing',
    stream_owner_message_id = $3,
    attached_at = now()
WHERE submission_id = $1
  AND agent_id = $2
  AND state = 'accepted'
  AND stream_owner_message_id IS NULL

SELECT agent_id, state, stream_owner_message_id, submission_json,
       accepted_ordinal
FROM agent.message_mailbox
WHERE submission_id = $1
FOR UPDATE

SELECT EXISTS (
  SELECT 1
  FROM agent.message_mailbox
  WHERE agent_id = $1
    AND state = 'accepted'
    AND accepted_ordinal < $2
    AND (NOT $3 OR submission_kind <> 'internal_handoff')
)
tracked mailbox successor unexpectedly lost custodymessage mailbox successor promotion cannot overtake an older priority peer
UPDATE agent.message_mailbox
SET state = CASE WHEN $4 THEN 'completed' ELSE 'aborted' END,
    checkpoint_custody = coalesce(checkpoint_custody, 'executing'),
    terminalized_at = now()
WHERE agent_id = $1
  AND stream_owner_message_id = $2
  AND submission_id = ANY($3)
  AND state = 'attached'

UPDATE agent.message_mailbox
SET state = 'attached',
    checkpoint_custody = 'executing',
    stream_owner_message_id = $2,
    attached_at = coalesce(attached_at, now())
WHERE agent_id = $1
  AND submission_id = ANY($3)
  AND (
    (state = 'accepted' AND stream_owner_message_id IS NULL)
    OR (state = 'attached' AND stream_owner_message_id = $2)
  )

UPDATE agent.message_mailbox
SET checkpoint_custody = 'queued'
WHERE agent_id = $1
  AND stream_owner_message_id = $2
  AND submission_id = ANY($3)
  AND state = 'attached'

UPDATE agent.message_mailbox
SET state = CASE
      WHEN state = 'attached' AND $2 THEN 'completed'
      ELSE 'aborted'
    END,
    terminalized_at = now()
WHERE agent_id = $1
  AND state IN ('accepted', 'attached')
SELECT session_id, COALESCE(prompt_floor_seq, -1) AS prompt_floor_seq,
                kind = 'root' AND parent_agent_id IS NULL
                AND ephemeral IS DISTINCT FROM TRUE
                AND status NOT IN ('shutdown', 'not_found') AS eligible
         FROM agent.agents WHERE agent_id = $1 FOR UPDATEstartup_root_changedSELECT EXISTS(SELECT 1 FROM agent.message_mailbox
         WHERE agent_id = $1 AND state = 'accepted' AND accepted_ordinal < $2)startup mailbox promotion cannot overtake an earlier accepted input
SELECT payload_json
FROM agent.runtime_restart_checkpoints
WHERE agent_id = $1
FOR UPDATE
message mailbox attachment cannot overtake an older priority peer
INSERT INTO agent.runtime_restart_checkpoints (
  agent_id, mode, recovery_class, recovery_owner_id, execution_config_json,
  payload_json, created_at, updated_at
) SELECT $1, $2, $3, $4, $5, $6, $7, $7
WHERE EXISTS (
  SELECT 1
  FROM agent.agents
  WHERE agent_id = $1
    AND status NOT IN ('shutdown', 'not_found')
)
ON CONFLICT (agent_id) DO NOTHING
SELECT EXISTS (SELECT 1 FROM agent.agents WHERE agent_id = $1 AND status NOT IN ('shutdown', 'not_found'))conversation epoch
INSERT INTO agent.message_mailbox (
  submission_id, agent_id, conversation_epoch, submission_kind,
  routing_scope, state, checkpoint_custody, stream_owner_message_id,
  submission_json, transcript_event_seq, attached_at
) VALUES (
  $1, $2, $3, $4, $5, $6, $7, $8, $9, $10,
  CASE WHEN $6 = 'attached' THEN now() ELSE NULL END
)
ON CONFLICT (submission_id) DO NOTHING
RETURNING accepted_ordinal, accepted_at
startup mailbox promotion requires its previously accepted input
SELECT agent_id, conversation_epoch, submission_kind, routing_scope,
       state, stream_owner_message_id, submission_json,
       transcript_event_seq, accepted_ordinal, accepted_at
FROM agent.message_mailbox
WHERE submission_id = $1
FOR UPDATE
update chat.message_bindings set admitted_at = coalesce(admitted_at, now())
                    where jarvis_message_id = $1 and chat_id = $2 and binding_epoch = $3 and transport = $4binding epochconversation_epochsubmission_kindrouting_scope
UPDATE agent.message_mailbox
SET state = 'attached',
    checkpoint_custody = $5,
    stream_owner_message_id = $2,
    submission_json = $3,
    transcript_event_seq = coalesce($4, transcript_event_seq),
    attached_at = now()
WHERE submission_id = $1
  AND state = 'accepted'
  AND stream_owner_message_id IS NULL
mailbox stream ownerselect a.account_id from chat_private.accounts a
             join chat_private.binding_authorizations b on b.provider = a.provider and b.account_id = a.account_id
             where b.provider = $1 and b.binding_id = $2
               and a.connection_id = $3 and not a.revoked for share of adirect input has no captured binding epochaccount_retiredselect connection_id, generation, transport_json, delivery_target
             from chat_private.binding_authorizations
             where provider = $1 and binding_id = $2 and chat_id = $3
               and account_id = $4 and external_kind = 'direct' and participation = 'active'
             for shareaccount_authorization_retiredtransport_jsontransport_authorization_absentconnection_iddelivery_targetselect epoch from chat_private.bindings
         where chat_id = $1 and provider = $2 and not revoked for sharetransport_authorization_changedbinding_retiredsource classifiercall portrait frameinvalid call portrait recipe labelcall portrait reference recipe mismatchinvalid call portrait referencecall portrait checkcall idle clipupdate runtime.browser_invocations set suspended_state = 'running'
                 where invocation_id = $1 and suspended_state = 'waiting_child'# Dev-notice audit log — APPEND ONLY.
#
# Add a [[version]] entry only when a deploy must correct already-live sessions'
# stale/poisoned history (tool/skill/API renames, deprecated capabilities,
# incident corrections), labeled with a `notify` mode. Do not use this ledger
# for ordinary prompt wording or behavior tuning.
#
# The same machinery also delivers opt-in deploy/incident notices (set `kind`,
# omit `hash`). Full schema + semantics: 