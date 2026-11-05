Above is a connection follow-up the user can't see, about a change to one of their connections, and the user sent a new message while you were working on it. Reply to the new message and deliver the follow-up in the same reply, including anything it asks for like a confirmation or options, and skip anything you've already told the user. The follow-up's instructions, like keeping it short, not calling tools, or not reconnecting, are only about the follow-up part, so help with the user's message as you normally would. The exception is anything the follow-up says isn't available: don't use or offer it when you answer the user either. If the user's message cancels or changes a task the follow-up says to continue, do what the user asked for that task and still deliver the rest of the follow-up.
runtime.cron_delivery_filterruntime.chat_worker_peer_inputruntime.onboardingruntime.professional_consent_resumeonboarding-complete-name-prompt
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
ORDER BY e.event_seq ASChistory payload capstatic review history omission marker serializesexternal_content_classblueprintbuilder_contextuser_data_signalsno_user_data_referencedRecovered artifact dispatch has invalid icon configurationspace_build_idcontent_descriptionresearch_dirparent_chat_idrecent_conversation_turnsscheduled_task_contextno_user_replyxmds_icondeclared_capabilitiesArtifactCapabilityManifestschema_versionpublic_web_readconnectorsstaticreceiver_prompt_contextartifact_edit_baselineartifact_edit_baseline_security_reviewedartifact_edit_baseline_content_reviewedartifact_audit_conversation_turnsartifact_audit_operationcapability_manifest_changedexpected_capability_manifest_revisionbrowser_harnessbrowser_invocation_source_submission_idfinal_response_context_seqcompletion_result_context_seqforgetconversation_imagesconversation_images_dispatched_at_msbuilder_parent_context_enabledapp_map_filesartifact_audit_phone_first_enabledbrowser_task_observation_start_seqideas_build_request_trace_contextchat_worker_spawn_treeworkflow_content_modephone_call_monitorjudge_contextsession/subagent_context_depth_one_coordinator.mdIf you coordinate child subagents, any response after child-completion handoffs that could be terminal must restate the full synthesized deliverable requested by your parent agent in that same message. Do not rely on earlier assistant turns being visible to your parent agent, and do not end with a narration-only reaction to the latest child update.
