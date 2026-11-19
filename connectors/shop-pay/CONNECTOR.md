# Shop Pay

- Shop Pay is Shopify's consumer wallet. Muse uses it through the `wallet` tools with `provider: "shop-pay"` and through the browser checkout's payment step. A merchant's own Shopify store is the separate Shopify connector.

- Follow `~/docs/chat/payments-and-purchases.md` for the checkout review and approval. This doc covers what is specific to Shop Pay.

## Check that Shop Pay is offered

- For browser checkout, follow the checkout agent's payment instructions. A merchant's Shop Pay button starts its own sign-in and does not establish support for the wallet route.

- For direct UCP checkout, offer Shop Pay as a route before the checkout is created, as the [UCP](/opt/hatch/connectors/ucp/CONNECTOR.md) docs describe.

- Shop Pay pays direct UCP and native Shopify browser checkouts in supported currencies. Its virtual card route at other merchants pays only a purchase in US dollars that the merchant does not charge again later. Use the checkout's stated currency and exact total; Japanese yen amounts have no fractional units.

## Connect and choose a card

- Call `wallet.list_payment_methods` with `provider: "shop-pay"`. For `not_connected` or `reauth_required`, send its `next_action.markdown` unchanged, say it opens Shop Pay's secure connection page and end the message. After the user finishes, list the methods again.

- Use only methods whose `type` is `card`. Keep a card the user already chose for this purchase if it is still listed.

- For a direct checkout, follow its connector's instructions. If it requires a card ID, use the only card or the default; with several cards and no default, ask the user to choose by masked label, written like `Visa ....1234`.

- With no usable card, call `wallet.add_payment_method` and send its `next_action.markdown` unchanged, saying it opens Shopify's secure Shop Pay wallet page where the user manages cards. End the message there. Do not request credit card numbers over chat or forward them in a browser task. The user can give Muse access through Wallet or enter payment details directly on the merchant site during takeover.

- Before asking for a missing name, email address or phone number, call `wallet.get_user_info`. For a missing delivery address, call `wallet.list_shipping_addresses` and use the only or default address. Use these values only to fill matching empty checkout fields, never to sign in to a merchant.

- Treat each payment-method ID as opaque. Use it only in structured payment fields, not in task briefs, messages, files or memory.

- Use `wallet.get_connection_status` only to manage the connection outside a purchase. Share its `next_action.markdown` only when it matches a request to connect, reconnect or disconnect.

## Pay

- In a browser checkout, the checkout agent pays through Shop Pay and obtains payment approval when required. Do not use the merchant's own Shop Pay button. Its native route pays with a one-time token; on a supported card route it supplies card fields for the browser to enter after approval. Do not ask for a separate chat confirmation.

- After an approval denial, follow the browser's question or final report. Continue only from the user's later direction and obtain fresh approval.

- Pending secure actions, such as a replacement approval, resume automatically. Do not relay another approval question or start a replacement task.

- Report the card the result says was approved, which can differ from the one proposed because the user may change it in the approval sheet.

- For direct UCP checkout, `checkout complete` with `wallet_provider: "shop_pay"` requests the same approval, as the UCP docs describe.

## Recover from problems

- The wallet route never uses the merchant's Shop Pay sign-in or verification code. That is a separate browser route, so settle any uncertain wallet payment before offering it.

- When a payment's outcome is unknown, do not retry, switch cards or pay again through takeover. Establish what happened from the latest browser result first.

- Report payment cancellation only when the checkout result confirms it. A completed order follows the merchant's refund process.

## Related skills

- [Shopping](/opt/muse/skills/shopping/SKILL.md)

- Use `muse.skill_search` to find other skills and `muse.connector_search` to find other connectors.
