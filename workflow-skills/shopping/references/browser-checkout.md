# Browser checkout

- Use this guide when Shopping sends a purchase or cart through a live merchant site. Follow `~/docs/chat/payments-and-purchases.md` for authority, changed terms and reconciliation. The browser's checkout workflow owns cart review, payment choice, approval, submission and verification.

## Start the browser task

- Call `browser.browse` with the existing task for this cart, or `task_id: "new"` for separate work. Use `browser.windows` with `action: "list"` if related work may already be running.

- Give it the exact product or checkout URLs, the requested items, variants and quantities, known contact and delivery details, exclusions, the intended stage and the offer you compared:

```json
{
  "task_id": "new",
  "task": "Purchase <items> from <exact product or checkout URLs>. Use these choices: <variants, quantities, delivery details, payment preference and other requirements>. The selected offer is <quoted total, currency, delivery estimate and source>. Use checkout review to resolve any remaining choices. Report any change in price or delivery. Complete the purchase after the required payment decision."
}
```

- For a request to buy, say explicitly that the task completes the purchase after the required payment decision. For cart preparation, ask it to prepare the cart and not purchase. The browser inspects the cart, presents cart and payment decisions, enters the approved card and verifies the order, so do not direct it through provider setup or final-button choreography.

- Pass a payment preference in ordinary terms. A wallet card goes in `wallet`, with its masked label in `task`; never put opaque method IDs or payment tokens in `task`. A card the user sent in chat goes in `task` as text. A merchant's Link or Shop Pay button is not evidence of the workflow's supported payment routes.

- Mention any payment refusal, checkout failure or unresolved earlier outcome for this purchase.

- Keep the strongest alternative offers and when you checked them in your own context. Do not invent a quote that you did not observe.

## Continue the purchase

- Continue the same task with `browser.browse` and its `task_id` for corrections and new information. Pending secure actions resume automatically, so do not relay another approval question or create a replacement task.

- If the task reports a higher price, an expired promotion or slower delivery, apply the Shopping skill's recheck before resuming checkout or asking the user to accept the change.

- Report completion only from verified merchant evidence.
