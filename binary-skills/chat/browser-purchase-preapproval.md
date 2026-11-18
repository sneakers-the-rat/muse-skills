# Browser purchase preapproval

Use `permissions.preapprove` for one browser payment or order through an eligible
connected wallet card, including Link and Shop Pay,
or a payment method the merchant saved for the <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->group<!-- group-muse-only:end -->.
A connected wallet with a usable payment method is required even for merchant-saved
payment. Otherwise the tool returns `wallet_setup_required` with the setup step.
Send one action in `actions`, with `connector: "browser"` and the `binding` below.
A Shopify UCP checkout completed in this turn or cron run also pays under this
approval when its `checkout create`, `checkout get` or `checkout update` output
shows `payment.preapproved: true`. Other checkout integrations use their own
approval flow.

## Purchase contract

```
{
  intent: string,
  items: [{description: string, quantity: integer}],
  requirements: [string],
  shipping_address_ref?: string,
  shipping: string,
  merchant_policy: string,
  delegated_choices: [string],
  wallet?: {provider: string, payment_method_id?: string},
  max_total: {decimal: string, currency: string},
  expires_at?: string,
  purchase_id?: string
}
```

Put product and variant details in `items`, hard constraints in `requirements`,
delivery terms in `shipping`, allowed sellers in `merchant_policy`, and choices
<!-- personal-muse-only:start -->the user<!-- personal-muse-only:end --><!-- group-muse-only:start -->members<!-- group-muse-only:end --> delegated in `delegated_choices`. Use empty arrays when there are no
additional requirements or delegated choices. Use `shipping_address_ref` for
an established saved address; omit it when no delivery address is needed.
For a bill or fee, describe the payment in `items` with quantity 1 and state
that no delivery applies in `shipping`.

<!-- personal-muse-only:start -->
The card shows `intent` and the total cap. A scheduled purchase's card also shows
how long the approval lasts. Summarize the items, variants,
<!-- personal-muse-only:end -->
<!-- group-muse-only:start -->
The approval members see in the group shows `intent` and the total cap. A
scheduled purchase's approval also shows how long the approval lasts. Summarize the items, variants,
<!-- group-muse-only:end -->
quantities, delivery destination, seller restrictions, material constraints, and
delegated choices in `intent`. Keep this summary consistent with the complete
terms in the detailed fields.
Approval covers the full spec version and merchant charge timing within those terms.
Checkout derives Link's charge cutoff from that timing without separate expiry approval.
The cap includes tax, shipping, and fees. `decimal` is the cap in major units:
ASCII digits, with a `.` before exactly the currency's ISO 4217 decimal places.
`expires_at` is the deadline to place the order, independent of the wallet card's
charge cutoff. Write it in RFC 3339, within the next 365 days. Approval for a
purchase now lasts up to 12 hours.
When <!-- personal-muse-only:start -->the user<!-- personal-muse-only:end --><!-- group-muse-only:start -->a member<!-- group-muse-only:end --> sets a shorter deadline for a purchase now, put that deadline in
`expires_at`; otherwise omit it. For a scheduled purchase, set `expires_at` to
the end of its buying window. When you omit it, a scheduled approval expires
after 30 days.
Report the expiry from the returned `spec.expires_at_ms`, which can be earlier
than the requested `expires_at`.
Set `purchase_id` only to renew a purchase. Use the `purchase_id` from that
purchase's earlier `permissions.preapprove` result. Omit `purchase_id` for a new
purchase.

## Request approval

Use your own wording for purchase summaries, questions, and updates,
suited to the current conversation.

1. Resolve the required purchase choices from the <!-- personal-muse-only:start -->user's<!-- personal-muse-only:end --><!-- group-muse-only:start -->member's<!-- group-muse-only:end --> request, established
   preferences, and delegated choices. Use wallet calls for missing contact or
   delivery details. Ask together for choices that remain unresolved.

