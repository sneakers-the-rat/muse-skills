# Shopping

- Find high-quality, low-priced products that match every constraint, and aim to save the user money.

## Understand what the user needs

- Establish whether the user wants a specific product or a recommendation, who it is for and whether used or refurbished is acceptable. Apply this conversation first, then relevant preferences in `~/memory/shopping/PROFILE.md` and `~/USER.md`, or the person's `~/memory/people/` page when buying for someone else.

- Resolve the attributes that decide whether a product is correct before searching, such as the wearer's gender and size, the device a part must fit or the software platform. Use a stored size only when its category, sizing system, brand and wearer match. Never infer gender from a name or styling, and never fall back to a default.

- Ask for one missing attribute per message before searching, starting with the one that most changes the results, such as the wearer's gender before their size. Wait for the answer before asking the next one.

- Use `muse.create_options` for a bounded choice and plain text for an open question. Never put two questions or two option widgets in one message, because a second widget appears as a stray list beside the one the user is answering.

- Resolve required attributes before the first search rather than narrowing the results afterwards, because an unresolved attribute returns wrong products.

- During a browser checkout, ask for every missing choice together, as `~/docs/chat/payments-and-purchases.md` describes.

- If the user cannot say or declines, search each plausible value separately and label the results by value, rather than guessing or using the user's own value.

- Apply every resolved attribute to every search for the request, refinements included.

## Search every source in parallel

- Use `browser.search` first when it helps write better queries, to learn trends, well-known sellers for the category, reviews or typical prices.

- Run the request's product searches in parallel, with every requirement in each one:
  - Meta Catalog, starting from this command and adding the flags the [Meta Catalog](/opt/hatch/connectors/meta_catalog_search/CONNECTOR.md) docs give for categories, gender, brands, sellers, prices and images:
<!-- catalog-search-v1-only:start -->
    ```text
    catalog_results=$(mktemp "${TMPDIR:-/tmp}/meta-catalog-search.XXXXXX")
    /opt/hatch/bin/meta-catalog-search --query "<product with every requirement>" --retries 2 --out "$catalog_results"
    ```
<!-- catalog-search-v1-only:end -->
<!-- catalog-search-v2-only:start -->
    ```text
    catalog_results=$(mktemp "${TMPDIR:-/tmp}/shopping-catalog-search.XXXXXX")
    /opt/hatch/bin/shopping catalog-search --query "<product with every requirement>" --retries 2 --out "$catalog_results"
    ```
<!-- catalog-search-v2-only:end -->
  - A browser product search with `browser.spawn_task`, briefed as below. Always run it, especially for home goods, unless the user asked only for Facebook Marketplace.
  - Facebook Marketplace with `/opt/hatch/bin/facebook-cli marketplace search` for used, local, pickup or tight-budget requests, following the Facebook connector's [Marketplace guide](/opt/hatch/connectors/facebook_cli/references/marketplace.md).

- Cover the brand's official store and a few established retailers, such as Walmart, Target or Best Buy in the US, plus a specialist or local shop when the item calls for one.

- For an exact request, match the model, variant, size, pack and condition rather than a similar title or photo.

- Never relax a required attribute or a stated price limit. A retry may relax only preferences the user did not require, and those results stay separate and are never presented as exact matches.

- Start fresh searches for each request rather than reusing earlier results, unless they clearly still fit.

- When too few results fit, adjust the queries or add a source and search again. Stop when more searching is unlikely to change the recommendation.

### Brief the browser search

- The browser task cannot see this conversation, so give it a complete, self-contained brief.

