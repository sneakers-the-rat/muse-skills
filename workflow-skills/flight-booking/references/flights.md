# Compare flights

- Use this guide for a flight request. Add Trip Planning only when the user wants help with the wider trip.

## Establish the search

- Establish the route, dates, travelers with children's ages, cabin and how flexible the user is. Search with natural assumptions, such as one adult flying one way, and state them. Ask only for a missing detail that would change the route, price or traveler.

- When the user gives exact dates, search them without a separate date check. Work out relative dates such as "next Friday" in the origin's timezone, and check a connected calendar for hard conflicts.

- Price children by their age on the final travel date. Ask whether an infant under two will sit on a lap or in a seat, and ask once for any missing ages rather than guessing.

- Use relevant preferences for airlines, airports, seats and connections. One past trip is a hint, not a standing preference. Identity, accessibility needs and room to exceed a budget come from the user rather than inference.

- Read a cabin request in airline terms. Airlines sell extra legroom in different ways: as an economy fare brand, as a seat added to an economy fare, or as a premium economy cabin, which is mostly on longer flights. When the user names one airline's product, find the matching option on each airline that flies the route and say how they differ.

- Work out what this trip needs before ranking: when the traveler has to arrive or leave, whether they will check a bag, seats together or a preferred seat, and status that brings free bags, seats or upgrades on a carrier. Take these from the request, the travel profile, the calendar and the trip itself, such as a long stay or children making a checked bag likely. Search with a time limit the trip sets, such as a meeting the traveler must reach, and compare each flight's full arrival date and time with it.

- Check loyalty status, credits and card benefits when they could change the choice, and confirm that a credit applies to the operating or marketing carrier and has not expired. A linked card shows which card the user holds, not its reward rules or a points balance. Mention a useful program and tier name once, without the membership number. Status benefits come with the loyalty number on the booking wherever it is bought, as [booking](booking.md) describes.

<!-- gflights-first-off-only:start -->
## Search available connectors first

- Confirm a flight connector is available with `muse.connector_search` before reading its docs or calling its CLI. If none is available, continue directly to the browser fallback below without a trial CLI call.

- Search an available connector that sells bookable fares before any website. Cover every airport, cabin and date the request allows in as few searches as its docs allow, and choose from the options it returns, as its docs describe.

- For a request for an exact flight, the bookable offer is one that carries that flight number. Schedule data shows a flight operates, not that it can be booked, and a different flight is a different request.

- A flight search is short enough to need no todo list, and its results and picks change quickly, so they become memories only when the user asks.

- A carrier missing from a connector's results may still fly the route. Run one targeted search for a requested or expected carrier, as the connector's docs describe.

- Keep connector searches and the combined comparison in the main conversation. A connector's request limits apply to that connector, not to other legitimate sources.

## Fall back to Google Flights

- Use Google Flights or the airline's site directly when no flight connector is available. Otherwise check Google Flights when the connector search fails or finds nothing useful; when a carrier the user named, or one that dominates the route such as Southwest, is absent from the results after the targeted search; or when the user asks for a wider comparison. Low-cost carriers already in the results are covered.

- Present any useful connector offers first and say in one sentence that you are checking Google Flights and why. Then run one `browser.browse` research task with a complete brief, since it cannot see this conversation: the airports and allowed alternatives, dates, travelers with ages, cabin, bags, connection limits, and the goal of finding both the shortest practical trip and the lowest worthwhile price. Ask it to research without purchasing and to return complete itineraries with the payable total, fare terms, seller URL and time checked.

- A Google Flights price is a lead until an available connector or the airline reproduces it. When a lead looks meaningfully better and no available connector sells it, mention its airline, flights and price in one sentence and offer to check it on the airline's site. When Google Flights is blocked or fails, say so once and keep any useful connector results; if there are none, check the airline's site.

- When a targeted connector search after the check adds a better or materially different bookable trip and the user has not chosen a flight, present one replacement list that says it supersedes the earlier one. Once the user has chosen, keep that choice, mention the better option in one sentence, and change the selection only if they ask.

