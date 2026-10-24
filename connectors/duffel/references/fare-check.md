# Check the fare on a booked trip

- Flight Tracking's fare job runs this check daily. Write these rules into the job's body.

- Run exactly one `search` per run for the complete booked itinerary and passenger mix, with `--limit 30`, saved to a new file. Duffel is the pricing source here, since a browser or web price isn't comparable with the booked fare; a failed scheduled search waits for the next run.

- Compare an offer only when its priced scope matches the booked baseline exactly. That means every leg's dated flight numbers and airports, the passenger mix, the cabin or fare family, included bags, stop pattern, refund and change restrictions, currency and the basis for taxes and fees.

- A one-way or single-leg offer isn't comparable with a round-trip or multi-leg total, and a booking total splits across legs only where line-item prices give the exact amount.

- Treat three baseline gaps as missing scope. An unstated booked fare family makes any basic, light or saver brand non-comparable. Extras in the paid total come out, or the candidate's price for the same extras goes in. A total that may not cover every traveler is not comparable.

- Record a missing or mismatched scope as non-comparable, clear any pending candidate tied to it, and stay silent.

- Net savings are the fare drop minus known change, cancellation and rebooking costs. A candidate qualifies when net savings exceed 10 percent of the original paid total or the booking-currency equivalent of USD 100.

- Convert USD 100 with a fresh exchange-rate source and record that source's time. When no reliable rate is available, use only the 10 percent threshold.

- The first qualifying candidate is not an alert. Save it as pending, with its itinerary, total, currency and check time, and update the same fare job to run once about an hour later.

- On that confirmation run, search once more and confirm only when equivalent inventory still qualifies. Clear the pending candidate when it has disappeared, no longer matches or fell below both thresholds. Keep it with a failure note when the search failed. Return the job to its daily schedule after any of these outcomes.

- Before notifying, read the owner's recent activities for a later booking change, such as a rebooked leg or an added traveler. If the booking changed, update the baseline, clear the candidate and stay silent.

- When the candidate is confirmed, save the comparison and notify under Flight Tracking's notice rules. Say when the fare was confirmed, that fares can change before the user acts, and ask whether they want help investigating a credit, refund or rebooking.

- If the user says yes, run one fresh search before quoting savings. That answer authorizes investigation and preparation only; whether a credit or refund is granted is up to the airline.
