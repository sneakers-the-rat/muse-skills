). A detected or similar product does not prove an exact match or the best price.

- Read a pasted Marketplace item or share link through the Facebook connector as its [docs](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) describe, never in the browser, then search for similar items from its title and description.

- Compare a used item with a new one on transport, inspection, seller reliability and the missing warranty, and keep new, used and refurbished offers distinct.

## Complete the purchase

- Route the purchase from the main conversation, through direct checkout or `browser.browse`. The browser owns its focused login and payment workers. Do not delegate live shopping to a subagent.

- Before checkout, continue the task that found the chosen product and close the product-search tasks that no longer matter with `browser.windows` `close`.

- Choosing items or building a cart moves no money. When a connector provides checkout instructions, follow those instead of the routing below.

- For catalog products, confirm each selected product's exact variant as the [Meta Catalog](/opt/hatch/connectors/meta_catalog_search/CONNECTOR.md) docs describe. When its product details carry a `checkout_token`, check out as the [Shopify UCP](/opt/hatch/connectors/shopify-ucp/CONNECTOR.md) docs describe, whatever its checkout flags say.

- Otherwise follow [browser checkout](