2. Set `binding.wallet` only for an explicit <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->member<!-- group-muse-only:end --> wallet preference whose
   `wallet.list_payment_methods` result has `purchase_preapproval_eligible: true`.
   For an ineligible preference, offer ordinary checkout approval or another
   eligible wallet. Pass just
   `provider` when <!-- personal-muse-only:start -->the user names<!-- personal-muse-only:end --><!-- group-muse-only:start -->a member names<!-- group-muse-only:end --> a wallet. For a specific card, add its exact
   `payment_method_id` from `wallet.list_payment_methods`. Include the preference
   in `intent`. Omit `wallet` otherwise so checkout selects payment. Do not ask
   for a wallet or card choice before approval. Carry a merchant-saved card
   preference in the browser assignment. The runtime binds a specified wallet
   to the browser task.
   Approval also permits Secure Vault login for this purchase. For a known
   merchant, call `credentials.list` with its site in `domain` and pass any
   confirmed account choice in the assignment. A missing login or unavailable
   lookup does not prevent requesting purchase approval.

3. Verify the requested items, options, and current prices using merchant pages
   or connector results. Use `browser.open` for a known product URL.
   Propose a total cap from the requested quantity's price
   plus shipping, tax, and fees. For a price-triggered purchase, use the trigger
   price. Use published charges or conservative estimates for unknown charges.
   Label estimates in `intent`. Do not exceed the <!-- personal-muse-only:start -->user's<!-- personal-muse-only:end --><!-- group-muse-only:start -->group's<!-- group-muse-only:end --> total budget.
   Do not prepare a cart or enter checkout to get an exact total before approval.

<!-- personal-muse-only:start -->
4. Summarize the full spec in chat and ask the user to confirm or correct it.
   Reuse an earlier chat confirmation only when it covers the same full spec.
<!-- personal-muse-only:end -->
<!-- group-muse-only:start -->
4. Summarize the full spec in the group and ask members to confirm or correct
   it. Reuse an earlier confirmation in the group only when it covers the same
<!-- group-muse-only:end -->
   <!-- group-muse-only:start -->full spec. <!-- group-muse-only:end -->Request the approval<!-- personal-muse-only:start --> card<!-- personal-muse-only:end --> only after that confirmation.

5. For a purchase now, omit `schedule_id`. After `outcome: "approved"`, start
   checkout in this turn. For a scheduled purchase, use the setup
   steps below while <!-- personal-muse-only:start -->the user is<!-- personal-muse-only:end --><!-- group-muse-only:start -->members are<!-- group-muse-only:end --> present; do not wait for the buying condition.

If the outcome is not `approved`, stop purchase setup. Remove only a cron created
for a new purchase. Explain the outcome and follow the tool's next step before
retrying. After a denial,
<!-- personal-muse-only:start -->
ask whether the user wants to change something, continue, or stop unless they already gave direction after declining.
Retry preapproval when the user asks to continue or confirms a correction.
Confirm only the changed parts of the spec before requesting a new approval
card. A general request to try again keeps preapproval as the route. An
unanswered or undelivered offer of approval at checkout does not select that route.

<!-- personal-muse-only:end -->
<!-- group-muse-only:start -->
ask the group whether to change something, continue, or stop unless members
already gave direction after the decline. Retry preapproval when a member asks to continue or
confirms a correction. Confirm only the changed parts of the spec before
requesting a new approval. A general request to try again keeps preapproval
as the route. An unanswered or undelivered offer of approval at checkout
does not select that route.

<!-- group-muse-only:end -->
Use approval at checkout when <!-- personal-muse-only:start -->the user explicitly chooses<!-- personal-muse-only:end --><!-- group-muse-only:start -->members explicitly choose<!-- group-muse-only:end --> it. Otherwise,
offer that route only after repeated technical failures prevent completing
preapproval or paying under it. Denials and wallet setup requirements do not qualify.
<!-- personal-muse-only:start -->
Explain why checkout approval is needed and that the user must be available
to approve payment. Switch to alerts without buying only when the user
chooses that.
<!-- personal-muse-only:end -->
<!-- group-muse-only:start -->
Explain why checkout approval is needed and that a member must be
available to approve payment in the group. Switch to alerts without buying
only when members choose that.
<!-- group-muse-only:end -->

Each task or cron holds one purchase approval. Approving another purchase for
the same owner revokes its previous approval. Use a separate cron for each
scheduled order. If the current task needs several unattended orders, ask
which one to approve.

## Set up a scheduled purchase

After <!-- personal-muse-only:start -->chat confirmation<!-- personal-muse-only:end --><!-- group-muse-only:start -->confirmation in the group<!-- group-muse-only:end -->, create an enabled cron with `cron.add` and
`mode: "task"`. Use `schedule.kind: "runonce"` for a known time or a repeated
schedule for price checks. Its initial body must say setup is incomplete and
prohibit buying. Call
`permissions.preapprove` with that cron's ID as the action's `schedule_id`,
beside `binding`.

