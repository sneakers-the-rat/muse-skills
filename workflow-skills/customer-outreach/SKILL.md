# Customer Outreach

## Choose the audience and channel

- Establish the business account, the outcome the user wants and who should receive the message. A CRM segment, an email list and an automation trigger can each contain different people, so check the actual recipients.

- Choose the channel for the message and the audience. A newsletter or campaign suits a large opted-in list, a text suits a short time-sensitive note to people who agreed to texts, and a few personal emails from the user's mailbox often work better for a small group.

- Select recipients from the business's own records. Do not infer sensitive traits such as health, religion or finances to target people.

## Respect consent and opt-outs

- Send marketing email and texts only to people who opted in, or who have a relationship with the business that the user can point to. List membership alone is not consent.

- Exclude unsubscribed, suppressed and bounced contacts in every tool you use, including when an audience moves between platforms.

- Make every marketing message identify the business honestly, use a subject line that matches the content and keep the platform's unsubscribe link or STOP reply handling in place.

- Send texts at reasonable hours in each recipient's timezone.

- Check with the user before contacting anyone whose consent is unclear. Rules differ by country and channel, for example CAN-SPAM and TCPA in the US and GDPR in Europe, so use the platform's consent and compliance settings rather than working around them.

## Write the message

- Focus on what the recipient needs, use claims the business can support and give one clear next step.

- Check every personalization field against real data and set a sensible fallback for missing values. Verify the links, the sender name and address, and where replies will go.

- Preview the message or send a test to the user when the platform supports it.

## Get approval and send

- Show the user the final audience with its size, the exact content, the sender and the send time with its timezone, and get their approval before sending, scheduling or activating anything.

- Keep a draft separate from a live automation. Activating a flow or enrolling contacts in one can start sending immediately.

- Never retry a send automatically. When a result is uncertain, check the campaign or message status first so nobody receives a duplicate.

- Report a message as accepted or scheduled until the platform confirms delivery.

## Measure and follow up

- Keep accepted sends, deliveries, opens, clicks, replies, unsubscribes and conversions distinct, each with the right denominator and attribution window. Treat opens as a weak signal, since some mail apps load images automatically.

- Read replies promptly and route each to the person or tool that should answer it.

- Keep customer records in the business's own tools. A lesson about what worked can improve a skill, but individual customer details do not belong in reusable instructions.

## Available connectors

- [HighLevel](/opt/hatch/connectors/ghl/CONNECTOR.md) for CRM contacts, pipelines, conversations, appointments and campaign or workflow enrollment.

- [Klaviyo](/opt/hatch/connectors/klaviyo/CONNECTOR.md) for email and SMS campaigns, flows, lists, segments, subscription consent and campaign reports.

- [Gmail](/opt/hatch/connectors/gmail/CONNECTOR.md) for individual emails from the user's own Gmail address.

- [Outlook Mail](/opt/hatch/connectors/outlook_mail/CONNECTOR.md) for individual emails from the user's own Outlook address.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Beehiiv](/opt/hatch/connectors/beehiiv_mcp/CONNECTOR.md) for newsletters, subscribers, automations and post performance.

- [Quo](/opt/hatch/connectors/quo_mcp/CONNECTOR.md) for business texts, including bulk messages, and contacts in the user's Quo workspace.

- [Fin by Intercom](/opt/hatch/connectors/intercom_mcp/CONNECTOR.md) for reading customer conversations, contacts and help articles and adding internal notes. It cannot send customer replies.

## Websites

- Use the user's existing email or CRM platform through `browser.spawn_task` when its connector lacks an operation or no connector exists. Carry the approved audience, content, sender and schedule into the task, keep the same exclusions, and have it return the campaign status and link.

- [Mailchimp](https://mailchimp.com/) for audiences and campaigns already managed there.

- [HubSpot](https://www.hubspot.com/) for contacts and marketing email already managed there.

- [Brevo](https://www.brevo.com/), a European platform for email and SMS campaigns, for audiences already managed there.

- Use the [Intercom](https://app.intercom.com/) inbox only to send a customer reply, which the Intercom connector cannot do.

- Moving an audience to a new platform is the user's decision, never a fallback for one failed send.

## Alternatives for better results

- Pilot a new message with a small consented segment before sending to everyone, and judge it by qualified replies or the user's business outcome rather than opens.

- Test one change at a time, such as the subject line or the offer, so the result is clear.

- Win back lapsed customers only within the consent they gave, and offer an easy way to update preferences rather than only unsubscribe.
