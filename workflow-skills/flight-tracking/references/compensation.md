<!-- flight-compensation-only:start -->
# Flight compensation

## When to check

- Check a journey when a tracked trip ends disrupted: a confirmed cancellation, a diversion, a missed connection, or a final arrival 2 hours 45 minutes or more late. The status job does this as described under **Scheduled runs**.

- Check when the user asks whether an airline owes them money, compensation or a refund for a flight, or describes a flight that went wrong.

- Check the flights in the travel history once per history build, as described under **Past flights in the travel history**.

- Search the mailbox for flights older than the travel history only when the user asks for it.

## Check a journey

- A journey is one direction of one booking: its legs in order, from the first departure to the final destination. Check an outbound and a return separately.

- Take the legs, local departure dates, booked arrival time and traveler count from the trip's `flight.json` when Muse tracked it, and otherwise from the booking mail.

- Run the [FlightAware](/opt/hatch/connectors/flightaware/CONNECTOR.md) `compensation check` with each booked leg. Add `--flown` for each leg the traveler took after a cancellation or missed connection, `--booked-departure` and `--booked-arrival` with the ticket's times when they differ from the current schedule, and `--passengers` with the travelers on the booking.

- For a flight to, from or within Canada, pass `--carrier-size small` when the operating airline is a small Canadian carrier and `large` for a large one. Left out, the check counts the large airlines it knows, such as the major Canadian, US and international carriers, as large, and for any other airline it asks for the size.

## Read the result

- `likely` lists the laws whose amount FlightAware's record supports. The airline still decides the cause first, and weather, air traffic control and other exempt causes can defeat the claim, so present the amount as likely owed rather than guaranteed.

- For `needs_facts`, find what `facts_to_confirm` names in the booking mail or ask the traveler: when they heard about a cancellation, the flight they were rebooked on, or the time the doors opened. Then check again with `--flown`, `--actual-arrival` or `--booked-arrival`.

- A law with `coverage_uncertain` applies only if the disrupted flight's airline or route qualifies, as on a journey that only connects through the EU. Find in the mail which flight caused the disruption, and present the claim as possible rather than likely.

- When several laws cover one disruption, the traveler can collect under only one. Recommend the larger amount, comparing currencies roughly.

- A `us_refund` verdict of `refund_if_not_flown` means a cash refund for a flight the traveler did not take. US law pays nothing for a delay they flew through.

- `expired` means the law's claim period has passed. Mention it only when the traveler may already have claimed in time.

- Stay silent about a journey no law covers or pays for, unless the user asked about it.

## Tell the traveler

- Send one message per likely claim with the flight and date, what happened, the law, the amount per traveler and in total, the deadline and anything still uncertain, and offer to prepare the claim.

- For a flight from the travel history, add that it applies if they took that flight, since booking mail does not prove the traveler flew.

- Persist the claim's fingerprint in the compensation state before sending, so each claim is offered once.

- Log each offer with `compensation record --law LAW --status offered --total TOTAL --currency CODE --passengers N`, using the check's law id and total.

## Prepare and file a claim

- Claim from the airline that operated the disrupted flight, through its own claim form or customer relations address, which `browser.browse` can find on its website. Filing directly costs the traveler nothing.

- Draft the claim with each passenger's name as ticketed, the booking reference from the booking mail, each flight number, date and route, what happened, the law and the amount per passenger, and a request for payment by bank transfer or to the original card rather than vouchers.

- Show the draft and get the user's approval before submitting a form or sending an email. Filing a claim contacts a provider, which the monitoring approval does not cover.

- Once the claim is submitted, log it with `compensation record --status filed` and the same law, total and currency.

- Hand the step to the user, with the draft ready, when the form needs their login, an identity check, a CAPTCHA, or payout details such as a bank account.

- Act openly as the traveler's assistant. Muse files as their agent, not as them, so say you are an AI assistant acting for the traveler whenever the airline asks, and let the traveler sign anything the airline wants from them personally.

## Follow a claim

- Add one activity to the **Flight compensation** Tracking item when a claim is filed, with the airline, flight, law and amount. Schedule one follow-up job owned by that item for 30 days later, to check the mailbox for the airline's answer.

- When the airline pays, record it, log `compensation record --status paid` with the total actually paid, and remove the follow-up job. Log `--status refused` when the airline refuses for good and `--status withdrawn` when the traveler drops the claim.

- When it refuses or misses its deadline, tell the user the next step: the national enforcement body or an ADR body in the EU, an approved ADR scheme or the CAA in the UK, the Canadian Transportation Agency, small claims court in Israel, or a DOT complaint for an unpaid US refund. A refusal blaming extraordinary circumstances is worth challenging when the cause was a technical fault or the airline's own staff striking.

## Past flights in the travel history

- The travel email bootstrap writes a year of the user's bookings to `~/memory/travel/HISTORY.md`, with routes, airlines and flight numbers but only the month each booking's mail started.

- Run `compensation screen --history ~/memory/travel/HISTORY.md`. It reads no mail and looks up only airports and airlines, and it lists the bookings whose routes a law could cover.

- For each candidate, find the travel date and leg order in that booking's mail by searching the connected mailbox for its flight numbers from the booked month on, and read the confirmation or a later change. Then check each journey.

- When a booking's laws are only under `possible_laws`, continue only if its confirmation shows a leg operated by an airline that law covers, in its "operated by" line.

- Skip a candidate whose date the mail does not show rather than guessing one.

- Mark the build in progress in the compensation state before screening, check off each journey as it is checked or skipped, and mark the build checked only once every candidate is done. When a lookup fails, keep the build in progress and move the `flight-compensation-history` job a day later with `cron.update`, so it resumes with the journeys still open. After three tries, mark the build checked and add one Tracking activity naming the journeys left unchecked.

## Scheduled runs

- When a trip's status job sees the last leg land or a cancellation confirmed, run the journey check before completing the trip, and keep its notice fingerprint in that trip's `flight.json` like its other notices.

- When a status job starts the travel history check and the **Flight compensation** item records no finished check of the history's build date, add the job `flight-compensation-history` to run once soon. A `cron.add` answer that the schedule already exists means another run claimed it. Run the past-flight check only in that job, so status jobs running at the same time cannot repeat it.

- The `flight-compensation-history` job finds or creates the **Flight compensation** item and follows **Past flights in the travel history**. It offers every likely claim it found in one message rather than one each, and each claim once by its fingerprint.

## Keep the state

- Keep the history screen's record and every filed claim under one **Flight compensation** Tracking item. Find it with `tracking.search`, and create it with `tracking.create` from the history job or when the first claim is filed.

- Store the minimum in `~/workspace/goals/<goal-slug>/hidden_files/travel/compensation.json`: the checked history build date, the checked journeys by flight number and date, notified fingerprints, and each claim's airline, law, amount, status, filing date and follow-up job id. Keep booking references, names and payment details out of it.

## Older flights

- When the user asks to check flights older than the travel history, search the mailbox for airline booking confirmations in the period they name and check each journey the same way. The EU, UK and Israeli laws reach back years, and Canada's 1 year.
<!-- flight-compensation-only:end -->
