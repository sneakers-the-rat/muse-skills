# Meta Catalog

- Meta Catalog searches products across many merchants and returns prices, images, variants, seller details and checkout capability. It needs no sign-in.

- For a shopping request, follow the [Shopping](/opt/muse/skills/shopping/SKILL.md) skill first. It owns the search workflow, the results widget and product citations, and this doc covers the catalog command.

- The user can allow catalog search, have it requested for each task or deny it. A denial applies only to this connector and leaves browser and Marketplace search available.

## Search the catalog

<!-- catalog-search-v1-only:start -->
- Run `/opt/hatch/bin/meta-catalog-search` with up to eight distinct `--query` values, using only as many as help. Write the results to a new file with `--out` and pass `--retries 2`. The default is 20 products per query, and `-n` changes it.

```text
catalog_results=$(mktemp "${TMPDIR:-/tmp}/meta-catalog-search.XXXXXX")
/opt/hatch/bin/meta-catalog-search \
  --query "<product query with every requirement>" \
  --retries 2 --out "$catalog_results"
```

- Query words only influence ranking, so express each firm requirement with a flag as well. `--category` requires a category, and `--gender male|female|unisex` requires the wearer category the user gave, kept on every refinement. `--prefer-gender` only ranks.

- Set price limits with `--currency` and `--min-price` or `--max-price` in cents.

- Always pass `--brand` when the user requests a specific brand and `--domain` when they name a seller, with the seller's canonical hostname without a scheme or path. Both rank their match first but can backfill with others, so check each result, and use both flags when the user names a brand and a seller.

- For used, vintage, refurbished or resale items, pass `--seller-type secondhand` and `--boost-brand-seller-website false`. Otherwise the defaults favor direct sellers and the brand's own website. `--color`, `--material`, `--style` and `--prefer-brand` only rank.

- When the current message attaches an image with a clear target, search first with `--image-path` and the uploaded file's path. Use text or `--visual-query` to complement it, never to replace an available uploaded image.

- Keep required attributes and price limits on every refinement. Relax only preferences that do not express a user requirement, and keep those results separate.
<!-- catalog-search-v1-only:end -->
<!-- catalog-search-v2-only:start -->
- Run `/opt/hatch/bin/shopping catalog-search` with up to eight semantic `--query` values, using only as many as help. Write the results to a new file with `--out` and pass `--retries 2`. The default is 20 products per query, and `--num-results` or `-n` changes it.

- Pass every user requirement as a flag on every search, the first one included. A requirement without its own flag, such as a size, model, variant or compatibility, goes in `--require`, which the CLI adds to every query. A search with `--require` therefore needs at least one `--query`, an image search included, and items with different requirements, such as different sizes, need separate searches.

Example usage:
- Base search showing the shared flags. `--intent` is optional:
```text
catalog_results=$(mktemp "${TMPDIR:-/tmp}/shopping-catalog-search.XXXXXX")
/opt/hatch/bin/shopping catalog-search \
  --query "Nike men's cushioned daily training shoes from Nordstrom" \
  --category footwear --gender male --restrict-brand Nike \
  --require "US men's size 10" \
  --domain nordstrom.com --currency USD --max-price 12000 \
  --retries 2 --out "$catalog_results"
```

- User demonstrated targeted shopping intent for a particular product:
```text
catalog_results=$(mktemp "${TMPDIR:-/tmp}/shopping-catalog-search.XXXXXX")
/opt/hatch/bin/shopping catalog-search \
  --query "Alo yoga women white hoodie" \
  --category clothing --gender female --restrict-brand Alo \
  --intent targeted --currency USD \
  --retries 2 --out "$catalog_results"
```

- User wants a brand's or store's range ("what does Arc'teryx have for hiking"); still targeted when split by product type:
```text
catalog_results=$(mktemp "${TMPDIR:-/tmp}/shopping-catalog-search.XXXXXX")
/opt/hatch/bin/shopping catalog-search \
  --query "Arc'teryx hiking jacket" --query "Arc'teryx hiking pants" \
  --restrict-brand "Arc'teryx" --intent targeted --currency USD \
  --retries 2 --out "$catalog_results"
```

