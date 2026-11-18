Your previous review did not satisfy the decision contract. Nothing has been sent. Review the same evidence and call `submit_connection_review` once with a corrected decision.

This conversation has no stored rules, so send no rule IDs with any decision. `allow` means everything the send reveals is already known to the company and it commits the <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->group<!-- group-muse-only:end --> to nothing new. `nothing_shared` needs a reason and applies only when the send conveys nothing about the <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->group, its members<!-- group-muse-only:end --> or anyone else. `ask_user` needs a reason naming the new detail or commitment; the message then waits for <!-- personal-muse-only:start -->the user's decision<!-- personal-muse-only:end --><!-- group-muse-only:start -->a member's decision in the group<!-- group-muse-only:end -->. `deny` needs a brief reason and applies only to a draft that accepts an Operations proposal, contains a lie or cover story, or that <!-- personal-muse-only:start -->the user's<!-- personal-muse-only:end --><!-- group-muse-only:start -->members'<!-- group-muse-only:end --> later messages refused. Optional `text`, only with `allow` or `nothing_shared`, is the complete revised message.
historythe main Muse, in its own words; not the user's words or approvalUser's taskUser's later messagesOwner in this conversationthe main Muse, in its own words; not a member's words or approvalMembers' later messagesMember in this conversationMembers' messagesConversationparticipant_identitiesParticipant identitiesturn_originTurn originpolicy_revisionSharing rules revisionowner_requestowner_later_messagesowner_in_chatowner_messageschat_summaryConversation notesRecent worker historyfinal_responseproposed_reactionProposed reactionshared_itemShared itemshared_accessShared accessshared_filesShared filesshared_item_filesShared item filesattached_imagesAttached imagesattached_filesAttached filesconnection review evidence must be an objectintegrationsupporteddefinitivelastingweb_disabledsite offers no personal agent protocolpersonal agent protocol probe could not read the sitepersonal agent protocol probe printed no answerdiscoverydiscovery_completeworkspace/your_files/workspace/your_filesdisconnected_subjectInternal delivery event: {disconnected_subject} has been disconnected.
<!-- personal-muse-only:start -->The user disconnected this provider or account from settings.
Reply with<!-- personal-muse-only:end --><!-- group-muse-only:start -->It no longer serves the group.
Tell the group in<!-- group-muse-only:end --> one concise sentence <!-- personal-muse-only:start -->confirming the disconnection<!-- personal-muse-only:end --><!-- group-muse-only:start -->that it is disconnected<!-- group-muse-only:end -->.
Do not attempt to reconnect or call tools.
provider_labelconnected_subjectInternal delivery event: {connected_subject} is now connected and ready to use<!-- group-muse-only:start -->. A member connected it, and it now serves the whole group<!-- group-muse-only:end -->.

The connection is complete. Do not ask <!-- personal-muse-only:start -->the user to repeat it or<!-- personal-muse-only:end --><!-- group-muse-only:start -->members to connect it again or to<!-- group-muse-only:end --> provide credentials<!-- personal-muse-only:start --> again<!-- personal-muse-only:end -->.

If recent context shows unfinished work that requires {provider_label}, continue it now. Connecting an account is not a request to buy, so continue a purchase only when <!-- personal-muse-only:start -->the user asked you to buy it and has not asked you to wait since<!-- personal-muse-only:end --><!-- group-muse-only:start -->a member asked you to buy it and no member has asked you to wait since<!-- group-muse-only:end -->. When you continue a purchase that was awaiting this wallet, call `wallet.list_payment_methods` and follow its setup guidance if no usable method is available. Then resume the same browser task, answering its waiting question with `answer_to` when present, or continue direct checkout through its connector's instructions. Complete every step that does not require <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->a member's<!-- group-muse-only:end --> input before replying. Do not call `wallet.get_connection_status`.

For any other purchase, such as one the <!-- personal-muse-only:start -->user is<!-- personal-muse-only:end --><!-- group-muse-only:start -->group is<!-- group-muse-only:end --> still choosing or comparing, do not start or resume checkout. Confirm the connection and ask whether to go ahead.

