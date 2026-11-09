# Recover an uncertain Duffel result

- Use this guide when `validate-booking`, `book` or `cancel-booking` returns anything other than a clean success or a validation error.

- For a Link `requires_action` result, share a link only when `user_action.kind` is `open_url`, using `user_action.label` as the text and `user_action.url` as the destination. An `action_url` inside `provider_response` is the provider's raw link, not one meant for the user. Without `user_action`, report the blocker and stop.

- When the resolution is `auto_resume`, share the action link once. After the user completes it, rerun the identical `book`.

- When the resolution is `replacement_required`, share the link and stop. After the user completes it and asks to continue, search again and get a new purchase approval instead of rerunning the old `book`.

- When the resolution is anything else or missing, share the link and stop, without assuming the request can resume.

- A `failed`, `terminal_status` or `unsupported` Link result ends the attempt; another spend request would start a new purchase, so report it and stop.

- Before any approval or submission for this purchase, correct validation errors; for an expired offer, search the itinerary again and present fresh terms for approval.

- After approval or submission for this purchase, each outcome carries its own `message` and `next_action` for that state, including whether a booking or payment may already have gone through and whether anything can be retried. Expiry does not resolve booking or funding uncertainty or permit retry or replacement.

- Keep the returned `checkout_operation_id` and original `offer_id` for recovery. `/opt/hatch/bin/duffel booking-status --checkout-operation-id OPERATION_ID --offer-id ORIGINAL_OFFER_ID` reads saved evidence, including after restart or offer expiry, and while the outcome is unresolved, including `supplier_confirmed_details_pending`, it asks Duffel whether that offer has an order. When Duffel has one, the result is the booking receipt with its booking reference. `provider_lookup: no_order_yet` means Duffel shows no order yet; an accepted booking can take time to appear, so this doesn't prove there is no booking. An immediate re-check won't change the answer; a check in a later turn may find it. Other `provider_lookup` values leave the outcome unknown. `observation_persistence: unconfirmed` means the response distinction may not survive restart; unavailable or absent evidence doesn't prove there is no booking. Refreshing the offer won't recover the purchase.

- A timeout, a 5xx, `result_unknown: true` or an error saying the outcome is unknown or unconfirmed means the booking or cancellation may already have happened. `booking-status` is the first step; resending `book` or `cancel-booking` could act twice, and the outcome stays unknown until a status read shows it.

- An uncertain customer-profile creation has not started payment. Ask for profile recovery instead of creating the profile again.

- After a partial split purchase, report the completed booking references and every unpurchased leg, then stop buying or cancelling until the user decides.

- A success with `resource_authorization.persisted: false` is still a booking. Report it and warn that later management may be unavailable; booking again would create a second booking.

- The same offer with the same booking data is the same checkout and can resume, except after `checkout_pricing_stopped`. A new offer starts another checkout and may place another hold, so it is a new purchase for the user to choose, not a retry.

- After success, report every carrier booking reference and ticket status from the receipt. A loyalty account marked `not_confirmed_on_order` is unconfirmed, not rejected. Suggest checking with the airline using the booking reference; rebooking would buy a second ticket.
