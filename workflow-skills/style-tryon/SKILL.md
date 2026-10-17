# Style Try-on

## Offer it

- When catalog or browser shopping results show clothing, shoes or accessories the user will wear, end that reply with one short offer and one `muse.create_options` chip in the user's language. It replaces the [Shopping](/opt/muse/skills/shopping/SKILL.md) skill's variant offer.

- For two or more products, ask "Want to see a few on you?" with "Visualize <category> on me". For one, ask "Want to see it on you?" with "Try it on me".

- Offer it once per request, for anything but swimwear, lingerie, rings, bracelets and watches. After the user declines, leave it out for the rest of the conversation.

## Run it

- When the user accepts, asks to see or compare items on themselves, or picks a favorite from a try-on comparison, follow the [try-on flow](references/flow.md).

- Those replies follow the flow instead of the Shopping skill's formatting, with no new results card and no further "Try it on me" offer.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.
