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
voice_fast_selectorvoice_capture_originimage_availablecheckout_records_unavailablepurchase_receipt_failedcheckout_save_failedWhen this call only records cart details and no order has been submitted for this checkout, you can retry the recording.

If an order has been submitted or its submission is uncertain, a recording error does not establish whether it was placed. Do not repeat the submission to resolve it or keep retrying the same failed record.

If recording remains unavailable, finish with `browser.report` using `status: blocked` and `summary`. Describe what the merchant showed, any confirmation number, and what remains unresolved. Leave out `outcome` and `confirmation` for this handoff; it returns the existing purchase records without trying to record the order again.
When the result calls for corrected purchase details, record them with `checkout.inspect` and use `checkout.review_cart` if cart review is needed. Use `checkout.commit` when the result calls for another payment attempt.
When the result calls for a correction or another payment attempt, use `checkout.prepare` with the current purchase. Follow the result's conditions for continuing.
walletbrowser.files Write it as {"tab": "t1", "kind": "download", "target": "@e12"}, with only the fields its kind takes.sign_in_records_unavailablesign_in_page_unreadablesign_in_fields_unavailablesaved_logins_unavailablesign_in_consent_failedsecure_entry_failedsign_in_fill_failednative_pagetargetdocnative_imagelocal_cellBrowser screenshot evidenceREPAIR_THREADS.yamlGoal briefings ready to surface. Mention the new briefings to the user when it fits the conversation; follow up on opened briefings if the user wants to go deeper. Do not force them into an unrelated reply.
new — offer to the useropened — follow up if usefulOpen relationship-repair threads. A prior turn ruptured trust; carry the repair forward when it fits: acknowledge the issue, correct the behavior, and confirm the user is satisfied before considering it resolved.
competence_failuredata_boundary_failureboundary_overreachoverfamiliarityunder_supportexternal_action_errorsafety_escalationfence_hand_editacknowledged — identify what went wrongassumption identified — correct the behaviorcorrected — record the future commitmentawaiting resolution — confirm the user is satisfiedunselectedNo work selected for deliveryat most one follow-up across both messagesgive each supplied key exactly one decisionRetained for reconsiderationUseful delivery window missedNot selected for further attentionunknown presentationprepared_workunknown kindan offer needs the exact action the user can acceptevidence needs an original referenceSelected prepared helpuse null when a priority has no work to sendinvalid candidate packetmissing candidate packetresume_from_snapshot_idstart_freshA 1Password readiness probe for this browser is already in progress, so no credential fill was dispatched. Report blocked for now and explain the fill failure in summary; do not call login.advance again immediately.An earlier 1Password fill on this tab has an unknown outcome, so 1Password cannot fill it again. Report blocked and explain the fill failure in summary.1Password could not finish filling this form and cleared anything it typed. If your assessment shows the sign-in form, that login.advance call fills it again; if 1Password fails again, report blocked and explain the fill failure in summary.The page may be signed in, on a next step such as a password or code, showing an error such as an incorrect password, or showing a bot check. If the site rejected the saved login, assess the page as rejected with login.advance and don't retry it. Don't submit the emptied form.1Password's result was unknown, so the page was hard-refreshed and nothing it typed remains. An earlier submit may still have reached the site, so read the page before you fill again; if 1Password fails again, report blocked and explain the fill failure in summary.The 1Password connection is no longer authorized, so 1Password filled nothing. Do not retry. Report needs_input and explain in summary that the user needs to reconnect 1Password.The saved 1Password login is not for this site, so 1Password filled nothing. Report needs_input and explain in summary that the user needs to choose the right login.1Password could not answer, so it filled nothing. You can call login.advance again once; if 1Password fails again, report blocked and explain the fill failure in summary.1Password was not ready to fill this form, and no credential fill was dispatched. One further readiness attempt is available on a new login.advance call; if it fails again, report blocked and explain the fill failure in summary.1Password was not ready to fill this form, and the readiness retry budget for this browser is exhausted. No credential fill was dispatched. Report blocked and explain the fill failure in summary; do not call login.advance again, reopen the browser, or recreate the task to work around this.1Password was not ready to fill this form.No such filenot foundstartLineendLineroom memory flush path must not traverse symlinksqueries cannot be 