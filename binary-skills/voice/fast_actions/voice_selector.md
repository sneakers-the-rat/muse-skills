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
voice_fast_selectorplanner-7x12-vinvalid portrait output pathcall portrait crop throttled:dark:static_framesvideo_clipsdarkmode_staticdarkmode_static_framesoptionsdarkmode_clipdarkmode_video_clips.avatar-media-avatar job: failed to remove temporary media artifact--avatar-animate-image1:1--orientation--aspect-ratio--output-nameupload_onlymedia generation exited successfully without structured output--avatar-animation-backend--avatar-caller-idjarvis_avatar_statusdurable provider video recovery is forbidden on a confidential VM--avatar-defer-pendingworkingavatar job removed incomplete outputavatar job failed to remove incomplete outputinternal server errorbad gatewaytoo many requestsrate limitvideo_fbidavatar job cancelled after supersessiongenerated avatar did not satisfy its chroma canvas contractmedia_paths has no existing local media filemedia_paths is missingresponsible aisensitive wordspolicyinvalid argsmust beavatar-media-generation--avatar-state-frame--avatar-state-frame-formanimalform_agnosticnative keyed status video does not use advanced-motion routingthis avatar stage runs directly, without media-generation argumentsrefusing to invalidate avatar frame outside the workspaceconfidential Avatar media authorization failedconfidential Avatar media operation failedartifact_idsmedia_context_handleconfidential Avatar output has an invalid local media fileconfidential Avatar output must not be a symbolic linkconfidential Avatar publish path has no parentconfidential Avatar output is outside its assigned directoryconfidential Avatar output must contain exactly one local media fileconfidential Avatar output is missing its local media fileconfidential Avatar output contains a forbidden reference--duration-seconds--last-frame-source--last-frame-image-id--last-frame-imageneeds inputshopify_checkout_handoffCheckout handoff: unavailable.Checkout handoff: unresolved.Checkout handoff: captured for Muse's direct checkout.Payment: the user declined itcart_reviewCart: left unconfirmed by Muse, so nothing is boughtCart: change requestedMoneyCart: confirmed by MuseeffectsEffects: an effect's outcome is unknown; do not repeat itEffects: none unknown/report/reasonsubmissionplacementconfirmationconfirmed_productsconfirmed_totalterms_totalapproved_totalThe user declined an approval the Poppy agent asked for, and that is their decision. Don't do that action on the company's site or ask for the same approval again unless the user asks again; report that it was not done. Other work the assignment still needs may go on, at this company or elsewhere.
A company sign-in the Poppy agent offered ended without connecting the user's account. Don't sign in to this company on its site or do work there that needs the account, such as an order or the account's history, unless the user asks again; report what still needs the account. Work that needs no account may go on, at this company or elsewhere.
Continue on the company's site only for what the report says neither the API nor the company's own agent could do. Opening it now goes ahead, in the same company session when the company offers browser sessions, so what the Poppy agent did there carries over. When the report names a conversation with the company, keep its IDs in your own report exactly as given: the conversation's ID while it is still open, so Muse can pass the user's follow-ups into it, and the company's `company_conversation_id`, which a later order needs.
When the report names a conversation with the company, keep its IDs in your own report exactly as given: the conversation's ID while it is still open, so Muse can pass the user's follow-ups into it, and the company's `company_conversation_id`, which a later order needs. When the report says a follow-up belongs in a conversation that is still open, Muse passes it on from the user's message: don't take that follow-up to the company's site. When the rest of your assignment is done, include that conversation's ID in your `completed` report.
If the report only hands back a captured checkout, follow the handoff below without asking for input or continuing browser payment preparation. Resolve any separately reported login need or blocker under your normal instructions first. When checkout is captured for Muse, leave the checkout tab open and finish with `browser.report`, `status: needs_input` and `reason: payment`, to hand checkout to Muse for UCP. Continue website checkout in the same task only if Muse explicitly instructed you to continue website checkout without another capture, or the handoff is unresolved. Report any blocker that prevents that continuation.
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
