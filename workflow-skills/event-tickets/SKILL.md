# Event Tickets

## Find the right event and seats

- Pin down the exact event and the number of tickets before searching seats. A request for three options does not mean three seats.

- Read [ticket search and checkout](references/tickets.md) before searching. It covers sources, comparing seats and the review.

- Compare exact seats by their delivered total for the whole party, with primary and resale offers side by side. Verify any feature that decides the choice, such as the view, accessible seating or cover from weather.

## Buy and confirm

- A search result or purchase link does not buy anything. Continue in the seller's checkout with [browser booking](/opt/muse/assets/booking/references/browser-booking.md).

- Follow [checkout](/opt/muse/assets/booking/references/checkout.md) for the final refresh, worse terms, approval and an uncertain result.

## Transfer or resell tickets

- Buy only the quantity the user needs, within the event's purchase limits. Never stockpile tickets or work around limits to create resale stock.

- For tickets the user already owns, check whether the issuer allows transfer or resale, and whether identity checks, local law or price caps apply. Some countries cap resale at face value or require named tickets.

- Compare the net proceeds after fees and the buyer's delivery deadline. Prefer the event's official exchange or supported transfer when it suits.

- Verify the exact tickets and recipient before an authorized transfer or listing. A listing is not a sale and a sale is not a completed transfer, so keep the confirmation for each step.

## Available connectors

- [Ticketmaster](/opt/hatch/connectors/ticketmaster/CONNECTOR.md) for event search, live seat picks with prices, and checkout links for Ticketmaster events.

- [Link by Stripe](/opt/hatch/connectors/stripe-link/CONNECTOR.md) for paying a website checkout with a one-time card.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- Use `browser.spawn_task` for seat selection and checkout with the official seller, found through the venue, team, artist or promoter page. Carry the event, date, quantity and seat requirements, and ask for the exact seats and delivered total.

- Use the Ticketmaster site or app for transferring or reselling tickets in the user's account, which the connector cannot do.

- [AXS](https://www.axs.com/) is the primary seller for many venues. [SeatGeek](https://seatgeek.com/), [StubHub](https://www.stubhub.com/) and [Vivid Seats](https://www.vividseats.com/) add resale in the US, and [Viagogo](https://www.viagogo.com/) internationally.

- In the UK and Europe, check [See Tickets](https://www.seetickets.com/), [Dice](https://dice.fm/) and [Eventim](https://www.eventim.de/) in Germany, with [Twickets](https://www.twickets.live/) and [TicketSwap](https://www.ticketswap.com/) for fan resale with price limits.

- In Japan, use the official route through [eplus](https://eplus.jp/) or [Ticket Pia](https://t.pia.jp/). Tickets are often tied to the buyer's name or a Japanese phone number, so check visitor eligibility before recommending an offer.

## Alternatives for better results

- Check the box office and official presales, such as fan clubs, card offers and venue newsletters, before turning to resale.

- Compare a nearby section, another permitted date or the official exchange when it could offer better value. Resale prices can move close to the event, so weigh waiting against the risk of selling out.

- Prefer a seller with a buyer guarantee and delivery well before the event when paying resale prices.