```json
{
  "task": "<what the user asked to find, in their words>. Find real purchasable products online for: <user request>. Preserve these requirements: <constraints>. Unless instructed otherwise, default to searching a maximum of 3 merchant sites and a maximum of 10 products in total - prefer to limit searching to the minimum amount necessary to provide a high-quality and seller-diverse response (e.g. if searching 2 merchant sites gives you enough high quality products, stop there). Return a concise shortlist with product name, merchant, price, availability, product URL, and why each product matches. Also populate browser_hand_off.product_results with every shortlisted product. Ensure that each URL is a dedicated product page, not a search page. For image_url, identify the primary rendered product image; inspect its src, srcset, lazy-load attributes, or element HTML, resolve relative URLs against the product-page URL, and include only a direct absolute HTTPS image URL. Omit products whose primary image cannot be verified or resolves to a blob/data URL, placeholder, logo, or tracking pixel. Use price for the regular/list price, or the current price when there is no sale. Include sale_price only when the page explicitly shows an actual sale with a distinct discounted price. Set availability to in_stock only when the product page indicates it can be added to cart or purchased. This is product discovery only: do not purchase, enter checkout, add items to cart, or request payment/shipping details. If the user asked to buy, order, purchase, or check out, ask them to choose or confirm one product before any separate checkout handoff."
}
```

- Run parallel browser tasks only for distinct discovery angles, such as different retailers or product types. Refine an angle inside the task already pursuing it, and let one task cover several retailers when separate tasks would add nothing.

- When a task completes, write its `completion_result.product_results` object verbatim to a JSON file and select products by `result_id`. Never rebuild products from the prose report or supply a missing image URL.

```json
{
  "version": 1,
  "kind": "browser_product_search_results",
  "count": 1,
  "products": [
    {
      "result_id": "browser:<stable URL hash>",
      "name": "Product name",
      "url": "https://merchant.example/product",
      "image_url": "https://merchant.example/product.jpg",
      "availability": "in_stock",
      "brand": "Merchant or brand",
      "price": "$49.00"
    }
  ]
}
```

- Wait for every browser task in the request to finish. Completions arrive automatically, so never poll.

- Browser products appear as cards with `type: "browser"`, without a `product_id` or direct checkout.

## Verify before showing products

- Filter out results that miss a constraint, look low quality or sit outside the normal price range for the product.

- Open every non-Marketplace product URL with `browser.open` and drop any that is not a dedicated product page showing in-stock availability. `browser.open` cannot fetch Meta-owned hosts such as instagram.com, facebook.com and threads.com, so read those through the [Facebook](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) or [Instagram](/opt/hatch/connectors/instagram/CONNECTOR.md) connector.

- Never show a price, availability or product URL from `browser.search` results, because they are unreliable. Get product details from a browser product search instead.

- Prefer the country-specific site for the user's home location, such as Walmart US rather than Walmart Canada for a US user.

- Rank the rest by fit, with full matches from well-known sellers first. A sponsored placement or a crossed-out "original" price does not prove value.

- When the user is choosing between offers for the same item, compare the delivered total with shipping, tax and fees, the arrival date, the return terms and the seller.

- When one seller cannot be verified, check another seller of the same item before recommending a substitute.

- Before showing any product in a widget or text, check it again against every constraint and general preference, such as the wearer's gender and size for clothing.

## Resolve and cite products

- Call `shopping.resolve_results` before naming any product, whether or not a widget follows. Pass every result file and the selected IDs in ranking order.

```json
{
  "result_paths": ["<catalog, Marketplace or browser results file>"],
  "selected_ids": ["<catalog product_id, Marketplace listing_id or browser result_id>"]
}
```

- The resolver returns a `path` for `shopping.create_shopping_results_widget` and a `marker` for each product in `product_citations`. It is the only way to resolve and cite products, and it creates no UI itself.

- Select catalog products and Marketplace listings only when the [Meta Catalog](/opt/hatch/connectors/meta_catalog_search/CONNECTOR.md) docs or the Facebook [Marketplace guide](/opt/hatch/connectors/facebook_cli/references/marketplace.md) say the resolver accepts them, such as listings that show an `image_url`, because one rejected selection fails the whole call.

- A subagent does not call the resolver. It reports `product_search_handoff: <JSON payload>` with the payload it would have passed, the main agent resolves it, and the handoff stays out of the user's reply.

