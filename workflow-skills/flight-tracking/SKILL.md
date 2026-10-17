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

- Record the booking and source fingerprints, the traveler relationship and count, the as-booked itinerary, the paid total and currency, the fare terms, the current facts, the last comparison and any pending fare candidate, the last notified facts and fingerprints, failure counts and both cron ids.

- Never store full messages, raw provider output, names, ticket numbers, identity documents, contact or payment details, loyalty numbers, Known Traveler Numbers or CLEAR identifiers.

## Run two monitoring jobs

- List the owner's jobs with `cron.list` and reuse an equivalent goal-owned job instead of adding another. Each job has the owner `goal:<goal-slug>`.

- The status job, `flight-status-<goal-slug>`, reads the next active leg from FlightAware on the cadence in the [FlightAware](/opt/hatch/connectors/flightaware/CONNECTOR.md) connector docs.

- The fare job, `flight-price-<goal-slug>`, runs the daily fare check in the [Duffel](/opt/hatch/connectors/duffel/CONNECTOR.md) connector docs. Create it only when the paid total, currency and fare terms are known. Otherwise record the trip, run the status job, and ask a present user for the missing facts.

- Write each job's body so it stands alone, because the cron worker sees neither this skill nor the conversation. Include the owner, the state file path, the exact legs and booked baseline, the exact commands each run needs, the comparison and alert rules from the connector docs, the deduplication rule, failure handling, cadence changes and stop conditions.

- Record both cron ids in the state file and read each job back with `cron.view` after `cron.add` or `cron.update`.

## Decide what to tell the user

- Keep unchanged and below-threshold checks silent. Notify only for the alert conditions in the FlightAware and Duffel connector docs, or for routine updates the user explicitly asked for.

- Before each notice, persist its stable fingerprint in the state file and add one concise activity with `tracking.create_entry`, or `user_goal.create_entry` for a user goal. Never send or log the same fingerprint twice.

- A failed read is not evidence that nothing changed. After three consecutive expected failures from one source, add one activity saying that source's coverage is degraded.

- When sources disagree, verify before calling a flight cancelled, following the cancellation rules in the FlightAware connector docs.

- Monitoring never authorizes changing, cancelling or rebooking a ticket, contacting a provider, accepting terms or spending money.

## Update and stop

- Apply a validated amendment or rebooking to the same owner. Update the current facts, keep the as-booked baseline, clear a pending fare candidate the change invalidates and add one activity. Compare provider timestamps so an older confirmation never undoes a newer amendment.

- When a cancellation is confirmed and no replacement exists, stop both jobs.

- After the final leg lands, complete a Tracking owner with `tracking.set_status`, which retires its goal-owned jobs. For a user goal, remove both jobs with `cron.remove` and leave the goal itself to the user.

- Stop the fare job earlier when the useful change or cancellation window closes. Remove either job when the user asks to stop, and check `cron.runs` when a promised update is missing.

## Available connectors

- [FlightAware](/opt/hatch/connectors/flightaware/CONNECTOR.md) for live status, delays, gates and positions, and the status job.

- [Duffel](/opt/hatch/connectors/duffel/CONNECTOR.md) for the daily fare check on a booked trip. It does not report flight status.

- [Gmail](/opt/hatch/connectors/gmail/CONNECTOR.md) for the booking confirmation and airline notices.

- [Outlook Mail](/opt/hatch/connectors/outlook_mail/CONNECTOR.md) for the booking confirmation and airline notices.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- Use `browser.browse` to confirm a change on the operating airline's flight-status page or the airport's departures and arrivals board. These carry gate and rebooking details first, in every country.

- [Flightradar24](https://www.flightradar24.com/) shows where the aircraft is. Its map position does not confirm boarding, gate or departure instructions.

## Alternatives for better results

- When a delay threatens a connection, look up the airline's next departures on the route so the user has options ready.

- For a pickup, offer landing and arrival-gate updates, since a final landing is otherwise silent.
