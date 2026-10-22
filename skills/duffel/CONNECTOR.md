# Duffel

- `/opt/hatch/bin/duffel` searches, books and manages flights from many airlines. Its commands are `search`, `seat-options`, `validate-booking`, `book`, `booking-status`, `cancellation-quote` and `cancel-booking`. It needs no user login, and payment uses the user's Link by Stripe card.

- Before a user-facing search or booking, read [Flight Booking](/opt/muse/skills/flight-booking/SKILL.md), which compares Duffel offers with other sources, and [checkout](/opt/muse/assets/booking/references/checkout.md). [Flight Tracking](/opt/muse/skills/flight-tracking/SKILL.md) uses Duffel only for the fare check on a booked trip. Duffel does not report live flight status.

## Search a complete trip

```sh
/opt/hatch/bin/duffel search --origin SFO --destination JFK --departure-date 2026-10-14 --return-date 2026-10-18 --adults 1 --cabin economy --sort duration --limit 300 > /tmp/sfo-jfk-flights.json
```

- Use exact three-letter airport IATA codes, and never guess an obscure or ambiguous one, because the CLI accepts any three letters. Metro codes such as `NYC` are not supported, and results exclude nearby airports. Add `--return-date` for a round trip, or repeat `--leg ORIGIN:DESTINATION:YYYY-MM-DD` for a multi-city trip.

- Price the full passenger mix in the search with `--adults`, one `--child-age` for each seated traveler aged 2 to 17 on the final travel date, and `--lap-infants`. Each lap infant needs a different adult. Search again whenever the mix changes, and never search a known child as an adult.

- Ask whether each infant under two will sit on a lap or in their own seat, rather than inferring it. An infant who needs their own seat has to book with the airline, because this connector cannot validate that case.

- Pass the cabin with `--cabin economy`, `premium_economy`, `business` or `first`. Omitting it searches economy.

- Use `--limit 300`, the maximum, so fare variants from one carrier do not crowd out other trips. The default is 20. If the provider returns fewer offers, use the complete result without retrying for more.

- Sort with `--sort duration` or the default `price`, following the user's priority. Use `duration` when the user gives none. One search with `--limit 300` usually holds enough offers to weigh both, so run the other sort only when the comparison needs it.

- Narrow with `--max-connections N` (0 means nonstop), `--airlines` (comma-separated names or IATA codes), `--max-price` and `--refundable`. `--refundable` keeps only offers marked refundable before departure without a penalty, which is not the same as cancel anytime, and it counts offers with unstated refund terms in `refundable_unknown_excluded`. Those offers are unknown, not non-refundable.

- Add or widen `--max-connections`, which accepts 0, 1 or 2, only when the user asked for a stop limit or an earlier search found nothing useful.

- When a requested or expected carrier is missing, even if other carriers returned useful offers, read `airlines_available` and run one targeted `--airlines` search before turning to the airline's site. A carrier's absence from Duffel does not mean it skips the route.

- For a request for an exact flight, book only an offer that carries that flight number. Never substitute a different flight or treat schedule data as proof that it is bookable.

- A domestic premium cabin may be sold as First. Unless the user excluded First, run one matching `--cabin first` search when a domestic business search finds nothing useful, or when a requested carrier sells its premium cabin as First. Keep the itinerary, passengers, price cap, carrier and stop limits.

- Report the actual cabin and fare brand on each leg. Domestic First does not promise a lie-flat seat, and economy is never a substitute without the user's agreement.

- For flexible dates or airports, run the smallest useful set of searches one at a time and inspect each before expanding. Start with the preferred airport pair and add another only when asked or when the first has no useful match.

## Keep the original results

- Redirect each search straight into its own JSON file on the first attempt and check the exit status. Never pipe it through `head` or a parser, truncate it, rewrite it or overwrite it. A read-only command may inspect the saved file.

- Check `ok` first. A successful search has a top-level `offers` array, which can be empty with `offers_total: 0` and `offers_shown: 0`. Read that array, not a nested `response.data`. An error, a missing array or an unfamiliar shape does not mean there are no flights.

- Read `search_coverage` and tell the user when coverage is incomplete (`complete: false`). Even a complete search covers only the offer request Duffel returned. `offers_total` counts matches in the pages scanned, with airline and price filters applied locally.

- When `ok` is false, present any useful `partial_results.offers` with a note that the search failed and coverage is incomplete, before another search or a browser check. If later checks you need add useful offers, present one replacement list that explicitly supersedes the partial one. That is the one exception to keeping each itinerary in a single list. Report the checks that did not finish. Empty incomplete results do not show that no flights match.

