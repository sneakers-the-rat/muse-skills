# Book a Duffel offer

- Use this guide once the user picks a complete offer to book. [Uncertain results](recovery.md) covers what follows a timeout, an unknown outcome or a Link action.

## Prepare passengers and seats

- `seat-options --offer-id OFFER` returns bookable seats for each passenger, and the flag repeats for a short list of offers. A zero price means no added fee, and an omitted seat is unavailable. Adjacent seats share a row and section on the same side of the aisle.

- Choose at most one seat per passenger and segment. Repeat `--seat PASSENGER:SEGMENT:SEAT`, with one-based numbers, once per seat, such as `--seat 1:1:28B --seat 2:1:28C`; the CLI reads each flag as one seat. Mention seat choice once without letting it block the booking.

- After the user picks an offer, ask only for what validation requires. That is each traveler's legal given and family name, birth date, title (`mr`, `ms`, `mrs`, `miss` or `dr`) and gender (`m` or `f`), one reachable trip email and phone, which each passenger entry carries and can share, the adult with each lap infant, and passport details only when validation asks. Ask for a loyalty account number only when the user wants credit. These values are for this booking's `validate-booking` and `book` only; keeping them out of memory and out of replies protects the traveler's identity.

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

- For a lap infant, add `"accompanying_adult": N` with the adult's one-based position. A required passport goes in the passenger's `identity_documents` array with `type: "passport"`, the number as `unique_identifier`, an uppercase two-letter `issuing_country_code` and `expires_on` as `YYYY-MM-DD`. Identity details come from the traveler, since an empty or invented document makes the booking fail or tickets the wrong person, and a traveler who has not been born cannot be ticketed. For an unborn traveler, booking waits until birth, and later fares, availability and seats are unknown until then.

- Offer loyalty credit once without letting it block the booking. When the user wants it, add the account to that passenger as `"loyalty_programme_accounts": [{"airline_iata_code": "UA", "account_number": "ACCOUNT_NUMBER"}]`, with one object per programme. Validation confirms whether the airline supports it, and the user decides whether to drop an account that fails.

- Leave out the fields the CLI owns, which are `id`, `infant_passenger_id`, `user_id`, `type`, `selected_offers`, `services`, `payment` and `payments`.

## Validate and book

```sh
/opt/hatch/bin/duffel validate-booking --offer-id OFFER --booking-json JSON
```

- Validation refreshes the offer and checks travelers, documents, seats and loyalty, without payment or approval. Ask for every `required_missing` and `invalid` item together and rerun until `ready_to_book: true`.

- Treat `selected_offer` as the current itinerary, price, bags and fare terms. Check each slice's `from` and `to` against the chosen airports, and stop if they differ.

- When validation asks for a first-time payment profile, pass the account holder's email and legal name with `--customer-email`, `--customer-given-name` and `--customer-family-name` to both validation and booking. This profile is not a passenger, and it is created only after purchase approval.

- List payment methods as [Link by Stripe](/opt/hatch/connectors/stripe-link/CONNECTOR.md) describes. Book once with the same booking JSON and seats. Add `--payment-method-id ID` only for a card the user chose for this purchase. Otherwise, approval preselects the default card or a usable card if none is default. The user can change it there.

```sh
/opt/hatch/bin/stripe-link payment-methods list --format json
/opt/hatch/bin/duffel book --offer-id OFFER --booking-json JSON --seat 1:1:28B --seat 2:1:28C
```

- `book` revalidates before any payment request. Its single approval covers the itinerary, travelers, seats and fees, fare terms, total, the first-time profile, a one-time virtual card, 3DS and immediate ticketing. Any change to the flight, fare, date, passengers, services or total needs a fresh approval.

- Held orders, Duffel balance payment, inline cards and raw order APIs are not supported.

- If Link is not connected, explain the one-time virtual card and share its connection link. For an airline-site fallback, use `browser.browse` and follow `~/docs/chat/payments-and-purchases.md`. A card the user supplies for that booking may go to the browser task as text with `wallet: null`; the browser checkout still requires payment approval. This does not enable inline cards in the Duffel API. If neither supported route works, stop with the itinerary prepared and say that payment is blocked.

- Prefer one offer that covers the whole itinerary. Split it into separate bookings only with the user's agreement before the first `book`. Explain that each booking has its own approval, payment and terms, that later offers are not held, and that a later failure can leave earlier tickets booked.

- For a split trip, validate both tickets before booking either, so a price change or missing detail shows up before any purchase. Then book each ticket's `id` with its own `book`.
