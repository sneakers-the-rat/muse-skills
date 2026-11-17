# Book the chosen flight

- Use this guide once the user picks a flight to book.

## Loyalty numbers, credits and points

- Status and mileage earning come from each traveler's loyalty number on the booking, wherever it is bought: in `loyalty_programme_accounts` on a Duffel booking, asked for with the traveler details when the travel profile lists the program, as Duffel's booking guide describes, or by booking signed in on the airline's website, as [browser booking](/opt/muse/assets/booking/references/browser-booking.md) describes. A traveler without the number at hand still books.

- Credits and certificates the traveler holds are money, and member fares are cash prices: offer a known, unexpired one that applies to the chosen flight's airline with the chosen trip. Using it runs on the airline's website with the traveler's consent, as checkout describes.

- Miles and points are the traveler's choice. Search first. When the travel profile lists their loyalty program with the chosen flight's airline, or past flights on it, offer once, in the message that shows the chosen trip, to check the points price on the airline's site, where they sign in, beside booking for cash. Otherwise book for cash, and use points when they ask.

<!-- gflights-first-only:start -->
- Each route decision's `points` says where a points booking runs: offer the check when its `route` is `airline_site`, and when it is `handoff_link`, say they can book it with points from the airline's link.
<!-- gflights-first-only:end -->

- A booking with miles or points, asked for at the start or after the pick, runs on the airline's website, where their account holds them.

## Choose where to buy

<!-- gflights-first-only:start -->
- Before booking a flight from a Google Flights search, route it again with `duffel route --search FILE --offer POINTER`, adding `--duffel FILE` when Duffel ran and `--prefer airline_site` when the traveler pays with points, and follow its `decision` and `instructions` for where to book, as Duffel's [Google Flights](/opt/hatch/connectors/duffel/references/google-flights.md) guide describes. An "Add to plan" tap adds the flight to the plan instead. A handed-off trip stays open until the traveler says they booked it.
<!-- gflights-first-only:end -->
- Book through the connector that sells the chosen itinerary, as its docs describe.

- Book on the airline's website instead when the traveler pays with miles, points, credits or a certificate, when the airline's own fare is meaningfully better, or when no connector can sell the trip. That runs in a visible browser task with [browser booking](/opt/muse/assets/booking/references/browser-booking.md), since sign-in and payment need the user.

- Google Flights sells nothing. A price it shows is a lead until a connector or the airline reproduces it.

## Review and book

- When the user picks a flight, show the chosen trip in chat before collecting traveler details: every flight with its date, times and flight number, the cabin and fare brand, bags, change and refund terms, any proposed seats, and the total. Invite changes to seats, bags or the fare, carry the changes the seller supports into the booking, and explain any limit before continuing, such as a connector that sells a bag only as part of a fare that includes it.

- If the chosen trip connects in a country other than the destination that has its own entry requirements, confirm in that same message that every traveler meets them, unless the conversation already shows it. Offer a comparable trip without that connection if someone doesn't.

<!-- duffel-payment-readiness-only:start -->
- When a connector will charge the flight to Link, learn whether Link can pay as soon as the user picks the flight, as the connector's docs describe. When it can't, ask the user to set it up in the same message as the traveler questions. Once Link is ready, continue the same booking from where it stopped, keeping the flight the user chose.

<!-- duffel-payment-readiness-only:end -->
- Follow [checkout](/opt/muse/assets/booking/references/checkout.md) for the final refresh, worse terms, approval and an uncertain result. For a flight, look for changes to bags, airports and the operating carrier as well as the fare, seats and schedule.

- The final review shows the exact itinerary, traveler count, cabin and fare brand, seats, bags, total, the loyalty program on each traveler's booking, any credits or points applied, the amount charged and the fare rules.

- For flights, the confirmation is the airline's booking reference with the status of each ticket. A hold or pending ticketing is not a completed booking.