<!-- personal-muse-only:start -->Present the update<!-- personal-muse-only:end --><!-- group-muse-only:start -->Announce the connection in the group thread<!-- group-muse-only:end --> as a natural continuation of the current conversation. Do not copy this event verbatim. When unfinished work exists, lead with its useful result or the one next action the <!-- personal-muse-only:start -->user needs. When you continue a purchase, make clear that nothing is charged until the user approves the payment, unless an existing approval or provider policy covers it. Include a brief connection confirmation<!-- personal-muse-only:end --><!-- group-muse-only:start -->group needs. When you continue a purchase, make clear that nothing is charged until a member approves the payment, unless an existing approval or provider policy covers it. Include the announcement<!-- group-muse-only:end --> in the same message. Do not mention this event, a handoff, instruction sections, tool names, or connection checks.

If no unfinished work requires {provider_label}, <!-- personal-muse-only:start -->confirm the connection in one short sentence<!-- personal-muse-only:end --><!-- group-muse-only:start -->announce in one short sentence that it is connected for the group,<!-- group-muse-only:end --> and stop. Do not call a tool only to recheck the connection.
Internal delivery event: The connection flow for {provider_label} did not complete. Reason: {reason} Tell the <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->group<!-- group-muse-only:end --> concisely that the connection did not complete<!-- personal-muse-only:start -->. When a browser purchase is waiting on {provider_label}, also suggest that they take over the browser to pay there, then hand control back<!-- personal-muse-only:end --><!-- group-muse-only:start -->, and offer to post a new link so a member can try again<!-- group-muse-only:end -->.
Internal delivery event: {provider_label} is now connected <!-- group-muse-only:start -->for the group <!-- group-muse-only:end -->and its credential is stored. <!-- personal-muse-only:start -->The provider is already connected, so do<!-- personal-muse-only:end --><!-- group-muse-only:start -->Do<!-- group-muse-only:end --> not ask <!-- personal-muse-only:start -->the user<!-- personal-muse-only:end --><!-- group-muse-only:start -->members<!-- group-muse-only:end --> to connect, link, authorize, set up, or provide credentials again. Open with a short, celebratory <!-- personal-muse-only:start -->confirmation<!-- personal-muse-only:end --><!-- group-muse-only:start -->announcement in the group<!-- group-muse-only:end --> that {provider_label} is connected (one sentence, plain language).

The stored credential is not a readable secret: it reaches a request through a surrogate exchange with authd, and a request that skips that exchange goes out unauthenticated. Call this API from a connector doc you author with `custom_connector_setup`.

If recent context shows a pending task that needs {provider_label}, use that connector doc to finish the task now, authoring it first if the provider has none yet. Otherwise <!-- personal-muse-only:start -->briefly ask what they want to do next<!-- personal-muse-only:end --><!-- group-muse-only:start -->stop after the announcement<!-- group-muse-only:end -->.
Internal delivery event: <!-- personal-muse-only:start -->the user submitted the Secure Vault form<!-- personal-muse-only:end --><!-- group-muse-only:start -->a member entered a login on the secure page linked in the group<!-- group-muse-only:end -->, and the login credentials are saved.

No browser task is waiting for this login. A browser task that asked for it while still working signs in with it on its own.
Confirm in one short sentence that the login is saved.
<!-- personal-muse-only:start -->Ask the user<!-- personal-muse-only:end --><!-- group-muse-only:start -->Only ask the group<!-- group-muse-only:end --> for this login again<!-- personal-muse-only:start --> only<!-- personal-muse-only:end --> when the site rejects the saved one.
Internal delivery event: the user granted Muse permission to use a login from their 1Password vault. We saved that permission. No username or password was exposed to the model or saved as part of this capture.

No browser task is waiting for this login. A browser task that asked for it while still working signs in with it on its own.
Confirm in one short sentence that the 1Password permission is saved.
Ask the user for this login again only when the site rejects the saved login.
Internal delivery event: <!-- personal-muse-only:start -->the user submitted the Secure Vault form<!-- personal-muse-only:end --><!-- group-muse-only:start -->a member entered a login on the secure page linked in the group<!-- group-muse-only:end -->, and the login credentials are saved.

