# Agoda

- `/opt/hatch/bin/agoda` searches places to stay, flights, tours, attraction tickets and experiences. Booking continues on Agoda's website through a returned link.

- Agoda needs no sign-in. A reply with `status: unavailable` means Agoda can't be used on this VM, so use the other routes.

## Search

```text
/opt/hatch/bin/agoda search --type <accommodation|flight|activity> --query '<full request>' [--currency SGD] [--locale en-us] [--limit N]
```

- Each call is independent. Include the complete destination or route, dates with the year, travellers, budget and currency. Stays also need rooms and children’s ages; flights need the cabin. Use the details established by the active travel skill, and make one call per product type.

- Pass `--currency` with the currency established for the trip on each product search, including activities. If the reply uses another currency, report the mismatch and keep the returned currency with its amounts. Compare amounts only in matching currencies.

- Use `--type activity` for tours, attraction tickets, experiences and airport transfers.

- The CLI sizes its output to be read in full, so read the complete JSON. Use `--limit` to request fewer compact hotel results when the user asks for a shortlist.

- `--full` returns Agoda's complete reply when the compact view lacks a detail the user asked for.

## Results and booking

- Agoda’s returned booking URLs carry pricing context and attribution. Share or open them unchanged. An option without a returned booking URL has no verified Agoda booking route.

- When Agoda returns no matching results, relay its explanation if one is provided.

- State each hotel price with its returned basis and tax coverage, using `price.description` or `price.basis` and `price.taxes` in compact results and Agoda’s own wording in full replies. With `basis: PER_BOOK`, `price.amount` is the booking total. Label `price.average_per_night` as a calculated average for comparison, not an offered nightly rate or a verified checkout price. Say when the basis is unstated. Prices and availability can change.

- `flight_code` joins the returned airline code and flight number. A field marked `omitted: true` with `reason: text_limit` is unknown in this view; use `--full` if that detail is needed.

- Cheapest-date flight results are indicative per-person starting fares, not confirmed prices for a specific flight. The selected flight’s price may differ.

- Keep a hotel's star rating (`star_rating`, such as 4★) separate from its guest review score and review count.

- When the user asks to book, use `browser.browse` with the returned URL and follow [browser booking](/opt/muse/assets/booking/references/browser-booking.md) and [checkout](/opt/muse/assets/booking/references/checkout.md).

## Related skills

- [Flight Booking](/opt/muse/skills/flight-booking/SKILL.md)

- [Hotel Booking](/opt/muse/skills/hotel-booking/SKILL.md)

- [Place Discovery](/opt/muse/skills/place-discovery/SKILL.md)

- [Trip Planning](/opt/muse/skills/trip-planning/SKILL.md)

- Use `muse.skill_search` to find other skills and `muse.connector_search` to find other connectors.
