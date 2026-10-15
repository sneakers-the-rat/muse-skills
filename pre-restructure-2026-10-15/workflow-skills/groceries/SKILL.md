# Grocery and Food Delivery

- Use [Shopping](/opt/muse/skills/shopping/SKILL.md) for products a grocery store does not sell.

## Build the basket

- Start from the user's own grocery list when they keep one in a connected app, and keep its quantities and notes.

- A request for a grocery list does not ask you to change a cart, so build the list first and shop only when the user asks.

- Choose a grocery service and store that deliver to the address or offer pickup near it, starting with one the user prefers. A user who is traveling may still be shopping for home.

- Turn recipes and household needs into quantities with clear units. Distinguish the amount needed from the size of one package.

- Compare pack sizes and unit prices within the chosen store. Keep the item subtotal apart from the final order cost, and include markups, minimum orders, fees and tips only when you know them.

- Avoid splitting an order across stores when extra fees or trips cancel out the saving.

- Use known substitution preferences. Ask before a replacement that would change an allergen, an essential ingredient or the budget, and group cart changes when the service allows it.

- When comparing another service, use equivalent quantities and its current delivery or pickup terms.

## Present products and the cart

- Resolve products with `shopping.resolve_results` before naming them, whether or not a widget follows, and present a search's results with `shopping.create_shopping_results_widget`, as the Instacart docs describe for Instacart results.

- Keep each store's product order, prices, brands, images and availability, and never rerank its results.

- Show the cart and summarize the changes, warnings and skipped items the way the store's connector doc describes, including when it leaves the cart out at checkout and where the widget goes relative to the summary.

- Take cart contents, quantities, prices and subtotals only from a fresh read of the store's cart, never from memory, saved lists or search results.

- A subagent does not call the resolver. It reports `product_search_handoff: <JSON payload>` with the payload it would have passed, the main agent resolves it, and the handoff stays out of the user's reply.

- Never put results or the basket in a Markdown file unless the user asks.

## Cite products

- Write each resolved product's name as its marker everywhere, in every message, for the whole conversation. That includes cart summaries, substitution questions and turns that come back to a product later.

- Reuse the same marker each time a product comes up, even when a widget above already shows it.

- Put the marker where the name would go, and never refer to a resolved product by a description, such as "the organic one" or "the $4 one", because that drops its verified name and link.

- Name a product without a marker only when no successful resolve returned one. Resolve a product from a result file before naming it, and if it cannot be resolved, name it plainly without inventing a marker, URL or link.

- Write each marker exactly as returned. Never build one from `citation_id`, repeat the product name beside it or add a link.

## Check out and confirm

- Before checkout, review quantities, substitutions, the address, the delivery or pickup window and the final cost.

- Confirm the order from the service's order record, and say which substitutions or delivery details are still provisional.

## Prepared meals

- The restaurant's own ordering can beat delivery apps on total cost or arrival time. Compare the delivered total, including fees and tip, before recommending one.

- When the user would rather eat out, use [Restaurant Reservations](/opt/muse/skills/restaurant-reservations/SKILL.md).

## Available connectors

- [Places](/opt/hatch/connectors/places/CONNECTOR.md) for nearby stores and restaurants and their opening hours.

- [Google Tasks](/opt/hatch/connectors/google_tasks/CONNECTOR.md) or [Todoist](/opt/hatch/connectors/todoist/CONNECTOR.md) for a grocery list the user keeps there.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Instacart](/opt/hatch/connectors/instacart/CONNECTOR.md) for grocery search, carts and checkout links at the user's chosen store.

- [Deglaze](/opt/hatch/connectors/deglaze_mcp/CONNECTOR.md) for the user's saved recipes, meal plans and grocery lists.

## Websites

- [Walmart](https://www.walmart.com/) for grocery delivery and pickup in the US, which Instacart does not cover.

- [Tesco](https://www.tesco.com/groceries/), [Sainsbury's](https://www.sainsburys.co.uk/) or [Ocado](https://www.ocado.com/) for groceries in the UK, where Instacart does not deliver, and the user's chosen supermarket elsewhere.

- The restaurant's own ordering page, [DoorDash](https://www.doordash.com/), [Uber Eats](https://www.ubereats.com/) or [Grubhub](https://www.grubhub.com/) for prepared meals in the US, and [Deliveroo](https://deliveroo.co.uk/), [Just Eat](https://www.just-eat.co.uk/) or [Uber Eats](https://www.ubereats.com/gb) in the UK.

## Alternatives for better results

- Offer pickup when delivery fees, minimum orders or tips outweigh the convenience.

- Suggest a store brand or a larger pack when its unit price is clearly lower and the user is flexible.
