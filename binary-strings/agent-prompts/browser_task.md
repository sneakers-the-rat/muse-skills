browser.steer_specialistbrowser.kill_specialistbot_challenge.guidetool_result_safety_reviewsystem PostToolUse hook could not build presentation trace contextparse-failure heal delivering schema for fully rendered toolparse-failure self-heal delivering interfacetruncated_tools_loadedfailed to list runtime restart checkpoints during orphaned subagent reconciliationfailed to list pre-startup active subagents during restart orphan reconciliationsubagent was active before daemon restart but has no live runtime handle or restart checkpointmarked orphaned active subagent errored after restartfailed to persist orphaned active subagent terminal state after restartfailed to persist orphaned detached parent terminal state after restartmarking orphaned detached parent agent errored after restartdetached parent agent was active before daemon restart but has no live runtime handle or restart checkpointnotification opt-in turn offers lock poisonednotification opt-in offer outside a turnnotification opt-in has no root sessionreplace_runtime_restart_checkpoint_if_exact_payloadentertainment-media:star-front-viewfront-view icon candidates exhausted; using embedded defaultfront-view icon unavailable; trying the next fallbackbrowser.end_invocationbrowser.finish_invocationbrowser.note_task_progressavatar-state: exhausted CAS retries persisting default visual metadatasubagent RuntimeWork admission listener is closed; queueing untrackedsubagent RuntimeWork admission bridge is unavailable; queueing untrackedsubagent RuntimeWork admission did not settle; queueing untrackedfailed to load conversation while preparing Spaces builder close resultfailed to load subagent row while preparing Spaces builder close resultresuming subagent from session transcript historysubagent session transcript unavailable during resume; using persisted prompt history fallbackfailed to load subagent session transcript history during resume; using persisted prompt history fallbackfailed to load client context by context_seq during resume; continuing without per-message client contextfailed to load reply prefixes by context_seq during resume; ideas storage unavailablefailed to load reply prefixes by context_seq during resume; continuing without reply augmentationfailed to load transcript provenance by context_seq during resume; continuing without prompt provenancefailed to load parent_message_id for resumed subagent; continuing without attributionfailed to load root session metadata during resume; disabling memory flushowner-mail revocation unavailable; continuing agent cleanuphard-cancelling agent after user approval already wondeferring agent close because user approval already wonerroredfailed to persist aborted follow-up terminal settlement; retaining non-appendable restart checkpointprompt_shape_invalid_tool_callprompt_shape_invalid_assistant_partscurrent_iteration_inputno latest compaction checkpoint row matched sanitized prompt quarantine updatefailed to persist sanitized compaction checkpoint after prompt quarantineprompt_poison_quarantinefailed to mark quarantined chat events excluded from context windowfailed to mark quarantined tool-call chat events excluded from context windowcontext attachments require a user message or visible attachmentsession/onboarding_app_setup_completed.mdomitting unavailable best-effort follow-up file refThe sharing check could not complete. No candidate has been cleared for this chat.Your drafts haven't passed the sharing check. Reply briefly, in your own voice, that you can't help with this request. Don't share the information you were asked to leave out, and don't describe it in your refusal. Don't do any more work on the request. If no one in this chat asked for it, send nothing.
{discretion}{feedback}{draft}## Response Revision

Your draft hasn't been sent. Revise it to follow the feedback and this chat's discretion policy, both shown below. Keep your own voice and the useful parts of your answer, and reuse work you've already done. When you leave details out, don't repeat them in a warning, an explanation, or a description of what you removed.

{discretion}

Apply the feedback below only to this draft, not to drafts of unrelated later messages.

{feedback}

Draft to revise:
{draft}
group discretion could not clear refusalrequest verification classifier did not settleverifier_not_relevantverifier_unchangedverifier_feedback_returnedverifier_failedresponse verification failedcontext urgency classification must finish in one model passA safety policy refused this helper's work. Do not retry it, rephrase it, or route around it with another helper or tool. Tell the user this part of the request can't be helped with, and answer them now. The refusal covers this attempt only, and the safety system re-checks every attempt: if the user asks again in a later turn you may try once, and treat unrelated requests normally.subagent inference stream timed out waiting for first model output chunksubagent inference stream timed out waiting for next model output chunkerror decoding response body: provider stream ended before Done event; categories=[decode]; source=request or response body errorbrowser task execution requires an owned taskbrowser task scope is unavailablebrowser task queuebrowser taskbrowser task does not existbrowser task settlementbrowser workflow ownershipbrowser harness metadatabrowser task harness changedbrowser task owner changedcould not resolve the owning chat for a thread-less tracethis scheduled run has no job contextthis worker no longer owns its scheduled runThis resource is not shared with your conversation. Use connection.list_resources to find resources you can change.browser task policy is unavailable1password grant request failed1password grant request timed outchat worker provenance unavailablescheduled job's side chat unavailablescheduled job's side chat access unavailableThis connection's worker was replacedThis connection's worker is no longer currentThis circle task has no recorded connection lifetimebrowser specialist child fence closedauto_publish_enabledcurrent_build_publishedshare_update_requiredpublish_errorpublished_static_artifactartifact_slugfollow_up_settlementactionhandoff_message_idsubmission_message_idsubmission_sourceassistant_message_idfollow-up reached a terminal settlementroot follow-up settlement requires handoff identity and sources
SELECT event_seq, event_name, source, role::text AS role, visibility::text AS visibility,
       message_id, agent_id, parent_agent_id, parent_message_id, reply_to_message_id,
       transcript_surface::text AS transcript_surface, payload_json,
       (extract(epoch from created_at))::bigint AS created_at
