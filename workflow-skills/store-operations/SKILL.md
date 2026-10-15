# Store Operations

## Find the right store and record

- Identify the store and the exact product, variant, order or customer before acting, and read its current state first.

- Keep the store's states apart. A product's visibility, stock on hand, reserved inventory, payment status and fulfillment status describe different things, and updating inventory does not mean an order shipped.

## Change the catalog and inventory

- Change only what the merchant asked, preserving other variants, prices, tax and shipping settings. A request to create a product does not authorize a promotion or other catalog changes.

- Show the exact change and get the merchant's approval before creating, editing, publishing or deleting products, or changing stock or prices.

- For a bulk change, review the complete intended set first, try one item when the result is uncertain and keep a result for each item. Use record versions and the provider's idempotency keys where they exist.

- For print-on-demand, choose the product, print provider and variants together, and check production and shipping cost against the selling price before the listing goes live.

## Handle orders, refunds and fulfillment

- Keep cancellation, refunds and fulfillment as separate actions, each with its own approval. Confirm the amount and items for a partial refund.

- Show the cost, provider, address and delivery estimate before submitting a fulfillment or freight order, because it can charge the merchant.

- Compare freight quotes on the same cargo, dates and terms, and confirm a booking only from the provider's record.

- Use [Customer Outreach](/opt/muse/skills/customer-outreach/SKILL.md) for messages to customers about their orders.

## Verify and report

- After a timeout or lost response, read the record before repeating a change, because the first attempt may have succeeded. Retry only items confirmed unchanged, and report partial success.

- Check totals, currencies, fees and refunds against the merchant's records, and link the records you changed.

## Available connectors

- [Shopify](/opt/hatch/connectors/shopify/CONNECTOR.md) for products, collections, inventory, orders, customers, discounts and store analytics.

- [Printify](/opt/hatch/connectors/printify/CONNECTOR.md) for print-on-demand products, print providers, artwork uploads and fulfillment orders.

- [Stripe](/opt/hatch/connectors/stripe/CONNECTOR.md) for the store's payments, refunds and disputes.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Gumroad](/opt/hatch/connectors/gumroad_mcp/CONNECTOR.md) for digital products, sales and payouts, and for drafting and publishing products.

- [Wix](/opt/hatch/connectors/wix_mcp/CONNECTOR.md) for a store built on Wix.

- [Flexport](/opt/hatch/connectors/flexport_mcp/CONNECTOR.md) for freight quotes, shipment tracking and bookings.

- [AfterShip](/opt/hatch/connectors/aftership/CONNECTOR.md) for carrier tracking of shipped orders.

## Websites

- Use the store's own admin site with `browser.spawn_task` for an operation its connector lacks, such as a bulk import, keeping the same store and product IDs. Have the task report exactly what changed.

- [Shopify Admin](https://admin.shopify.com/) for themes, checkout, payments and domains, which the Shopify connector cannot change.

- [Square Dashboard](https://squareup.com/dashboard/) for a Square store, and the merchant's own WordPress admin for a WooCommerce store.

- [Etsy](https://www.etsy.com/) Shop Manager for an existing Etsy shop.

## Alternatives for better results

- Export the catalog and use the dashboard's bulk import for complex variant changes, keeping product and order IDs.

- Try a price or listing change on a few products before rolling it out to the whole catalog.

- For an inventory or delivery discrepancy, compare warehouse, payment-processor and carrier records with the storefront, and report what the records support.
