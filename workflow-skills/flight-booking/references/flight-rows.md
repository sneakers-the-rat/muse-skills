# Build flight rows

- Use this guide when creating flight rows with `widget.create_list_widget`. The tool's description defines the row and list fields; this covers filling them so each row matches a bookable offer.

## Rows from a search file

- Save the search output unchanged to a temporary file and pass its path in `data.flight_details_file`, with the `data.json_pointer` the connector gives for each chosen offer, such as "/offers/0". A rewritten or trimmed offer may not match what the provider sells, and copying offers into the tool arguments makes the call large, so leave the file's flight objects as they are. Use a different pointer for each row, and omit it when the whole file is one flight object.

- Keep the file until the list is created. The runtime reads each file once per list and stores the selected data; paths and pointers aren't stored or sent to clients. For a normalized search file, it maps segment `departing_at` and `arriving_at` to the row's local times and derives the display fields, so the offer needs no separate id.

- When the connector names a list of more offers for browsing, its `more_flights` puts the ones you didn't choose in the list's See all view, up to 20 rows with `items`; the chat shows only your `items`. The connector's docs say when to leave it out.

## Rows from a verified website fare

- Supply inline `data.flight_data`, or save the same object to a file, filled from verified facts. Keep known baggage, fare conditions, passenger cabins and durations, and include source summary facts when per-passenger facts are unavailable. Omit unknown optional facts, and use a stable private key for `id` when the source has no offer id.

- Keep slices and segments in travel order: one slice for a one-way trip, two for a round trip, with connections in their slice's `segments`. `price` is the whole trip for all passengers, so a per-slice price or legs from different offers would misstate what the user can buy.

- Set each segment's `depart` and `arrive` to an airport-local ISO 8601 datetime without a timezone suffix, such as "2026-09-15T07:35:00", and get the local date and time for every endpoint before creating the row. The server derives slice endpoints and display strings from the segments. Keep the source's duration strings, since subtracting airport-local clocks gives wrong durations across timezones.

- Put known segment cabins and baggage in `segments[].passengers`; the runtime summarizes them when the facts are complete. With only summary facts, use offer-level `bags` and `slices[].cabin`, and keep the source's `baggage_varies` or `slices[].cabin_varies`. Add a slice's `stops` only for technical stops within a segment; the runtime counts connections.

- Keep each segment's `carrier` and `flight`, its IATA or ICAO code in `carrier_code` when known, and codeshare operators in `operating_carrier` and `operating_flight`. Leave out `response_message`, slice `from` and `to`, offer `stops` and `nonstop`, which the runtime derives.

- Add `flight_link` only for a verified absolute HTTP(S) details URL, and keep checkout credentials out of the row.

## The row's action

- A row offers `Book with Muse` unless the list sets a `flight_action`, such as the planning action in [flight comparison](flights.md). Either way the runtime appends the exact itinerary and total to the reply, and the offer id stays the private checkout mapping. Creating a row doesn't submit it or authorize a purchase.