FROM runtime.events WHERE idempotency_key = $1

SELECT ci.item_json, ci.message_source,
       (extract(epoch from ci.created_at))::bigint AS created_at,
       projection.client_context_json
FROM agent.context_items AS ci
LEFT JOIN agent.context_item_resume_projection AS projection
  ON projection.agent_id = ci.agent_id AND projection.seq = ci.seq
WHERE ci.agent_id = $1 AND ci.seq = $2
cancellation retry does not match its committed identity
SELECT
  GREATEST(
    (SELECT COALESCE(MAX(seq), -1) FROM context_items WHERE agent_id = $1),
    (SELECT COALESCE(MAX(seq), -1) FROM context_item_resume_projection WHERE agent_id = $1),
    COALESCE((SELECT handoff_context_high_water_seq FROM agent.agents WHERE agent_id = $1), -1),
    (SELECT COALESCE(MAX(root_seq), -1) FROM agent.companion_trace_imports WHERE root_agent_id = $1),
    (SELECT COALESCE(MAX(producer_seq), -1) FROM agent.companion_trace_imports WHERE producer_agent_id = $1),
    COALESCE((SELECT settled_seq FROM agent.companion_trace_sources WHERE producer_agent_id = $1), -1)
  ) AS max_item_seq,
  COALESCE((SELECT prompt_floor_seq FROM agents WHERE id = $1), -1)
    AS prompt_floor_seq,
  (SELECT COALESCE(MAX(checkpoint_seq), -1)
     FROM agent_compactions
     WHERE agent_id = $1
       AND checkpoint_seq IS NOT NULL
       AND has_replacement_history)
    AS checkpoint_seq
max_item_seqcheckpoint_seqlegacy completion has no verifiable batch ownerUPDATE agent.agents SET handoff_context_high_water_seq =
                GREATEST(COALESCE(handoff_context_high_water_seq, -1), $2)
             WHERE agent_id = $1SELECT state, submission_json, accepted_at, transcript_event_seq,
                    stream_owner_message_id FROM agent.message_mailbox
             WHERE agent_id = $1 AND submission_id = $2 FOR UPDATEstartup_submission_missinglegacy startup cancellation changed its replyaccepted_atstartup_submission_terminalstartup_execution_ownedstartup_already_cancelledtranscript_event_seqstartup cancellation input already has execution custodystartup_submission_changedUPDATE agent.message_mailbox SET state = 'aborted', terminalized_at = now(),
                    transcript_event_seq = $3
             WHERE agent_id = $1 AND submission_id = $2 AND state = 'accepted'
               AND stream_owner_message_id IS NULL AND transcript_event_seq IS NULLstartup cancellation custody changed before commitSELECT state, submission_json, accepted_at, transcript_event_seq,
                    stream_owner_message_id, checkpoint_custody FROM agent.message_mailbox
             WHERE agent_id = $1 AND submission_id = $2 FOR UPDATElegacy startup quota rejection changed its replypending startup input already has a transcript eventstartup_quota_rejectionUPDATE agent.message_mailbox SET state = 'completed', terminalized_at = now(),
                    transcript_event_seq = $3
             WHERE agent_id = $1 AND submission_id = $2 AND state = 'accepted'
               AND stream_owner_message_id IS NULL AND checkpoint_custody IS NULL
               AND transcript_event_seq IS NULLstartup quota rejection custody changed before commitbrowser.pending_inputsbrowser.pending_actionspresentation_localesend_item_completedpublication reviewthe publication review does not cover this revision of the Ideashared_wwwshared_ideaauthored_atsource changedthe Idea changed while sharingshared_payload_versionthe source Idea changed while sharingfleet feed records dropped below the freshness floorfleet feed-unit query task failedlive connector inventory socket unavailable; omitting connector statuslive connector inventory unavailable; omitting connector status/ideas/data-connections
# Live Connected Data Sources

This section is fresh for this accepted-Idea build. Use it before asking for account or data-source access. Do not ask the user to connect a source listed here; verify and read it with the available connector.

Currently connected:

Where a line carries a `Can:` list, that is the connector's whole declared surface (a permission plus the commands granting it). If the Idea needs data or an action no listed command provides, that connector cannot deliver it however the card is worded: say so rather than substituting a different source's numbers or shipping an automation you cannot verify. A line closing with `and more not listed here` was trimmed, and a line with no list did not publish its commands here; on either, check the connector the way you would have otherwise.
No outside data sources are currently connected.
http://localhost/hatch/muse/ideasJARVIS_TRACE_CONTEXT-only:start -->shopping/SKILL.mdshopping/references/browser-checkout.mdpurchase-preapproval-offpurchase-preapproval-onmuse-promo-code-offmuse-promo-code-onproduct-search-improvements-offproduct-search-improvements-oncatalog-search-v1catalog-search-v2muse-charm-purchaseucp/references/checkout-protocol.mdopentable/CONNECTOR.mdopentable-native-payments-offwhatsapp/references/commands.mdwhatsapp-sent-contactsCart reader returned an unsupported responseUnsupported cart response kindCart reader output too largeCart widget is unavailableforget memory reindex invoker is not installedforget confirm retracted memory claims before reindexforget confirm cleanup finished but memory reindex failedMuse could not refresh memory search after cleanup. Forgetting is not yet verified; retry after the memory index is available.mail task tools require the active mail Sessionmail conversation turn is no longer currenttodo continuation skipped: invalid snapshot