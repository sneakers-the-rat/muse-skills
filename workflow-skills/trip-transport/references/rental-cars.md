# Rental cars

- Use this guide for live rental-car searches, reservations, status checks and cancellations. The command details for each source are in its connector doc, linked from Trip Transport's Available connectors. A reservation is a commitment even when nothing is charged now.

## Gather the search inputs

- Establish the exact pickup and drop-off places, local dates, the primary driver's age on the pickup date and two-letter residence country, and any requirement that changes inventory, such as an automatic, vehicle type, seats, luggage, accessibility or a hard total.

- Resolve each place to a verified location, and ask one short question when a place is materially ambiguous, such as a city with several airports or similarly named branches.

- Driver age and residence country change rental prices and eligibility. When either is missing, ask for whichever is missing in one short question before searching.

- When the user gives dates but no local times, search with 10:00 for both pickup and drop-off and say so in one sentence with the results, such as "I assumed a 10:00 pickup and drop-off; tell me your real times and I'll search again." Ask first when a time clearly matters, such as a flight arrival or an early departure.

- When the user or memory names a preferred rental company or loyalty program, include that company's best rate, using the connector's company filter when it has one.

- Ask for the driver's legal name, birth date, email and phone only after the user picks a live rate, and ask for a card only when the chosen rate is paid now.

## Compare sources

- Search each connector in Available connectors that returns live rental-car rates, following its connector doc, and present its rates as soon as they arrive.

- After the list, offer to compare the rental company's own site and a broker from Trip Transport's Websites with `browser.browse`, and say it takes several minutes. Compare right away when no connector returns a rate that meets the request, a connector is unavailable, or a quote's price rises or its terms get worse. Use the same places, local dates and times, driver age and vehicle needs, and stop when another source is unlikely to change the pick.

- When the user asks for other or specific rental companies, answer from the companies the connector already returned, searching it again for them when its doc says how, and browse for the companies it does not return. This does not replace the website comparison above: still offer it, and run it when the user asks or one of its triggers applies.

- Show each verified website option in one sentence with its company, full total and currency, and what differs from the best connector rate.

## Check airport pickups and returns

- For an airport pickup, compare how the user gets from the arrival gate to the car, not only the price. For an airport return, compare how they get from the car to the departure terminal.

- Before presenting options, check the airport's official ground-transportation page or another verified source for how rentals work there: counters in the terminal, a consolidated rental car center reached by train or shuttle, or off-airport branches reached by a supplier shuttle or a ride.

- Place each returned branch in one of those groups. For each option, state the location type and an estimated transfer time that includes the walk, the train or shuttle ride and the typical wait. Base it on the airport's site, the supplier's stated shuttle frequency or a map drive time, and label it as an estimate.

- Treat "in terminal", "at the airport" or "closest" as a request for the most convenient pickup the airport offers. When the airport has no counters in the terminal, say so in one sentence and name the closest option and how to reach it. For example, every company at SFO operates from the Rental Car Center, reached from all terminals by AirTrain.

- When every returned rate at an airport pickup is less convenient than the best pickup the airport offers, present the list first, then say in one sentence that a closer pickup exists and name it.

- Make that airport-convenience comparison only for a pickup, not for a trip that only returns the car at an airport, and within it suggest only pickup places the user asked about.

## Present the options

- Present four to eight distinct rates. Use the native list the connector doc describes; when the list tool is absent or a valid call fails to render, use the rental-car table in [booking presentation](/opt/muse/assets/booking/references/presentation.md).

- Keep every visible fact bound to the same rate: the supplier, the exact vehicle or "or similar", the category or type, the local rental period, the pickup location type and transfer estimate, and the full total and currency.

- Treat age, license, deposit, card, geography, mileage, fuel and cancellation conditions as supplier terms stated by the source, and remember that a model shown as "or similar" is not guaranteed.

## Choose and book

- Get a firm quote for the chosen rate before collecting driver details. When the price, supplier, vehicle, dates, places, payment type or material terms changed from the search, show the difference, recheck strong alternatives as Compare sources describes, and let the user choose again.

- Book through the source that showed the rate: a connector's own reservation steps, or [browser booking](/opt/muse/assets/booking/references/browser-booking.md) for a website option.

- Check the status of a reservation made here before describing or cancelling it, with the connector doc's management steps, and cancel only when the user asks.
