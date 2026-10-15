# Shop Pay

- Shop Pay is the consumer wallet that Shopify merchants accept. Muse uses it through the `wallet` tools with `provider: "shop-pay"` and through the browser checkout's native payment step. A merchant's own Shopify store is the separate Shopify connector.

- Follow `~/docs/chat/payments-and-purchases.md` for the checkout review and approval. This doc covers what is specific to Shop Pay.

## Check that Shop Pay is offered

- Offer Shop Pay for a browser checkout only when the final-review handoff lists `shop-pay` in `available_payment_providers`. A Shop Pay button on the merchant's page starts the merchant's own sign-in and does not show that the wallet route is available.

- For direct Shopify UCP checkout, offer Shop Pay as a route before the checkout is created, as the [Shopify UCP](/opt/hatch/connectors/shopify-ucp/CONNECTOR.md) docs describe.

- If a wallet call says Shop Pay is not supported for this account yet, tell the user it is unavailable and offer another route.

- Shop Pay pays checkouts in US dollars, Canadian dollars, Mexican pesos and euros.

## Connect and choose a card

- Call `wallet.list_payment_methods` with `provider: "shop-pay"`. For `not_connected` or `reauth_required`, send its `next_action.markdown` unchanged, say it opens Shop Pay's secure connection page and end the message. After the user finishes, list the methods again.

- Use only methods whose `type` is `card`. Keep a card the user already chose for this purchase if it is still listed, otherwise use the only card or the default. With several cards and no default, let the user choose by masked label, written like `Visa ....1234`.

- With no usable card, call `wallet.add_payment_method` and send its `next_action.markdown` unchanged, saying it opens Shopify's secure Shop Pay wallet page where the user manages cards. End the message and never ask for card details in chat.

- Before asking for a missing name, email address or phone number, call `wallet.get_user_info`. For a missing delivery address, call `wallet.list_shipping_addresses` and use the only or default address. Use these values only to fill matching empty checkout fields, never to sign in to a merchant.

- Treat each payment-method ID as opaque. It goes only in the `wallet_payment` field of `browser.steer_task` or in the UCP completion input, never in a task brief, message, file or memory.

- Use `wallet.get_connection_status` only to manage the connection outside a purchase. Share its `next_action.markdown` only when it matches a request to connect, reconnect or disconnect.

## Pay

- After the user accepts the checkout review and the card, resume the same browser task with `browser.steer_task` and this field:

```json
{"wallet_payment": {"provider": "shop-pay", "payment_method_id": "<exact id from wallet.list_payment_methods>"}}
```

- The browser task then presents Shop Pay's native approval for the exact merchant, total and card, and Shop Pay pays with a one-time token. Do not ask for a separate chat confirmation, and treat the approval decision as final.

- A declined approval ends the attempt without a charge. A later attempt with a card the user picks starts a fresh approval.

- Include `wallet_payment` with the selected card whenever you resume this task to continue the payment, such as when you relay the user's acceptance of a replacement approval. A steer without it clears the selection, and the browser task then hands off again instead of paying.

- Report the card the result says was approved, which can differ from the one proposed because the user may change it in the approval sheet.

- For direct UCP checkout, `checkout complete` with `wallet_provider: "shop_pay"` requests the same approval, as the UCP docs describe.

## Recover from problems

- The wallet route never uses the merchant's Shop Pay sign-in or verification code. That is a separate browser route, so settle any uncertain wallet payment before offering it.

- When a payment's outcome is unknown, do not retry, switch cards or pay again through takeover. Establish what happened from the latest browser result first.

- Cancelling a pending purchase releases its approval. It does not refund a completed order, which follows the merchant's refund process.

## Related skills

- [Shopping](/opt/muse/skills/shopping/SKILL.md)

- Use `muse.skill_search` to find other skills and `muse.connector_search` to find other connectors.
