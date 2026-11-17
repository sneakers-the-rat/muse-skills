# Purchases and Payments

Use the relevant shopping or booking skill to select the route. Direct
integrations retain their own checkout and approval contract. For a live
website, assign the work through `browser.browse`; the browser's checkout
workflow owns cart review, payment choice, approval, submission and verification.

<!-- purchase-preapproval-only:start -->
## Payment preapproval

For browser purchase preapproval, follow
`~/docs/chat/browser-purchase-preapproval.md` before preparing checkout.
Use `binding.wallet` only for an explicit wallet preference when requesting purchase preapproval.
<!-- purchase-preapproval-only:end -->

## Wallet readiness

Use `wallet.list_payment_methods` to check readiness; a connection alone does
not prove a usable payment method. Follow the Wallet tool's instructions to
choose and present one secure setup action. Keep shopping and retain details
<!-- personal-muse-only:start -->the user supplies<!-- personal-muse-only:end --><!-- group-muse-only:start -->members supply<!-- group-muse-only:end --> while setup is pending.
If a provider is unavailable, do not select it or offer setup; follow the
unsupported-method guidance below.

After setup, list the methods again. Continue the same browser task, answering
its waiting question with `answer_to` when present. Include the details supplied
while waiting. Pass `wallet` only for an explicit provider or method preference,
as below. For direct checkout, resume through its connector's instructions.

## Assign the purchase

Include the requested stage, whether research, cart preparation or purchase,
with the exact items, variants, quantities, exclusions and known checkout
details. Preserve the<!-- personal-muse-only:start --> user's named<!-- personal-muse-only:end --> merchant and payment preference<!-- group-muse-only:start --> a member named<!-- group-muse-only:end -->. Do not
invent contact details, addresses, currency codes or product substitutions. A
saved preference resolves a choice only when it identifies one supported value.

Before asking for a missing name, email or phone, call `wallet.get_user_info`
for the selected or connected wallet, when one is available. Before asking for
a delivery address, call `wallet.list_shipping_addresses` for that wallet.
Use a sole or default value when it fits the <!-- personal-muse-only:start -->user's<!-- personal-muse-only:end --><!-- group-muse-only:start -->member's<!-- group-muse-only:end --> request; ask only when the
choice remains ambiguous or the information is unavailable. Pass the relevant
details to the browser task. For a connector's checkout or a `poppy` order,
look details up the same way and use available ones without asking <!-- personal-muse-only:start -->the user<!-- personal-muse-only:end --><!-- group-muse-only:start -->a member<!-- group-muse-only:end --> to
supply them again; keep any confirmation that connector's checkout
instructions require. Wallet profile details do not identify which merchant
account to sign in to.

Continue the existing task for its cart and checkout. Use a new task for
separate work, checking `browser.windows` when necessary. Tell the worker about
earlier refusals and uncertain outcomes. Different profiles can still share a
merchant's server-side account cart; do not initiate overlapping purchases of
the same cart or use another task to bypass an unresolved order.

Sign in when a login for the merchant is available, use guest checkout
otherwise, and create an account only when the checkout offers neither.
Decline optional memberships, subscriptions and other extras nobody asked for.

## Cart and payment decisions

The checkout workflow collects the merchant, final items, seller, variants,
quantities, contact and destination, shipping option/cost/delivery estimate,
taxes, fees, exact currency/total, payment method and material commitments.
It returns the verified cart and unresolved shopping choices through the
browser task to this conversation. Payment authorization uses the
payment interface. For preparation only, it must stop before purchasing. A request to buy remains unfinished
until the submitted order is verified.

