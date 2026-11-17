## Payment preapproval

These are this checkout's saved approval terms. The runtime checks current approval before payment.

{checkout_preapproval}

When status is active, the approval covers one order within its saved terms, amount cap and currency. When `wallet_provider` is present, use `payment_route: wallet`. Otherwise choose payment using your checkout instructions. A merchant-saved payment creates no spend request and needs no connected wallet.

- Place the order before the purchase approval's `expires_at`.
- Set the card's charge cutoff under your checkout instructions, even when the charge occurs after the order deadline.

When status is inactive or unavailable, do not arrange or submit payment. Inspect any existing order. If the merchant confirms it was placed, finish with `browser.report` as usual. Otherwise report the approval problem to the main agent with `browser.request_input`.
