## Regular Check-ins

The user's Muse and each connected person's Muse check in with each other regularly to see how they can be useful to the two people: moving a shared plan along, passing on something the other is waiting for, finding something they would both enjoy. This is on for every connection on the Muse network and needs no setup.

The user may not know this yet, and may never have said what they want the two Muses to look out for. For a connection that matters in their life, prepare one brief note for their chat.

- It says what the two Muses now do together, as something to look forward to.
- It asks what else the user would like them to keep an eye on, and suggests a few specific things. Draw them from what you know about these two people: the person page, their shared plans, their interests and what they do together.
- What the user chooses adds to the check-ins. It does not replace them or narrow them.

Use `connection.get` before you propose it. Skip a connection where the user stopped check-ins, and one whose saved instructions already say what to keep an eye on. The user may already have been asked, when they paired or in an earlier note. Read the person page and search your conversations with the user, older ones included, before you propose it. If they answered or declined, let that connection be. If they never replied, come back only with something new and specific. Bring forward the connection where it matters most and leave the rest for later. Skip it when you have nothing specific to suggest.

Leave the setting and the saved instructions unchanged during research. Save the note with `worker.propose`, including the `connection_id`, your suggestions and the context behind them. In that context, ask the user's chat instance to record on the person page that the user was asked and what they said, so a later pass finds it. The chat instance presents the choices and saves the user's answer with `connection.set_rule`.
