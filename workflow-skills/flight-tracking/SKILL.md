# Flight Tracking

## Answer a status question

- Identify the operating carrier, flight number, local departure date and airports from the request, memory or an authorized confirmation. Codeshares, repeated flight numbers and local dates make a flight number alone ambiguous. Use Flight Booking when the user is choosing a new flight.

- Read the dated flight's live status from a flight-status source such as FlightAware, even for "when's my flight?" or a remembered time, since memory identifies the trip but does not verify its schedule. Confirm a consequential change with the operating airline or airport. Label scheduled, estimated and actual times as such, and add the terminal, gate or connection impact when it helps.

- A missing signal or a delayed feed establishes neither a cancellation nor a safe connection.

- A one-time status check does not create a watch, a goal or a Tracking item.

## Start monitoring a booked trip

- Start monitoring when the user asks for ongoing updates on a booked flight, or when the runtime hands off a validated booking for an upcoming flight. Either one authorizes the watch, so after a runtime handoff start without asking. A connected mailbox is not required.

- Ask, in a live conversation, only for the flight or booking facts that monitoring needs and the context lacks. Resolve each exact dated leg before scheduling anything.

- Find the trip's owner before scheduling. Search with `user_goal.search` and `tracking.search`, use a matching user goal, otherwise reuse a matching active Tracking item, and otherwise create one with `tracking.create`. Never create a shadow goal, a duplicate Tracking item, a travel database or a price-tracker entry.

- Keep confirmation references, ticket numbers and connector identifiers out of user-visible goal text.

## Keep the trip state

- Store the minimum machine-readable state in `~/workspace/goals/<goal-slug>/hidden_files/travel/flight.json`. Use it only as the owner's job state.

- Record the booking and source fingerprints, the traveler relationship and count, the as-booked itinerary, the paid total and currency, the fare terms, the current facts, the last comparison and any pending fare candidate, the last notified facts and fingerprints, failure counts and the ids of the jobs that exist.

- Keep a top-level `trip` object current on every write: `first_departure_at` and `last_arrival_at` are RFC 3339 times with offsets from the current itinerary across every leg, and `cancelled` is `true` once a cancellation with no replacement is confirmed. Ideas reads this object to find trips that still need a stay or car booked, so it describes the whole trip rather than the next leg.

- Never store full messages, raw provider output, names, ticket numbers, identity documents, contact or payment details, loyalty numbers, Known Traveler Numbers or CLEAR identifiers.

## Schedule monitoring

- List the owner's jobs with `cron.list` and reuse an equivalent goal-owned job instead of adding another. Each job has the owner `goal:<goal-slug>`.

- The status job, `flight-status-<goal-slug>`, reads the next active leg from FlightAware on the cadence in the [FlightAware](/opt/hatch/connectors/flightaware/CONNECTOR.md) connector docs.

<!-- flight-compensation-only:start -->
- Write two compensation steps into the status job's body, and leave `/opt/muse/skills/flight-tracking/references/compensation.md` unread on runs where neither applies. A journey runs from one place the traveler stays to the next, connections included: the outbound, the return, a one-way trip or one part of a multi-city trip. When the last leg of a journey lands or its cancellation is confirmed, and that journey ended in a cancellation, a diversion, a missed connection or an arrival 2 hours 45 minutes or more late, read that reference, check the journey under its **Scheduled runs** and record it as checked in the trip state. On the first run, when `~/memory/travel/HISTORY.md` exists and the **Flight compensation** item records that the user asked for the past-flights check, read the same section, start the travel history check it describes, and record in the trip state that it was started.
<!-- flight-compensation-only:end -->

- The optional fare job, `flight-price-<goal-slug>`, requires Duffel to be returned by `muse.connector_search` before reading its docs or scheduling any calls. If it is unavailable or the lookup fails, continue with status monitoring and record the fare-coverage limitation in the trip's monitoring activity. Explain the limitation in a live conversation; background reconciliation records it without messaging the user. Do not call the CLI to test availability.

- When Duffel is available, create the fare job only when the paid total, currency and fare terms are known, using its fare-check guide under **When available**. Otherwise record the trip, run the status job, and ask a present user for the missing facts.

