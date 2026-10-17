# Compare and book flights

- Use this guide for a flight request. Add Trip Planning only when the user wants help with the wider trip.

## Establish the search

- Work out relative dates in the origin's timezone, and check a connected calendar for hard conflicts.

- Price children by their age on the final travel date. Ask whether an infant under two will sit on a lap or in a seat, and ask once for any missing ages rather than guessing.

- Use relevant preferences for airlines, airports, seats and connections. One past trip is a hint, not a standing preference. Do not infer identity, accessibility needs or permission to exceed a budget.

- Check loyalty status, credits and card benefits when they could change the choice, and confirm that a credit applies to the operating or marketing carrier and has not expired. A linked card shows which card the user holds, not its reward rules or a points balance. Mention a useful program and tier name once, without the membership number.

## Search promising sources

- Keep the source list short. Search beyond the first few sources only when a carrier, airport or fare type that could change the result is missing.

- A carrier missing from one source's results may still fly the route. Run a targeted search for a requested or expected carrier, or check its own site.

- Give each browser task a complete brief, since it cannot see this conversation. Include the airports and allowed alternatives, dates, travelers with ages, cabin, bags, connection limits and the goal of finding both the shortest practical trip and the lowest worthwhile price. Ask it to research without purchasing and to return complete itineraries with the payable total, fare terms, seller URL and time checked.

- Keep connector searches and the combined comparison in the main conversation. A connector's request limits apply to that connector only, never to other legitimate sources.

- A broken site, CAPTCHA or lost session ends that attempt, not the search. Move to another strong source instead of repeating the failed interaction.

## Verify comparable offers

- Follow a promising result to the airline or seller and confirm every segment, every passenger and the full payable total in one currency. Keep a cached or teaser price out of the bookable shortlist until the seller reproduces it.

- Check the cabin on every segment. A business-class label can include an economy leg, so describe a mixed cabin as mixed.

- Compare bags, seats, change and refund terms, and who services the ticket afterward. Add required bag and seat fees before calling a fare the cheapest. An unknown term is neither restrictive nor flexible.

- Treat separate tickets and self-transfers as their own kind of trip. Account for collecting and rechecking bags, transit entry rules, connection time and a missed connection that no airline will protect, and label them clearly.

## Rank a short list

- Drop any option that costs more and takes longer than another with equivalent terms. Then weigh the number of legs, ground transfers, arrival time, connection reliability and flexibility.

- Recommend the tradeoff that fits this request without inventing a universal price for the user's time. Include a flexible fare when it is a meaningful alternative, and leave out near-duplicates.

- Call a fare the lowest found among the sources checked, never the lowest available anywhere.

- Stop when the leading options are verified with their sellers and more searching is unlikely to change the choice. Keep going when a missing carrier, an unclear fare or a coverage gap could change it.

## Present the flight list

- Load the `widget` namespace with `tool_search.load_tool_namespace` and present live comparisons as a native flight list with `widget.create_list_widget`. Use the Markdown fallback in [booking presentation](/opt/muse/assets/booking/references/presentation.md) only when the tool is absent or a valid call returns an explicit unsupported or rendering error. Fix invalid arguments and retry. Output size and schema complexity are not reasons to switch.

- Point connector rows into the saved search file as the connector docs describe, and build rows for browser results from verified flight facts. Put every complete offer for the same itinerary and dates in one list.

- Create the list in the main conversation. When a worker did the search, get its unchanged response file and the chosen offer pointers instead of relaying its table.

- Add a short recommendation and the decisive tradeoff. Do not repeat the flights as prose, a table, a shopping widget or an options picker.

- For a direct booking request or a trip that is ready to book, omit `flight_action` so the runtime supplies its booking action. For a trip that is still being planned, set the list-level action to:

```json
{
  "cta_text": "Add to plan",
  "response_message_prefix": "Add this flight to my trip plan:"
}
```

- Return a planning selection to Trip Planning, which offers the separate choice of booking now or later.

## Review and book

- Follow [checkout](/opt/muse/assets/booking/references/checkout.md) for the final refresh. For a flight, look for changes to bags, airports and the operating carrier as well as the fare, seats and schedule.

- When status, points, credits or certificates could apply, ask one combined question before choosing where to buy. Offer to sign in to the airline and compare cash with points, to check cash only, or to check points only.

- The final review shows the exact itinerary, traveler count, cabin and fare brand, seats, bags, total, any credits or points applied, the amount charged and the fare rules.

- For flights, the confirmation is the airline's booking reference with the status of each ticket. A hold or pending ticketing is not a completed booking.
