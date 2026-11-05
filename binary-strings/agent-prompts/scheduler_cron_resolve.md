scheduler_heartbeat_resolvecron worker resolution completed without terminal tool call; retrying from saved historycron.scheduler.worker.resolveresolutionresolution exited without recording a terminal cron signaldetached resolution handle unavailableresolution worker spawn returned a different agent identityConnection authorization is unavailableencode pending cron resultread pending result recoveryscheduled resume acknowledgement call gated off; clearing registration locallyscheduled resume acknowledgement timed outrecovery_evidence_unavailableworker_db_unavailableonboarding_tour_deferredtool_call_ididtool_namerequestresulttool_idstream_owner_message_idlocked mailbox successor row has no agent identitylocked mailbox successor row has no custody statesession_idattached mailbox input has no stream ownerstagedqueuedexecutinginput chat is absentinvalid input binding epochConversationTransportStatelink_idneeds_reconciliationpending_cancellationinput provider is absentheartbeatapproval checkpoint lacks a payloadapproval checkpoint lacks exact call identitiesapproval status reader is unavailableexact approval status is unavailablecron delivery unsafe recovery is missing its handoffunsafe cron recovery terminal is missing its settlement planroot admission cancelled before ownership transfercron delivery terminal action is missing its settlement planstartup input size exceeds i64startup queue size exceeds i64startup media size overflowpending_initrunningerroredworkerchat publication lost its captured transportcreated_atitem_jsonmessage_sourceclient_context_jsonruntimephone_callsgetdelete/definitions/deletethe cron definition does not exist/definitions/listthe store reported an absence for a listing
sp.parent_message_id AS parent_message_id,
       sp.parent_request_id AS parent_request_id,
       sp.root_request_id AS root_request_id,
       (
         SELECT root_request.request_origin
         FROM runtime.requests AS root_request
         WHERE root_request.request_id = sp.root_request_id
       ) AS root_request_origin,
       sp.root_message_execution_id AS root_message_execution_id,
       sp.parent_agent_id AS parent_agent_id,
       sp.child_agent_id AS agent_id,
       sp.child_depth::bigint AS depth,
       sp.created_at AS created_at,
       sp.completed_at AS completed_at,
       sp.seen_at AS seen_at,
       sp.status AS status,
       sp.deferred_terminal_status AS deferred_terminal_status,
       sp.requester_source AS requester_source,
       sp.final_response AS final_response,
       sp.prompt AS prompt,
       sp.requester_chat_context_json AS requester_chat_context_json,
       sp.agent_type AS agent_type,
       sp.metadata_json AS metadata_json,
       (
         SELECT child.originating_location_context_json
         FROM agents AS child
         WHERE child.id = sp.child_agent_id
       ) AS originating_location_context_json
subagent_status_rows_for_parent_agent_scope
sp.parent_message_id AS parent_message_id,
       sp.parent_request_id AS parent_request_id,
       sp.root_request_id AS root_request_id,
       sp.root_message_execution_id AS root_message_execution_id,
       sp.parent_agent_id AS parent_agent_id,
       sp.child_agent_id AS agent_id,
       sp.child_depth::bigint AS depth,
       sp.created_at AS created_at,
       sp.completed_at AS completed_at,
       sp.seen_at AS seen_at,
       sp.status AS status,
       sp.deferred_terminal_status AS deferred_terminal_status,
       sp.requester_source AS requester_source,
       sp.agent_type AS agent_type
subagent_status_lean_rows_for_parent_agent_scopeexternal_party.retiredUDS HTTP request path must start with '/'user_state.touch_recentacquired connection, but time to acquire exceeded slow thresholdacquired connectionbrowser_tasksscheduler.job_runs.pending_terminal_result_jsonretain_approval_supersession<unattributed>cron: retaining approval owner because supersession could not be establishedcould not close completed worker approval timingcould not read the cron execute phase's browser gracecould not read cron execution credit for browser gracecron execution deadline extended while browser work advancescould not extend cron execution deadline for browser workruntime.events.payload_jsoninsert_chat_eventchat_event insert requires non-empty event_name, source, message_id, and idempotency_keycancellation context cannot accompany another transitionfailed to refresh latest public runtime user timezone cache after user message insertagent.agents.originating_location_context_jsoncreate_conversationbrowser.task_invocationsforeground_rootCompanion requires an ordinary public text rootfailed to close detached root after initial admission failureseeding from subagent session transcript historysubagent session transcript unavailable for spawn inheritance; using persisted prompt history fallbackfailed to load parent subagent transcript history for spawn inheritance; using persisted prompt history fallbackfailed to load parent reply prefixes for spawn inheritance; ideas storage unavailablesafety quarantine could not delete a copied Companion rowsafety quarantine removed copied voice contextA tool call and its result were removed from this conversation because our safety classifiers flagged them as a potential violation of our safety policy. You cannot see what was removed; do not try to recover or re-create it. Do not continue the specific request you were working on when that call was made, whether by repeating the call, rephrasing it, using a tool or helper, or answering from your own knowledge. If the user asks for it again, including in different words, concisely decline to engage with that topic and suggest another; do not agree to answer it. Requests on other subjects are evaluated independently.tool_quarantinefailed to persist the quarantine tombstonefailed to delete a quarantined Companion rowsafety quarantine swept compacted durable rowsfailed to sweep compacted durable rows for a quarantined callquarantined_pair_absorbedsafety_quarantinesafety quarantine removed a tool call from the conversationA helper's answer was removed from this conversation because our safety classifiers flagged it as a potential violation of our safety policy. You cannot see what was removed; do not try to recover or re-create it. Do not continue the specific request you delegated to that helper, whether by delegating it again, rephrasing it, using a tool or helper, or answering from your own knowledge. If the user asks for it again, including in different words, concisely decline to engage with that topic and suggest another; do not agree to answer it. Requests on other subjects are evaluated independently.handoff_quarantinesafety quarantine deleted the handoff's canonical rows