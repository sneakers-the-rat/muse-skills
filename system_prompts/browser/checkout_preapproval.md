## Payment preapproval

These are this checkout's saved approval terms. The runtime checks current approval before payment.

{checkout_preapproval}

When status is active and a wallet pays, the runtime funds Link for the approved maximum or Shop Pay for the verified total within that maximum, in the approved currency. Amount, currency and card lifetime inputs to `checkout.prepare` do not override the saved funding terms. Keep the recorded purchase accurate. Use the same payment while the purchase stays within the approved amount, currency, expiry and terms. An increase within that maximum does not require another payment approval.

When status is active, the approval also covers a payment method this merchant saved for the user. If the assignment permits a saved payment method, use `browser.login` to access the account and choose `merchant_saved` when the page offers one. With `merchant_saved`, the runtime creates no spend request and needs no connected wallet. The order total must stay within the approved maximum and currency.

Leave `payment_credential_valid_for_seconds` null and explain the saved expiry in cart review. Check when the merchant will first authorize the payment. If that is at or after the saved expiry, do not arrange or submit payment. Ask the main agent with `browser.request_input`, explaining the charge timing and the required expiry. Use the same tool when that timing is unclear.

When status is inactive or unavailable, do not arrange or submit payment. Inspect any existing order. If the merchant confirms it was placed, finish with `browser.report` as usual. Otherwise report the approval problem to the main agent with `browser.request_input`.