- User asks where to buy one particular product, its price or the best deal:
```text
catalog_results=$(mktemp "${TMPDIR:-/tmp}/shopping-catalog-search.XXXXXX")
/opt/hatch/bin/shopping catalog-search \
  --query "Alo yoga women bae hoodie beige" \
  --category clothing --gender female --restrict-brand Alo \
  --intent targeted --compare-sellers --currency USD \
  --retries 2 --out "$catalog_results"
```

- User demonstrated exploratory shopping intent based on a need or use case:
```text
catalog_results=$(mktemp "${TMPDIR:-/tmp}/shopping-catalog-search.XXXXXX")
/opt/hatch/bin/shopping catalog-search \
  --query "lightweight packable rain jacket women for travel" \
  --category clothing --gender female \
  --intent explore --currency USD \
  --retries 2 --out "$catalog_results"
```

- User wants something like a named product but cheaper or different ("like Levi's trucker jacket but cheaper"):
```text
catalog_results=$(mktemp "${TMPDIR:-/tmp}/shopping-catalog-search.XXXXXX")
/opt/hatch/bin/shopping catalog-search \
  --query "classic denim trucker jacket women" \
  --category clothing --gender female \
  --intent explore --currency USD \
  --retries 2 --out "$catalog_results"
```

- `--category` requires a category, and `--gender male|female|unisex` requires the wearer category the user gave. Keep it on refinements and never infer it from styling.

- `--restrict-brand` takes one brand the user limits acceptable results to. Repeat it for multiple brands.

- `--prefer-brand` takes one brand the user favors but does not require. Repeat it for multiple brands. Also include each preferred brand in a `--query` with the product requirements.

- Always pass `--domain` when the user names a retailer, giving its hostname without a scheme, path or port. Repeat it for multiple retailers.

- `--currency` takes a three-letter code, which also selects the market, and defaults to the shopper's currency. `--min-price` and `--max-price` are inclusive bounds in hundredths of that currency, so `2500` means 25.00.

- `--seller-type secondhand` suits used, pre-owned, thrifted, vintage or refurbished inventory, and `direct` favors direct sellers.

- `--intent` says what the user is shopping for. It changes how results are ordered, not which products are retrieved:
  - `targeted`: the user named what they want, e.g., one specific product (model, SKU, product line or variant), an item with binding requirements that any matching item satisfies (size, fit, compatibility, exact dimensions, capacity or color), or a brand's or store's range ("Polar H10 chest strap", "women's white leather sneakers size 7", "Lululemon leggings", "what's new at Uniqlo"). Pass the brand with `--restrict-brand` when one is named. Several phrasings of that one item as multiple `--query` are fine, and a brand's or store's range stays `targeted` when you split it into product types. A product type with required specs is `targeted` even when no brand is named; a budget, recipient or occasion alone is not a requirement. Add `--compare-sellers` only when the user's words ask where to buy one targeted product, what it costs or where the best deal is ("where can I get", "cheapest", "best price"). Naming an exact model, size or color is not enough, and it never applies to a comparison of different products. Results then contain that product from several good stores. When the user names retailers, pass `--domain` for each and leave out `--compare-sellers`; otherwise do not pass `--domain`.
  - `explore`: the user wants help choosing a need or use case, "best X", a comparison of two or more named products (even though each one is named), similar product but cheaper or different, or several different items in one request. Give each option or item its own `--query` when they share the same requirement flags, and a separate search otherwise, and do not add paraphrases; results interleave the queries so each one appears near the top. A gift or occasion request that names only a product type and a budget is `explore`. For queries that look for similar products to a named one, do not name that product in a query. Leave its brand out of `--restrict-brand` and the queries unless the user requires that brand.

- When the current message attaches an image with a clear target, start with `--image-path` and the uploaded file's path, adding `--query` only to clarify or to carry `--require`. Never replace an available image with a text description.

### Refine a search

- The summary's `requirements` lists the hard-constraint flags the search applied. Pass the same flags with the same values on every refinement and retry for that item, plus `--domain` when the user named the retailer. Change only the queries, `--intent` and flags that express no user requirement, such as `--prefer-brand`, `--seller-type` or a `--domain` you chose yourself.

