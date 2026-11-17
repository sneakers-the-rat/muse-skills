# Zocdoc

- Zocdoc finds US healthcare providers, their locations, specialties, visit reasons, accepted insurance and open appointment times. Use `/opt/hatch/bin/zocdoc`, which reads these details and returns booking links.

- The CLI cannot book, reschedule or cancel an appointment. Use the browser flow to book after aligning on the provider and available time slot.

## Find providers and availability

- Before searching health providers, work with the user to figure out what insurance plan the user has or they want to self pay, then search with a correct insurance filter. Many providers don’t accept out of network insurance, so searching without an insurance filter may lead to results that cannot be booked.

```text
/opt/hatch/bin/zocdoc list-tools
/opt/hatch/bin/zocdoc call-tool --name <tool> --arguments-json '<json-object>'
```

- Run `list-tools` for each tool's current inputs. The tools are `searchProviders`, `getProviderLocation`, `getAppointmentAvailability`, `listSpecialties`, `listVisitReasons`, `searchInsurancePlans` and `listInsuranceCarriers`, and all of them only read.

- Pass the IDs one tool returns, such as provider-location, specialty, visit-reason and insurance-plan IDs, into the next tool. Keep them in tool calls only, not in replies.


## Present and verify the results

- Write widget titles, row text and selection messages in the user's language. Treat the English labels below as examples.

- Before offering an appointment or starting browser booking, verify the returned location, specialty, visit reason, visit mode, insurance status and appointment date and time against the user's request and symptoms. When offering a clinically relevant alternative because no exact match is available, highlight each unmet requirement and obtain the user's agreement before proceeding. Omit providers that do not match the user's care needs.

- Present initial provider choices in the widget defined below, without duplicating them in a separate text list or summary.

- Present at most 4 providers using `widget.create_list_widget`, with one `type: "send_message"` row per provider location. Set `image_url` to the returned `providerPhotoUrl` when available. Put the provider name and specialty in `title`, star rating and review count in `subtitle` (e.g. "★ 4.8/5 · 120 reviews"), and the user's insurance plan and network status in `tertiary_title` (e.g. "Aetna PPO · In network"). Use "Self-pay" when applicable. Get rating and review details, `image_url` with `getProviderLocation`; omit unavailable values. Set `data.text` to a reply selecting that provider. Use a widget title meaning "Tap to select a doctor".

- After the user selects a doctor, briefly acknowledge the selected provider and location and ask which appointment time they prefer, using natural wording that fits the conversation. Use `muse.create_options` for at most 6 of that doctor's matching slots, with each option showing the local date, time and time zone. Embed the returned `embed_token` unchanged in the same message as the question. Keep each option linked to its provider location and exact returned `bookingUrl` for the browser booking flow. Selecting a slot does not approve final booking.

## Complete the booking

- When the user asks to book, continue with the selected appointment through [browser booking](/opt/muse/assets/booking/references/browser-booking.md) and [checkout](/opt/muse/assets/booking/references/checkout.md). Use one `browser.browse` task with the selected slot's exact `bookingUrl` and known booking choices, and keep its `task_id` through review, changes, submission and verification.

- Zocdoc will need user email and phone number to book (no password needed). Prioritize using the user's known contact email and phone number unless they specify different details for this appointment. Ask only for missing or unclear required details. For retrieving verification codes, follow [Privacy and credentials](~/docs/privacy-and-credentials.md#sign-in-secrets).

- Before clicking the booking button, do a final review with the user by confirming provider, address, specialty, visit reason, visit mode, date, time, time zone, insurance status, and email, phone number, patient name, DOB used for booking, plus any fees or cancellation terms. Report success only after Zocdoc confirms the appointment.

- When user input or takeover is required, pause and explain what is needed. After it is provided, resume the same browser task using its `task_id`.



## Related skills

- [Health Review and Visit Preparation](/opt/muse/skills/health-review/SKILL.md)

- [Scheduling](/opt/muse/skills/scheduling/SKILL.md)

- Use `muse.skill_search` to find other skills and `muse.connector_search` to find other connectors.