- Write each product's name as its marker everywhere, in every message, for the whole conversation. That includes early updates, answers about a product on screen, comparisons, status notes and turns that come back to a product much later.

- Reuse the same marker each time a product comes up, even when the widget above already shows it.

- Put the marker where the name would go. Answering a question about one product still names it, so write "yes, <marker> fits three lenses", not "yes, the Lowepro fits three lenses".

- Never refer to a resolved product by a description, such as "the merino one" or "the $199 one", because that drops its verified name and link.

- Name a product without a marker only when no successful resolve returned one. Resolve a product from a result file before naming it, and if it cannot be resolved, name it plainly without inventing a marker, URL or link.

- Write each marker exactly as returned. Never build one from `citation_id`, repeat the product name beside it or add a link.

## Present the results

- Present products in a shopping-results widget when their source supports one, in a single presentation per request after every product search for it has finished. Create no widget before then. A search that failed or returned nothing usable has finished.

- In the turn interim results arrive, resolve and name one or two strong products, such as catalog results from a well-known retailer. Say the update is early and what is still running, and keep it free of superlatives, rankings and verdicts.

- Once the last search finishes, pass every result file for the request in one `result_paths` list, rank the best products across the whole pool and call `shopping.create_shopping_results_widget` with the returned `path`. A later search adds candidates and never replaces earlier ones.

- Give distinct product groups, such as shoes and pants, one widget each in the same presentation, each resolving its own selection from the pool.

- Order widget products from most to least relevant, so the top five are full matches from well-known sellers.

- Before the presentation, or when no source supports a widget, keep to the takeaway and at most one or two recommendations.

- Lead with the recommendation or takeaway, keep the reply short and compare the decisive tradeoff between the top choices when useful.

- When variants such as sizes or colors exist for a named product, offer to show them without naming more products.

- Never put results in a Markdown file, link or attachment unless the user asks.

<!-- shopping-results-response-contract:start -->
### Write the reply that accompanies the results

- Open with one short takeaway drawn from all the results, not only the search that finished last. Do not list, recap or describe the products the widget shows, and do not mention the skill, instructions, widget, tools or formatting.

- Name at most two products, only for the decisive recommendation or tradeoff, and keep the widget's order. Refer to the others collectively.

- Write each named product as the complete `marker` returned in `product_citations`, without rebuilding it, repeating the name beside it or adding a link. Use the plain name only when no marker was returned.

- Keep the results out of a Markdown file unless the user asks for one.
<!-- shopping-results-response-contract:end -->

## Follow-up turns

- Keep the original request's constraints in follow-up turns. Drop them only when the user says so or starts a new search, and then keep only general preferences.

- On a new search, close the old request's browser tasks with `browser.close_task`, finding them with `browser.list_tasks`, and ignore their late results.

## Find a deal

- Establish the product's usual price, then research where deals for it or its category appear, such as Newegg for electronics.

- Search thoroughly with `browser.spawn_task` for listings below the usual price, and separately for current sales and coupon or promo codes at the sellers themselves.

- Test a code in the basket when the user allows it.

- Lead with a recommendation. When there is no current deal, say so and share what you learned about past or upcoming sales.

## Search by photo

- When a photo shows several plausible products and the user has not said which one, ask which item to shop before searching.

- When the current message attaches a photo with a clear target and every required attribute is resolved, run the catalog image search before any other step, as the [Meta Catalog](/opt/hatch/connectors/meta_catalog_search/CONNECTOR.md) docs describe.

- Without catalog image search or an uploaded image path, write a detailed visual description of the product and search with it.

- Search the other sources with image inputs where they accept them, and with descriptive queries otherwise.

- Check product pages and images against the photo, and rank exact matches ahead of visually similar results.

- Keep refining the queries until the product is identified or further refinement stops helping, then offer the closest matches. Say plainly when there is no exact match.

## Shop from a link

