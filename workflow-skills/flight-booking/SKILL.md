# Flight Booking

## Plan the search

- Establish the route, dates, travelers with children's ages, cabin and how flexible the user is. Search with natural assumptions, such as one adult flying one way, and state them.

- Ask only for a missing detail that would change the route, price or traveler.

- Read [flight comparison](references/flights.md) before searching. It covers choosing sources, verifying fares, ranking and the flight list.

## Compare complete trips across sources

- Search connected inventory such as Duffel and strong websites such as Google Flights, Kayak, Skyscanner and the airline that operates the route. Duffel is one good source, not the only way to book a flight.

- Choose sources for the route. Add a regional or low-cost carrier that flies it, since some sell mainly on their own sites.

- Rank verified total price and total travel time together, within the requested cabin. When the shortest practical trip and the cheapest worthwhile trip differ, show both and say what the extra money or time buys.

- Compare whole itineraries only. Never set a one-way price against a round-trip total, or quietly change the airport, date or cabin.

- For a request for an exact flight, book only an offer that carries that flight number. Never substitute a different flight or treat schedule data as proof that it is bookable.

## Book the chosen flight

- Book through the source that sold the verified fare. Use the connector docs for connected inventory and [browser booking](/opt/muse/assets/booking/references/browser-booking.md) for an airline or other website.

- Follow [checkout](/opt/muse/assets/booking/references/checkout.md) for the final refresh, worse terms, approval and an uncertain result.

## Available connectors

- [Duffel](/opt/hatch/connectors/duffel/CONNECTOR.md) for bookable fares from many airlines, with native booking and cancellation.

- [Gmail](/opt/hatch/connectors/gmail/CONNECTOR.md) for existing confirmations, airline credits and loyalty details.

- [Outlook Mail](/opt/hatch/connectors/outlook_mail/CONNECTOR.md) for existing confirmations, airline credits and loyalty details.

- [Google Calendar](/opt/hatch/connectors/google_calendar/CONNECTOR.md) for date conflicts and existing travel.

- [Outlook Calendar](/opt/hatch/connectors/outlook_calendar/CONNECTOR.md) for date conflicts and existing travel.

- [Link by Stripe](/opt/hatch/connectors/stripe-link/CONNECTOR.md) for paying a Duffel booking or a website checkout with a one-time card.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Agoda](/opt/hatch/connectors/agoda/CONNECTOR.md) for flight searches and returned links to book on Agoda.

- [ShopBack](/opt/hatch/connectors/shopback_mcp/CONNECTOR.md) for flight prices from travel partners and the cashback each offer pays.

## Websites

- Check these sites with `browser.browse`, using the brief in [flight comparison](references/flights.md) so each task returns complete itineraries with the payable total.

- [Google Flights](https://www.google.com/travel/flights), [Kayak](https://www.kayak.com/flights) and [Skyscanner](https://www.skyscanner.com/) compare carriers and sellers on most routes and link out to the seller, which holds the bookable fare.

- The operating airline's own site shows member fares, credits and full fare rules, and it services the booking afterward.

- Regional and low-cost carriers can be missing from comparison sites or cheaper on their own sites, such as [Ryanair](https://www.ryanair.com/), [easyJet](https://www.easyjet.com/) and [Wizz Air](https://wizzair.com/) in Europe, [Volaris](https://www.volaris.com/) and [Viva Aerobus](https://www.vivaaerobus.com/) in Mexico, [Porter](https://www.flyporter.com/) in Canada and [Peach](https://www.flypeach.com/) in Japan. Add their bag and seat fees, which these fares often leave out.

- [Booking.com Flights](https://www.booking.com/flights/) is another seller to compare. Check who issues the ticket and who handles changes.

- [ITA Matrix](https://matrix.itasoftware.com/search) explores complex routings and fare rules. It does not sell tickets, so take its candidates to a seller.

## Alternatives for better results

- Widen dates, airports or the order of cities when the user allows it. Count the extra ground transfer, hotel night or bag fee before calling the result cheaper.

- Check member fares, credits, companion certificates and points when the user has them. Compare points with cash on live award availability, taxes and transfer rules, and never transfer points just to see whether an award exists.

- Try the airline's site for the departure country when it may price differently, and check that a resident-only or local-payment fare is open to this traveler.

- Book with the airline when flexibility or support matters more than a small saving, since it handles changes and disruptions for its own bookings.