Resume the browser task that asked for this login with `browser.browse`.
Set `task_id` to `{browser_task_id}`.
The handoff and `browser.windows` identify the existing task. The waiting task shows status `needs_user`.
In `task`, tell it the login is saved, to sign in with the saved login, and to continue its original assignment. Do not restate its brief.
Continue the existing task. A new task loses the page state and the credential authorization, and it asks the <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->group<!-- group-muse-only:end --> for the login again.
When `browser.browse` accepts the instruction, tell the <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->group<!-- group-muse-only:end --> in one short sentence that the login is saved and the task is continuing.
When it does not accept the instruction, tell the <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->group<!-- group-muse-only:end --> the login is saved and the task did not continue, with the reason the result gives.
When no browser task is waiting for this login and <!-- personal-muse-only:start -->the user<!-- personal-muse-only:end --><!-- group-muse-only:start -->a member<!-- group-muse-only:end --> asked for something that needed it, carry that request out now. If it needs the browser, start it with `browser.browse` and `task_id: "new"`, and tell the task the login is saved and to sign in with it.
When nothing in the conversation is waiting on this login, confirm in one sentence that the <!-- personal-muse-only:start -->credentials are<!-- personal-muse-only:end --><!-- group-muse-only:start -->login is<!-- group-muse-only:end --> saved and stop.
<!-- personal-muse-only:start -->Ask the user<!-- personal-muse-only:end --><!-- group-muse-only:start -->Only ask the group<!-- group-muse-only:end --> for this login again<!-- personal-muse-only:start --> only<!-- personal-muse-only:end --> when the site rejects the saved one.
Internal delivery event: the user granted Muse permission to use a login from their 1Password vault. We saved that permission. No username or password was exposed to the model or saved as part of this capture.

Resume the browser task that asked for this login with `browser.browse`.
Set `task_id` to `{browser_task_id}`.
The handoff and `browser.windows` identify the existing task. The waiting task shows status `needs_user`.
In `task`, tell it the 1Password permission is saved, to sign in with the saved 1Password login, and to continue its original assignment. Do not restate its brief.
Continue the existing task. A new task loses the page state and the credential authorization, and it asks the user for the login again.
When `browser.browse` accepts the instruction, tell the user in one short sentence that the 1Password permission is saved and the task is continuing.
When it does not accept the instruction, tell the user the 1Password permission is saved and the task did not continue, with the reason the result gives.
When no browser task is waiting for this login and the user asked for something that needed it, carry that request out now. If it needs the browser, start it with `browser.browse` and `task_id: "new"`, and tell the task the 1Password permission is saved and to sign in with the saved 1Password login.
When nothing in the conversation is waiting on this login, confirm in one sentence that the 1Password permission is saved and stop.
Ask the user for this login again only when the site rejects the saved login.
browser_task_idInternal delivery event: {provider_label} has been disconnected from Muse and the integration has been removed from Ring.
Reply with one concise sentence confirming the disconnection.
Do not attempt to reconnect or call tools.
Internal delivery event: The {provider_label} connection saved the key <!-- personal-muse-only:start -->the user<!-- personal-muse-only:end --><!-- group-muse-only:start -->a member<!-- group-muse-only:end --> provided, but could not verify it with the provider yet, so it is connected <!-- group-muse-only:start -->for the group <!-- group-muse-only:end -->with verification pending. In one or two concise sentences, <!-- personal-muse-only:start -->let the user know<!-- personal-muse-only:end --><!-- group-muse-only:start -->tell the group<!-- group-muse-only:end --> it is set up<!-- personal-muse-only:start --> and<!-- personal-muse-only:end --><!-- group-muse-only:start -->,<!-- group-muse-only:end --> that the first real use will confirm the key<!-- personal-muse-only:start --> — and that<!-- personal-muse-only:end --><!-- group-muse-only:start -->, and that a member can enter the key again from a new link<!-- group-muse-only:end --> if that use fails with an authentication error<!-- personal-muse-only:start -->, they should re-enter the key<!-- personal-muse-only:end -->. Do not call tools.
Get updates from this tasknotification_opt_in.card.bodyText under the title of a chat card offering to turn on notifications after the user schedules a taskGet notified when this is donenotification_opt_in.card.body_long_runningText under the title of a chat card offering to turn on notifications when the assistant starts a task that takes a few minutes, such as browsing a websiteNotificationsnotification_opt_in.card.titleTitle of a chat card offering to turn on notifications for a taskEnablenotification_opt_in.card.buttonButton on a chat card that asks for permission to send notifications about a taskEnablednotification_opt_in.card.enabled_buttonDisabled button on a chat card about a task, shown once notifications are onThis artifact's share status couldn't be updated. Please try again later.internal_error_share_rate_limit_cooldownprovider did not confirm delivery after dispatch claimidea activation notice chat owner missingidea activation notice target missingapproval iddestinationout-of-credits delivery idout-of-credits-replyidea activation notice ididea-activation-noticechat publication requires its canonical assistant message idchat effect owner mismatchunsupported chat publication parametersis_final_chunkchunk_index/connect/oauthservicecredentialYour cartshopping.cart.titleTitle of a saved shopping cart snapshotStart checkoutshopping.cart.start_checkoutButton in an expanded shopping cart that asks the assistant to help check out the cart. Final order approval is still required.wallet checkout contract has an invalid merchant URLwallet checkout contract must contain exactly one selected payment optionwallet checkout contract has an invalid payment method labelwallet checkout contract has an invalid card brandwallet checkout contract has an invalid card suffixwallet checkout contract has an invalid currencywallet checkout contract has an invalid purchase amountwallet checkout contract has an invalid amount or currencybrowser checkout approval has no wallet contractbrowser checkout preview is missing its typed presentationfollow_up_root_turnlayoutcollectionConnect your professional accounts to continue with this request.connector.professional_consent.connect_accountsPrompt shown after a professional business tool requires consent to access the user's professional accountsgoals cursor does not match the requested collectionlimit must be greater than zerovaluestill_sizeimage_encodeimage_decodeimage_orientationimage_formathost_musethumbnail_urlSTEFI refused the peer connections reporthatch:shared-message:v1readoptedalready_ownerowned_elsewhereendingowner_unknownother_clientvoice_call_owner_followI'm sorry, but I couldn't show my new look on this call.voice.call.live_avatar_failedSpoken on a voice call when a requested avatar change could not be shown liveThis is my new voice.voice.call.live_voice_updatedSpoken in the new voice when a voice change landed on a call that already heard an avatar failure lineMy new look can't be shown live, so I'll keep this one on the call.voice.call.live_avatar_not_animatableSpoken on a voice call when the chosen avatar cannot be animated liveThis is my new voice, but I couldn't show my new look on this call.voice.call.live_voice_updated_avatar_failedSpoken in the new voice when a voice change landed but the avatar change in the same update failedI couldn't confirm the voice change just now.voice.call.switch_failedSpoken when a requested voice change fails during the same active callThat voice change didn't go through.voice.call.switch_refusedSpoken when a requested voice change during an active call definitely did not happenI couldn't confirm whether the voice changed.voice.call.switch_unconfirmedSpoken when a requested voice change during an active call could not be confirmedconsent_versionconsent_granted_at__integration_keyadaptermessenger_readhttps://agent.meta.ai/settings/connectorsauth_intent/connect/threads_messagesresolved Hatch URL is valid/connectors/connect/whatsapp_business/connect/instagram_messages/connectors/connect/whatsapp/connect/messenger_companionoperation/result/continuation_urlauthorize_urlconnectreauthConnectorSkillManifestFilegatingconsent_screenmanifest.yamlmanifest.ymlfailed to parse connector manifest; consent screen omittedmeta_catalog_searchversion: 1
metadata:
  visible_in_settings: true
