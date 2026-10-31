) in one browser task through confirmation.

- Products with a `checkout_token` keep their merchant cart as the Shopify UCP connector docs describe, and a connector with its own cart support keeps it there. Otherwise, ask `browser.browse` to build the merchant cart with the specified variants and quantities and prepare it for confirmation, without purchasing, and continue the same task when the user changes the cart. The store holds, prices and discounts that basket, so never keep a list of your own as a cart. Follow the connector's instructions for cart reads, changes and widgets.

- Keep the catalog `cart_id` or browser `task_id` in context, and never show internal IDs to the user. Cart confirmations return through the browser task to this conversation, each with its own `confirmation_id`, and payment authorization uses the payment approval interface. Do not ask for either decision twice.

- Once the user chooses, carry the exact variant, merchant, quoted total and its source, and the delivery estimate into checkout.

- When the checkout gets worse, such as a sale that ended, a higher price or slower delivery, recheck the strongest alternatives, including the official store. Show any better option with its total and arrival date before asking the user to accept worse terms. Agreement to a higher price is not a preference for it over a cheaper offer the user has not seen.

- Respect a seller the user chose on purpose, and explain the tradeoff instead of switching stores silently.

- Follow `~/docs/chat/payments-and-purchases.md` for the checkout review, payment choice and approval, and the chosen wallet's docs, [Link by Stripe](/opt/hatch/connectors/stripe-link/CONNECTOR.md) or [Shop Pay](/opt/hatch/connectors/shop-pay/CONNECTOR.md), for its setup.

- Stop after a denial. After a timeout or unclear result, look for an existing order before retrying or switching routes, and confirm success from the merchant's record with its delivery estimate.

- For a delivery question, match the tracking number to the order and read the carrier's latest scan, through the AfterShip connector under When available once `muse.connector_search` shows it for this session, labeling arrival dates as estimates. A status check does not ask you to keep watching.

## Available connectors

- [Meta Catalog](/opt/hatch/connectors/meta_catalog_search/CONNECTOR.md) for fast product search with prices, images, variants and checkout eligibility.

- [Facebook](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) for Marketplace listings and the products shown in Facebook posts and Reels.

- [Instagram](/opt/hatch/connectors/instagram/CONNECTOR.md) for products tagged or shown in Instagram posts.

- [Shopify UCP](/opt/hatch/connectors/shopify-ucp/CONNECTOR.md) for checkout of catalog products that carry a `checkout_token`.

- [Link by Stripe](/opt/hatch/connectors/stripe-link/CONNECTOR.md) for paying with a saved card through a one-time virtual card.

- [Shop Pay](/opt/hatch/connectors/shop-pay/CONNECTOR.md) for paying with a saved Shop Pay card at supported merchants.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [AfterShip](/opt/hatch/connectors/aftership/CONNECTOR.md) for carrier tracking after a purchase.

## Websites

<!-- product-search-improvements-off-only:start -->
- Search the brand's store and the chosen retailers with the browser product search brief above, giving the exact model, variant, quantity and delivery country.
<!-- product-search-improvements-off-only:end -->
<!-- product-search-improvements-on-only:start -->
- When a browser product search runs, search the brand's store and the chosen retailers with the brief above, giving the exact model, variant, quantity and delivery country.
<!-- product-search-improvements-on-only:end -->

- [Walmart](https://www.walmart.com/) and [Target](https://www.target.com/) for general goods in the US, [Best Buy](https://www.bestbuy.com/) for electronics, and [Home Depot](https://www.homedepot.com/) or [Lowe's](https://www.lowes.com/) for home improvement.

- [Walmart Canada](https://www.walmart.ca/) and [Best Buy Canada](https://www.bestbuy.ca/) in Canada, and [Walmart Mexico](https://www.walmart.com.mx/) or [Liverpool](https://www.liverpool.com.mx/) in Mexico.

- [Argos](https://www.argos.co.uk/), [John Lewis](https://www.johnlewis.com/) and [Currys](https://www.currys.co.uk/) in the UK, [MediaMarkt](https://www.mediamarkt.de/) for electronics in Germany and much of Europe, and [Yodobashi](https://www.yodobashi.com/) or [Rakuten](https://www.rakuten.co.jp/) in Japan.

- [Google Shopping](https://shopping.google.com/) to find other sellers of the same item, each verified on its own site before you quote it.

## Alternatives for better results

- Offer the previous model, a refurbished unit, a rental or a repair when the user is flexible, and explain the tradeoff. Never substitute a cheaper lookalike for an exact request.

- Check a preferred retailer's price-match policy when a rival sells the identical item for less.

- Consider resale listings through [Marketplaces](/opt/muse/skills/marketplaces/SKILL.md) when used condition suits the request, keeping condition, returns and buyer protection in the comparison.

- Offer a price watch when the user can wait for a better price.
<!-- shopping-results-response-contract:start --><!-- shopping-results-response-contract:end -->document has no file namedocument is not a regular fileinvalid document pathskill search cache lock poisoned; recovering guardskill_search index cache hitskill_search index built (cache miss).content-copy-pendingmigration input is not a regular fileinvalid migration path.content-migrations/rolloutcustom-connectorsskillsself_improvement/skill_improvementself_improvement/objectives/skill_improvementrecovered-skill-notesinvalid rollout 