# Compare flights

- Use this guide for a flight request. Add Trip Planning only when the user wants help with the wider trip.

## Establish the search

- Establish the route, dates, travelers with children's ages, cabin and how flexible the user is. Search with natural assumptions, such as one adult flying one way, and state them. Ask only for a missing detail that would change the route, price or traveler.

- When the user gives exact dates, search them without a separate date check. Work out relative dates such as "next Friday" in the origin's timezone, and check a connected calendar for hard conflicts.

- Price children by their age on the final travel date. Ask whether an infant under two will sit on a lap or in a seat, and ask once for any missing ages rather than guessing.

- Use relevant preferences for airlines, airports, seats and connections. One past trip is a hint, not a standing preference. Identity, accessibility needs and room to exceed a budget come from the user rather than inference.

- Check loyalty status, credits and card benefits when they could change the choice, and confirm that a credit applies to the operating or marketing carrier and has not expired. A linked card shows which card the user holds, not its reward rules or a points balance. Mention a useful program and tier name once, without the membership number.

## Search connectors first

- Search a connector that sells bookable fares before any website. Cover every airport, cabin and date the request allows in as few searches as its docs allow, and choose from the options it returns, as its docs describe.

- For a request for an exact flight, the bookable offer is one that carries that flight number. Schedule data shows a flight operates, not that it can be booked, and a different flight is a different request.

- A flight search is short enough to need no todo list, and its results and picks change quickly, so they become memories only when the user asks.

- A carrier missing from a connector's results may still fly the route. Run one targeted search for a requested or expected carrier, as the connector's docs describe.

- Keep connector searches and the combined comparison in the main conversation. A connector's request limits apply to that connector, not to other legitimate sources.

## Fall back to Google Flights

- Check Google Flights only after showing the connector's options, and only when the connector search fails, is unavailable, is refused for this user's country or finds nothing useful; when a carrier the user named, or one that dominates the route such as Southwest, is absent from the results after the targeted search; or when the user asks for a wider comparison. Low-cost carriers already in the results are covered.

- Present any useful connector offers first and say in one sentence that you are checking Google Flights and why. Then run one `browser.browse` research task with a complete brief, since it cannot see this conversation: the airports and allowed alternatives, dates, travelers with ages, cabin, bags, connection limits, and the goal of finding both the shortest practical trip and the lowest worthwhile price. Ask it to research without purchasing and to return complete itineraries with the payable total, fare terms, seller URL and time checked.

- A Google Flights price is a lead until a connector or the airline reproduces it. When a lead looks meaningfully better and no connector sells it, mention its airline, flights and price in one sentence and offer to check it on the airline's site. When Google Flights is blocked or fails, say so once and keep the connector results.

- When a targeted connector search after the check adds a better or materially different bookable trip and the user has not chosen a flight, present one replacement list that says it supersedes the earlier one. Once the user has chosen, keep that choice, mention the better option in one sentence, and change the selection only if they ask.

- Search another comparison site or seller, listed in [other sources](sources.md), only when the user asks for more coverage. Following a chosen offer to its airline or seller to verify it is not another search.

## Verify comparable offers

- Follow a promising result to the airline or seller and confirm every segment, every passenger and the full payable total in one currency. Keep a cached or teaser price out of the bookable shortlist until the seller reproduces it.

- Whole itineraries compare cleanly: a one-way price set against a round-trip total, or a quietly changed airport, date or cabin, misleads the choice.

- Check the cabin on every segment. A business-class label can include an economy leg, so describe a mixed cabin as mixed.

- Compare bags, seats, change and refund terms, and who services the ticket afterward. Add required bag and seat fees before calling a fare the cheapest. An unknown term is neither restrictive nor flexible.

- Treat separate tickets and self-transfers as their own kind of trip. Account for collecting and rechecking bags, transit entry rules, connection time and a missed connection that no airline will protect, and label them clearly.

## Rank a short list

- Rank verified total price and total travel time together, within the requested cabin. When the shortest practical trip and the cheapest worthwhile trip differ, show both and say what the extra money or time buys.

- Drop any option that costs more and takes longer than another with equivalent terms. Then weigh the number of legs, ground transfers, arrival time, connection reliability and flexibility.

- Recommend the tradeoff that fits this request without inventing a universal price for the user's time. Include a flexible fare when it is a meaningful alternative, and leave out near-duplicates.

- A fare is the lowest found among the sources checked, which is different from the lowest available anywhere.

- Stop when the leading options are verified with their sellers and more searching is unlikely to change the choice. When a missing carrier could change it, run the targeted connector search, then offer the airline's site.

## Present the flight list

- Load the `widget` namespace with `tool_search.load_tool_namespace`, and show the options as a native flight list with `widget.create_list_widget`: one flight row per offer pointer the connector gives. When the tool is absent or a valid call returns an explicit unsupported or rendering error, the connector's option lines read well as a short list, as they are; they already carry what a table would. Rows point at bookable offers, which a Google Flights lead isn't.

- Create the list in the main conversation. Add a short recommendation and the decisive tradeoff in a sentence or two. The list already shows the flights, so repeating them as prose, a table, a shopping widget or an options picker adds noise.

- A one-way trip is one list. For a trip that is ready to book, omit `flight_action` so the runtime supplies its booking action.

- A round trip is two lists when the connector groups return flights by outbound. First the outbound flights, with the action below. Their cards show no price, since each is half a trip, so give each outbound's lowest round-trip price from the connector's lines in the reply. When the user picks one, by tapping or describing it, show the complete round trips sold with it, read from the saved search as the connector's docs describe, with the booking action. Run no new search, and book only an offer from the return list.

```json
{
  "cta_text": "Choose outbound",
  "response_message_prefix": "Show return flights for outbound"
}
```

- For a trip that is still being planned, put this action on the final list instead of the booking action, and return the selection to Trip Planning:

```json
{
  "cta_text": "Add to plan",
  "response_message_prefix": "Add this flight to my trip plan:"
}
```

- Once the user picks a flight to book, [booking](booking.md) covers where to buy, the final review and the confirmation.