auth: none
connector: meta_catalog_search
category: social
display_name: Shopping search
description: Enable Muse shopping with faster results and more choice
icon: meta_catalog_search
actions:
  read:
    default: allow
    label: Read permissions
    methods:
      catalog.search:
        label: Search
        approval_phrase: search Meta's product catalog
consent_screen:
  bullets:
    - icon: info
      title: "You choose what Muse can do"
      text: "By default, Muse will ask before taking actions it thinks need review. Disconnect at any time in Settings."
    - icon: caution
      title: "Keep an eye on things"
      text: "Muse may take unexpected actions. Monitor it carefully."
  callout_title: "Non-confidential connector"
  footer_paragraphs:
    - text: "Shopping search works by connecting through Meta, which means the info exchanged will be visible to Meta. [Learn more](https://muse.ai/privacy)"
      variants:
        confidential_vm:
          text: "Shopping search works by connecting through Meta, which means the info exchanged will be visible to Meta. [Learn more](https://muse.ai/privacy)"
          placement: callout
    - text: "Muse will exchange info with Meta. To learn more, view Meta's [terms](https://www.facebook.com/legal/terms) and [privacy policy](https://www.facebook.com/privacy/policy/)."
version: 1
metadata:
  visible_in_settings: true
auth:
  provider: shop-pay
  required: true
connector: shop-pay
category: wallet
display_name: Shop Pay
icon: shop_pay
description: Make secure purchases across millions of stores
actions:
  write:
    default: ask
    label: Write and delete permissions
    methods:
      payment_approval.create:
        approval_policy: dedicated_consent
        # Shop Pay uses the same delegated-spend permission shape as Stripe
        # Link: only spend creation is user-managed. Wallet reads use the
        # connected credential, payment-method management returns a
        # provider-hosted interaction, and cancellation only releases an
        # existing approval.
        label: Create spend requests
        approval_phrase: approve a payment from your Shop Pay wallet
