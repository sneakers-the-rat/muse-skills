## purchase_outcome

The browser task invoked its checkout workflow (`browser.pay`). Set `purchase_outcome` to the merchant result. A cart review that stopped before purchase is `not_submitted`.

Select exactly one `purchase_outcome`. Answer any other sections of the schema by their own rules; the purchase outcome does not change them.

- `succeeded`: The merchant's receipt, order confirmation, or order history verifies that the order was placed.
- `failed`: The merchant definitively rejected the submitted payment or order, and no later evidence verifies that the order was placed.
- `not_submitted`: The browser task did not submit the payment or order to the merchant. Use this when preparation, approval, credential preparation, or wallet application stopped before merchant submission.
- `unknown`: The evidence does not establish whether the merchant placed the order. Use this whether or not the evidence establishes merchant submission.

When `purchase_outcome` is `succeeded`, set `purchase_outcome_reason` to null.

When `purchase_outcome` is `failed`, set `purchase_outcome_reason` to one of:

- `payment_rejected`: The merchant or its payment processor explicitly declined the payment submitted at the merchant's checkout.
- `order_rejected`: The merchant explicitly rejected the submitted order. The evidence attributes the rejection to a cause other than payment.
- `other_rejection`: The merchant explicitly rejected the submitted payment or order, but the evidence does not support a more specific rejection reason.

For `failed`, select the first supported reason in this order: `payment_rejected`, `order_rejected`, `other_rejection`.

When `purchase_outcome` is `not_submitted`, set `purchase_outcome_reason` to one of:

- `approval_denied`: The user explicitly denied the required purchase approval before merchant submission.
- `payment_setup_failed`: Payment approval, credential preparation, or wallet application failed before merchant submission.
- `pre_submission_user_action_required`: The browser task stopped before merchant submission because the user needed to provide information or make a decision. No explicit purchase-approval denial was recorded.
- `other`: The evidence verifies that merchant submission did not happen, but it does not support another `not_submitted` reason.

For `not_submitted`, select the first supported reason in this order: `approval_denied`, `payment_setup_failed`, `pre_submission_user_action_required`, `other`.

Do not use `pre_submission_user_action_required` for user action requested after merchant submission. Classify that case from later merchant evidence, or as `unknown` when no result was observed.

When `purchase_outcome` is `unknown`, set `purchase_outcome_reason` to one of:

- `result_not_observed`: The evidence establishes submission, but no merchant acceptance or rejection was observed.
- `submission_uncertain`: The evidence does not establish whether the purchase submission completed.
- `inconclusive_evidence`: The evidence is contradictory or does not support another `unknown` reason.

For `unknown`, select the first supported reason in this order: `result_not_observed`, `submission_uncertain`, `inconclusive_evidence`.

Use the browser task status, terminal reason, list of the agent's tool calls, agent's message history, and screenshots as evidence. The browser task's reasoning alone does not establish a merchant action. If the evidence does not establish whether submission happened, use `unknown` with `submission_uncertain` instead of any `not_submitted` reason.

A successful payment tool call proves only that the tool returned a result. A `browser.pay` result with status `purchased` reports that the checkout workflow verified the merchant's confirmation; `pending_reconciliation` means the submission outcome is not yet established. Browser task status is supporting evidence, not proof of purchase success. Use `succeeded` only when the evidence verifies the merchant order.

Classify the latest established result for this purchase. A later verified order placement supersedes an earlier payment rejection. Conflicting evidence without a verified final result is `unknown`. Absence of success evidence is not proof of failure.