- `/offers/INDEX`, using the offer's original zero-based index, points to one complete offer with all its slices and segments. Partial results use `/partial_results/offers/INDEX`. Give `widget.create_list_widget` one row per offer, pointing into the unchanged file, such as `{"type":"flight","data":{"flight_details_file":"/tmp/sfo-jfk-flights.json","json_pointer":"/offers/0"}}`.

- A tap on a native flight row selects that row's complete offer. For a trip that is still being planned, return it to the plan and stop before seats, traveler details or validation. Otherwise validate and book the same offer, never only its first leg.

- If the original file was lost or altered, rerun the search into a new file. Never rebuild an offer from truncated output or a summary.

- Group offers that share airports, local times, flight numbers and segment order before choosing. Keep a second fare for the same schedule only when its cabin, bags, refund or change terms, or price make a real difference.

- Keep differences between passengers and segments. Show a missing fare brand, cabin, bag, refund or change fact as not stated, never as none, non-refundable or an airline's usual fee. Convert airport-local times only when the airport's timezone is known.

## Respect search limits

- Reuse a complete response while its offers are still valid. Corrected arguments, another relevant itinerary, expired offers or lost output justify another search. Repeating an identical search in a shell loop or launching duplicates in the background does not.

- Do not retry an unchanged failed search, even when its response says `retriable: true`.

- Other failed reads, such as `booking-status`, `seat-options` and `validate-booking`, may be retried.

- A 429 rate-limit response ends Duffel calls for the current task. Report the limit without changing the query to get around it.

- `ok: false` with `code: duffel_unavailable` means new Duffel searches and bookings are unavailable right now. Do not retry during this turn. Continue with the airline's site through `browser.browse`.

## Prepare passengers and seats

- `seat-options --offer-id OFFER` returns bookable seats for each passenger, and the flag repeats for a short list of offers. A zero price means no added fee, and an omitted seat is unavailable. Adjacent seats share a row and section on the same side of the aisle.

- Choose at most one seat per passenger and segment. Repeat `--seat PASSENGER:SEGMENT:SEAT`, with one-based numbers, once per seat, such as `--seat 1:1:28B --seat 2:1:28C`, and never join seats with commas. Mention seat choice once without letting it block the booking.

- After the user picks an offer, ask only for what validation requires. That is each traveler's legal given and family name, birth date, title (`mr`, `ms`, `mrs`, `miss` or `dr`) and gender (`m` or `f`), one reachable trip email and phone, which every passenger entry must carry and can share, the adult with each lap infant, and passport details only when validation asks. Ask for a loyalty account number only when the user wants credit. Use these values only for this booking's `validate-booking` and `book`, never store them, and do not repeat them back.

- Put passengers in `data.passengers` in search order:

```json
{
  "data": {
    "passengers": [{
      "given_name": "Legal given name",
      "family_name": "Legal family name",
      "born_on": "1990-01-01",
      "title": "ms",
      "gender": "f",
      "email": "trip-contact@example.com",
      "phone_number": "+14155550123"
    }]
  }
}
```

- For a lap infant, add `"accompanying_adult": N` with the adult's one-based position. A required passport goes in the passenger's `identity_documents` array with `type: "passport"`, the number as `unique_identifier`, an uppercase two-letter `issuing_country_code` and `expires_on` as `YYYY-MM-DD`. Never send an empty document, invent identity details or ticket a traveler who has not been born. For an unborn traveler, explain that booking must wait until birth, and promise nothing about later fares, availability or seats.

- Offer loyalty credit once without letting it block the booking. When the user wants it, add the account to that passenger as `"loyalty_programme_accounts": [{"airline_iata_code": "UA", "account_number": "ACCOUNT_NUMBER"}]`, with one object per programme. Validation must confirm support, and a failed account comes off only with the user's agreement.

- Leave out the fields the CLI owns, which are `id`, `infant_passenger_id`, `user_id`, `type`, `selected_offers`, `services`, `payment` and `payments`.

## Validate and book

```sh
/opt/hatch/bin/duffel validate-booking --offer-id OFFER --booking-json JSON
```

- Validation refreshes the offer and checks travelers, documents, seats and loyalty, without payment or approval. Ask for every `required_missing` and `invalid` item together and rerun until `ready_to_book: true`.

- Treat `selected_offer` as the current itinerary, price, bags and fare terms. Check each slice's `from` and `to` against the chosen airports, and stop if they differ.

- When validation asks for a first-time payment profile, pass the account holder's email and legal name with `--customer-email`, `--customer-given-name` and `--customer-family-name` to both validation and booking. This profile is not a passenger, and it is created only after purchase approval.

- List payment methods and choose the card as [Link by Stripe](/opt/hatch/connectors/stripe-link/CONNECTOR.md) describes. Then book once with its exact ID and the same booking JSON and seats:

