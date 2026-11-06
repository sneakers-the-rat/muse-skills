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
voice_fast_selectorplannervoice_capture_originattached held confidential image to Companion provider requestimage_available[voice id withheld]system_voice_catalog[voice name withheld]developer[commentary omitted][thinking omitted][tool item omitted][compaction omitted]

Return only JSON that validates against this JSON Schema:
```json
correction_feedback"voice_name""display_name""system_voice_catalog"unparsed_voice_fieldssystem_catalog_entriessaved_voice_entries|invalid avatar dance mode--avatar-animate-image--avatar-animation-mode--output-dir--output-name--avatar-model-override--avatar-group-id--orientation--aspect-ratio1:1avatar dance requires one reference framedance reference is no longer selecteddance reference is not prepared:dark:static_framesvideo_clipsdarkmode_staticdarkmode_static_framesuploaddarkmode_clipdarkmode_video_clips.avatar-media-avatar job: failed to remove temporary media artifactupload_onlymedia generation exited successfully without structured outputundecodable_output--avatar-animation-backend--avatar-caller-idjarvis_avatar_statusrun_summarydurable provider video recovery is forbidden on a confidential VM--avatar-defer-pendingworkingmedia_unavailablerate_limitedavatar job removed incomplete outputavatar job failed to remove incomplete outputinternal server errorbad gatewaytoo many requestsrate limitno media attachmentstemporarily unavailablevideo_fbidavatar job cancelled after supersessiongenerated avatar did not satisfy its chroma canvas contractmedia_paths has no existing local media filemedia_paths is missingimage_idsresponsible aisensitive wordsinvalid argsmust beoutput_pathavatar-media-generation--avatar-state-frame--avatar-state-frame-formanimalform_agnosticnative keyed status video does not use advanced-motion routingthis avatar stage runs directly, without media-generation argumentsopen input file for fd-passing:no such file or directory(os error 2)refusing to invalidate avatar frame outside the workspaceconfidential Avatar media authorization failedconfidential Avatar media operation failedartifact_idsmedia_handlesmedia_context_handlecitationsconfidential Avatar output has an invalid local media fileconfidential Avatar output must not be a symbolic linkconfidential Avatar publish path has no parentconfidential Avatar output is outside its assigned directoryconfidential Avatar output must contain exactly one local media fileconfidential Avatar output is missing its local media fileconfidential Avatar output contains a forbidden reference--duration-seconds--last-frame-source--last-frame-image-id--last-frame-imagethe saved image has no image admission receiptneeds inputshopify_checkout_handoffCheckout handoff: unavailable.Checkout handoff: unresolved.Checkout handoff: captured for Muse's direct checkout.Payment: the user declined itcart_reviewCart: left unconfirmed by Muse, so nothing is boughtCart: change requestedMoneyCart: confirmed by MuseeffectsEffects: an effect's outcome is unknown; do not repeat itEffects: none unknownsubmissionplacementconfirmationconfirmed_productsconfirmed_totalterms_totalapproved_totalIf the report only hands back a captured checkout, follow the handoff below without asking for input or continuing browser payment preparation. Resolve any separately reported login need or blocker under your normal instructions first. When checkout is captured for Muse, leave the checkout tab open and finish with `browser.report`, `status: needs_input` and `reason: payment`, to hand checkout to Muse for UCP. Continue website checkout in the same task only if Muse explicitly instructed you to continue website checkout without another capture, or the handoff is unresolved. Report any blocker that prevents that continuation.
This call chain returned after a confirmed or uncertain environment replacement. Keep this BrowserTask and its recorded outcomes and purchase references. Respect stopped work and declined payments.

Recovery is a prerequisite, not completion of the assignment. Compare the current page with the original requested outcome and continue the work that remains through the appropriate specialists. Continuing that authorized work needs no new permission.

Before continuing affected work, inspect the current tabs and page. Combine your task history with the specialists' progress reports to identify completed steps, choices, constraints, verified entry URLs and missing state. Use that context to reconstruct only the missing steps from a known entry point in the tab the browser state names. Give each fresh specialist an explicit assignment with the relevant history and reconstruction steps; it does not inherit your conversation. A reopened URL does not restore POST data, JavaScript state, sign-in or form entries, and a merchant may still retain a cart or order on its server.

Reconcile uncertain submissions before retrying them, preserve confirmed outcomes, and continue an existing checkout by its reference. Do not request another replacement to resolve an unconfirmed move. If essential context is missing, report the specific gap rather than guessing what happened.
Continue your assignment.
Report the login agent's need with `browser.report` as `needs_input`, with its `reason` and the explanation it gave in `summary`. Get what any other specialist needs from your assignment, or ask Muse with `browser.request_input`. Follow your specialist instructions to continue the work or report the unresolved blocker.
Follow your instructions for this blocker. Do not do its protected work with ordinary browser actions.
You stopped this specialist.
The specialist stopped without a verified result, and its recorded actions may still need checking. Call the same specialist again, or report the blocker in `browser.report`. Do not do its protected work with ordinary browser actions or another tool, and do not repeat an uncertain purchase.
The user declined the payment. Report that outcome in `browser.report`. Do not start another checkout.
browser.paybrowser.loginbrowser.bot_challengeSubagentCompletionMetadatasubagent completion lists have different lengths
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
ORDER BY e.event_seq ASCprepared work arrayunresolved_referenceunverified_observationNo work selected for deliveryat most one follow-up across both messagesgive each supplied key exactly one decisionRetained for reconsiderationUseful delivery window missedNot selected for further attentionunknown presentationunknown kindan offer needs the exact action the user can acceptevidence needs an original referenceSelected prepared helpuse null when a priority has no work to sendinvalid candidate packetwearable announcement fetch for a call opening returned an unreadable payloaddevice returned announcements Hatch has no record of announcing; dropping themall_unrecordeddevice returned the same announcement event id more than once; keeping one of eachannouncement result shrunk to stay under the tool-output spill boundswearable announcement fetch returned an unreadable payloadmalformed_payloaddevice_returned_nothingedit-baselinelocation_lookup_reasonturn_context_unavailablecoordinates_unavailableinvalid_coordinatesclient_unavailableupstream_errorno_resultvoice_fast_search_location_fallbackvoice_tool_llm_expert_fallback_missing_search_queryvoice_tool_llm_expert_fallback_missing_required_locationvoice_tool_llm_expert_fallback_fast_search_failuremissing_search_querymissing_required_locationfast_search_failurecard brandbalanceuser-infopayment-methods--include-catalog-statusaddconfigurebank namebank_accountPayment methodBank accountPaymentMethodcard_detailsbank_account_detailsaddress line 1address line 2dependent localityadministrative areapostal codesorting codecountry codeWalletCatalogpayment_methodsapproval_policy_availableapproval_policypayment-methods list did not contain any usable recordsUse `next_action.markdown` exactly as provided; do not paste the raw URL. Explain that it opens Stripe Link's secure payment-method page and ask the user to add a payment method.
Stripe Link returned an unexpected wallet URLshipping-addresses list did not contain any usable recordscontinue_urlauth.inspectauth.userinfopayment_methods.listpayment_methods.addShop Pay does not support balance configurationshipping_addresses.listShop Pay response omitted its resultShop Pay returned an incompatible machine responseManage Shop Pay payment methodsUse `next_action.markdown` exactly as provided. Explain that it opens Shopify's secure Shop Pay wallet page and ask the user to manage their payment methods there.Shop Pay response omitted connection statususer infoShopPayUserInfofirst namelast nameShop Pay user info retrieval did not succeedaction URLShop Pay response omitted action URLShop Pay did not return a user interactionpayment method labelShop Pay returned an invalid responsewallet displayinstrumentsShop Pay wallet display did not contain any usable card optionsShop Pay payment method result omitted its instrumentsShop Pay payment method listing did not succeedconnection statusWalletDisplayaddressesShop Pay wallet display did not contain any usable addressesShop Pay shipping address listing did not succeedtool_resultruntime_roleskipped_task_context_too_largeskipped_authorization_context_too_largeskipped_target_too_largeruntime.audio_transcriptskipped_authorization_context_unavailablehistory_truncatedskipped_input_too_largerather than instead of don't want do not want no less  but  while  yet ;high-pitchedhigh pitchedhigh registerhigherlow-pitchedlow pitchedlowerfast-pacedfast pacedbriskquickfasterunhurriedslowersmoothsilkysatinyraspyhuskyraspierlouderquietsofterquieterNo sign-in agent has tried this sign-in in this run, so the report was not accepted. If your assignment or the user's latest direction rules out signing in, or the page offers no way to sign in, report again. Otherwise call `browser.login` on the tab that asks for the sign-in, follow its result under your instructions, and continue the assignment once the sign-in succeeds.
browser.reportA 1Password readiness probe for this browser is already in progress, so no credential fill was dispatched. Report blocked for now and explain the fill failure in summary; do not call login.advance again immediately.An earlier 1Password fill on this tab has an unknown outcome, so 1Password cannot fill it again. Report blocked and explain the fill failure in summary.1Password could not finish filling this form and cleared anything it typed. If your assessment shows the sign-in form, that login.advance call fills it again; if 1Password fails again, report blocked and explain the fill failure in summary.The page may be signed in, on a next step such as a password or code, showing an error such as an incorrect password, or showing a bot check. If the site rejected the saved login, assess the page as rejected with login.advance and don't retry it. Don't submit the emptied form.1Password's result was unknown, so the page was hard-refreshed and nothing it typed remains. An earlier submit may still have reached the site, so read the page before you fill again; if 1Password fails again, report blocked and explain the fill failure in summary.The 1Password connection is no longer authorized, so 1Password filled nothing. Do not retry. Report needs_input and explain in summary that the user needs to reconnect 1Password.The saved 1Password login is not for this site, so 1Password filled nothing. Report needs_input and explain in summary that the user needs to choose the right login.1Password could not answer, so it filled nothing. You can call login.advance again once; if 1Password fails again, report blocked and explain the fill failure in summary.1Password was not ready to fill this form, and no credential fill was dispatched. One further readiness attempt is available on a new login.advance call; if it fails again, report blocked and explain the fill failure in summary.1Password was not ready to fill this form, and the readiness retry budget for this browser is exhausted. No credential fill was dispatched. Report blocked and explain the fill failure in summary; do not call login.advance again, reopen the browser, or recreate the task to work around this.1Password was not ready to fill this form.No such filenot foundstartLineendLineroom memory flush path must not traverse symlinksqueries cannot be empty (the user's window: change it only if they ask)user_controlledwaiting_on_userwaiting_on_root (default)