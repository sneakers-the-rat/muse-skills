# Shopping from Facebook Reels

- `post read` is useful for shopping for products found in a Facebook Reel. [Posts](/opt/hatch/connectors/facebook_cli/references/reading-posts.md) explains how to decode share links.

```sh
/opt/hatch/bin/facebook-cli post read --url '<Reel URL>'
```

- to save recommendations as a local shopping catalog file, use `--out '<file>'`

- If the user asks to choose only from products previously returned to the user, filter just those by verified attributes. A missing or unclear attribute isn't a match, and if none fit, say so without starting another search. This comes before the fresh-search paths below.

- If the response reveals a hard requirement, reuse its context for fresh searches rather than filtering recommendations or reading the Reel again.

- For a named product, a product type, or a hard requirement, leave out `--out` and use [Shopping](/opt/muse/skills/shopping/SKILL.md) for fresh searches with every requirement.

```sh
/opt/hatch/bin/facebook-cli post read --url '<Reel URL>'
```

- `shoppable_products` contains detected products. `featured_products` contains system-generated similar-product candidates; this does not mean the creator tagged or recommended those products. Exact matches, current prices and availability need supporting product data.

## Products from the Reel's shopping sheet

- Check the current request's `product_context` attachment. For `data.entrypoint` = `FB__REELS__SHOP_WITH_MUSE_PILL`, `data.params.tagged_product_ids` contains the IDs of the products Facebook recommended in the Reel's shopping sheet. Use this list if it is not empty.

- If the list is empty or missing, follow the Reel workflow above.

- If the list contains IDs, use those products as the starting recommendations instead of fetching another list with `post read --out`. Use the command below to look up each ID. Use the returned details when describing these products.

```sh
/opt/hatch/bin/shopping product-details --product-id '<id>' --out '<new file>'
```

- Skip products if fetching their details fails. For each successful lookup, keep the output file path and the returned `product.id`. When calling `shopping.resolve_results`, put the file paths in `result_paths` and the IDs in `selected_ids`. Keep IDs and lookup errors out of replies.

- If every lookup fails:

  - If the user asked to use only products from the shopping sheet, say you couldn't verify those products and stop.

  - Otherwise, follow the Reel workflow above.

- When calling `shopping.resolve_results`, put those products' IDs first in `selected_ids`, keeping their order from `tagged_product_ids`. If you also found other matching products through additional searches, add their IDs at the end of `selected_ids`. If the user asks to choose only from the products Facebook recommended, do not search for other products. Otherwise, use [Shopping](/opt/muse/skills/shopping/SKILL.md) to find more options if needed.

## Find products

- When shopping from Reels, prioritize the stated requirements and instructions. Apply relevant saved hard requirements even when the user did not repeat them, and let explicit current instructions override conflicting ones.

- If a required detail is missing, explain what you couldn't verify.

## Use recommendations

- If the user hasn't specified a product, product type, or hard requirement, use the products from `tagged_product_ids` when the list is not empty. If the list is empty or missing, use the recommendations returned by `post read --out`. Do not filter or reorder these recommendations just to match a soft preference.

- For `post read --out` without a hard requirement, `featured_products_status` describes the next step:

  - `available`: pass the file and all `ordered_featured_product_ids`, unchanged and in order, to `shopping.resolve_results`. These recommendations are ready to use without extra searches. The summary provides the context; the file goes directly to the resolver.

  - `unavailable`: the IDs are empty and no catalog was written. Search for detected products through Shopping, or ask what the user wants if there is no target. This status does not mean the Reel could not be read or that creator tags are missing.

## Present products

- Fresh searches use Shopping's catalog and browser sources, or catalog sources only when requested.

- After the searches are complete, combine all usable files and selected IDs in one `shopping.resolve_results` call. Present the results together as shopping cards with corresponding citation markers. File paths and the availability of the optional recommendation list are internal search details; omit them from progress updates and final replies.

- Before a purchase, verify the offer and use Shopping's price, delivery and checkout checks.