- Never drop a flag that expresses a user requirement to find more results, even when the exact product seems missing. Rephrase the queries instead, and if that still fails, follow the Shopping skill's fallback.

- Put several phrasings of one item in one search, up to eight `--query` values, rather than in successive searches.
<!-- catalog-search-v2-only:end -->

- If the CLI rejects an argument, correct it and retry once with the same constraints. Any other failure or an unreadable results file ends the catalog attempt, so continue with the other sources instead of running diagnostic calls or dropping requirements.

## Read the results

- Preview products while keeping their IDs and leaving out image URLs:

```text
jq -r '.products[0:20][] | [.product_id, .brand, .name, (.sale_price // .price), .seller_type, .seller_quality, .rating, .size] | @tsv' "$catalog_results"
```

- Check every result against each firm requirement before selecting it, because `--prefer-brand` and `--domain` can backfill with others. For example, keep only one seller's products at or under 100.00:

```text
jq -r '
  .products[]
  | select(.url // "" | test("^https?://([^/]+\\.)?nordstrom\\.com(/|$)"))
  | select(((.sale_price // .price // "") | gsub("[^0-9.]"; "")) as $p | $p != "" and ($p | tonumber) <= 100)
  | [.product_id, .brand, .name, (.sale_price // .price), .seller_type, .seller_quality] | @tsv
' "$catalog_results"
```

- Keep `product_id` in every projection you print, because `shopping.resolve_results` selects by it. Pass the original results file to the resolver so the signed image URLs reach the cards without entering your reply.

- Select only products that have a `url`, `name` and `image_url`, because `shopping.resolve_results` rejects the whole call when a selected catalog product lacks one.

- Each product has `product_id`, `url`, `name`, `brand`, `price`, `currency`, `description` and `image_url`, plus `sale_price` only when the source shows a real sale. When known, it adds `color`, `material`, `size`, `gender`, `category` and `rating`.

- Some results also carry `seller_type` (`brand_direct`, `authorized_retailer`, `new_item_marketplace`, `secondhand_marketplace` or `gray_market`), `seller_quality` (`elite`, `good`, `acceptable`, `poor`, `not_a_seller` or `unrated`) and `shopify_product_id`. Products carry the checkout flags `is_agentic_checkout_creation_enabled` and `is_agentic_checkout_completion_enabled` when the catalog knows them.

- Compare prices and budgets with `sale_price` when present, otherwise `price`, keeping the currency and exact variant together. Missing fields stay unknown, and a result is one snapshot, so check the variant, stock, delivery and total before purchase.

## Confirm a variant

- Run `/opt/hatch/bin/shopping product-details --product-id ID` for a returned product, adding `--currency` when the result has one, to read its variants.

- For a requested size, find it in the size variant group and fetch its candidate `product_ids` while holding color and the other chosen attributes constant. Choose only a response whose `product.selected_variant_info` confirms the whole combination and whose availability allows purchase, and treat `is_available: false` as unavailable.

- Use the confirmed response's `product.id` for checkout, not an ID read from `variant_groups`, and confirm its checkout eligibility in that same response before routing it to direct checkout. Never pick an arbitrary candidate when the attributes cannot be confirmed, and keep the IDs and this lookup out of your reply.

## Check the purchase route

- Route on the checkout flags the search already returned, without fetching product details just to decide. Direct Shopify UCP checkout needs `is_agentic_checkout_creation_enabled` to be exactly `true` on every selected product, and missing or null counts as false.

- Read the [Shopify UCP](/opt/hatch/connectors/shopify-ucp/CONNECTOR.md) docs before using that route. Other products use the Shopping skill's browser checkout.

## Related skills

- [Shopping](/opt/muse/skills/shopping/SKILL.md)

- Use `muse.skill_search` to find other skills and `muse.connector_search` to find other connectors.

### When available

- These skills depend on the user's channel or devices. `muse.skill_search` shows which ones this session has.

- [Deal Monitoring](/opt/muse/skills/price-tracker/SKILL.md)
