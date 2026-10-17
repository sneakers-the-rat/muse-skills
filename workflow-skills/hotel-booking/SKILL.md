# Hotel Booking

## Find a stay that fits

- Establish the destination, dates, number of rooms and who sleeps in each, with every child's exact age. Use the known budget, location and accessibility needs. Guest identity and payment can wait until the user chooses a rate.

- Read [hotel comparison](references/hotels.md) before searching. It covers sources, ranking the full stay and how to show results.

## Compare full stays across sources

- Compare the property's own site with strong sellers such as Google Hotels, Booking.com and Expedia. Add a rental platform when a kitchen, a group or a long stay makes one useful.

- Choose sources for the destination. Local booking sites and regional chains often have stock the global sites lack.

- Rank by the full-stay total with mandatory taxes and fees, together with location and terms. Refundable, prepaid and pay-at-property rates are different offers, even at the same hotel.

- Verify any amenity or access feature that decides the choice. A property description does not establish what a particular room includes, and hotel star class is separate from guest ratings.

## Book the chosen stay

- Book with the seller of the verified rate. [Hotel comparison](references/hotels.md) explains when to use native checkout and when to continue on the seller's website.

- Follow [checkout](/opt/muse/assets/booking/references/checkout.md) for the final refresh, worse terms, approval, an uncertain result and cancellation.

## Available connectors

- [Link by Stripe](/opt/hatch/connectors/stripe-link/CONNECTOR.md) for paying a website checkout with a one-time card.

- [Gmail](/opt/hatch/connectors/gmail/CONNECTOR.md) for existing hotel confirmations and loyalty details.

- [Outlook Mail](/opt/hatch/connectors/outlook_mail/CONNECTOR.md) for existing hotel confirmations and loyalty details.

- [Places Search](/opt/hatch/connectors/places/CONNECTOR.md) for a property's exact location, coordinates and ratings.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Expedia Lodging](/opt/hatch/connectors/expedia/CONNECTOR.md) for Expedia search, live room rates and native checkout of pay-now rates.

## Websites

- Check rates with `browser.spawn_task` on the property's own site and on sellers. Carry the exact dates, rooms with their occupants and children's ages, the room type and the cancellation terms, and ask for the full total and payment timing.

- [Google Hotels](https://www.google.com/travel/hotels) compares sellers for the same property. [Booking.com](https://www.booking.com/) has wide coverage, especially in Europe.

- [Expedia](https://www.expedia.com/) adds packages and the changes and cancellations its connector cannot make, and it covers Expedia wherever the connector is unavailable.

- [Airbnb](https://www.airbnb.com/) and [Vrbo](https://www.vrbo.com/) list rentals, from apartments to whole houses.

- [Agoda](https://www.agoda.com/) and [Trip.com](https://www.trip.com/) are strong across Asia. In Japan, [Rakuten Travel](https://travel.rakuten.com/) and [Jalan](https://www.jalan.net/) add ryokan and local hotels. [Despegar](https://www.despegar.com.mx/) adds offers in Mexico and Latin America.

## Alternatives for better results

- Book a refundable rate and recheck the price before the cancellation deadline. Offer to watch it, and rebook only with the user's approval when it drops.

- Use member rates, loyalty benefits, points and free-night certificates the user has. Count breakfast, parking or flexibility as a benefit only when the traveler will use it.

- Compare door-to-door travel time and transport costs. A cheaper hotel far from what the user came for can cost more overall.

- For a long stay or a group, ask the hotel directly about a better rate or room block.
