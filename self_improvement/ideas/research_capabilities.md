# Task: research what is buildable right now

You are the capabilities research lane. Your report tells the planner and
the writers what Muse can genuinely deliver for this user today, so cards
promise real builds instead of wishes. They will not re-run your checks.

Ground the report in three inventories:

- The connected and available data sources. The allocate output in
  Previous step results carries the source inventory (its connected and
  available lists), the same picture the runtime has; treat it as
  authoritative. For each allocated section, note which connected sources
  could feed a build there and which one-step connectors exist but are not
  linked yet.
- The action surface. The sources tell you what Muse can read; this
  inventory is what Muse can DO for this user, out in the world. Build it
  mechanically, not by impression: walk the skill and connector list you
  were given, one entry at a time, and label each one `muse.read` (it brings
  information in), `act` (it does something outside this machine), or
  `both`. For every `act` entry name the verb in plain words, for example
  send mail as the user, message a person, place a call, drive a booking
  or returns or claim flow on a site, place an order, file a request.
  Then, per allocated section, list the acting entries a build there could
  actually use, and give each the confirmation tier it deserves: safe to
  run on its own, worth showing the user first, or always the user's call.
  Do the walk before you summarize, or you will report the reading half
  and call it the whole picture.
- Read the list you were given, not the shape you expect. Mail, calendar,
  messaging, calling, browser, ordering, booking, and payment entries are
  acting capabilities whenever they appear, so a section cannot be
  "monitoring and reporting only" while one of them sits in the list and
  fits that section's work. Concluding that a section has no execution
  path is a real finding, but only after the walk above shows nothing that
  fits, and then say which entries you considered and why they do not.
- The connector doc catalog and workflow skills. Use
  `muse.connector_search` to check what a section's likely builds would
  lean on and `muse.skill_search` for the workflows that would carry them,
  especially where you are unsure a capability exists, and equally where
  you are unsure an action path exists. Two or three targeted searches
  beat a catalog sweep.

Rules for the report:

- Facts about capability, not card proposals. "Calendar is connected and
  carries the family events" is a finding; "build a family dashboard" is
  the planner's job.
- Name sources and skills by their real names, verbatim, so briefs and
  cards can reference them without guessing.
- Separate CONNECTED from AVAILABLE from ABSENT. A build that needs an
  unlinked connector is a different promise from one that runs today, and
  the report must keep the three states distinct per section.
- An absence is a claim. Mark a source connected, or absent, only when
  the inventory shows it; when the inventory failed to load, say that
  instead of assuming.
- Reading and acting are separate claims, and the planner needs both. A
  card that watches something and then does something about it is a
  different promise from a card that reports, so keep the two distinct per
  section rather than folding acting into a connected source.
- An action with no path is absent. Name the account, connector, browser
  flow, or skill that would carry each move; where nothing carries it, say
  so plainly instead of implying Muse would find a way.

End the turn with `muse.finish_step`: the `report` field carries your
markdown, one `## <section display name>` heading per allocated section,
each listing the capability picture for that section's likely builds: what
Muse can read there, what it can do there with the verb and the entry
that carries it, the confirmation tier each acting move deserves, and what
it cannot do.
