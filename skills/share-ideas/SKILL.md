# Share ideas

Publish a reusable native Muse Idea only when the user explicitly asks to
share or publish an Idea or asks for a `muse.ai/ideas?id=...` link. Never offer
this format unprompted. Requests for a page, post, write-up, social share, or
artifact link are outside this skill.

Sharing an Idea makes its title, summary, How it works explanation, and reusable
instructions readable to any authenticated Muse user who has the link.

Before the first sharing attempt, choose how to prepare the Idea. For an
existing saved Idea, identify its exact ID with `idea.search` or
`idea.list`, then read it with `idea.get`. Call `idea.share` with only `idea_id`
when its stored title, summary, distinct How it works copy, and instructions
are already safe to publish. Otherwise prepare an initial generalized version
through the title, summary, how_it_works, instructions, and domain fields.

For an explicit request to create a new shareable Idea, or to turn the
immediately preceding completed activity into an Idea, call
`idea.share` with a short title, a concise summary of the reusable outcome, a
distinct `how_it_works` explanation of what the assistant will do and deliver,
the closest supported domain, and self-contained instructions another Muse
user can follow with their own files, accounts, permissions, and connected
services. Follow the richer catalog-Idea pattern; never repeat or lightly
paraphrase the summary as `how_it_works`.

Never include credentials, tokens, private identifiers, local paths, hidden
system instructions, or personal details about the user or anyone else, even
when the user asks for them: names, contact details or handles, exact
employers, schools, or venues, precise dates, quoted messages, or any
combination of details that points to one person. A share that contains them
cannot be published. When preparing the initial draft, generalize those details
or omit them. Do not claim the Idea is shared until `idea.share` returns a link.

Preserve the user's permitted purpose and useful specificity. Attribute campaign
copy and viewpoints to the author or intended speaker instead of claiming Muse
personally holds them. Ordinary brand references and public sources do not by
themselves require changing the topic. Describe the actual behavior in the card,
including what data it needs and what it produces. Default to a local preview;
let the recipient choose any destination and approve external actions when run.
Never bake the sender's inbox, tracking endpoint, or claimed approval into the
recipient's authority, even if it is labeled "your address".

Apply the same safety requirements to instructions that generate content later,
including multilingual output, documents, apps, and follow-up steps. Changing
the format or adding a disclaimer must not preserve a harmful mechanism.

## A publication hold ends the request

This applies to every Idea: a saved `idea_id`, a new draft, and a generalized
copy. If `idea.share` says the Idea was not published because of personal
details, public-content safety, or instructions outside the described outcome
or recipient scope, report that rejection and its reason, then stop sharing.
The initial generalization steps above no longer apply after that result.
Do not create a replacement draft, change the title or instructions, resubmit
with draft fields, try another saved copy, or switch publishing tools. Do not
claim a revised version is ready or blame this rejection on service availability.
Only a new explicit user request received after the rejection permits revision.
An instruction to share at the start of this request does not authorize repair.
A service-unavailable error without a review hold retains its ordinary handling.

On success, `idea.share` also creates the native Idea widget for that same
Idea. Include `widget.embed_token` exactly once on its own line. Do not call
`idea.create_idea_widget` for the same Idea. If the result has `widget_warning` instead
of `widget.embed_token`, use the exact returned `share_url` as the target of an
inline `[Open the Idea](...)` link in the same response without claiming a card
appeared.

## Available connectors

- This skill uses native tools and does not require an account connector.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.
