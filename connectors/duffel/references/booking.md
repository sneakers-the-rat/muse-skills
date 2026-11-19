# Book a Duffel offer

- Use this guide once the user picks a complete offer to book. [Uncertain results](recovery.md) covers what follows a timeout, an unknown outcome or a Link action.

## Prepare passengers and seats

- `seat-options --offer-id OFFER` returns bookable seats for each passenger with their `position` (window, aisle or middle), and the flag repeats for a short list of offers. A zero price means no added fee, and an omitted seat is unavailable. Each seat also carries `exit_row` and `over_wing` when they apply, an upper `deck` when the map states one, the airline's `disclosures`, such as limited recline or no window, and each traveler's price in `available_for`. The flight's `cabin` names the class of its bookable seats, or each seat does when they differ. `flights_summary` counts, per flight and in seats (each seat once, whatever the number of travelers), the bookable, free and paid seats, the free ones by position and in exit rows, and gives the paid seats' per-traveler price range when one currency covers them. Flights Duffel returned no seat map for are listed under `segments_without_seat_map`, and a `seat_map_request_failed` result means the request itself failed and availability is unknown. Adjacent seats share a row and section on the same side of the aisle.

- Choose at most one seat per passenger and segment. Repeat `--seat PASSENGER:SEGMENT:SEAT`, with one-based numbers, once per seat, such as `--seat 1:1:28B --seat 2:1:28C`; the CLI reads each flag as one seat.

- When the user picks an offer, run `seat-options` for it and propose a free seat for each traveler on each flight: their saved or stated preference, otherwise a window or aisle, with travelers who fly together side by side. Weigh each seat's facts before choosing. An `exit_row` seat brings extra legroom and the airline's exit-row conditions, so offer it to a traveler who wants legroom and skip it for a child, an infant's adult or anyone a disclosure excludes. Pass over a seat whose `disclosures` say limited recline, no window or a lavatory beside it unless nothing else fits. `over_wing`, `deck` and `cabin` say where it is.

- Name each proposed seat in the review message with its position, what makes it the pick and that it is free, as a choice the traveler can change or decline before validation, and carry their answer into `--seat`. A reply that says nothing about seats keeps the proposed ones, which the approval card then shows. When no free seat fits, when `flights_summary` shows few free seats or none in their preferred position, or when a paid seat fits much better than any free one, name the cheapest paid seat that fits with its price, once, and keep the booking moving without waiting for a seat choice.

- When Duffel returned no seat map for a flight, say so once in that same review message, with the airline assigning that flight's seats at check-in, and go on with the booking here. The airline's website is not a place to look for that flight's seat map or to pick its seats, so no browser task is started for it.

- A `seat_map_request_failed` result is a different case: the request failed, so whether those flights have seats to choose is unknown, and nothing in it says how the airline assigns them. Its `seat_map_status` and `seat_map_error_codes` carry what came back. Say once in that same review message that the seat map could not be read, and keep the booking moving without waiting for a seat choice.

<!-- duffel-bags-only:start -->
- The fare's own bag allowance is on each flight row. When the user wants more checked bags than it includes, or asks to add one, `bag-options --offer-id OFFER` lists the bags the airline sells with that offer: each traveler's bags per journey, with type, weight limit, how many can be added and the price per bag. An empty list means Duffel sells no extra bags for it, so the airline's site is the place to add them after booking.

- Add each bag with `--bag BAG:QUANTITY` on `validate-booking` and `book`, using `bag` from that list, such as `--bag 1-1.1-checked-23kg:1`. Bag prices are added to the total the user approves, so the user should know each bag and its price before they approve.
<!-- duffel-bags-only:end -->

- When the user picks an offer, call `wallet.list_payment_methods` with `provider: "stripe-link"` and `wallet.get_user_info` in the same turn. Fill the trip email and phone from the conversation, `~/USER.md` and `wallet.get_user_info`. Use the user's own name for a passenger only when the conversation shows the user is flying; each other passenger needs their own legal name. Show the prefilled name, email and phone in your question so the user can correct a name that differs from their ID.
- In the same `wallet.get_user_info` result, `agent_wallet_spend_limits` holds the user's Link limits in minor units. When the offer is in the wallet's `default_spend_request_currency` and its total is above `per_transaction.limit` or the `daily` or `thirty_day` `remaining`, tell the user before collecting details: they can raise the limit in Link, which covers every Link card, or book on the airline's own site. `book` refuses such a purchase before the approval card with `link_spend_limit_exceeded`. When the currency differs or `default_spend_request_currency` is absent, skip this check and let `book` decide.

- Show the chosen trip in that same message, so the traveler can ask for changes before validation: each flight with its date, times and flight number, the cabin and the fare brand exactly as the offer names it, bags, change and refund terms, each proposed seat, and the total. Then ask for what is still missing: usually each traveler's birth date and gender (`m` or `f`), and each traveler's legal given and family name when not already known. If Link is `not_connected`, ask for what is still missing first, then end that message with Link's connection link (`next_action.markdown`, unchanged), so the user connects while answering.

- Validation also needs the adult with each lap infant, and passport details only when it asks. The CLI sets `title` from gender and gives every passenger the first passenger's email and phone, so ask for a title or a second contact only when the traveler wants one. Ask for a traveler's loyalty account number as one optional item in that same question when the travel profile lists their program with the airline or a partner that credits it, lists the airline among the ones they fly, or the travel history shows an earlier flight on it. Use a number they already gave, and when they have none, book without it rather than asking again.

