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
replay-forbidden checkpoint is missing its current submissionreplay-forbidden checkpoint contains duplicate submission identitiesreplay-forbidden checkpoint current submission identity disagrees<none>runtime_restart_orphaned_subagents_reconciledcutoff_created_atactive_subagent_row_countrestart_checkpoint_row_countruntime_owned_subagent_countrestart_checkpointed_subagent_countorphaned_subagent_countorphaned_spaces_builder_countorphaned_subagent_terminalize_failure_countcandidate_parent_agent_countparent_agent_current_root_skip_countparent_agent_seen_active_row_skip_countparent_agent_owned_child_skip_countparent_agent_runtime_owned_skip_countparent_agent_restart_checkpointed_skip_countorphaned_parent_agent_countorphaned_parent_agent_terminalize_failure_countby_requester_sourcehotset capture skippedremote_postgresruntime_resume_handoffmarker_slotindex_bytesindex_itemsindex_rewriteshandoff-epochhandoff epoch sidecar write failed; clean-stop proof will read epoch 0 (unclean path)embed_tokenchange_live_but_no_card_after_interruptasked_userchange_live_but_no_card_after_failuresuccess_but_card_not_sentcard_shown_but_review_opencard_showncard_shown_but_unverifieddelivered_space_build_completed_widget_idsbrowser current-run outcome scope unavailablebrowser retained current-run observations unavailable;|&><`$(instagram-messages-clithreads-messages-clihatch_messenger_clihatch_igd_clihatch_wai_clisharepolicyguard_exp_policyphone update is not owedphone update changedThe phone provider did not accept the call, so it was not placed.phone delivery has no supported outcometranscript_pathphone transcript could not be materializedtranscript_truncatedphone recovery expiry has no reportable outcomephone result is not readyphone question is not owedphone question 