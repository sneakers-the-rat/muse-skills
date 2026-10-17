# Shop a Facebook Reel

- Read the Reel with `post read --url '<link>'`, decoding a share link first as [Posts](posts.md) describes. Use this connector for the Reel's context instead of opening it in the browser.

- Before the read, collect only the requirements already known to apply. Resolve category-specific requirements from the returned context afterward. Apply relevant saved hard requirements even when the user did not repeat them, and let explicit current instructions override conflicting ones. A soft preference alone never starts a fresh search or changes the default recommendations or their order.

- Keep detected `shoppable_products` separate from recommended `featured_products`. Neither establishes an exact item, current price or availability without supporting data.

## Choose the discovery path

- If the user asks to choose only from products already shown, filter those results by verified attributes. A missing or unclear attribute is not a match, and if none fit, say so without starting another search.

- For a named product, a category or an applicable hard requirement, read the Reel without `--out`. Then run fresh searches through [Shopping](/opt/muse/skills/shopping/SKILL.md) with every requirement, searching for the named target or otherwise the detected `shoppable_products`.

- Ask which product the user means when neither a named target nor a detected product identifies one. Filtering the similar-product recommendations never replaces those searches.

- For general Reel shopping, add `--out '<new file>'`. If the read then reveals an applicable hard requirement, reuse its context for fresh searches without reading the Reel again or filtering the recommendations. Search for the detected products, or ask which product when none were detected.

## Use the general recommendations

- If no hard requirement applies and `featured_products_status` is `available`, pass the `--out` file and every ID from `ordered_featured_product_ids`, unchanged and in the same order, to `shopping.resolve_results`. Do not drop, rerank or add searches, and do not read the file, because the command's summary is enough.

- If the status is `unavailable`, the ordered IDs are empty and no catalog was written, so ignore the output path. Use Shopping to find the detected products, or ask what the user wants when there is no target.

## Compare and present

- Fresh searches follow Shopping's normal choice of sources. Honor a request for catalog-only results, and otherwise use suitable catalog and browser sources.

- Finish the required searches before one presentation, combining every usable file and selected ID in a single `shopping.resolve_results` call.

- Present the resolved products as shopping cards with their returned citation markers, keeping the file and status details out of the reply. Before a purchase, verify the offer and follow Shopping's price, delivery and checkout checks.
