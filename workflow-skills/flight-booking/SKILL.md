# Flight Booking

- Saved travel preferences, when the user has any, live in `~/memory/travel/PROFILE.md`: home airports, airlines, cabin, seat, stops and loyalty programs for the user and the people they travel with. Reading it early lets you search from what Muse already knows about them instead of asking again. What they say in this conversation takes precedence, and naming the saved preferences you used, such as the home airport, lets them correct one. Muse updates the profile in the background.

- Earlier bookings may be listed in `~/memory/travel/HISTORY.md`. When a route repeats, follow [earlier bookings](/opt/muse/assets/booking/references/travel-history.md) to use it.

- Use `muse.connector_search` to find available flight connectors before reading their docs or running their CLIs. A link here does not establish availability, and a CLI call is not an availability check. If none is available, go directly to Google Flights or the airline's site through `browser.browse`.

<!-- gflights-first-off-only:start -->
- Available connected flight inventory comes first: a connector that sells fares from many airlines returns bookable offers quickly and books them natively. Comparison websites are a fallback when no flight connector is available, when the connectors may be missing something or when the user asks.

- Read [flight comparison](references/flights.md) before searching, together with the connector's docs when an available connector will be used. They cover planning the search, reading its results, ranking, and the flight list.
<!-- gflights-first-off-only:end -->
<!-- gflights-first-only:start -->
- When `muse.connector_search` returns Duffel, a flight search also reads Google Flights in a browser task, as Duffel's [Google Flights](/opt/hatch/connectors/duffel/references/google-flights.md) guide describes. Duffel's offers come first, and the airline booking policy gives each trip its route: checkout with Muse, the airline's website, or a link the traveler books from.

- Read [flight comparison](references/flights.md) before searching, together with Duffel's docs and its Google Flights guide. They cover planning the search, reading its results, routing, ranking, and the flight list.
<!-- gflights-first-only:end -->

<!-- gflights-first-off-only:start -->
- Search and comparison can include clearly labeled read-only connector results and flexible-date suggestions. Follow the connector's presentation guidance. Booking requires a bookable connector offer or an airline fare verified on the airline's site.
<!-- gflights-first-off-only:end -->
<!-- gflights-first-only:start -->
- Search and comparison can include clearly labeled read-only connector results and flexible-date suggestions. Follow the connector's presentation guidance. Booking follows each trip's route: a bookable connector offer, an airline fare verified on the airline's site, or a link the traveler books from.
<!-- gflights-first-only:end -->

- [Booking](references/booking.md) covers loyalty numbers and points, choosing between a connector and the airline's site, the final review and the confirmation.

- [Other sources](references/sources.md) lists airline and comparison sites and ways to find a better fare, for when the user wants more coverage.

## Available connectors

- [Gmail](/opt/hatch/connectors/gmail/CONNECTOR.md) for existing confirmations, airline credits and loyalty details.

- [Outlook Mail](/opt/hatch/connectors/outlook_mail/CONNECTOR.md) for existing confirmations, airline credits and loyalty details.

- [Google Calendar](/opt/hatch/connectors/google_calendar/CONNECTOR.md) for date conflicts, existing travel and adding booked flights.

- [Outlook Calendar](/opt/hatch/connectors/outlook_calendar/CONNECTOR.md) for date conflicts, existing travel and adding booked flights.

- [Link by Stripe](/opt/hatch/connectors/stripe-link/CONNECTOR.md) for paying a Duffel booking or a website checkout with a one-time card.

### Discover more

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's country, channel or devices. Confirm availability with `muse.connector_search` before reading their docs or running their CLIs.

- [Duffel](/opt/hatch/connectors/duffel/CONNECTOR.md) for bookable fares from many airlines, with native booking and cancellation.

- [Despegar](/opt/hatch/connectors/despegar/CONNECTOR.md) for flight searches and comparisons, flexible dates, monthly trends and deals.

<!-- despegar-checkout-only:start -->
- Despegar can also generate a checkout link for the selected itinerary so the user can continue on Despegar.
<!-- despegar-checkout-only:end -->

- [Agoda](/opt/hatch/connectors/agoda/CONNECTOR.md) for flight searches and returned links to book on Agoda.

- [easyJet](/opt/hatch/connectors/easyjet/CONNECTOR.md) for easyJet flights and live fares, live easyJet flight status, and returned links to book on easyJet.

- [Ryanair](/opt/hatch/connectors/ryanair/CONNECTOR.md) for Ryanair's own lowest fares, cheapest days and routes, shown as flight cards with links to book on ryanair.com.

- [ShopBack](/opt/hatch/connectors/shopback_mcp/CONNECTOR.md) for flight prices from travel partners and the cashback each offer pays.
