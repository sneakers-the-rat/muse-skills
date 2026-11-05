Use this fast action only during a live voice call, when the caller asks to
choose, try, recommend, or change to a voice without naming one exact voice.
The action immediately selects and demonstrates one voice; it never returns a
picker.

Use it when the caller asks you to pick a voice, gives qualities that define
the choice, asks for one voice recommendation, asks for a new or
different voice, or asks to create a custom voice with a usable direction or a
delegated creative choice such as “surprise me.” Do not
promise that custom creation is available;
`voice.options` owns that capability decision.

Do not use it for a bare request to create, design, or make a custom voice with
no direction and no choice between describing one or having you pick; that
belongs to `other` so the conversational agent can ask one natural question.
Do not use it for one
exact named voice (`set_voice`), the current voice, a request to go back to an
earlier voice, a request to see several voice options, broad browsing,
previewing, open-ended comparison, multiple
newly created or custom voices, an ambiguous reference, a request
limited to saved voices without one exact name, or a request combined with
another task. Those conversational requests belong to `other`. If a saved-only
request nevertheless reaches this scoped action, fail
closed by finishing without a tool. Never substitute catalog voices for the
requested saved voices or existing voices for requested new designs.

Call `voice.options` exactly once with a self-contained request in the
caller's terms. Resolve confirmations and references from the conversation:
“yes please” after you offered warmer voices becomes “a warmer voice.” When
the current utterance answers the immediately preceding clarification, include
the original request; for example, pass both “make a brand-new voice” and
“surprise me.” Describe the qualities of the voice the caller wants, such as
“a warmer voice” or “a deep male voice,” rather than phrasing it relative to
the current voice, unless the caller explicitly asks for a change relative to
it, such as “deeper than now” or “same but more upbeat.” Refer to a voice from
earlier options as “the voice” and its name, such as “the voice Bloom.” Never
pass a bare confirmation, or a generic request for options when the
conversation gives the qualities discussed. Do not add the current voice's
name. The runtime identifies a catalog current voice but not a custom or saved
one, so for a relative request while a custom or saved voice is current,
describe that voice's qualities from the conversation.

Omit `candidate_count`. Omit `gender` unless the caller explicitly asks for a feminine, masculine, or
neutral acoustic presentation; then use `F`, `M`, or `N`. Pass `any` when the
caller explicitly permits any gender or requests a gender change without
naming a target presentation. Never infer gender from the request's other
traits, the current voice, or the persona. Pass
`accent` only when the caller explicitly requests one, using the caller's
wording; never infer it from the caller, persona, avatar, locale, or
demographics. When `current` cannot be resolved from trusted catalog metadata,
the runtime continues without a gender filter; do not ask a clarification.

The runtime chooses only among capabilities available to this user. Do not
present a picker, write assistant prose, call another tool, or retry.

The runtime switches and demonstrates one voice per turn, so the caller can
react and refine conversationally. This action never presents a voice widget,
voice note, or audio control, and never speaks a list of internal voice names.
voice_fast_selectorshortplannervoice library reranking failed; using the voice-option plannerjina_fallback_plannersafety_blocksafety_adult_substitutionsafety_planner_fallbackvoice library safety check failed; refusing the reranked resultsafety_errorvoice_library_rerankerRank voice-library candidatesvoice_option_selection_resolvednot_run[voice id withheld]system_voice_catalog[voice name withheld]developer[commentary omitted][tool item omitted][thinking omitted][compaction omitted]

Return only JSON that validates against this JSON Schema:
```json
correction_feedback"voice_name""display_name""system_voice_catalog"unparsed_voice_fieldssystem_catalog_entriessaved_voice_entries|-7x12-vinvalid portrait output pathcall portrait crop throttled:dark:staticstatic_framesvideo_clipsdarkmode_staticdarkmode_static_framesdarkmode_clipdarkmode_video_clips.avatar-media-avatar job: failed to remove temporary media artifact--avatar-animate-image1:1--orientation--aspect-ratio--output-dir--output-nameupload_onlymedia generation exited successfully without structured output--avatar-animation-backend--avatar-caller-idjarvis_avatar_statusrun_summarydurable provider video recovery is forbidden on a confidential VM--avatar-defer-pendingworkingavatar job removed incomplete outputavatar job failed to remove incomplete outputinternal server errorbad gatewaytoo many requestsrate limitvideo_fbidavatar job cancelled after supersessiongenerated avatar did not satisfy its chroma canvas contractmedia_paths has no existing local media filemedia_paths is missingimage_idsresponsible aisensitive wordsinvalid argsmust beoutput_pathavatar-media-generation--avatar-state-frame--avatar-state-frame-formanimalform_agnosticnative keyed status video does not use advanced-motion routingthis avatar stage runs directly, without media-generation argumentsrefusing to invalidate avatar frame outside the workspaceconfidential Avatar media authorization failedconfidential Avatar media operation failedartifact_idsmedia_handlesmedia_context_handlecitationsconfidential Avatar output has an invalid local media fileconfidential Avatar output must not be a symbolic linkconfidential Avatar publish path has no parentconfidential Avatar output is outside its assigned directoryconfidential Avatar output must contain exactly one local media fileconfidential Avatar output is missing its local media fileconfidential Avatar output contains a forbidden referencetransition--duration-seconds--last-frame-source--last-frame-image-id--last-frame-imagethe saved image has no image admission receiptslot0slot1body_lengthmagiclengthquarantine prune skipfailed to quarantine handoff marker filehandoff_selector_readhandoff_slot_readhandoff_marker_validationhandoff_marker_digestidea_executionidea_generationartifact_generationbrowser current-run outcome scope unavailablebrowser retained current-run observations unavailable&><`$(visibilityvisibility_verifiedowner_namefull_nameauthor_usernamepermalinkpost_captionpost_commentsstatic provenance coverage serializesshare_provenance_evidence_v1share provenance evidence bundle serializes[tool output bounded:[Tool output exceeded 100KB[Background exec output exceeded 100KB but paging failed.public_headerhandleprepared work arrayunresolved_referenceunverified_observationNo work selected for deliveryat most one follow-up across both messagesgive each supplied key exactly one decisionRetained for reconsiderationUseful delivery window missedNot selected for further attentionunknown presentationunknown kindan offer needs the exact action the user can acceptevidence needs an original referenceSelected prepared helpuse null when a priority has no work to sendinvalid candidate packetcontent_limitSource limitationdisplayNameEmailphone update is not owedphone update changeddialingringinghandoff_pendingThe phone provider did not accept the call, so it was not placed.phone delivery has no supported outcomephone transcript could not be materializedphone recovery expiry has no reportable outcomephone result is not readyphone question is not owedphone question 