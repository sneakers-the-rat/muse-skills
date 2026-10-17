# Trip Transport

## Choose how to get there

- Establish the route, local dates and times, the travelers with children's ages, luggage, any vehicle or bike, and how firm each time is. Use the trip plan and existing confirmations before asking.

- Compare door-to-door time and full cost across the realistic modes, including transfers, parking, tolls, fuel or charging, and the hotel night a slow option can add. Use `map.navigation` for driving, transit and walking estimates, and plan in the destination's local time.

- Name what makes an option fail as well as what makes it cheaper, such as a last ferry before the flight lands, a pickup desk that closes early, or a reservation-only train.

- Only an operator, rental company or reseller showing a live departure or vehicle establishes availability. A timetable page, route planner or old confirmation does not.

## Rental cars

- Confirm the driver's age, license country and how long it has been held. Under-25 and over-70 drivers often pay surcharges or face limits, and many countries require an International Driving Permit alongside a foreign license.

- Compare the full price, not the daily rate: one-way and after-hours fees, young-driver and extra-driver fees, airport surcharges, mileage limits, the fuel policy, and the deposit hold. Most companies require a credit card in the main driver's name.

- Explain cover plainly. Collision damage waivers, third-party liability and theft cover work differently by country, and a credit card's rental cover may exclude some countries, vehicle types or long rentals. Check the card's terms before the user declines the counter's cover.

- Check what the trip needs from the car: an automatic in countries where manual is the default, seats for luggage and child seats, winter tires, permission to cross a border or take the car on a ferry, and range and charging for an electric car.

- Flag local driving rules that cost money on the trip, such as Italy's restricted ZTL zones, motorway vignettes in Switzerland and Austria, congestion and low-emission zones, and electronic tolls that rental companies bill with a fee.

- Compare a city or station pickup with the airport when the first days need no car, and a peer-to-peer rental when it suits the trip.

## Trains and buses

- Check the national operator for live times and fares, and note when a seat reservation is required or advance fares rise as departure nears.

- Compare a rail pass with point-to-point tickets for the actual journeys before recommending it. Passes pay off only for some itineraries.

- Use long-distance buses where they beat rail on price or reach, and check the luggage allowance.

## Ferries

- Separate foot passengers from vehicles. Vehicle space sells out first on popular summer and holiday routes, and some routes need a reservation for any car.

- Check the season's timetable, the check-in cutoff, the terminal location, and whether a rental agreement allows the car on board.

- Weather cancels sailings. For an onward flight or tight connection, allow a buffer or name the next sailing and an alternative route.

## Bikes, scooters and walking

- For short city trips, compare bike share, e-scooters and walking with transit. Check whether the system needs a local app, account or deposit.

- For a bike rental or tour, confirm frame size or e-bike, helmet rules, lock and drop-off, and whether bikes may ride on the trains or ferries in the plan.

## Rides and airport transfers

- Compare ride apps with the local taxi, transit and a prebooked transfer, using the arrival time, luggage and party size. A fixed-price transfer can beat surge pricing after a late flight.

- For a prebooked transfer, confirm the meeting point, how long the driver waits after a delay, and the flight number to share.

## Book and confirm

- Book through the source that showed the live option, whether a connector, the operator's own site or a reseller. Follow [checkout](/opt/muse/assets/booking/references/checkout.md) for the final refresh, worse terms, approval, an uncertain result and cancellation.

- When the trip has a plan, write the result back to it through [Trip Planning](/opt/muse/skills/trip-planning/SKILL.md), keeping proposed, selected and booked options distinct.

- Report the confirmation number, pickup or departure point, the local time, what the user must bring, such as the license, permit, card or ticket, and the cancellation deadline.

## Available connectors

- [Places Search](/opt/hatch/connectors/places/CONNECTOR.md) for rental desks, stations, terminals and their opening hours.

- [Gmail](/opt/hatch/connectors/gmail/CONNECTOR.md) for existing rental, rail and ferry confirmations.

- [Outlook Mail](/opt/hatch/connectors/outlook_mail/CONNECTOR.md) for existing rental, rail and ferry confirmations.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- Use `browser.browse` for live availability and booking on operator and reseller sites. Give the task the local dates and times, the travelers, the vehicle or ticket type, and ask for the full price with its fees and cancellation terms.

- For rental cars, compare a rental company's own site, such as [Hertz](https://www.hertz.com/), [Enterprise](https://www.enterprise.com/), [Avis](https://www.avis.com/), [Sixt](https://www.sixt.com/) or [Europcar](https://www.europcar.com/), with a broker such as [Kayak](https://www.kayak.com/cars), [Discover Cars](https://www.discovercars.com/) or [Auto Europe](https://www.autoeurope.com/). [Turo](https://turo.com/) rents cars from their owners.

- [Rome2Rio](https://www.rome2rio.com/) and [The Man in Seat 61](https://www.seat61.com/) suggest ways to combine trains, buses, ferries and flights. Verify live departures and fares with the operator.

- Check rail with the national operator, such as [National Rail](https://www.nationalrail.co.uk/) in Britain, [SNCF Connect](https://www.sncf-connect.com/) in France, [Deutsche Bahn](https://int.bahn.de/en) in Germany, [Trenitalia](https://www.trenitalia.com/) in Italy, [Renfe](https://www.renfe.com/) in Spain, [Amtrak](https://www.amtrak.com/) in the US, [VIA Rail](https://www.viarail.ca/) in Canada and [SmartEX](https://smart-ex.jp/en/) for the Tokaido, Sanyo and Kyushu Shinkansen in Japan. [Trainline](https://www.thetrainline.com/) sells tickets across Britain and Europe, and [Eurail](https://www.eurail.com/) sells European rail passes.

- For buses, check [FlixBus](https://www.flixbus.com/) in Europe and the US, [National Express](https://www.nationalexpress.com/) in Britain and [Greyhound](https://www.greyhound.com/) in North America.

- For ferries, [Direct Ferries](https://www.directferries.com/) compares many routes and [Ferryhopper](https://www.ferryhopper.com/) covers Greece and the Mediterranean. Book reservation-heavy routes with the operator, such as [BC Ferries](https://www.bcferries.com/) or [Washington State Ferries](https://wsdot.wa.gov/travel/washington-state-ferries).

- For rides, compare [Uber](https://www.uber.com/) or [Lyft](https://www.lyft.com/) with local apps such as [Bolt](https://bolt.eu/) in Europe and [Grab](https://www.grab.com/) in Southeast Asia, and with the local taxi, transit or airport transfer.

## Alternatives for better results

- Split a long drive with a train or a one-way rental when it saves a day of backtracking or a long return to the pickup city.

- Rent the car only for the days that need it, and use transit in cities where parking, tolls and restricted zones cost more than the car saves.

- When vehicle space on a ferry is sold out, check foot-passenger travel with a car at the other side, a different port, or a different day within the user's flexibility.

- Recheck a refundable rental before the trip, since prices often fall and a new booking can replace the old one.