- All traveler details for this booking are for its `validate-booking` and `book` only. Keeping them out of memory, and out of replies apart from the prefilled name, email and phone shown for confirmation, protects the traveler's identity.

- Put passengers in `data.passengers` in search order:

```json
{
  "data": {
    "passengers": [{
      "given_name": "Legal given name",
      "family_name": "Legal family name",
      "born_on": "1990-01-01",
      "gender": "f",
      "email": "trip-contact@example.com",
      "phone_number": "+14155550123"
    }]
  }
}
```

- For a lap infant, add `"accompanying_adult": N` with the adult's one-based position. A required passport goes in the passenger's `identity_documents` array with `type: "passport"`, the number as `unique_identifier`, an uppercase two-letter `issuing_country_code` and `expires_on` as `YYYY-MM-DD`. Identity details come from the traveler, since an empty or invented document makes the booking fail or tickets the wrong person, and a traveler who has not been born cannot be ticketed. For an unborn traveler, booking waits until birth, and later fares, availability and seats are unknown until then.

- Add each traveler's loyalty account to their passenger whenever they have one for the airline or a partner program that credits it, as `"loyalty_programme_accounts": [{"airline_iata_code": "DL", "account_number": "ACCOUNT_NUMBER"}]`, with one object per programme. It puts their status and mileage earning on the booking, and a traveler without the number at hand still books. Validation confirms whether the airline supports it, and the user decides whether to drop an account that fails.

- Leave out the fields the CLI owns, which are `id`, `infant_passenger_id`, `user_id`, `type`, `selected_offers`, `services`, `payment` and `payments`.

## Validate and book

```sh
/opt/hatch/bin/duffel validate-booking --offer-id OFFER --booking-json JSON
```

- Validation refreshes the offer and checks travelers, documents, seats and loyalty, without payment or approval. Ask for every `required_missing` and `invalid` item together and rerun until `ready_to_book: true`.

<!-- duffel-payment-readiness-only:start -->
- Validation also checks whether Link can pay. `payment_setup_required` means `book` would stop for Link setup, even when `ready_to_book` is true. Share its `next_action.markdown` unchanged at the end of the same message that asks for any missing details, so the user sets up Link while answering, and don't run `book` until Link is ready. Keep the offer and booking JSON and follow its `resume`; the user doesn't pick the flight again.
<!-- duffel-payment-readiness-only:end -->

- Treat `selected_offer` as the current itinerary, price, bags and fare terms. Check each slice's `from` and `to` against the chosen airports, and stop if they differ.

- Pass the account holder's email and legal name on the first `validate-booking`, using what the user said and filling only missing fields from `wallet.get_user_info`, with `--customer-email`, `--customer-given-name` and `--customer-family-name`, so a first booking needs no extra round for its payment profile. Validation ignores them once a profile is stored. Pass the same three flags to `book` only when validation returned `customer_profile_stored: false`. This profile is the account holder, not a passenger, and it is created only after purchase approval.

- If Link connects before the traveler details arrive, confirm it in one line and wait for them. Once the details are in, validate and `book`; the approval card handles the card choice.

- Book once with the same booking JSON and seats, after Link is connected as [Link by Stripe](/opt/hatch/connectors/stripe-link/CONNECTOR.md) describes. Add `--payment-method-id ID` only for a card the user chose for this purchase. Otherwise, approval preselects the default card or a usable card if none is default. The user can change it there.

```sh
/opt/hatch/bin/duffel book --offer-id OFFER --booking-json JSON --seat 1:1:28B --seat 2:1:28C
```

- `book` revalidates before any payment request. Its single approval covers the itinerary, travelers, seats and fees, fare terms, total, the first-time profile, a one-time virtual card, 3DS and immediate ticketing. When the card shows an "Authorized up to" amount, the airline's final total may be charged up to that amount if it settles slightly above the approved total after the order is sent. Any change to the flight, fare, date, passengers, services or total before payment needs a fresh approval.

- `book` reads the live offer itself, including one whose quote expired, and the approval card shows its current total and fare terms. When they differ from what was last quoted, the card says what changed. If Duffel no longer sells the offer, `book` returns `offer_unavailable` with `next_step: search_again`: search the same route and dates again and let the user choose, since a different flight is a new purchase for them to pick.

- When the price changes after approval, `book` closes that checkout and re-quotes the offer in the same call; see `next_step: requote` in [recovery](recovery.md).

- Held orders, Duffel balance payment, inline cards and raw order APIs are not supported.

- If Link is not connected, explain the one-time virtual card and share its connection link.
<!-- duffel-payment-readiness-only:start -->
  When `book` itself stops for Link setup, its `resume` says how to continue: once Link is ready, rerun the same `book` unchanged rather than starting the booking over.
<!-- duffel-payment-readiness-only:end --> For an airline-site fallback, use `browser.browse` and follow `~/docs/chat/payments-and-purchases.md`. Use Wallet for secure payment or assign browser takeover for the user to enter payment on the merchant site. Do not pass card details in task text. If neither supported route works, stop with the itinerary prepared and say that payment is blocked.

- Prefer one offer that covers the whole itinerary. Split it into separate bookings only with the user's agreement before the first `book`. Explain that each booking has its own approval, payment and terms, that later offers are not held, and that a later failure can leave earlier tickets booked.

- For a split trip, validate both tickets before booking either, so a price change or missing detail shows up before any purchase. Then book each ticket's `id` with its own `book`.
