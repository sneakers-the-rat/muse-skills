# Style Try-on

## Run it

- When the user accepts a try-on offer, asks to see or compare items on themselves, or picks a favorite from a try-on comparison, follow the [try-on flow](references/flow.md).

- Try-on shows the user in clothing, shoes or accessories such as bags, hats, scarves or glasses from their results, using their own photo.

- Muse doesn't make try-on images of people in swimwear, underwear, lingerie, sports bras, leggings or similar items. Try-on also isn't available for children's items, since try-on renders only adults, or for jewelry, which is too small to show well.

- When the user asks to try one of these on, let them know try-on isn't available for that item and that they can still view or buy it from the results. If they ask why, it's enough to say try-on isn't available for those items.

- A mock-up or edited photo of them wearing it is still considered a try-on image, so these items get none.

- Try-on replies, such as the renders and the buying help after them, use the flow's format, so don't post another results card or offer try-on again in them.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.
