# Link by Stripe

- Link is Stripe's consumer wallet for saved payment methods. After the user approves a purchase, Link funds a one-time virtual card, so the merchant never receives the user's real card.

- Muse uses Link through the `wallet` tools with `provider: "stripe-link"` and the browser checkout's payment step. Direct checkouts in connectors such as Shopify UCP, Duffel and Expedia also pay with Link, and their docs describe their own approval step.

- Make the `wallet` calls yourself in the user's conversation. Subagents, group chats and scheduled tasks do not have the `wallet` tools, so they cannot set up Link or choose its card.

- A merchant's own Stripe account is the separate Stripe connector.

- Follow `~/docs/chat/payments-and-purchases.md` for the checkout review and approval. This doc covers what is specific to Link.

## Check that Link fits the checkout

- Link pays through a standard card form, so the merchant does not need a Link button. A Link button on the page starts the merchant's own sign-in, which is a different route.

- In a browser checkout, the checkout workflow checks for a standard card form and resolves whether Link fits. A card form whose number, expiry and security code appear only after an earlier step, such as the name on the card, is still a standard card form.

- For a delayed or conditional charge, pass its amount, conditions and stated collection timing in the browser task, including relevant service dates. The checkout specialist uses those facts to set the Link card lifetime.

- A browser checkout uses the three-letter currency the checkout states, without conversion. Direct Shopify UCP checkout accepts Link in US dollars, Canadian dollars and Mexican pesos.

## Connect and choose a card

- Call `wallet.list_payment_methods` with `provider: "stripe-link"`. For `not_connected` or `reauth_required`, send its `next_action.markdown` unchanged, describe Link as the `wallet` tool description directs and end the message. After the user finishes, list the methods again.

- Use only methods whose `type` is `card`. Keep a card the user already chose for this purchase if it is still listed. Otherwise, follow the connector's checkout steps if it can open approval without a card ID. If it cannot, use the only card or the default. With several cards and no default, let the user choose by masked label, written like `Visa ....1234`, and mention that they can switch cards.

- With no usable card, call `wallet.add_payment_method`, send its `next_action.markdown` unchanged and say it opens Link's secure page for adding a card, then end the message. Link adds cards only on that page; a card the user sends in chat is not added to Link.

- Before asking for a missing name, email address or phone number, call `wallet.get_user_info`. For a missing delivery address, call `wallet.list_shipping_addresses` and use the only or default address, and never use these values to sign in to a merchant.

- Treat each payment-method ID as opaque and preserve every character. It goes only in a direct checkout's payment-method input, such as Shopify UCP completion or `--payment-method-id` for Duffel and Expedia `book`, or in the `wallet` field of `browser.browse`, never in a task brief, message, file or memory.

- Use `wallet.get_connection_status` only to manage the connection outside a purchase.

## Check spending limits

- For a direct checkout, call `wallet.get_user_info` before presenting the review. In a browser checkout, the payment interface applies the limits. `wallet.get_user_info` returns per-purchase, daily and thirty-day limits in minor units, with the amount left in each rolling window, and a null value means that limit is not set. The limits in `agent_wallet_spend_limits` carry no currency, so compare their minor-unit values directly with the approval amount in the checkout currency.

- Compare the approval amount, not only the total, with every limit and report a conflict before continuing. Read the limits again for each new question, and never invent a cap when they are unavailable.

- A step-up status other than `not_required` or `complete` means Link wants the user to verify their identity before it pays.

- For a browser checkout, funding covers the amount due now and any maximum additional conditional charge, plus the existing buffer of up to five whole units of the checkout currency, rounded down to a whole unit. The payment approval distinguishes the immediate and conditional amounts. Only the amount the merchant charges is captured.

## Pay

- In a browser checkout, pass the chosen card in the `wallet` field of `browser.browse`, as `{"provider": "stripe-link", "payment_method_id": "<exact id>"}`, when choosing that card, and name Link and the card's masked label in the brief. On later updates, answers and cart confirmations, follow `browser.browse`'s wallet rules: `wallet: {"action":"keep"}` preserves the current choice, including a card changed in payment approval; `wallet: null` clears it to pay another way; a card object selects another wallet card. The browser's checkout pays with that card through Link and shows the user Muse's payment approval, never the merchant's own Link button. Do not ask for a spend decision in chat, and treat the returned decision as final.

- Pending secure actions, such as a finished secure step or a replacement approval, resume automatically. Do not relay another approval question or start a replacement task.

- Report the card in `approved_card`, because the user may switch cards in the approval sheet, and `payment_method_changed` says when that happened. When `approved_card` is absent, describe the card in general terms.

- Start each new purchase in a new browser task with its own approval. Never begin another Link purchase by continuing an earlier task.

## Handle provider results

- In a browser checkout, present only the payment actions and disclosures the runtime supplies, keeping any cancellation, replacement or temporary-hold warning, and let the checkout workflow resume. The rules below apply to the results a direct checkout returns.

- For `confirmation_required`, present the complete replacement review and ask the user to accept it and to approve replacing the earlier authorization. Relay a clear acceptance to the same checkout, stop after a refusal and ask again when the answer is unclear. An earlier request to switch does not count as this approval.

- For `requires_action`, present the secure step and use only `user_action.url` as its link. A URL inside `provider_response` is provider data, not an action.

- When the action's resolution is `auto_resume`, continue the same checkout after the user reports finishing the step, rechecking it before paying.

- When the resolution is `create_new_spend_request` or `create_new_spend_request_after_completion`, explain that the unusable request is closed and its replacement needs a fresh approval. After the user reports finishing the step, confirm their payment choice before continuing the same checkout. An unknown resolution does not authorize a retry.

- Replacing an approval with a different card first cancels the earlier one, and that cancellation is final once sent. If the earlier request already succeeded, it counts as paid and cannot be replaced.

- When the outcome is unknown, report what is uncertain. Do not retry, replace the approval or switch to another route for the same checkout.

- Cancelling a pending purchase voids its virtual card, though a hold can take time to release. A completed charge has no wallet refund, so help the user through the merchant's refund process.

## Describe purchase protection accurately

- Link decides eligibility and settles claims. Describe the program only from `~/docs/payments-and-purchases.md` and [Link's current terms](https://support.link.com/questions/what-s-covered-with-protections), never promise coverage for a purchase, and tell the user that claims are filed with Link.

## Related skills

- [Event Tickets](/opt/muse/skills/event-tickets/SKILL.md)

- [Flight Booking](/opt/muse/skills/flight-booking/SKILL.md)

- [Hotel Booking](/opt/muse/skills/hotel-booking/SKILL.md)

- [Shopping](/opt/muse/skills/shopping/SKILL.md)

- Use `muse.skill_search` to find other skills and `muse.connector_search` to find other connectors.