```sh
/opt/hatch/bin/stripe-link payment-methods list --format json
/opt/hatch/bin/duffel book --offer-id OFFER --payment-method-id ID --booking-json JSON --seat 1:1:28B --seat 2:1:28C
```

- `book` revalidates before any payment request. Its single approval covers the itinerary, travelers, seats and fees, fare terms, total, the first-time profile, a one-time virtual card, 3DS and immediate ticketing. Any change to the flight, fare, date, passengers, services or total needs a fresh approval.

- Held orders, Duffel balance payment, inline cards and raw order APIs are not supported.

- If Link is not connected, explain the one-time virtual card and share its connection link. For an airline-site fallback, use `browser.browse` and follow `~/docs/chat/payments-and-purchases.md`. A card the user supplies for that booking may go to the browser task as text with `wallet: null`; the browser checkout still requires payment approval. This does not enable inline cards in the Duffel API. If neither supported route works, stop with the itinerary prepared and say that payment is blocked.

- Prefer one offer that covers the whole itinerary. Split it into separate bookings only with the user's agreement before the first `book`. Explain that each booking has its own approval, payment and terms, that later offers are not held, and that a later failure can leave earlier tickets booked.

## Recover an uncertain result

- For a Link `requires_action` result, share a link only when `user_action.kind` is `open_url`, using `user_action.label` as the text and `user_action.url` as the destination. Never open or share an `action_url` from `provider_response`. Without `user_action`, report the blocker and stop.

- When the resolution is `auto_resume`, share the action link once. After the user completes it, rerun the identical `book`.

- When the resolution is `replacement_required`, share the link and stop. After the user completes it and asks to continue, search again and get a new purchase approval instead of rerunning the old `book`.

- When the resolution is anything else or missing, share the link and stop, without assuming the request can resume.

- A `failed`, `terminal_status` or `unsupported` Link result ends the attempt. Report it, and do not retry or create another spend request.

- Before any approval or submission for this purchase, correct validation errors; for an expired offer, search the itinerary again and present fresh terms for approval.

- After approval or submission for this purchase, follow the returned outcome's recovery rule. Expiry does not resolve booking or funding uncertainty or permit retry or replacement.

- An `approved_credential_unresolved` result means stop. Explain that payment credentials are unavailable and this attempt stopped before submitting a booking, and that any card authorization or hold is unknown. Do not retry `book`, offer retry or replacement choices, or start another purchase while the state is unresolved.

- A missing charge or hold, or renewed permission to buy, does not prove that the payment state is resolved. This checkout cannot resolve it and has no supported recovery action or verified escalation destination. Tell the user that limitation, and do not promise when another purchase can begin or invent a condition for treating the payment as resolved.

- `checkout_receipt_unverified` means the attempt is closed, but its saved receipt does not establish whether a booking or payment occurred. Report both as unknown and stop. Do not retry or start a replacement purchase, infer resolution from a missing booking or charge, elapsed time or renewed permission, or invent a recovery action.

- `checkout_preparation_rejected` preserves a known traveler-profile requirement during 3DS preparation. This attempt did not submit its order or payment; earlier bookings and funding remain unverified. Explain the required profile details and stop. Updating them or renewing permission does not resolve funding uncertainty or permit another purchase.

- `held_payment_failed` preserves Duffel's failed status for the listed payment attempt on an existing order. Report those references and that status without inferring the current order status, other payments, refunds or hold release. Stop; do not retry payment or start a replacement purchase while those effects remain unknown.

- `order_submission_rejected` confirms rejection of this submission only; `merchant_outcome_unknown` leaves it unconfirmed. Earlier bookings and funding remain unknown in both cases. Do not claim that no booking exists, that no payment was captured, or that an authorization will be released. Stop; do not retry `book` or start a replacement purchase. A missing `booking-status` order or renewed permission resolves neither booking nor funding.

- `supplier_confirmed_details_pending` means the supplier reports confirmation, but booking details are unavailable. Tell the traveler their reservation was reported confirmed and this flow cannot retrieve the missing booking reference or ticket details; do not claim ticket issuance or settled payment. `booking_outcome_unknown` means confirmation is still unknown. Neither permits another `book` call or a replacement purchase.

- Keep the returned `checkout_operation_id` and original `offer_id` for recovery. `/opt/hatch/bin/duffel booking-status --checkout-operation-id OPERATION_ID --offer-id ORIGINAL_OFFER_ID` reads saved evidence only, including after restart or offer expiry. It does not contact the provider or reconcile later changes. Tell the traveler this flow cannot fetch missing booking details or resolve an unknown outcome. Do not promise booking references or tickets from later status checks. `observation_persistence: unconfirmed` means the response distinction may not survive restart; unavailable or absent evidence never proves no booking. Do not refresh the offer to recover this purchase or repeatedly poll this local read. Later reconciliation is not available in this flow.

