# Book the chosen flight

- Use this guide once the user picks a flight to book.

## Choose where to buy

- When status, points, credits or certificates could apply, ask one combined question before choosing where to buy. Offer to sign in to the airline and compare cash with points, to check cash only, or to check points only.

- Book through the connector that sells the chosen itinerary, as its docs describe.

- Book on the airline's website instead when the user wants to use miles, points, credits or status, when the airline's own fare is meaningfully better, or when no connector can sell the trip. That runs in a visible browser task with [browser booking](/opt/muse/assets/booking/references/browser-booking.md), since sign-in and payment need the user.

- Google Flights sells nothing. A price it shows is a lead until a connector or the airline reproduces it.

## Review and book

- Follow [checkout](/opt/muse/assets/booking/references/checkout.md) for the final refresh, worse terms, approval and an uncertain result. For a flight, look for changes to bags, airports and the operating carrier as well as the fare, seats and schedule.

- The final review shows the exact itinerary, traveler count, cabin and fare brand, seats, bags, total, any credits or points applied, the amount charged and the fare rules.

- For flights, the confirmation is the airline's booking reference with the status of each ticket. A hold or pending ticketing is not a completed booking.
