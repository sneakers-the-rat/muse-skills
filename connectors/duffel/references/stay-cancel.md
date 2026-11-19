# Cancelling a hotel stay

- Cancel only when the user asks. `/opt/hatch/bin/duffel stay-cancel --booking-id bok_...` takes the `booking_id` that `book` returned. Stays can't be looked up yet, so it needs that id.

- The user approves first. The approval shows the hotel, the dates and what cancelling refunds at that moment, or for a stay paid at the hotel, what the hotel can charge. If that changes before the user approves, nothing is sent, and `cancellation_terms_changed` means running `stay-cancel` again to show the current terms.

- `status: cancelled` means the booking is cancelled. `cancellation_terms` is what the approval said cancelling refunds or costs, or that its deadline passed during the cancellation. Report a refund or charge only as it states, and say when it isn't stated instead of calling the cancellation free.

- `already_cancelled` means Duffel already shows the stay cancelled. After `cancellation_unconfirmed` or another unclear result, run `stay-cancel` again. It reads the booking first and asks the user again only if the stay is still booked.