- Read an Instagram or Facebook link through the [Instagram](/opt/hatch/connectors/instagram/CONNECTOR.md) or [Facebook](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) connector first and follow the matching workflow in [social links](references/social-shopping-links.md). A detected or similar product does not prove an exact match or the best price.

- Read a pasted Marketplace item or share link through the Facebook connector as its [docs](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) describe, never in the browser, then search for similar items from its title and description.

- Compare a used item with a new one on transport, inspection, seller reliability and the missing warranty, and keep new, used and refurbished offers distinct.

## Complete the purchase

- Run the purchase yourself in the main conversation. A subagent has neither wallet nor browser access, so it cannot complete one.

- Before checkout, close product-search browser tasks that no longer matter with `browser.close_task`, finding them with `browser.list_tasks`, and ignore their late results.

- Choosing items or building a cart moves no money. When a connector provides checkout instructions, follow those instead of the routing below.

- Choose the route from the checkout flags the catalog search already returned, without a separate product lookup just to decide it.

- For catalog products with `is_agentic_checkout_creation_enabled: true`, confirm each selected product's exact variant as the [Meta Catalog](/opt/hatch/connectors/meta_catalog_search/CONNECTOR.md) docs describe, then check out directly as the [Shopify UCP](/opt/hatch/connectors/shopify-ucp/CONNECTOR.md) docs describe.

- Otherwise follow [browser checkout](references/browser-checkout.md) in one browser task through confirmation.

- Only products eligible for direct checkout have a merchant cart, unless a connector supports one. The store holds, prices and discounts that basket, so never keep a list of your own as a cart, and say so when the route has none.

- Keep the `cart_id` as internal state for the rest of the conversation, never show it to the user, and follow the connector's instructions for cart reads, changes and widgets.

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

- [Shopify UCP](/opt/hatch/connectors/shopify-ucp/CONNECTOR.md) for direct checkout of eligible catalog products.

- [Link by Stripe](/opt/hatch/connectors/stripe-link/CONNECTOR.md) for paying with a saved card through a one-time virtual card.

- [Shop Pay](/opt/hatch/connectors/shop-pay/CONNECTOR.md) for paying with a saved Shop Pay card at supported merchants.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [AfterShip](/opt/hatch/connectors/aftership/CONNECTOR.md) for carrier tracking after a purchase.

## Websites

- Search the brand's store and the chosen retailers with the browser product search brief above, giving the exact model, variant, quantity and delivery country.

- [Walmart](https://www.walmart.com/) and [Target](https://www.target.com/) for general goods in the US, [Best Buy](https://www.bestbuy.com/) for electronics, and [Home Depot](https://www.homedepot.com/) or [Lowe's](https://www.lowes.com/) for home improvement.

- [Walmart Canada](https://www.walmart.ca/) and [Best Buy Canada](https://www.bestbuy.ca/) in Canada, and [Walmart Mexico](https://www.walmart.com.mx/) or [Liverpool](https://www.liverpool.com.mx/) in Mexico.

- [Argos](https://www.argos.co.uk/), [John Lewis](https://www.johnlewis.com/) and [Currys](https://www.currys.co.uk/) in the UK, [MediaMarkt](https://www.mediamarkt.de/) for electronics in Germany and much of Europe, and [Yodobashi](https://www.yodobashi.com/) or [Rakuten](https://www.rakuten.co.jp/) in Japan.

- [Google Shopping](https://shopping.google.com/) to find other sellers of the same item, each verified on its own site before you quote it.

## Alternatives for better results

- Offer the previous model, a refurbished unit, a rental or a repair when the user is flexible, and explain the tradeoff. Never substitute a cheaper lookalike for an exact request.

- Check a preferred retailer's price-match policy when a rival sells the identical item for less.

- Consider resale listings through [Marketplaces](/opt/muse/skills/marketplaces/SKILL.md) when used condition suits the request, keeping condition, returns and buyer protection in the comparison.

- Offer a price watch when the user can wait for a better price.
