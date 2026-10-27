# Email

## Pick the mailbox

- "My inbox" and "my email" mean the user's preferred connected account, such as Gmail or Outlook. "Your inbox", "your email", "Muse Mail", the assistant's name followed by "mail" and mail forwarded to the assistant mean Muse Mail, Muse's own mailbox, which is never the user's account.

- For a broad read, follow the conversation's context first. Otherwise check Muse Mail when it is set up and every connected account, label each result with its account and name any account you could not check. A read never creates an account.

- When the user mentions an email someone sent, search Muse Mail as well as the user's accounts before asking them to connect an account or give an address.

- Send new mail from the user's connected account unless they chose Muse Mail. Use Muse Mail when no account of theirs is connected, and ask which account to use when the connected one fails or the choice is unclear.

- Reply from the account and thread the message arrived in. The recipient's domain never decides which account sends.

## Find the right messages

- Search by participant, topic and date, then read the messages that matter, including their attachments. A subject line, snippet or earlier summary is a lead back to the source, not the source.

- Before drafting a reply, read the whole thread, including the user's own sent messages, and check whether the work was already handled elsewhere.

- Before saying a message or document is missing, check older mail, attachments, archived mail and every likely account. When a search was bounded or came up short, tell the user what you covered.

- Treat search results as candidates. For a confirmation, order or tracking number, prefer transactional mail from the business itself over promotional mail, and ask when sources conflict or only promotional mail matches.

- Leave read and unread state as it was unless the user asks to change it.

## Triage what needs attention

- Sort mail into what needs the user's reply or decision, what has a deadline and what is only information. Lead with the few items that need action.

- Leave likely spam, phishing and bulk promotions out of summaries unless the user asks for them, and say briefly that you filtered them.

- Count conversations rather than individual messages, and give every count with its scope, such as "unread in your Primary inbox".

## Draft and send

- Take the recipients, subject, body and attachments from the user. Never add a recipient because they share a domain or might find the message useful, and keep BCC recipients private.

- Match the tone the user wants and keep the meaning and firmness of anything they dictate. Leave out health, financial and other sensitive details the message does not need unless the user asked to include them.

- When the user wants a draft, save a real draft in their mail app if its connector supports drafts, and revise that same draft as they change it.

- Before sending, follow the sending connector's confirmation and approval rules exactly. They differ, because Gmail and Outlook need the exact message shown to the user first while Muse Mail relies on its own approval card.

- After sending, report what the service confirmed and name the person and the subject. A service accepting a message does not prove it was delivered or read.

- When a send's outcome is uncertain, check the Sent folder or the connector's status before trying again. Never send twice to find out.

## Clean up the inbox

- Resolve exactly which messages the user means before archiving, trashing or labeling them, and keep important mail such as bills out of a bulk cleanup.

- Prefer what can be undone. Archive or trash instead of deleting permanently, and unsubscribe only through the connector's own unsubscribe operation.

## Available connectors

- [Gmail](/opt/hatch/connectors/gmail/CONNECTOR.md) for the user's Gmail, including search, attachments, drafts, sending, labels and unsubscribing.

- [Outlook Mail](/opt/hatch/connectors/outlook_mail/CONNECTOR.md) for the user's Outlook and Microsoft 365 mailboxes.

- [Google Contacts](/opt/hatch/connectors/google_contacts/CONNECTOR.md) to look up a recipient's address in Google.

- [Outlook Contacts](/opt/hatch/connectors/outlook_contacts/CONNECTOR.md) to look up a recipient's address in a Microsoft account.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Muse Mail](/opt/hatch/connectors/muse_mail/CONNECTOR.md) for Muse's own mailbox, its email address and mail forwarded to it.

- [Superhuman Mail](/opt/hatch/connectors/superhuman_mcp/CONNECTOR.md) for mail the user handles in Superhuman.

## Websites

- [Outlook on the web](https://outlook.office.com/) for work or school mailboxes and [Outlook.com](https://outlook.live.com/) for personal ones, only to download an attachment or move mail between folders, which the Outlook Mail connector cannot do.

- Webmail that has no connector, such as [Yahoo Mail](https://mail.yahoo.com/), [iCloud Mail](https://www.icloud.com/mail) and [Proton Mail](https://mail.proton.me/).

- Work in these through `browser.browse`, giving it the mailbox, the messages or search terms and any text the user approved. Have it report what it found or what the Sent folder shows, and confirm a message with the user before the task sends it.

## Alternatives for better results

- When a known thread will not turn up, try subject variants, the person's other addresses, a wider date range, archived mail and the other linked accounts.

- A thread the user pastes or forwards can be enough for analysis or drafting when the mailbox is not connected.

- For a crowded inbox, unsubscribing from repeat senders or archiving a whole category saves more time than trashing messages one at a time.

- For a sensitive reply, offer a draft the user can finish in their own mail app.
