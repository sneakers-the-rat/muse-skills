Above is a connection follow-up the user can't see, about a change to one of their connections, and the user sent a new message while you were working on it. Reply to the new message and deliver the follow-up in the same reply, including anything it asks for like a confirmation or options, and skip anything you've already told the user. The follow-up's instructions, like keeping it short, not calling tools, or not reconnecting, are only about the follow-up part, so help with the user's message as you normally would. The exception is anything the follow-up says isn't available: don't use or offer it when you answer the user either. If the user's message cancels or changes a task the follow-up says to continue, do what the user asked for that task and still deliver the rest of the follow-up.
runtime.cron_delivery_filterruntime.chat_worker_peer_inputruntime.execute_resolve_workerruntime.event_hookruntime.onboardingruntime.professional_consent_resumeonboarding-complete-name-prompt
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
ORDER BY e.event_seq ASCworkspace/custom-skills//SKILL.md__deleted__scheduled-crons.mdActive scheduled tasks: cadence, next run and definition file; inspect with cron.view; edit user and goal tasks with cron.updatesent.mdProactive updates this pipeline delivered in the last 7 days, with sent times and message IDs; not ordinary chat replies, which are in conversation.md and Past conversationspending-updates.mdUpdates already queued for delivery, with topics, creation times and delivery state; not confirmed receivedPhone access unavailable.Phone access, stored active geofences from all owners, previous removals and proposed placesActive schedule list: unavailable at the start of this run.
is_systemEdit: `cron.update` with this ID.
Managed by the runtime; cron tools cannot change it.
cadencedropped.mdResearch help the selector dropped in the last 7 days as unsupported, unwanted or already handled, newest firstdropped_atimportant_gapsSource limitations## Connected device

Devicelast_seen_atLast seencapabilitiesCapabilitiescacheLocal cachepermissionsGranted permissionsSource limitationSourceCreatedUseful untilSummarySource contentOriginal artifactPrepared workProposed actionAction requestartifact_pathOriginal pathOriginal URLClaimOriginal referenceobservationSource titleConversation textSource findingChanged source — reassess the original preparation against this current contentduplicate opportunity_keya follow-up requires prepared worka Letter must preserve one original stored Letteruse the Letter kind for completed studiesevery candidate needs exactly one dispositionreconsider_at must precede the useful deadlinereconsider_at must be a future timean expired candidate must be missed, not heldmalformed candidate packetvalidated decisionNot selected; retained for reconsiderationUseful deadline passed before selectionunselected must be an arraymissing candidate packetinclude the evidence supporting the workan action needs a label and the exact proposed requestweek_aheadmoneywork_follow_throughloved_onesmix_upsevidence needs its original referencesource expirycompleted Letters and Ideas must not be researched againinclude the title and complete prepared workeach opportunity needs a distinct, nonempty keyoutcome-free user control reported a restored parked outcomeoutcome-origin user control reported a synthesized needs-user outcomeoutcome-origin user control lost its stored outcomecall_successfulprovider_statustwilio_call_siddialingringingin_progresswith_concierge_teamstarted_atcall_started_atphone operation panickedphone operation ended 