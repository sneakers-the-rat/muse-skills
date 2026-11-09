## Payment preapproval

These are this checkout's saved approval terms. The runtime checks current approval before payment.

{checkout_preapproval}

When status is active, the runtime creates the spend request for the approved maximum in the approved currency, expiring at the stated time. Amount, currency and card lifetime inputs to `checkout.prepare` do not override these funding terms. Keep the recorded purchase accurate. Use the same payment while the purchase stays within the approved amount, currency, expiry and terms. An increase within that maximum does not require another payment approval.

Leave `payment_credential_valid_for_seconds` null and explain the saved expiry in cart review. Check when the merchant will first authorize the payment. If that is at or after the saved expiry, do not arrange or submit payment. Ask the main agent with `browser.request_input`, explaining the charge timing and the required expiry. Use the same tool when that timing is unclear.

When status is inactive or unavailable, do not arrange or submit payment. Inspect any existing order. If the merchant confirms it was placed, finish with `browser.report` as usual. Otherwise report the approval problem to the main agent with `browser.request_input`.