A browser checkout asks you to review the cart before an agent submits it.
<!-- personal-muse-only:start -->
A takeover checkout returns the prepared cart and remaining steps in its final
report for the user to complete. For a cart-review question, check against what the
user asked for: items, variants, quantities, sizes, delivery, dates, addresses,
cancellation terms, conditional charges, recurring obligations and any price
or store limits. Reply with `browser.browse`, setting `answer_to` to the
question's `question_id` and writing your answer in `task`. Confirm the cart
or explain exactly what to change; the checkout makes the change and asks
again when needed. Settle a difference the request leaves open with the
closest match to what the user asked for, and tell them what you chose when
it changes what they get. Ask the user only for a decision outside their
<!-- personal-muse-only:end -->
<!-- group-muse-only:start -->
For a cart-review question, check against what the member asked for: items,
variants, quantities, sizes, delivery, dates, addresses, cancellation terms,
conditional charges, recurring obligations and any price or store limits.
Reply with `browser.browse`, setting `answer_to` to the question's
`question_id` and writing your answer in `task`. Confirm the cart or explain
exactly what to change; the checkout makes the change and asks again when
needed. Settle a difference the request leaves open with the closest match
to what the member asked for, and tell the group what you chose when it
changes what they get. Ask the group only for a decision outside the
<!-- group-muse-only:end -->
request, such as a new commitment, and send <!-- personal-muse-only:start -->their<!-- personal-muse-only:end --><!-- group-muse-only:start -->the<!-- group-muse-only:end --> answer the same way.
<!-- personal-muse-only:start -->
No user can answer in scheduled or proactive work or in a task a web artifact
started. There, tell the browser to leave the purchase unfinished when it
needs a decision outside the request, and name the open choice in your final
message. The payment choice carries over unless you change it with `wallet`
as below. Payments require the user's checkout approval unless an existing
approval or provider policy covers the purchase.
<!-- personal-muse-only:end -->
<!-- group-muse-only:start -->
No member can answer in scheduled or proactive work or in a task a web
artifact started. There, tell the browser to leave the purchase unfinished
when it needs a decision outside the request, and name the open choice in
your final message. The payment choice carries over unless you change it
with `wallet` as below. Payments require a member's approval in the group
unless an existing approval or provider policy covers the purchase.
<!-- group-muse-only:end -->

Naming a wallet in `task` does not select it. For a purchase without preapproval,
set `wallet` in `browser.browse` <!-- personal-muse-only:start -->for an explicit wallet provider preference from the user, including a preference
in memory or their shopping profile, only when that provider is available.
When they name only a provider, pass just
`provider`, including when answering a browser question. The runtime selects a payment method and handles any required payment approval. Do not ask for a card choice in chat before
proceeding. Payment approval lets the user choose among the selected wallet's
payment methods. Without preapproval, change providers through `browser.browse.wallet`; checkout
must prepare payment approval for that provider.
<!-- personal-muse-only:end -->
<!-- group-muse-only:start -->
for an explicit wallet provider preference from a member, including a
preference in memory, only when that provider is available. When they name
only a provider, pass just `provider`, including when answering a browser
question. The runtime selects a payment method and handles any required
payment approval. Do not ask for a card choice in the group before
proceeding. Without preapproval, change providers through `browser.browse.wallet`;
checkout must prepare payment approval for that provider.
<!-- group-muse-only:end -->

<!-- personal-muse-only:start -->
For a purchase without preapproval, when the user chose a particular payment method, include its exact `payment_method_id`
from `wallet.list_payment_methods` in `wallet` and name its returned label in
`task`. Do not reproduce the payment sheet as another chat approval.
When the user prefers a method saved by the merchant, include that preference
in the task. For a new task, leave `wallet` unset; to change an existing payment
choice, use `wallet: null`. Without an explicit wallet preference, omit `wallet`
and leave payment out of `task`. Checkout pays with a method saved by the
merchant before a connected wallet, and handles payment approval.
When the user requests a method Wallet cannot supply, such as Apple Pay
or Google Pay, offer Wallet first: the usable connected wallet, or one secure
setup action. Assign takeover only after the user declines Wallet or the browser
reports that Wallet cannot pay this checkout. When you assign takeover, preserve
the requested method in the task. The browser prepares checkout and returns the
remaining steps for the user to complete.
<!-- personal-muse-only:end -->
<!-- group-muse-only:start -->
For a purchase without preapproval, when a member chose a particular payment
method, include its exact
`payment_method_id` from `wallet.list_payment_methods` in `wallet` and name its
returned label in `task`. Do not reproduce the payment approval as another
message in the group. When members prefer a method saved by the merchant,
include that preference in the task. For a new task, leave `wallet` unset; to
change an existing payment choice, use `wallet: null`. Without an explicit
wallet preference, omit `wallet` and leave payment out of `task`. Checkout pays
with a method saved by the merchant before a connected wallet, and handles
payment approval. When a member requests a method Wallet cannot
supply, such as Apple Pay or Google Pay, offer Wallet first: the usable
connected wallet, or one secure setup action. Nobody can take over this
browser to pay, so when members decline Wallet or the browser reports that
Wallet cannot pay this checkout, tell the group the purchase can't be paid
from here and post the merchant's link so a member can buy it themselves.
<!-- group-muse-only:end -->

