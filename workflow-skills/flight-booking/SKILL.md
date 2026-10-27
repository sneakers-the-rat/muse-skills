# Flight Booking

- Saved travel preferences, when the user has any, live in `~/memory/travel/PROFILE.md`: home airports, airlines, cabin, seat, stops and loyalty programs for the user and the people they travel with. Reading it early lets you search from what they have already told Muse instead of asking again. What they say in this conversation takes precedence, and naming the saved preferences you used, such as the home airport, lets them correct one. Muse updates the profile in the background from the conversation.

- Use `muse.connector_search` to find available flight connectors before reading their docs or running their CLIs. A link here does not establish availability, and a CLI call is not an availability check. If none is available, go directly to Google Flights or the airline's site through `browser.browse`.

- Available connected flight inventory comes first: a connector that sells fares from many airlines returns bookable offers quickly and books them natively. Comparison websites are a fallback when no flight connector is available, when the connectors may be missing something or when the user asks.

- Read [flight comparison](references/flights.md) before searching, together with the connector's docs when an available connector will be used. They cover planning the search, reading its results, ranking, and the flight list, including round trips chosen outbound first.

- The list holds only offers that can be booked: connector offers, or airline fares verified on the airline's site.

- [Booking](references/booking.md) covers choosing between a connector and the airline's site, the final review and the confirmation.

- [Other sources](references/sources.md) lists airline and comparison sites and ways to find a better fare, for when the user wants more coverage.

## Available connectors

- [Gmail](/opt/hatch/connectors/gmail/CONNECTOR.md) for existing confirmations, airline credits and loyalty details.

- [Outlook Mail](/opt/hatch/connectors/outlook_mail/CONNECTOR.md) for existing confirmations, airline credits and loyalty details.

- [Google Calendar](/opt/hatch/connectors/google_calendar/CONNECTOR.md) for date conflicts and existing travel.

- [Outlook Calendar](/opt/hatch/connectors/outlook_calendar/CONNECTOR.md) for date conflicts and existing travel.

- [Link by Stripe](/opt/hatch/connectors/stripe-link/CONNECTOR.md) for paying a Duffel booking or a website checkout with a one-time card.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's country, channel or devices. Confirm availability with `muse.connector_search` before reading their docs or running their CLIs.

- [Duffel](/opt/hatch/connectors/duffel/CONNECTOR.md) for bookable fares from many airlines, with native booking and cancellation.

- [Agoda](/opt/hatch/connectors/agoda/CONNECTOR.md) for flight searches and returned links to book on Agoda.

- [ShopBack](/opt/hatch/connectors/shopback_mcp/CONNECTOR.md) for flight prices from travel partners and the cashback each offer pays.