- Write each job's body so it stands alone, because the cron worker sees neither this skill nor the conversation. Include the owner, the state file path, the exact legs and booked baseline, the exact commands each run needs, the comparison and alert rules from the connector docs, the deduplication rule, failure handling, cadence changes and stop conditions.

- Record the ids of the jobs that exist in the state file and read each job back with `cron.view` after `cron.add` or `cron.update`.

## Decide what to tell the user

- Keep unchanged and below-threshold checks silent. Notify only for the alert conditions in the FlightAware and Duffel connector docs, or for routine updates the user explicitly asked for.

<!-- flight-compensation-only:start -->
- A likely compensation claim under [Flight compensation](references/compensation.md) is also worth one notice.
<!-- flight-compensation-only:end -->

- Before each notice, persist its stable fingerprint in the state file and add one concise activity with `tracking.create_entry`, or `user_goal.create_entry` for a user goal. Never send or log the same fingerprint twice.

- A failed read is not evidence that nothing changed. After three consecutive expected failures from one source, add one activity saying that source's coverage is degraded.

- When sources disagree, verify before calling a flight cancelled, following the cancellation rules in the FlightAware connector docs.

- Monitoring never authorizes changing, cancelling or rebooking a ticket, contacting a provider, accepting terms or spending money.

## Update and stop

- Apply a validated amendment or rebooking to the same owner. Update the current facts, keep the as-booked baseline, clear a pending fare candidate the change invalidates and add one activity. Compare provider timestamps so an older confirmation never undoes a newer amendment.

<!-- flight-compensation-only:start -->
- When a journey ended disrupted, check it under [Flight compensation](references/compensation.md) as the status job's compensation step describes, before moving past it or stopping or completing the trip. A booking the traveler cancelled or changed themselves is not a disruption. Leave out a journey whose flights are more than two days ahead: the check reads FlightAware's record of each flight, and there is none yet.
<!-- flight-compensation-only:end -->

- When a cancellation is confirmed and no replacement exists, set `trip.cancelled` to `true` and stop all of the trip's monitoring jobs.

- After the final leg lands, complete a Tracking owner with `tracking.set_status`, which retires its goal-owned jobs. For a user goal, remove the trip's monitoring jobs with `cron.remove` and leave the goal itself to the user.

- Stop the fare job earlier when the useful change or cancellation window closes. Remove either job when the user asks to stop, and check `cron.runs` when a promised update is missing.

<!-- flight-compensation-only:start -->
## Check compensation

- When the user asks whether an airline owes them money for a flight, or asks to check their past flights, follow [Flight compensation](references/compensation.md). It checks the laws that cover the journey, the past flights in the travel history, and how to file a claim with the user's approval.
<!-- flight-compensation-only:end -->

## Available connectors

- [FlightAware](/opt/hatch/connectors/flightaware/CONNECTOR.md) for live status, delays, gates and positions, and the status job.

- [Gmail](/opt/hatch/connectors/gmail/CONNECTOR.md) for the booking confirmation and airline notices.

- [Outlook Mail](/opt/hatch/connectors/outlook_mail/CONNECTOR.md) for the booking confirmation and airline notices.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- Confirm availability with `muse.connector_search` before reading these connector docs or scheduling their commands. Availability can depend on the user's country.

- [Duffel](/opt/hatch/connectors/duffel/CONNECTOR.md) for the daily [fare check](/opt/hatch/connectors/duffel/references/fare-check.md) on a booked trip. It does not report flight status. Copy the guide's availability check and refusal handling into the fare job so each run checks before calling Duffel.

## Websites

- Use `browser.browse` to confirm a change on the operating airline's flight-status page or the airport's departures and arrivals board. These carry gate and rebooking details first, in every country.

- [Flightradar24](https://www.flightradar24.com/) shows where the aircraft is. Its map position does not confirm boarding, gate or departure instructions.

## Alternatives for better results

- When a delay threatens a connection, look up the airline's next departures on the route so the user has options ready.

- For a pickup, offer landing and arrival-gate updates, since a final landing is otherwise silent.
