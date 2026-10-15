# Meeting Notes and Follow-ups

## Find the meeting record

- Identify the meeting by its title, date and attendees, then read its actual notes, transcript or recording. A calendar event or a short summary identifies the meeting but is not a record of what was said.

- Look where the user keeps meeting records, such as a notetaker app, a Zoom recording or summary, recordings from their glasses through the Audio Notes skill when it is available, shared notes or an emailed recap. Google Meet saves its transcripts to the organizer's Google Drive and attaches them to the calendar event.

- Confirm the user can open the recording or transcript before promising a recap. An attendee often cannot open the host's recording.

- Keep speaker names and timestamps where they help verify a decision, and say when a transcript is partial or garbled.

## Extract decisions and actions

- Separate decisions from proposals, open questions and background. Record an owner or deadline only when the meeting or the user set one, and flag actions nobody owns.

- When accounts of the meeting disagree, quote or link the passage and ask the user rather than inventing agreement.

## Deliver the follow-up

- Write the recap with decisions first, then actions with their owners and dates, then open questions. Link the source and any records you create.

- Put the recap where the user wants it. To update their existing notes or project page, find it in that app first, since a new file elsewhere does not update it.

- When the user would rather not connect an app, a local file under `~/workspace/notes/` works well, or a file made with `artifact.create_file`.

- Sending a recap, creating tasks and scheduling the next meeting are separate actions. Do only the ones the user asked for, with Email, Task Management and Scheduling, and check for existing tasks before adding new ones.

- Draft a follow-up email only to the attendees the user confirms, from the account they use for that meeting. Report what was actually saved, sent or booked.

## Available connectors

- [Granola](/opt/hatch/connectors/granola/CONNECTOR.md) for the user's Granola notes and transcripts.

- [Zoom](/opt/hatch/connectors/zoom/CONNECTOR.md) for Zoom recordings, transcripts and meeting summaries the user can access.

- [Google Calendar](/opt/hatch/connectors/google_calendar/CONNECTOR.md) to identify the meeting and its attendees and find an attached Google Meet transcript.

- [Outlook Calendar](/opt/hatch/connectors/outlook_calendar/CONNECTOR.md) to identify a meeting and its attendees in a Microsoft account.

- [Gmail](/opt/hatch/connectors/gmail/CONNECTOR.md) to find an emailed recap and send the follow-up.

- [Outlook Mail](/opt/hatch/connectors/outlook_mail/CONNECTOR.md) to find an emailed recap and send the follow-up from Outlook.

- [Notion](/opt/hatch/connectors/notion/CONNECTOR.md) to update the user's existing meeting notes or project pages.

- [Google Drive](/opt/hatch/connectors/google_drive/CONNECTOR.md) to read a Google Meet transcript saved in the organizer's Drive.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Otter](/opt/hatch/connectors/otter_mcp/CONNECTOR.md) for Otter conversations and transcripts.

- [Circleback](/opt/hatch/connectors/circleback_mcp/CONNECTOR.md) for Circleback notes, transcripts and action items.

- [Speak AI](/opt/hatch/connectors/speak_ai_mcp/CONNECTOR.md) for Speak AI recordings, transcripts and analysis.

- [Read AI](/opt/hatch/connectors/readai_mcp/CONNECTOR.md) for Read AI meeting reports.

## Websites

- [Microsoft Teams](https://teams.microsoft.com/) for a Teams meeting's recording, transcript or recap, which no connector reads.

- Notetakers that have no connector, such as [Fireflies](https://fireflies.ai/).

- Open these through `browser.spawn_task` in the user's account, naming the meeting's title, date and attendees, and have it return the transcript or recap text it found.

## Alternatives for better results

- Fill gaps in a transcript with the agenda, shared notes, chat messages and later emails. When exact wording matters, quote the passage with its timestamp so the user can check the recording.

- Ask the user or an attendee about an unclear owner or decision rather than guessing.

- A short list of decisions and actions is often more useful than a full summary.

- Offer to turn dated actions into tasks or reminders.
