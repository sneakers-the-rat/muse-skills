# Restaurant Reservations

## Find a suitable table

- Establish the local date, time window and party size, and search where the restaurant is rather than where the user is now. Search for useful options before asking about optional preferences.

- Read [restaurant booking](references/restaurants.md) before searching. It covers reservation routes, comparing tables and the review.

- Only a reservation source establishes that a table is available. Opening hours, a map listing or a search snippet do not.

## Reserve and confirm

- Book through the route that showed the table, whether a connector, the restaurant's own booking page or a call. Follow [checkout](/opt/muse/assets/booking/references/checkout.md) for the final refresh, worse terms, approval, an uncertain result and cancellation.

## Available connectors

- [OpenTable](/opt/hatch/connectors/opentable/CONNECTOR.md) for live availability, booking, changes and cancellations at OpenTable restaurants.

- [Places Search](/opt/hatch/connectors/places/CONNECTOR.md) for finding restaurants and their hours, photos and reviews when the user has not named one. It does not show table availability.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- Use `browser.browse` to check live tables on the restaurant's own booking page or its reservation partner. Carry the exact branch, local date and time and party size, and ask for the available times with their deposit and cancellation terms.

- [Resy](https://resy.com/) and [Tock](https://www.exploretock.com/) cover many restaurants in the US and some abroad. Use a [SevenRooms](https://www.sevenrooms.com/) booking page when the restaurant links to one.

- [TheFork](https://www.thefork.com/) covers much of Europe, and [Quandoo](https://www.quandoo.de/) is common in Germany.

- In Japan, use [Tabelog](https://tabelog.com/en/) and [TableCheck](https://www.tablecheck.com/), or [Omakase](https://omakase.in/) for sought-after sushi and kaiseki counters. Expect deposits, strict cancellation windows and sometimes a Japanese phone number.

## Alternatives for better results

- Check more than one route for a booked-out restaurant, since each service holds different inventory and an empty result on one does not rule out a table elsewhere.

- Offer the platform's waitlist or release alert, a walk-in at the bar, or nearby times and a sister restaurant when they fit the user's flexibility.

- When the phone tools are available, a call can secure a table online channels do not show or confirm a special request with the restaurant.