- Search another comparison site or seller, listed in [other sources](sources.md), only when the user asks for more coverage. Following a chosen offer to its airline or seller to verify it is not another search.
<!-- gflights-first-off-only:end -->
<!-- gflights-first-only:start -->
## Search Google Flights first

- This applies when `muse.connector_search` returns Duffel. Without Duffel, check Google Flights or the airline's site in the browser.

- Search Duffel and read Google Flights in one browser task, as Duffel's Google Flights guide shows. Duffel covers every airport, cabin and date the request allows. The browser reads one search, up to three airports per side, for the date and cabin the traveler named, or the first ones a flexible request allows; when the request allows more, say which it checked and offer to compare more there, without calling the result the cheapest overall.

- Show Duffel's offers as the first list in the same turn, without waiting for the browser, as Duffel's Google Flights guide shows. When the browser reports, send one follow-up with only the trips `duffel route` marks `better` that also meet every limit the traveler set, saying what makes each better; when none qualify, send nothing.

- When the traveler chooses a first-list trip before the browser finishes, or changes the request, follow Duffel's Google Flights guide.

- Duffel, Google Flights and the routing commands are internal details: tell the traveler about airlines, flights, prices and where each one books, and describe the sources as a direct flight search and a browser search, including when you say where a fact came from or why a search failed, instead of naming Duffel or a site the browser reads.

- For a request for an exact flight, the trip shown is one that carries that flight number. Schedule data shows a flight operates, not that it can be booked, and a different flight is a different request.

- A flight search is short enough to need no todo list, and its results and picks change quickly, so they become memories only when the user asks.

- When the browser task fails or is blocked after the first list, send nothing more. When there was no first list, say once that the search couldn't be completed. Search another comparison site or seller, listed in [other sources](sources.md), only when the user asks for more coverage.

- Each trip books where `duffel route` sends it. A trip routed to the airline's site or a link is still a real option: its price is the one the browser read, which the airline confirms at checkout.

- Keep the searches and the combined comparison in the main conversation. A source's request limits apply to that source, not to other legitimate sources.

<!-- gflights-first-only:end -->
## Verify comparable offers

<!-- gflights-first-off-only:start -->
- Follow a promising result to the airline or seller and confirm every segment, every passenger and the full payable total in one currency. Keep a cached or teaser price out of the bookable shortlist until the seller reproduces it.
<!-- gflights-first-off-only:end -->
<!-- gflights-first-only:start -->
- With Google Flights, a Duffel match reproduces a trip's price, and the airline confirms any other trip's price at checkout, so don't open sellers or booking pages to verify the list.
<!-- gflights-first-only:end -->

- Whole itineraries compare cleanly: a one-way price set against a round-trip total, or a quietly changed airport, date or cabin, misleads the choice.

- Price a round trip as one round-trip fare from a round-trip search. Two one-way prices added together aren't a round-trip quote, and the round trip can cost less, so search the round trip rather than adding one-way fares. When the return isn't confirmed, price the likeliest return as a round trip and say which return you assumed. Present one-way tickets bought separately only as split tickets, with their caveat.

- Check the cabin on every segment. A business-class label can include an economy leg, so describe a mixed cabin as mixed.

- Compare bags, seats, change and refund terms, and who services the ticket afterward. Count the bags and seats this traveler will need before calling a fare the cheapest; a fare that already includes them adds no fee. An unknown term is neither restrictive nor flexible.

- Treat separate tickets and self-transfers as their own kind of trip. Account for collecting and rechecking bags, transit entry rules, connection time and a missed connection that no airline will protect, and label them clearly.

- A connection in a country other than the destination can have its own entry requirements. When a traveler may not meet them, say so under the list and include a comparable trip that avoids that connection.

## Rank for this traveler

- Compare what each option costs this traveler for this trip, not the headline fare, together with total travel time within the requested cabin. A fare without a bag or seat they need costs more than it shows, and status can make a pricier carrier the better deal. When the shortest practical trip and the cheapest worthwhile trip differ, show both and say what the extra money or time buys.

- Drop any option that costs more and takes longer than another with equivalent terms. Then weigh the number of legs, ground transfers, arrival time, connection reliability and flexibility.