The result's `card_picked` names the payment method approved in that interface,
including when funding failed. Use that identity when explaining a failure;
it may differ from the method you proposed. It does not prove a charge or an order.

Updates and answers keep the current payment choice when
you omit `wallet`, including a method picked in payment approval. When changing
how to pay, use a wallet object to change the provider or payment-method choice, or `wallet: null`
to switch to a merchant-saved method<!-- personal-muse-only:start --> or browser takeover<!-- personal-muse-only:end -->. Renew a preapproval
before changing its bound wallet preference; an unbound approval needs no renewal.

A merchant logo does not prove that a route is supported. Preserve an exact
<!-- personal-muse-only:start -->user choice<!-- personal-muse-only:end --><!-- group-muse-only:start -->choice a member made<!-- group-muse-only:end -->; do not silently replace it with a default. When the workflow
reports missing information, provide already established values together or
present its remaining secure action.

Send a Wallet setup offer on its own, <!-- personal-muse-only:start -->except for a saved-card CVV choice on a
purchase without preapproval<!-- personal-muse-only:end --><!-- group-muse-only:start -->without another way to pay<!-- group-muse-only:end -->. Suggest
<!-- personal-muse-only:start -->
another way to pay for that CVV choice or after the user declines setup, the wallet
connection fails, the wallet refuses payment or is over its spend limit, the
wallet integration does not support this checkout, the merchant declines the
card, or the checkout takes no card entry. When wallet payment has definitively failed or cannot pay this checkout,
ask the user about another wallet or offer browser takeover. The checkout uses
`payment_route: takeover` to prepare checkout as far as the assigned details
allow. It then returns the prepared cart and remaining steps through its final
report. Offer the user the live browser to enter payment and complete the
order. After they complete payment and return control, continue the same task with `wallet: null` to
verify the merchant's outcome. While a payment is pending or its outcome is unknown,
wait for it to settle before suggesting another way. With no user to ask, as
in scheduled work, report the blocked payment in your final message.
<!-- personal-muse-only:end -->
<!-- group-muse-only:start -->
another way to pay only after members decline setup, the wallet connection
fails, the wallet refuses payment or is over its spend limit, the wallet
integration does not support this checkout, the merchant declines the card,
or the checkout takes no card entry. When wallet payment has definitively
failed or cannot pay this checkout, ask the group about another wallet.
Nobody can take over this browser to enter payment, so when no wallet can
pay, tell the group the purchase can't be paid from here and post the
merchant's link so a member can buy it themselves. While a payment is
pending or its outcome is unknown, wait for it to settle before suggesting
another way. With no member to ask, as in scheduled work, report the blocked
payment in your final message.
<!-- group-muse-only:end -->

<!-- personal-muse-only:start -->
Never request, repeat, store or forward card numbers or CVVs in chat. For CVV entry, have the user take over, complete verification and leave the CVV page before handing back. Resume the same task with `wallet: null` to verify an order they placed or finish with `merchant_saved`. Wallet provides secure access to cards; its issued credentials stay in checkout.
<!-- personal-muse-only:end -->
<!-- group-muse-only:start -->
Do not request card numbers or CVVs in the group or repeat, store, or forward
numbers a member sends there. When a saved card needs its CVV, nobody can take
over this browser to enter it, so pay with a connected wallet. A member can
securely give Muse access to a card through Wallet; its issued credentials
stay in checkout.
<!-- group-muse-only:end -->

<!-- personal-muse-only:start -->
A wallet connection, method selection, cart review, completed login or return
of browser control does not itself authorize spending. For a preapproved purchase, the checkout agent selects a usable saved card or a connected wallet under its checkout instructions. Other purchases require checkout approval unless provider policy covers them.
<!-- personal-muse-only:end -->
<!-- group-muse-only:start -->
A wallet connection, method selection, cart review or completed login does
not itself authorize spending. For a preapproved purchase, the checkout agent
selects a usable saved card or a connected wallet under its checkout
instructions. Other purchases require a member's approval in the group unless
provider policy covers them.
<!-- group-muse-only:end -->
The payment <!-- personal-muse-only:start -->sheet<!-- personal-muse-only:end --><!-- group-muse-only:start -->approval<!-- group-muse-only:end --> owns provider disclosures and final consent. Funding
allowance is not permission to raise the purchase total.

## Changes and uncertain outcomes

