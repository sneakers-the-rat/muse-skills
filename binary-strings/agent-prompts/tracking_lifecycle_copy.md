You write the user-facing state and activity when an assistant-tracking goal is
reopened.

Use only the supplied goal, lifecycle reason, recent activity, and optional
state hint. Do not invent work, results, blockers, dates, or next steps.

If the item resumed as private tracking after its connection ended, reflect that
scope. The connection and its previous automatic follow-ups have not resumed.

For `current_state`, write one short sentence containing only the single most
relevant durable state now. Prefer a specific wait, blocker, monitored
condition, or user-facing cadence from the evidence. If the responsibility is
waiting for user input, state exactly what input is needed. If no specific
state exists, state that the responsibility resumed and what it concerns.

Do not claim work is currently in progress. Do not append a next step, combine
two states with a semicolon, or restate the goal title or description.

For `activity_title`, write a concise user-facing reopening event label.

Do not mention internal runtime or scheduler machinery, job identifiers,
internal action names, or counts of schedules restored. User-facing cadence,
dates, and meaningful quantities from the evidence are allowed when they are
the most relevant current state.

Your only response must be one invocation of the available
`muse.set_tracking_goal_lifecycle_copy` function tool with exactly these named
arguments:

- `current_state`: one short sentence with the durable state now.
- `activity_title`: a concise reopening event label.

Invoke the function tool itself. Do not output text, Markdown, JSON, XML, or a
written or pseudo-code representation of the call.
encode direct Space search requestdirect Space search request length does not fit the RPC framesystem clock is before the Unix epochdirect Space search deadline does not fit u64JARVIS_RUNTIME_CONTEXT_TOKENfailed to prepare a trusted runtime context for direct Space searchbuilder probe runtime context token is emptytimed outtimeoutstatus 502status 503status 401status 403connectionconnecttophas_vertical_datavertical_data_countresult_size_bytesweatherfinancelocalctx.tool.sports_dataupstream_retrylocal_workerbuilder_probeverified_publishedbrowser_tool_backend_selectedList ranked ideasReturns recent ideas plus deterministic feed selection and records surfaced events. `Accept-Language` projects current exclusively bundled-catalog-owned title and summary copy; other stored text remains verbatim.daemon_ideas_resetReset the Ideas feedDeletes the local Ideas corpus, feed snapshots, build status, ranking state, and readiness metadata. The next `/api/idea-cards` read rebuilds the cold null-state feed from DiscoveryPool, matching a fresh user's Ideas surface without resetting chat, files, goals, Spaces, or onboarding.daemon_idea_createCreate an ideaCreates a structured idea record.daemon_idea_getGet idea detailReturns a single idea by id. `Accept-Language` projects current exclusively bundled-catalog-owned presentation fields; instructions and generated, user-authored, or external text remain verbatim.daemon_space_ideasList ideas for a web artifactReturns the first-class ideas attached to a web artifact slug. `Accept-Language` applies bundled-catalog projection only to current exclusively catalog-owned rows.daemon_idea_refreshRefresh the Ideas feed nowEnqueues an immediate Ideas self-improvement objective run (the same retrieval-augmented generation pipeline the background cadence drives) so a client can pull fresh, personalized ideas on demand instead of waiting for the next scheduled cadence. The endpoint returns as soon as the durable run is accepted or coalesced; the background drain rewrites the materialized `/api/idea-cards` feed after a successful Ideas run. `Accept-Language` selects the generation locale and is retained through retries and restart continuation. A development-only `limit` query parameter can cap the number of generated Ideas for faster VM iteration.daemon_idea_decisionRecord an idea decisionRecords a deterministic idea decision event and updates an anchor when supplied.daemon_idea_feedbackRecord idea feedbackRecords structured feedback for calibration and idea quality loops.daemon_idea_lifecycleUpdate idea lifecycleUpserts lifecycle state for an idea anchored to a runtime object.daemon_idea_card_debugGet Ideas tab idea-card debug metadataRead-only attribution for one Ideas tab card: stored idea row (including the rationale and install markdown the product card withholds), verifier quality scores, generator provenance blobs (run id, authoring request id, lens ratings and feedback, grounding, execution contract), recent idea events with their ranking decomposition, engagement funnel, dedup, anchors, build status, and the active feed snapshot. Employee-only: a viewer who does not pass the `abra_hatch_show_employee_disclosures` Gatekeeper gets the same `404` a nonexistent card returns.Ideasdaemon_idea_card_shareShare an Ideas tab cardIdempotently resolves the card's public target. Catalog cards return their external catalog id; personalized cards publish their pre-generated generalized variant to WWW. Returns the canonical shareable Idea id and full Muse deep link. An optional `expectedPreviewRevision` refuses the share with 409 `idea_share_preview_changed` when the content no longer matches that preview.daemon_idea_cards_listList Ideas tab cardsReturns the pre-materialized native Ideas feed for the current Muse Ideas tab contract, windowed by section cursor when `pageSize` is supplied: native sections first, then the materialized fallback tail. Stored domain labels remain server-internal. Missing or incompatible feed pointers receive a projection-only background repair. Other reads arm the next daily Ideas phase; this read path does not generate inline. `Accept-Language` localizes deterministic card chrome and current exclusively bundled-catalog-owned copy; other stored text remains verbatim.daemon_idea_engagementRecord idea engagementRecords a canonical engagement/feedback event (impression | click | engagement | feedback_up | feedback_down) on an idea so the measurement layer can consume the impression -> click -> engage funnel plus the explicit thumbs signal.daemon_idea_anchor_feedList ideas for an ancho