- A timeout, a 5xx, `result_unknown: true` or an error saying the outcome is unknown or unconfirmed means the booking or cancellation may already have happened. Run `booking-status` before anything else, and never resend `book` or `cancel-booking` or claim an outcome.

- An uncertain customer-profile creation has not started payment. Ask for profile recovery instead of creating the profile again.

- After a partial split purchase, report the completed booking references and every unpurchased leg, then stop buying or cancelling until the user decides.

- A success with `resource_authorization.persisted: false` is still a booking. Report it, warn that later management may be unavailable, and never book again.

- The same offer with the same booking data is the same checkout and can resume. A new offer starts another checkout and may place another hold, so it is never an automatic retry.

- After success, report every carrier booking reference and ticket status from the receipt. A loyalty account marked `not_confirmed_on_order` is unconfirmed, not rejected. Suggest checking with the airline using the booking reference, and never rebook to fix it.

## Manage a booking

```sh
/opt/hatch/bin/duffel booking-status
/opt/hatch/bin/duffel booking-status ORDER_ID
/opt/hatch/bin/duffel cancellation-quote ORDER_ID
/opt/hatch/bin/duffel cancel-booking QUOTE_ID
```

- `booking-status ORDER_ID` looks up a booking. If you don't have the ID, run `booking-status` and match the trip's dates, route and total before sharing a confirmation number. It checks up to 25 bookings made here, so the list may be incomplete.

- `cancellation-quote` does not cancel. Report its refund amount, refund destination, airline credits and expiry. A null refund amount means the carrier gave no quote, not zero.

- `cancel-booking` rechecks the exact quote and asks for approval once before the irreversible cancellation.

- This connector does not handle paid bags or other extras, cancelling some passengers, date, time or name changes, pets, unaccompanied minors, check-in or boarding passes. Direct those to the airline instead of improvising with raw APIs.

## Check the fare on a booked trip

- Flight Tracking's fare job runs this check daily. Write these rules into the job's body.

- Run exactly one `search` per run for the complete booked itinerary and passenger mix, with `--limit 30`, saved to a new file. Never reprice with a browser or web search, and never retry a failed scheduled search. The next run tries again.

- Compare an offer only when its priced scope matches the booked baseline exactly. That means every leg's dated flight numbers and airports, the passenger mix, the cabin or fare family, included bags, stop pattern, refund and change restrictions, currency and the basis for taxes and fees.

- Never compare a one-way or single-leg offer with a round-trip or multi-leg total, and never split a booking total across legs unless line-item prices give the exact amount.

- Treat three baseline gaps as missing scope. An unstated booked fare family makes any basic, light or saver brand non-comparable. Extras in the paid total must be removed, or the candidate's price for the same extras added. A total that may not cover every traveler is not comparable.

- Record a missing or mismatched scope as non-comparable, clear any pending candidate tied to it, and stay silent.

- Net savings are the fare drop minus known change, cancellation and rebooking costs. A candidate qualifies when net savings exceed 10 percent of the original paid total or the booking-currency equivalent of USD 100.

- Convert USD 100 with a fresh exchange-rate source and record that source's time. When no reliable rate is available, use only the 10 percent threshold.

- The first qualifying candidate is not an alert. Save it as pending, with its itinerary, total, currency and check time, and update the same fare job to run once about an hour later.

- On that confirmation run, search once more and confirm only when equivalent inventory still qualifies. Clear the pending candidate when it has disappeared, no longer matches or fell below both thresholds. Keep it with a failure note when the search failed. Return the job to its daily schedule after any of these outcomes.

- Before notifying, read the owner's recent activities for a later booking change, such as a rebooked leg or an added traveler. If the booking changed, update the baseline, clear the candidate and stay silent.

- When the candidate is confirmed, save the comparison and notify under Flight Tracking's notice rules. Say when the fare was confirmed, that fares can change before the user acts, and ask whether they want help investigating a credit, refund or rebooking.

- If the user says yes, run one fresh search before quoting savings. That answer authorizes investigation and preparation only, so never promise that a credit or refund will be granted.

## Talk about results

- In replies, name the airlines, itineraries and fares. Never name Duffel, show commands or `off_`, `ord_` and `ore_` IDs, or ask the user to choose between Duffel and the airline. The approval and receipt carry any required attribution.

## Related skills

- [Flight Booking](/opt/muse/skills/flight-booking/SKILL.md)

- [Flight Tracking](/opt/muse/skills/flight-tracking/SKILL.md)

- Use `muse.skill_search` to find other skills and `muse.connector_search` to find other connectors.

### When available

- These skills depend on the user's channel or devices. `muse.skill_search` shows which ones this session has.

- [Deal Monitoring](/opt/muse/skills/price-tracker/SKILL.md)
