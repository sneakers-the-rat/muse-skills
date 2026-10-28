# Agoda

- `/opt/hatch/bin/agoda` searches places to stay, flights, tours, attraction tickets and experiences. Booking continues on Agoda's website through a returned link.

## Connect an account

- `status` returns `connect_url` when consent is needed. Share that exact link as `[Connect Agoda](<connect_url>)`, never one you composed, and check `status` again after the user connects. `disconnect` removes the connection, so do not send the user to Settings.

- `unavailable` means Agoda cannot be used here, so skip the connection offer and use the other routes.

## Search

```text
/opt/hatch/bin/agoda search --type <accommodation|flight|activity> --query '<full request>' [--currency SGD] [--locale en-us]
```

- Each call is independent. Include the complete destination or route, dates with the year, travellers, budget and currency. Stays also need rooms and children’s ages; flights need the cabin. Use the details established by the active travel skill, and make one call per product type.

- Use `--type activity` for tours, attraction tickets, experiences and airport transfers.

- `--full` returns Agoda's complete reply when the compact view lacks a detail the user asked for.

## Results and booking

- Agoda’s returned booking URLs carry pricing context and attribution. Share or open them unchanged. An option without a returned booking URL has no verified Agoda booking route. When Agoda returns no matching results, relay its explanation if one is provided.

- State each hotel price with its returned basis and tax coverage, using `price.description` or `price.basis` in compact results and Agoda’s own wording in full replies. Say when the basis is unstated. Prices and availability can change.

- Cheapest-date flight results are indicative per-person starting fares, not confirmed prices for a specific flight. The selected flight’s price may differ.

- Keep a hotel's star rating (`star_rating`, such as 4★) separate from its guest review score and review count.

- When the user asks to book, open the returned URL with `browser.browse` using `task_id: "new"`. Keep the returned `task_id` through review, changes, submission and verification, following [browser booking](/opt/muse/assets/booking/references/browser-booking.md) and [checkout](/opt/muse/assets/booking/references/checkout.md).

## Related skills

- [Flight Booking](/opt/muse/skills/flight-booking/SKILL.md)

- [Hotel Booking](/opt/muse/skills/hotel-booking/SKILL.md)

- [Place Discovery](/opt/muse/skills/place-discovery/SKILL.md)

- [Trip Planning](/opt/muse/skills/trip-planning/SKILL.md)

- Use `muse.skill_search` to find other skills and `muse.connector_search` to find other connectors.
