# Browser checkout

- Use this guide when Shopping sends a purchase through a product or checkout page. Follow `~/docs/chat/payments-and-purchases.md` for the checkout review, payment choice and approval.

## Start the browser task

- Call `browser.spawn_task` with the exact product or checkout URLs, every choice already made for this purchase and the offer you compared:

```json
{
  "task": "Purchase <items> from <exact product or checkout URLs>. Use these choices: <variants, quantities, delivery details, payment choice and other requirements>. The selected offer is <quoted total, currency, delivery estimate and source>. Ask only for missing required item or checkout choices. Pause with ask_for_information at final review, before payment or submission. Report any change in price or delivery. Complete the purchase only after the required approval."
}
```

- Name a selected wallet by its provider ID, `stripe-link` or `shop-pay`, and a selected saved card by its masked label. Never put the opaque payment-method ID or card details in `task`.

- Leave the payment route out when none is selected. The runtime adds the checkout's supported providers to the browser handoff, so do not ask the task to infer them from checkout buttons.

- If the user picked Link "if it is there", pass `stripe-link` without requiring a Link button on the page. If the user will enter payment themselves, say in `task` that they will do it during browser takeover.

- Mention any payment refusal or checkout failure that already happened for this purchase.

- Keep the strongest alternative offers and when you checked them in your own context. Do not invent a quote that you did not observe.

## Continue the purchase

- Follow the acknowledgment that `browser.spawn_task` returns, then continue the same task with `browser.steer_task`. Do not replace it with a new task during wallet setup or approval.

- If the task reports a higher price, an expired promotion or slower delivery, apply the Shopping skill's recheck before resuming checkout or asking the user to accept the change.
