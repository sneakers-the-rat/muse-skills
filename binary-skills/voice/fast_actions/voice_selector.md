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
voice_fast_selector[voice id withheld]system_voice_catalog[voice name withheld][commentary omitted][thinking omitted][tool item omitted][compaction omitted]

Return only JSON that validates against this JSON Schema:
```json
correction_feedback"voice_name""display_name""system_voice_catalog"unparsed_voice_fieldssystem_catalog_entriessaved_voice_entries|:dark:staticstatic_framesvideo_clipsdarkmode_staticdarkmode_static_framesuploaddarkmode_clipdarkmode_video_clips.avatar-media-avatar job: failed to remove temporary media artifact--avatar-animate-image1:1--orientation--aspect-ratio--output-dir--output-nameupload_onlymedia generation exited successfully without structured outputundecodable_output--avatar-animation-backend--avatar-caller-idjarvis_avatar_statusrun_summarydurable provider video recovery is forbidden on a confidential VM--avatar-defer-pendingworkingmedia_unavailableavatar job removed incomplete outputavatar job failed to remove incomplete outputtimed outinternal server errorbad gatewaytoo many requestsrate limitno media attachmentstemporarily unavailablevideo_fbidavatar job cancelled after supersessiongenerated avatar did not satisfy its chroma canvas contractinvalid_outputmedia_paths has no existing local media filemedia_paths is missingimage_idsresponsible aisensitive wordspolicyinvalid argsmust beoutput_pathlocal--avatar-state-frame--avatar-state-frame-formanimalform_agnosticnative keyed status video does not use advanced-motion routingthis avatar stage runs directly, without media-generation argumentsopen input file for fd-passing:no such file or directory(os error 2)refusing to invalidate avatar frame outside the workspaceconfidential Avatar media authorization failedconfidential Avatar media operation failedartifact_idsmedia_handlesmedia_context_handlecitationsconfidential Avatar output has an invalid local media fileconfidential Avatar output must not be a symbolic linkconfidential Avatar publish path has no parentconfidential Avatar output is outside its assigned directoryconfidential Avatar output must contain exactly one local media fileconfidential Avatar output is missing its local media fileconfidential Avatar output contains a forbidden reference--duration-seconds--last-frame-source--last-frame-image-id--last-frame-imagesign-inbot-checkuntypedresidential_egress_profile_mismatchegress_replacement_unsupported_route/voice_companion/root_seed_context_seqdiscovery_pool_idea_card_buildidea_executionidea_generationartifact_generationwearable announcement fetch for a call opening returned an unreadable payloaddevice returned announcements Hatch has no record of announcing; dropping themall_unrecordeddevice returned the same announcement event id more than once; keeping one of eachannouncement result shrunk to stay under the tool-output spill boundswearable announcement fetch returned an unreadable payloadmalformed_payloaddevice_returned_nothingvoice.end_callvoice.set_muteruntime_roleskipped_task_context_too_largeskipped_authorization_context_too_largeskipped_target_too_largeruntime.audio_transcriptskipped_authorization_context_unavailablehistory_truncatedskipped_input_too_largerather than instead of don't want do not want no less  but  while  yet ;high-pitchedhigh pitchedhigh registerhigherlow-pitchedlow pitchedlowerfast-pacedfast pacedbriskquickfasterunhurriedslowersmoothsilkysatinyraspyhuskyraspierlouderquietsofterquieterNo sign-in agent has tried this sign-in in this run, so the report was not accepted. If your assignment or the user's latest direction rules out signing in, or the page offers no way to sign in, report again. Otherwise call `browser.login` on the tab that asks for the sign-in, follow its result under your instructions, and continue the assignment once the sign-in succeeds.
browser.reportA 1Password readiness probe for this browser is already in progress, so no credential fill was dispatched. Report blocked for now and explain the fill failure in summary; do not call login.advance again immediately.An earlier 1Password fill on this tab has an unknown outcome, so 1Password cannot fill it again. Report blocked and explain the fill failure in summary.1Password could not finish filling this form and cleared anything it typed. If your assessment shows the sign-in form, that login.advance call fills it again; if 1Password fails again, report blocked and explain the fill failure in summary.The page may be signed in, on a next step such as a password or code, showing an error such as an incorrect password, or showing a bot check. If the site rejected the saved login, assess the page as rejected with login.advance and don't retry it. Don't submit the emptied form.1Password's result was unknown, so the page was hard-refreshed and nothing it typed remains. An earlier submit may still have reached the site, so read the page before you fill again; if 1Password fails again, report blocked and explain the fill failure in summary.The 1Password connection is no longer authorized, so 1Password filled nothing. Do not retry. Report needs_input and explain in summary that the user needs to reconnect 1Password.The saved 1Password login is not for this site, so 1Password filled nothing. Report needs_input and explain in summary that the user needs to choose the right login.1Password could not answer, so it filled nothing. You can call login.advance again once; if 1Password fails again, report blocked and explain the fill failure in summary.1Password was not ready to fill this form, and no credential fill was dispatched. One further readiness attempt is available on a new login.advance call; if it fails again, report blocked and explain the fill failure in summary.1Password was not ready to fill this form, and the readiness retry budget for this browser is exhausted. No credential fill was dispatched. Report blocked and explain the fill failure in summary; do not call login.advance again, reopen the browser, or recreate the task to work around this.1Password was not ready to fill this form.messages.failed to prepare deferred inline anthropic image 'failed to inspect prepared deferred anthropic image dimensions for 'failed to prepare deferred inline anthropic imagefailed to decode inline anthropic image blockfailed to inspect inline anthropic image dimensionsfailed to inspect prepared deferred anthropic image 