- Show three to five complete trips chosen from the connector's lines, each there for a reason: the cheapest, the best fit for this trip's needs, and any that buy clearly more for a little more, such as a nonstop, a better arrival time, a checked bag or a flexible fare on the same flights. A round trip is shown as complete round trips, both directions with one total, and only nonstop trips when the user asked for direct flights.

- Judge "a little more" against the ticket price and what the traveler has shown about price: a stated budget, past choices, the cabin and the trip's purpose. State a difference and what it buys rather than calling it small. When their price sensitivity is unclear, show both and let them choose.

- A fare is the lowest found among the sources checked, which is different from the lowest available anywhere. When an airline that flies the route wasn't checked, such as one the connector doesn't sell, name it.

- Stop when the leading options are verified with their sellers and more searching is unlikely to change the choice. When a missing carrier could change it, run the targeted connector search, then offer the airline's site.

## Present the flight list

<!-- gflights-first-off-only:start -->
- Load the `widget` namespace with `tool_search.load_tool_namespace`, and show the options as a native flight list with `widget.create_list_widget`: one flight row per chosen offer, using the pointer the connector gives for it. When the tool is absent or a valid call returns an explicit unsupported or rendering error, the connector's option lines read well as a short list, as they are; they already carry what a table would. Rows point at bookable offers, which a Google Flights lead isn't. [Flight rows](flight-rows.md) covers filling them from a connector's search file or a verified website fare.
<!-- gflights-first-off-only:end -->
<!-- gflights-first-only:start -->
- Load the `widget` namespace with `tool_search.load_tool_namespace`, and show the options as a native flight list with `widget.create_list_widget`: one flight row per chosen trip, using each route entry's `row` unchanged, with its `flight_action`, so every button says where that trip books. When the tool is absent or a valid call returns an explicit unsupported or rendering error, `duffel route`'s lines read well as a short list, with where each trip books. [Flight rows](flight-rows.md) covers rows from a search file.
<!-- gflights-first-only:end -->

- Create the list in the main conversation and reply with one message: the list's embed token first, then one short paragraph. Put the search assumptions, such as travelers, cabin or a time filter, in the list's subtitle. Notes the connector's docs require, such as failed searches, incomplete coverage or split tickets with their caveat, follow the paragraph in the same message.

- In that paragraph, recommend one trip and say why it fits this traveler's needs, such as their arrival time, bags, airline or budget, then give the main tradeoff of one or two alternatives in a clause each. The cards already show times, prices, stops and bags, so mention them only where they decide the choice, and leave the booking prompt to the cards' button.

- Text before the list splits the answer into separate messages. Before a slow search, follow the chat's acknowledgment guidance; only when no reaction is available, send a short note before the search starts.

- Offer a choice between flights as flight rows, which show each trip's fares and where it books, including in a later update about the same trip. When a reply instead asks the user to pick flights with `muse.create_options`, label each option with that trip's own fare and say whether it is the total or per passenger. A total that adds a hotel, car or other costs is a trip total: give it in the message text with its parts, rather than in a flight's label.

<!-- gflights-first-off-only:start -->
- Each row is a complete trip, a round trip included, so one list covers it. For a trip that is ready to book, omit `flight_action` so the runtime supplies its booking action.
<!-- gflights-first-off-only:end -->
<!-- gflights-first-only:start -->
- Each row is a complete trip, a round trip included, so one list covers it. For a trip that is ready to book, keep each row's own `flight_action` from its route, and set no list-level `flight_action`.
<!-- gflights-first-only:end -->

- For a trip that is still being planned, put this action on the final list instead of the booking action, and return the selection to Trip Planning:

```json
{
  "cta_text": "Add to plan",
  "response_message_prefix": "Add this flight to my trip plan:"
}
```
<!-- gflights-first-only:start -->

- Leave each row's own `flight_action` out of a planning list, since a row's action replaces the list's.
<!-- gflights-first-only:end -->

- Once the user picks a flight to book, [booking](booking.md) covers where to buy, the final review and the confirmation.