An approval covers every page of the checkout while the currency stays the
same and both the total and any conditional charge stay within their approved
amounts; the payment service checks those. Changing an issued Link card's
charge cutoff, earlier or later, requires replacement funding. Let the checkout
verify the prior order's outcome and recover funding before retrying.
If it requires purchase renewal, renew the same `purchase_id` through
`~/docs/chat/browser-purchase-preapproval.md`. When items, variants or quantities
change, or delivery, dates, addresses, cancellation terms or other obligations
materially change, the checkout asks you to check the cart again through the
same cart-confirmation handoff. Resolve the change within the <!-- personal-muse-only:start -->user's<!-- personal-muse-only:end --><!-- group-muse-only:start -->member's<!-- group-muse-only:end --> request
yourself, and ask the <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->group<!-- group-muse-only:end --> only for a decision outside it. A price within the
approved total does not authorize a new commitment.

Follow the workflow's pending decision, secure action or reconciliation state.
It resumes automatically. An approval or successful input is not evidence of
an order. Report only the verified outcome and the returned label of the method
actually used. Write masked cards as `Visa ....1234`.

When the browser reports that an order was submitted but not yet confirmed,
<!-- personal-muse-only:start -->
tell the user the order was submitted, the merchant has not confirmed it yet,
and you will check again shortly. Schedule that check yourself as one `cron.add` job
with `kind=runonce` about 10 minutes out; the user's purchase request already
covers it, so do not ask first. Write the job as a reminder for this chat that
names the browser task ID, the merchant, the total and when the order was
submitted, and that does not open the merchant's website itself. When the
reminder arrives, continue that browser task with `browser.browse` and ask it
to find the order. If the order is still unconfirmed, tell the user what you
found and schedule one final check about 30 minutes later the same way, saying
in the reminder that it is the final check. When the final check still finds no
confirmation, do not schedule another; tell the user they can look for the
merchant's confirmation in their email or in their account on the merchant's
site. Do not submit the order again while its outcome is unknown.
<!-- personal-muse-only:end -->
<!-- group-muse-only:start -->
tell the group the order was submitted, the merchant has not confirmed it
yet, and you will check again shortly. Schedule that check yourself as one
`cron.add` job with `kind=runonce` about 10 minutes out; the member's
purchase request already covers it, so do not ask first. Write the job as a
reminder for this chat that names the browser task ID, the merchant, the
total and when the order was submitted, and that does not open the
merchant's website itself. When the reminder arrives, continue that browser
task with `browser.browse` and ask it to find the order. If the order is
still unconfirmed, tell the group what you found and schedule one final
check about 30 minutes later the same way, saying in the reminder that it is
the final check. When the final check still finds no confirmation, do not
schedule another; tell the group to look for the merchant's confirmation in
the email or merchant account the order used. Do not submit the order again
while its outcome is unknown.
<!-- group-muse-only:end -->

When the browser asks how to proceed after a payment approval decline, ask
<!-- personal-muse-only:start -->
whether the user wants to change something, continue, or stop, unless they
<!-- personal-muse-only:end -->
<!-- group-muse-only:start -->
the group whether to change something, continue, or stop, unless members
<!-- group-muse-only:end -->
already gave direction after <!-- personal-muse-only:start -->declining<!-- personal-muse-only:end --><!-- group-muse-only:start -->the decline<!-- group-muse-only:end -->. Answer the pending question with
`browser.browse` and its `answer_to` so the same specialist can continue or
stop. <!-- personal-muse-only:start -->Their reply<!-- personal-muse-only:end --><!-- group-muse-only:start -->The answer<!-- group-muse-only:end --> does not replace payment approval. If the browser instead
reports that the checkout ended with a decline, tell the <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->group<!-- group-muse-only:end --> that attempt
<!-- personal-muse-only:start -->
did not place an order. When the merchant declines the card, tell the user
and suggest taking over the browser to pay another way, as above. Do not
retry or switch methods on your own. When an earlier order may have gone
through, find out before it is submitted again.
<!-- personal-muse-only:end -->
<!-- group-muse-only:start -->
did not place an order. When the merchant declines the card, tell the group
and offer another wallet, or say the purchase can't be paid from here, as
above. Do not retry or switch methods on your own. When an earlier order
may have gone through, find out before it is submitted again.
<!-- group-muse-only:end -->
Payment cancellation, release of a hold, order cancellation and refund are
distinct operations.

Read `~/docs/payments-and-purchases.md` for wallet limits, provider
protections, refunds and other payment capabilities.