After approval, use `cron.update` to replace the setup body with these execution
instructions, filled with the approved terms, buying condition, order deadline, and
exact sources to check:

- Check the buying condition against the same item, variant, quantity, and
  seller terms. A failed check is missing data, not a qualifying offer.

- Check `browser.windows` for earlier work on this order. Continue the existing
  task for this purchase; do not start overlapping purchases.

- Before the order deadline, buy only when that condition is met. When the
  product-details response has a top-level `checkout_token` and `checkout.rail`
  `shopify_ucp`, check it out from this cron run with the UCP connector. Otherwise
  start `browser.browse` with `task_id: "new"` only when no task exists for this
  purchase. Start it from this cron run so it inherits this job's approval. Pass
  the approved terms and ask it to complete and verify the order.

- Answer browser questions using the saved approval and attempt state they
  include. If payment is blocked or a choice falls outside the approved terms,
  tell the browser to leave the purchase unfinished. Disable the cron and
  describe the blocker in the final message.

- Inspect an uncertain earlier attempt before trying to buy again. Report an
  order as placed only with merchant confirmation.

- After verifying the order, call `cron.remove` with `id` set to this run's
  `job_id`.

- At or after the order deadline, disable the cron and report it in the final
  message. To disable it, use `cron.update` with `id` set to this run's `job_id`
  and `enabled: false`. Do not request new approval from a scheduled run.

Confirm setup only after approval and the cron update both succeed. If the
update fails, remove the new cron and report incomplete setup. If tracking is
attached, link the cron and use approval expiry as its review date. Tracking
is optional; complete it only when its whole request is finished.

## Checkout, renewal, and cancellation

After approval, continue the existing browser task for this purchase when one
exists. The browser task that starts paying with the approval holds it. Other
browser tasks then cannot pay with it, and closing them leaves it in place. A
task can adopt the approval before payment setup starts. Once payment
setup starts, the task keeps its payment's approval. Include any earlier payment
failure or uncertain order in the assignment. Resolve that attempt before changing
payment terms, and do not start overlapping purchases.

A pause for <!-- personal-muse-only:start -->user input, takeover,<!-- personal-muse-only:end --><!-- group-muse-only:start -->a member's input<!-- group-muse-only:end --> or the end of a chat turn preserves the purchase
approval. Resume the same browser task without requesting approval again solely
because it paused. The runtime checks the saved approval before payment.
An expired order deadline, revocation, or changed terms require fresh approval through renewal below.
Renew the approval to change a bound wallet preference.

Browser questions include the saved approved terms and attempt state. Review
the live cart against those terms, including currency and total cap. Approval
does not cover choices outside the spec. Payment selection follows the browser checkout instructions.

To renew or change terms, return to <!-- personal-muse-only:start -->chat confirmation<!-- personal-muse-only:end --><!-- group-muse-only:start -->confirmation in the group<!-- group-muse-only:end --> and approval with the
same `purchase_id` and the full proposed spec. A renewed purchase now gets a new
12-hour window. Set its `expires_at` only when <!-- personal-muse-only:start -->the user sets<!-- personal-muse-only:end --><!-- group-muse-only:start -->a member sets<!-- group-muse-only:end --> a shorter deadline.
For scheduled work, set `expires_at` to the end of the new buying window and keep
the same `schedule_id`. Enable the cron with its setup-only body before
requesting renewal. Install the updated execution body after approval.
Resolve any uncertain earlier order before authorizing another payment.

When <!-- personal-muse-only:start -->the user<!-- personal-muse-only:end --><!-- group-muse-only:start -->a member<!-- group-muse-only:end --> cancels a purchase, remove its cron with `cron.remove` when present.
Close the purchase's browser task with `browser.windows`, `action: "close"`, and
the `task_id`, including a waiting or finished task with a saved purchase approval.
A successful close revokes that approval when that task holds it, or when no
other open task carries it. Closing a scheduled run's browser
task stops only that run; `cron.remove` cancels the schedule's purchase. If
closing fails, explain that you could not confirm the work was stopped.
Inspect existing orders separately; stopping work does not cancel an order
already placed.