commands:
  auth.start: null
  auth.inspect: null
  auth.userinfo: null
  payment_methods.list: null
  payment_methods.add: null
  shipping_addresses.list: null
  checkout-approve: payment_approval.create
  browser-native-checkout-prepare: null
  browser-native-checkout-create-approved: payment_approval.create
  browser-native-checkout-cancel: null
  browser-card-checkout-prepare: null
  browser-card-checkout-create-approved: payment_approval.create
  browser-card-checkout-retrieve: null

consent_screen:
  bullets:
    - icon: data_types
      title: "Level up with Shop Pay"
      text: "Muse will access things like the last four digits of your credit card and your shipping address. Muse cannot access your full credit card details."
    - icon: info
      title: "You choose what Muse can do"
      text: "By default, Muse will ask before taking actions it thinks need review. Disconnect at any time in Settings."
    - icon: caution
      title: "Keep an eye on things"
      text: "Muse may take unexpected actions. Monitor it carefully."
  footer_paragraphs:
    - "The info used for your tasks is part of your interactions with Muse, which we may use to improve AI at Meta. You can manage this in Settings. [Learn more](https://www.facebook.com/privacy/genai/)"
    - "Muse will exchange info with Shop Pay. To learn more, view Shopify's [terms](https://www.shopify.com/legal/terms) and [privacy policy](https://www.shopify.com/legal/privacy)."
version: 1
metadata:
  visible_in_settings: true
auth:
  provider: onepassword
  required: true
cli:
  binary: onepassword
  skill: onepassword
connector: onepassword
category: productivity
display_name: 1Password
description: Securely use your passwords and vault items. You’ll need the 1Password app installed on this device.
icon: onepassword
actions:
  read:
    default: allow
    label: Read information from 1Password
    response_guard: verification_codes
commands:
  authorize-url: null
consent_screen:
  bullets:
    - icon: data_types
      title: "Level up with 1Password"
      text: "Muse will use logins you choose to share."
    - icon: info
      title: "You choose what Muse can do"
      text: "By default, Muse will ask before taking actions it thinks need review. Disconnect at any time in Settings."
    - icon: caution
      title: "Keep an eye on things"
      text: "Muse may take unexpected actions. Monitor it carefully."
  footer_paragraphs:
    - "The info used for your tasks is part of your interactions with Muse, which we may use to improve AI at Meta. You can manage this in Settings. [Learn more](https://muse.ai/privacy)"
    - "Muse will exchange info with 1Password. To learn more, view their [terms](https://1password.com/legal/terms-of-service) and [privacy policy](https://1password.com/legal/privacy)."
version: 1
metadata:
  visible_in_settings: true
auth:
  provider: paypal
  required: true
connector: paypal
category: wallet
display_name: PayPal
description: Make secure payments and purchases
icon: paypal
cli:
  binary: paypal
  skill: paypal
request_quota:
  workers:
    - paypal
actions:
  read:
    default: allow
    label: Read your PayPal identity
    response_guard: verification_codes
  write:
    default: ask
    label: Approve a PayPal checkout
    methods:
      approval_token.create:
        approval_policy: dedicated_consent
        label: Approve a PayPal checkout
        approval_phrase: approve a payment from your PayPal wallet
      write:
        label: Report checkout outcomes
commands:
  auth.authorize-url: null
  auth.connect-page: null
  auth.status: null
  wallet.user-info: read
  auth.inspect: read
  auth.disconnect: null
  disconnect: null
  payment-options: read
  checkout: approval_token.create
  report: write
consent_screen:
  bullets:
    - icon: data_types
      title: "Level up with PayPal"
      text: "Muse will access things like account info."
    - icon: info
      title: "You choose what Muse can do"
      text: "By default, Muse will ask before taking actions it thinks need review. Disconnect at any time in Settings."
    - icon: caution
      title: "Keep an eye on things"
      text: "Muse may take unexpected actions. Monitor it carefully."
  footer_paragraphs:
    - "The info used for your tasks is part of your interactions with Muse, which we may use to improve AI at Meta. You can manage this in Settings. [Learn more](https://muse.ai/privacy)"
    - "Muse will exchange info with PayPal. To learn more, view their [terms](https://www.paypal.com/us/legalhub/useragreement-full) and [privacy policy](https://www.paypal.com/us/legalhub/privacy-full)."
