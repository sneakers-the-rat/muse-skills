# Book the chosen flight

- Use this guide once the user picks a flight to book.

## Choose where to buy

- When status, points, credits or certificates could apply, ask one combined question before choosing where to buy. Offer to sign in to the airline and compare cash with points, to check cash only, or to check points only.

- Book through the connector that sells the chosen itinerary, as its docs describe.

- Book on the airline's website instead when the user wants to use miles, points, credits or status, when the airline's own fare is meaningfully better, or when no connector can sell the trip. That runs in a visible browser task with [browser booking](/opt/muse/assets/booking/references/browser-booking.md), since sign-in and payment need the user.

- Muse doesn't book United flights from any seller for now: United's fares are gone from Muse's main flight connector, and checkout on united.com fails in the browser. When the traveler picks one, they book it themselves on united.com rather than through a connector or a browser task. Send a link to United's results for the trip and list what to pick there: each flight with its date and times, the fare and the travelers. The booking is handed off, not done, until the traveler says they booked it.
  - One way: `https://www.united.com/en/us/fsr/choose-flights?f=EWR&t=SFO&d=2026-12-10&tt=1&px=1&taxng=1&newHP=True&clm=7&st=bestmatches`
  - Round trip: `https://www.united.com/en/us/fsr/choose-flights?f=EWR&t=SFO&d=2026-12-10&r=2026-12-14&px=1&taxng=1&newHP=True&clm=7&st=bestmatches&tqp=R`
  - `f` and `t` are the airports, `d` and `r` the dates and `px` the number of travelers. For other trips, link `https://www.united.com/` with the same details.

- Google Flights sells nothing. A price it shows is a lead until a connector or the airline reproduces it.

## Review and book

- When the user picks a flight, show the chosen trip in chat before collecting traveler details: every flight with its date, times and flight number, the cabin and fare brand, bags, change and refund terms, any proposed seats, and the total. Invite changes to seats, bags or the fare, carry the changes the seller supports into the booking, and explain any limit before continuing, such as a connector that sells a bag only as part of a fare that includes it.

- Follow [checkout](/opt/muse/assets/booking/references/checkout.md) for the final refresh, worse terms, approval and an uncertain result. For a flight, look for changes to bags, airports and the operating carrier as well as the fare, seats and schedule.

- The final review shows the exact itinerary, traveler count, cabin and fare brand, seats, bags, total, any credits or points applied, the amount charged and the fare rules.

- For flights, the confirmation is the airline's booking reference with the status of each ticket. A hold or pending ticketing is not a completed booking.
