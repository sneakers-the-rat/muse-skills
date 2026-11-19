# Duffel hotel stays

- These commands are for hotel stays. They're hidden from `--help`, so use them as shown here.

- Duffel books rates paid by card, in US dollars, and only for US accounts. Each hotel a search returns comes with its cheapest such rate, and the quote says when it's paid: now or at the hotel.

## Search

- Get the destination's coordinates from `map.geocode`, after loading the `map` namespace with `tool_search.load_tool_namespace`. Pass the destination as the user named it in `--location`.

```sh
/opt/hatch/bin/duffel stay-search --location "PLACE" \
  --latitude LAT --longitude LNG \
  --check-in 2026-12-04 --check-out 2026-12-06 --room 2 > /tmp/hotels-PLACE.json
```

- Pass one `--room` per room: the number of adults, then any child ages after a colon, such as `--room 2:5,9`.

- Optional flags: `--radius-km` (1–20, default 5), `--free-cancellation` to keep only hotels that offer it, and `--limit` (1–10, default 6) for how many hotels to price. A search can take a minute.

- The JSON goes to the file. Stderr lists each hotel with its prices, room, cancellation terms, and the `search_result` and `rate` IDs the next commands take.

- `stay-rates` shows the full details of a rate the search chose, as the search found it. It takes `--search-result` and `--rate` plus the same stay flags, and works for 30 minutes after the search.

## Hotel cards

- To show the hotels as cards, pass the search file unchanged to `travel.create_hotel_results_widget`, with up to four `hotel_id` values in `hotel_ids`. The cards read the hotels, prices and photos from it.

## Quote

```sh
/opt/hatch/bin/duffel stay-quote --search-result SEARCH_RESULT_ID --rate RATE_ID
```

- Quote the rate the user picked before asking for guest details, so they confirm the price first.

- When the user presses Book on a card, the selection gives the `search_result_id` and `rate_id` to quote.

- The quote has the current price and terms: what's charged now, any amount due at the property, the total, the cancellation terms and the rate's `conditions`. The user needs to see these before booking, including anything that changed since the search.

- A fee paid at the hotel, such as a resort fee, can appear only in `conditions` while `due_at_property` is zero, so the total may not include it.

- `ok: false` with a `code` means the rate can't be booked here, and `error` says why.

- `ok: false` without a `code` means the quote request failed, not that the rate is gone. `retriable: true` means quoting again is safe.

- A quote can be booked for up to 30 minutes.

## Book

```sh
/opt/hatch/bin/duffel book --quote-id QUOTE_ID \
  --booking-json '{"guests":[{"given_name":"GIVEN","family_name":"FAMILY"}],"email":"EMAIL","phone_number":"PHONE"}'
```

- List the lead guest first in `guests`, with no more guests than the search had travelers. The hotel holds the booking under the lead guest.

- `email` and `phone_number` are the lead guest's. The phone needs its `+` country code.

- If the quote names a `loyalty_programme` and the user has a number for it, add it as `loyalty_programme_account_number` in `--booking-json`.

- If the quote's `next_step` asks for the account holder's details, add `--customer-email`, `--customer-given-name` and `--customer-family-name`.

- `book` asks the user to approve, then books with their Link card. A pay-now rate is charged at booking. A guarantee rate charges nothing at booking. The guest pays at the hotel, and the card guarantees the booking, so the hotel can charge it as the rate's terms allow. The approval shows the hotel, dates, rooms, guests, room, amounts and cancellation terms.

- `booking_confirmed` includes the hotel's booking `reference`. `supplier_confirmed_details_pending` means the hotel confirmed the booking and the reference comes later.

- `booking_outcome_unknown` means the booking may exist. Booking the same quote or stay again could book it twice.

- `booking_rejected` and `booking_not_sent` mean nothing was booked. Their `next_action` says what can happen next.

- These commands can't look up, change or cancel a stay yet. If the user asks to, say so and share the cancellation terms they approved.
