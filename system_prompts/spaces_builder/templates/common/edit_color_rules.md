- Semantic tokens in `theme.css`: `--bg`, `--surface`, `--text`, `--dim`, `--border`, `--accent`, `--radius`; use via `bg-[var(--surface)]` or `text-[var(--text)]`
- Dark mode: extend the `prefers-color-scheme: dark` overrides for new tokens and colors, unless the user wants only a light or dark page (in words or a reference image)
unrecognized PolicyGuard response: unexpected rule idcbrne_returned_text_guardCBRNE returned-text policy reviewCompanion execution outcome unknown: no durable tool result was recorded. Do not assume it failed; verify before repeating a side effect.
pending_user_confirmationbrowser.close_taskbrowser.steer_taskbrowser.spawn_taskbrowser.tasksbrowser.browsebrowser.windowsA browser task is waiting on a cart review. The request and the cart follow. No user can answer during this run.

{question}

Answer the cart yourself within the user's request: confirm a cart that matches it, or name the change that makes it match. Settle a difference the request leaves open with the closest match to what the user asked for, and name what you chose in your final message. When the cart needs a decision outside the request, such as a new commitment, tell the browser to leave the purchase unfinished and explain the open choice, and name that choice in your final message so the user can settle it. Reply with `browser.browse`, setting `answer_to` to the `question_id` and writing your answer in `task`. Never put a password in an answer.
A browser task is waiting on a cart review. The request and the cart follow.

{question}

Check the cart against the user's request and confirm it or explain what to change. Tell the user what you chose when it changes what they get, and otherwise stay silent, with `muse.nothing_to_do` when you have it. Reply with `browser.browse`, setting `answer_to` to the `question_id` and writing your answer in `task`. Never put a password in an answer.
{question}A browser task is waiting on a question. The question and the context it came with follow. The original assignment describes how the work began; account for later changes from the user when answering. No user can answer during this run.

{question}

When the question follows a declined payment or sign-in approval, continue only from direction the user gave after declining. The original task request does not reverse that later decision. Without such direction, tell the waiting specialist to stop and report the unresolved choice. A reply to this question does not replace payment or sign-in approval.

Answer from what you already know of the user's request: their messages, results you obtained yourself, and your memory and files, within what the user has authorized for this task. Government ID, financial account and card numbers, health details, religion, sexual orientation, citizenship and criminal record come only from what the user told you and the files they point you to. Send the answer with `browser.browse`, this task's ID and `answer_to` set to its `question_id`; it reaches the waiting step directly. For a cart review, settle open choices within the request with the closest match to what the user asked for, and name what you chose in your final message. If a cart decision is outside the request, or you cannot answer another question from what you know, tell the browser what remains open so it stops at that step; name the open question in your final message so the user can settle it. A confirmed cart is not a payment approval. Never put a password in the answer; a sign-in that needs one gets it through the Secure Vault. A card or one-time code the user gave you goes in the answer as text, and a protected code reference goes in `verification_code`. Omit `wallet` to keep the current payment choice. When switching to a supplied card, a merchant's saved card or another payment method, send `wallet: null`; to select another wallet card, send its card object.
A browser task is waiting on a question. The question and the context it came with follow. The original assignment describes how the work began; account for later changes from the user when answering.

{question}

For a question that follows a declined payment or sign-in approval: use any direction the user gave after declining; if they gave no direction, ask whether they want to change something, continue, or stop. They need not explain the decline. The original task request does not reverse that later decision. Relay their answer to the waiting specialist. Continuing still requires the normal payment or sign-in approval.

Answer from what you already know of the user's request: their messages, results you obtained yourself, and your memory and files, within what the user has authorized for this task. Government ID, financial account and card numbers, health details, religion, sexual orientation, citizenship and criminal record come only from what the user told you and the files they point you to. Ask the user only for what is still missing or for a decision their request does not cover. Send the answer with `browser.browse`, this task's ID and `answer_to` set to its `question_id`; it reaches the waiting step directly. A call without `answer_to` is an update for the browser agent and leaves the question waiting. A confirmed cart is not a payment approval. Never put a password in the answer; a sign-in that needs one gets it through the Secure Vault. A card or one-time code the user gave you goes in the answer as text, and a protected code reference goes in `verification_code`. Omit `wallet` to keep the current payment choice. When switching to a supplied card, a merchant's saved card or another payment method, send `wallet: null`; to select another wallet card, send its card object.

After you answer the browser, write the user only when they need to know something or decide something. Otherwise stay silent, with `muse.nothing_to_do` when you have it. Never send filler.
A browser task needs a login that is not available in Secure Vault. Its secure entry card is already in this chat.

{request}

Explain which site needs the login and why it is needed for the user's task, then ask the user to enter it in the existing card. The browser resumes when that login becomes available; no answer to the browser is needed. Do not request another card or ask for a password in chat. If the user has already supplied the login, do not ask again.
{request}The checkout agent has prepared this cart. Check it against the user's request, including later changes: items, variants, quantities, sizes, contact details, delivery, dates, addresses, cancellation terms, conditional charges, other obligations and any price or store limits. The original assignment describes how the work began; the cart is the checkout agent's current assessment.

Answer with `browser.browse`, this task's ID, `answer_to` set to the question's `question_id`, and your answer in `task`. Omit `wallet` to keep the payment choice, or follow the tool's wallet rules to change it. Confirm the cart or explain what to change.
The user declined the payment approval. What should I do next: change something, continue, or stop?
The user declined sign-in consent. What should I do next: change something, continue, or stop?
runtime.lockruntime_resume_boot_verdictroot_agent_resume_failedruntime_root_agent_resumeruntime_restart_recoveryagent_resumeruntime_root_agent_resume_succeededguacamole_26b_safety_cronpolicyguard-nvfp4-cronfirst-boot maintenance claim changedfirst-boot maintenance workspace changedwhen_in_useNo phone is available to watch places. A useful offer may explain what connecting one would make possible.
cannot watch placescould watch places once background location is allowed; it is not yetcan watch places: background location is allowedPhone access could not be checked. Do not assume the user needs to change anything.
