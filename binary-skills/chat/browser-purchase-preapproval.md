# Browser purchase preapproval

Use `permissions.preapprove` for one browser payment or order through a
connected wallet the approval card offers and that `wallet.list_payment_methods`
marks `purchase_preapproval_eligible: true`, including Link and Shop Pay,
or a payment method the merchant saved for the user.
Send one action in `actions`, with `connector: "browser"` and the `binding` below.
Direct checkout integrations use their own approval flow.

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
  max_total: {amount: number, currency: string},
  expires_at?: string,
  purchase_id?: string
}
```

Put product and variant details in `items`, hard constraints in `requirements`,
delivery terms in `shipping`, allowed sellers in `merchant_policy`, and choices
the user delegated in `delegated_choices`. Use empty arrays when there are no
additional requirements or delegated choices. Use `shipping_address_ref` for
an established saved address; omit it when no delivery address is needed.
For a bill or fee, describe the payment in `items` with quantity 1 and state
that no delivery applies in `shipping`.

The card shows `intent` and the total cap. A scheduled purchase's card also shows
how long the approval lasts. Summarize the items, variants,
quantities, delivery destination, seller restrictions, material constraints, and
delegated choices in `intent`. Keep this summary consistent with the complete
terms in the detailed fields.
Approval covers the full spec version.
The cap includes tax, shipping, and fees. Write `expires_at` in RFC 3339,
within the next 365 days. Approval for a purchase now lasts up to 12 hours.
When the user sets a shorter deadline for a purchase now, put that deadline in
`expires_at`; otherwise omit it. For a scheduled purchase, set `expires_at` to
the end of its buying window. When you omit it, a scheduled approval expires
after 30 days.

## Request approval

Use your own wording for purchase summaries, questions, and updates,
suited to the current conversation.

1. Resolve the required purchase choices from the user's request, established
   preferences, and delegated choices. Use wallet calls for missing contact or
   delivery details. Ask together for choices that remain unresolved.

2. Preserve the user's established wallet or card preference. Do not add a
   wallet- or card-selection question. The approval also covers a payment
   method the merchant saved for the user. When the user chose one, pass that
   choice in the browser assignment. A merchant-saved payment needs no connected
   wallet. If the user's chosen payment method is unavailable from both the
   merchant's saved methods and a connected wallet with
   `purchase_preapproval_eligible: true`, ask whether to use wallet preapproval
   or keep that choice with approval at checkout.

   Approval also permits Secure Vault login on sites used for this purchase.
   Before proposing the spec for a known merchant, call `credentials.list`
   with its site in `domain`. Include the payment plan in the spec's payment
   details and in `intent`. Unless the user prefers another payment method,
   propose the card saved on the merchant account first, with the wallet
   covered by the approval as the fallback when available. The saved-card
   option is conditional on there being a saved card on file for that merchant.
   Pass the confirmed account and payment choices in the browser assignment.
   A missing login or unavailable lookup does not prevent requesting purchase
   approval. Describe only what the lookup established.

3. Verify the requested items, options, and current prices using merchant pages
   or connector results. Use `browser.open` for a known product URL.
   Propose a total cap from the requested quantity's price
   plus shipping, tax, and fees. For a price-triggered purchase, use the trigger
   price. Use published charges or conservative estimates for unknown charges.
   Label estimates in `intent`. Do not exceed the user's total budget.
   Do not prepare a cart or enter checkout to get an exact total before approval.

4. Summarize the full spec in chat and ask the user to confirm or correct it.
   Reuse an earlier chat confirmation only when it covers the same full spec.
   Request the approval card only after that confirmation.

5. For a purchase now, omit `schedule_id`. After `outcome: "approved"`, start
   the browser purchase in this turn. For a scheduled purchase, use the setup
   steps below while the user is present; do not wait for the buying condition.

For any outcome besides `approved`, stop setup and remove any purchase cron
created for it. Explain the approval outcome and next step. After a denial,
ask why the user declined or what they want changed unless they already explained.
Retry preapproval when the user asks to continue or confirms a correction.
Confirm only the changed parts of the spec before requesting a new approval
card. A general request to try again keeps preapproval as the route. An
unanswered or undelivered offer of approval at checkout does not select that route.

Use approval at checkout when the user explicitly chooses it. Otherwise,
offer that route only after repeated technical failures prevent completing
preapproval or paying under it. A user denial is not a technical failure.
Explain why checkout approval is needed and that the user must be available
to approve payment. Switch to alerts without buying only when the user
chooses that.

Each task or cron holds one purchase approval. Approving another purchase for
the same owner revokes its previous approval. Use a separate cron for each
scheduled order. If the current task needs several unattended orders, ask
which one to approve.

## Set up a scheduled purchase

After chat confirmation, create an enabled cron with `cron.add` and
`mode: "task"`. Use `schedule.kind: "runonce"` for a known time or a repeated
schedule for price checks. Its initial body must say setup is incomplete and
prohibit buying. Call
`permissions.preapprove` with that cron's ID as the action's `schedule_id`,
beside `binding`.

After approval, use `cron.update` to replace the setup body with these execution
instructions, filled with the approved terms, buying condition, expiry, and
exact sources to check:

- Check the buying condition against the same item, variant, quantity, and
  seller terms. A failed check is missing data, not a qualifying offer.

- Check `browser.windows` for earlier work on this order. Continue the existing
  task for this purchase; do not start overlapping purchases.

- Before expiry, buy only when that condition is met. Start `browser.browse`
  with `task_id: "new"` only when no task exists for this purchase. Start it from
  this cron run so it inherits this job's approval. Pass the approved terms and ask
  it to complete and verify the order.

- Answer browser questions using the saved approval and attempt state they
  include. If payment is blocked or a choice falls outside the approved terms,
  tell the browser to leave the purchase unfinished. Disable the cron and
  describe the blocker in the final message.

- Inspect an uncertain earlier attempt before trying to buy again. Report an
  order as placed only with merchant confirmation.

- After verifying the order, call `cron.remove` with `id` set to this run's
  `job_id`.

- At or after expiry, disable the cron and report the expiry in the final
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

A pause for user input, takeover, or the end of a chat turn preserves the purchase
approval. Resume the same browser task without requesting approval again solely
because it paused. The runtime checks the saved approval before payment.
Expiry, revocation, or changed terms require fresh approval through renewal below.

Browser questions include the saved approved terms and attempt state. Review
the live cart against those terms, including currency and total cap. Approval
does not cover choices outside the spec. It covers only the approved wallet and
payment methods the merchant saved for the user.

To renew or change terms, return to chat confirmation and approval with the
same `purchase_id`, the full proposed spec, and a new expiry. For scheduled
work, keep the same `schedule_id`; enable the cron with its setup-only body
before requesting renewal. Install the updated execution body after approval.
Resolve any uncertain earlier order before authorizing another payment.

When the user cancels a purchase, remove its cron with `cron.remove` when present.
Close the purchase's browser task with `browser.windows`, `action: "close"`, and
the `task_id`, including a waiting or finished task with a saved purchase approval.
A successful close revokes that approval when that task holds it, or when no
other open task carries it. Closing a scheduled run's browser
task stops only that run; `cron.remove` cancels the schedule's purchase. If
closing fails, explain that you could not confirm the work was stopped.
Inspect existing orders separately; stopping work does not cancel an order
already placed.
