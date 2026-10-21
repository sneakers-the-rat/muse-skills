# Scheduling

## Gather the constraints

- Settle who must attend, how long it runs, the date range, each person's timezone and any hard limits such as working hours, travel time or buffers. Ask once, together, for what you cannot find yourself.

- Take the timezone from where the meeting happens. An event during a trip uses the destination's timezone, and a call across countries needs each participant's local time.

- Check for a daylight-saving change between today and the meeting date, and keep the event in its own timezone rather than converting it to the user's.

## Find a time that works

- Read every calendar that matters, including other linked accounts and shared calendars. A calendar you could not read does not mean that person is free.

- Treat tentative events and holds as possible conflicts, and say which people or calendars you could not check.

- Offer two or three workable times in each participant's local time, with `muse.create_options` when the user only needs to pick one. Share early and late hours fairly across timezones.

## Hold, invite or share a link

- Match the action to the request. A hold or focus block is a private busy event, an invitation emails the guests, a booking link lets others choose a time, and times proposed in a message stay provisional until someone accepts.

- Never create, move or cancel an event, or send an invitation, that the user did not ask for. Finding a time is not permission to book it.

- When others should choose, share the user's booking link, such as a Calendly event type. To book on someone else's link, use their page with the time the user picked.

- Add a video link when the meeting needs one, such as Google Meet from the calendar or a Zoom meeting, and include it in the invitation.

- For a personal reminder, add a calendar event when the user wants it on their calendar. Otherwise set a reminder with `cron.add`.

## Create or change the event

- Work in the calendar and account that already hold the event, and keep its timezone, guests and other details the user did not ask to change.

- For a recurring event, settle whether the change applies to one occurrence, to this and later ones, or to the whole series.

- Before any write that notifies guests, follow the calendar connector's confirmation rules and make clear who will be notified.

- Read the event back after the write and confirm the final local time, timezone and guests. A sent invitation is not an acceptance.

- If a write's result is uncertain, read the calendar before trying again, so you never create a duplicate.

- A confirmation email or meeting notes the user also wants are separate tasks. Use Email or Meeting Notes and Follow-ups for them, in the account the user named.

## Book a medical appointment

- Match the specialty, visit reason, location, insurance, whether the user is a new or returning patient, timing, language and accessibility needs.

- Find candidates through the insurer's directory, the practice's own site or Zocdoc when it is available, then verify coverage with the insurer or the practice. A listed slot or booking link is not a confirmed appointment.

- Book through the practice's online booking or, when the phone tools are available, a call started with `phone.begin_call` and placed after the user confirms. Share only the medical details the booking needs.

## Available connectors

- [Google Calendar](/opt/hatch/connectors/google_calendar/CONNECTOR.md) for the user's Google calendars, free and busy times, events, invitations and Google Meet links.

- [Outlook Calendar](/opt/hatch/connectors/outlook_calendar/CONNECTOR.md) for the user's Outlook and Microsoft 365 calendars.

- [Calendly](/opt/hatch/connectors/calendly/CONNECTOR.md) for the user's own booking links, booked meetings and their invitees.

- [Google Contacts](/opt/hatch/connectors/google_contacts/CONNECTOR.md) to find attendees' addresses in Google.

- [Outlook Contacts](/opt/hatch/connectors/outlook_contacts/CONNECTOR.md) to find attendees' addresses in a Microsoft account.

- [Zoom](/opt/hatch/connectors/zoom/CONNECTOR.md) for a Zoom meeting link when the user's account offers meeting creation.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Zocdoc](/opt/hatch/connectors/zocdoc/CONNECTOR.md) for US doctors, accepted insurance and open appointment times, with a link for the user to book.

- [Superhuman Mail](/opt/hatch/connectors/superhuman_mcp/CONNECTOR.md) for availability and invitations from a Superhuman account.

## Websites

- A participant's own booking page, such as a Calendly or Microsoft Bookings link they sent, which the Calendly connector cannot book. Give `browser.browse` the link, the user's name and email and the chosen time with its timezone.

- Have that task stop for the user's go-ahead before it books, and report the confirmation it receives.

- [Doodle](https://doodle.com/) to poll a group when nobody's calendar is visible.

- [Zocdoc](https://www.zocdoc.com/) to search US doctors when the connector is unavailable. The user completes a booking there, since the connector cannot book.

- [Doctolib](https://www.doctolib.fr/) for doctors and booking in France, Germany and Italy.

## Alternatives for better results

- Without calendar access, propose a few times in a message, share the user's booking link or run a poll, and keep the times provisional until someone accepts.

- Leave buffer and travel time between in-person meetings.

- An email update can replace a meeting when the user is open to it, but keep an explicit request to meet.

- When the first open appointment is too far away, ask the practice about a cancellation list or a nearby location with earlier openings.