version: 1
metadata:
  visible_in_settings: true
auth:
  provider: stripe-link
  required: true
connector: stripe-link
category: wallet
display_name: Link
icon: stripe
description: Make secure payments and protect your purchases
request_quota:
  mode: shadow
  workers:
    - stripe-link
    # The checkout-card restricted-socket worker family
    # (com.hatch.stripe-link-checkout-card@.service). Same connector target as
    # the primary worker, so this grants no extra quota. Without it the
    # restricted worker's cgroup resolves to no binding, making the request
    # UNCLASSIFIED -- and unclassified admission follows the fleet-default
    # Enforce manager mode (SentinelConnectorQuotaEnforcementEnabled), which
    # fails closed before any provider call. This connector-level shadow mode
    # only softens quota exceedance for requests that classify.
    - stripe-link-checkout-card
actions:
  read:
    default: allow
    label: Read permissions
    methods:
      financial_insights:
        label: Read transactions
        requires_capabilities:
          - financial_insights
  write:
    default: ask
    label: Write and delete permissions
    methods:
      spend_requests.create_delegated:
        approval_policy: dedicated_consent
        label: Create spend requests
      spend_requests.transfer_ownership:
        approval_policy: dedicated_consent
        label: Manage spend requests

consent_screen:
  bullets:
    - icon: data_types
      title: "Level up with Link by Stripe"
      text: "Muse will access things like the last four digits of your credit card and your address. It will automatically be updated with the latest information, so it can help you keep up with what’s important to you. Muse cannot access your full credit card details, account or routing numbers."
    - icon: info
      title: "You choose what Muse can do"
      text: "By default, Muse will ask before taking actions it thinks need review. Disconnect at any time in Settings."
    - icon: caution
      title: "Keep an eye on things"
      text: "Muse may take unexpected actions. Monitor it carefully."
  footer_paragraphs:
    - "The info used for your tasks is part of your interactions with Muse, which we may use to improve AI at Meta. You can manage this in Settings. [Learn more](https://www.facebook.com/privacy/genai/)"
    - "Muse will exchange info with Link by Stripe. To learn more, view their [terms](https://stripe.com/legal/link) and [privacy policy](https://stripe.com/privacy)."
tailscaleversion: 1
metadata:
  visible_in_settings: true
auth:
  provider: tailscale
  required: true
connector: tailscale
category: productivity
display_name: Tailscale
description: Securely connect to the devices on your private network
icon: tailscale
actions:
  auth:
    default: ask
    label: Join or leave a Tailscale network
    methods:
      tailscale.up:
        label: Join a Tailscale network
      # Split from tailscale.up because the argument decides WHOSE network
      # this device joins: a standing allow on the plain join must never
      # cover a join that hands the node to a different control server.
      # The manifest policy blocks persistent Allow. Task-scoped Allow also
      # requires a write action, so this auth method remains single-use-or-deny.
      tailscale.up_login_server:
        approval_policy: fresh_consent_or_task_allow
        label: Join via a custom control server
        approval_phrase: join a Tailscale network via a custom control server
      tailscale.down:
        label: Leave and forget this device
  read:
    default: allow
    label: Read Tailscale status
    methods:
      tailscale.status:
        label: Connection status and devices
        approval_phrase: view connection status and devices in Tailscale
      tailscale.ip:
        label: This device's Tailscale addresses
        approval_phrase: view this device's Tailscale addresses
commands:
  up: tailscale.up
  down: tailscale.down
  status: tailscale.status
  ip: tailscale.ip

consent_screen:
  bullets:
    - icon: data_types
      title: "Level up with Tailscale"
      text: "Muse will access things like device names and network addresses, and the data returned from your devices."
    - icon: info
      title: "You choose what Muse can do"
      text: "By default, Muse will ask before taking actions it thinks need review. Disconnect at any time in Settings."
    - icon: caution
      title: "Keep an eye on things"
      text: "Muse may take unexpected actions. Monitor it carefully."
  footer_paragraphs:
    - "The info used for your tasks is part of your interactions with Muse, which we may use to improve AI at Meta. You can manage this in Settings. [Learn more](https://www.facebook.com/privacy/genai/)"
    - "Muse will exchange info with Tailscale. To learn more, view their [terms](https://tailscale.com/terms) and [privacy policy](https://tailscale.com/privacy-policy)."
