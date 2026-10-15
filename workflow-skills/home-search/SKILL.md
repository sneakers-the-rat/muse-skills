# Home Search

## Find homes that fit

- Start with the area, budget, property needs and timing the user gave, and begin a useful search with them. Ask for more only when it would prevent wasted work or change the choices. Separate firm requirements from preferences a strong home might justify relaxing.

- Search the market where the home is, using its main listing portals and the listing agent's or property manager's own page.

- Compare current listings and remove duplicates of the same property. Check the asking price or rent, status, layout, condition, recurring charges and location. For a commute or other regular journey, compare travel time from `map.navigation`, not distance.

- Keep facts from the listing apart from estimates and missing information.

- Show a few homes with meaningful tradeoffs, such as lower total cost, less travel or more usable space. Link each property and say why it fits.

- Compare monthly cost as well as price, since a higher asking price can still mean a lower monthly cost. Include taxes, insurance and association or service charges when available, and label estimates.

## Arrange useful visits

- An open house needs no booking. A private tour needs confirmation from the agent or booking service. Keep the times and number of bookings within the user's request, and remember that a tour receipt does not authorize an offer or purchase.

- Plan a visit day only when the user asks. Check the calendar for free time, choose up to three open houses or the number the user wants, and get driving times from the starting point to the first home and between homes with `map.navigation`.

- Schedule each visit for 30 minutes inside its open-house window, starting after the drive. Create one event per visit titled "Open house: <street address>", with the full address as its location and only the listing link in its description, plus a "Drive to <street address>" event sized to the drive.

- Check for existing events before creating any, and invite other people only when the user asks. Create tour events only after the tour is confirmed.

## Available connectors

- [Places Search](/opt/hatch/connectors/places/CONNECTOR.md) for schools, groceries, parks and transit near a listing.

- [Google Calendar](/opt/hatch/connectors/google_calendar/CONNECTOR.md) for free time and visit events.

- [Outlook Calendar](/opt/hatch/connectors/outlook_calendar/CONNECTOR.md) for free time and visit events.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Redfin](/opt/hatch/connectors/redfin/CONNECTOR.md) for homes for sale, open houses and tour booking through Redfin's agent.

- [HasData](/opt/hatch/connectors/hasdata_mcp/CONNECTOR.md) for Zillow and Redfin listing data.

## Websites

- Use `browser.spawn_task` to check a listing's current status, price and viewing times on the portal and the listing agent's page, in the country and city where the home is.

- In the US, use [Zillow](https://www.zillow.com/) and [Realtor.com](https://www.realtor.com/), with [Apartments.com](https://www.apartments.com/) for rentals. Use [Redfin](https://www.redfin.com/) for rentals and sold-home history, which its connector does not search, and wherever the connector is unavailable.

- Use [Rightmove](https://www.rightmove.co.uk/) and [Zoopla](https://www.zoopla.co.uk/) in the UK, [Realtor.ca](https://www.realtor.ca/) in Canada, [Idealista](https://www.idealista.com/) in Spain, Italy and Portugal, [SeLoger](https://www.seloger.com/) in France and [ImmobilienScout24](https://www.immobilienscout24.de/) in Germany.

- Use [SUUMO](https://suumo.jp/) in Japan, [Inmuebles24](https://www.inmuebles24.com/) in Mexico, and [Domain](https://www.domain.com.au/) or [realestate.com.au](https://www.realestate.com.au/) in Australia.

## Alternatives for better results

- Check the original listing or agent when portals disagree on price, status or visiting times. A stale portal entry does not prove a home is available.

- Learn how the local market quotes price, rent and fees, such as weekly or monthly rent and agent or key fees, before comparing homes across sources.

- Use local public records and map tools for property taxes, parcel boundaries and travel, and keep those findings apart from the seller's claims.

- In a fast market, offer a daily check for new matching listings with `cron.add`.
