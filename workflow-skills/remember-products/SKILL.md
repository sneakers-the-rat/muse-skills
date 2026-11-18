# Remember Products

- Save the products a user chooses to named lists, and show them again as product cards without a new search. Each command below runs `/opt/hatch/bin/product-lists`, which indexes the lists in `~/memory/products/INDEX.md`.

- After you save, remove or move products, finish by showing each list that changed and still exists as product cards, following "Show lists". A move changes two lists: the one the products left and the one they went to.

- `product-lists` deletes a list when its last product is removed or moved. After that, or after you delete a list, tell the user the list is gone.

## Save products

- Save only the products the user chose, to a matching list in `INDEX.md`, a new list named in their words, or "wishlist". Save each product as listed even if they want another size or color, because they pick that when buying.

- Run `product-lists save --list "<list>" --results <file> <ID>...` with a results file you passed to `shopping.resolve_results` in `result_paths`, plus the IDs you picked from it. Run one `save` per results file.

- `save` rejects the cards file that `shopping.resolve_results` wrote, so pass the results file.

- When `save` fails, tell the user why in plain words and whether a new search can help.

- Remove any `MEMORY.md` line about a product you save.

## Change a list

- Run `product-lists` with no arguments to see its `remove`, `move` and `delete` commands. `remove` and `move` take the IDs that `show` prints, and `delete` takes a list name.

## Show lists

- Run `product-lists show --list "<list>"` for each list. Use its output rather than the list files or memory search results, because it refreshes catalog products and writes the results files `shopping.resolve_results` reads.

- Load the `shopping` namespace with `tool_search.load_tool_namespace` if it isn't loaded.

- Before you name any saved product, resolve each list's `selected_ids`, in order, from its `result_paths` with `shopping.resolve_results`. Make one call per list even when you show several, and one per batch when `show` splits a list, because each call takes at most 50 IDs.

- Present the products with `shopping.create_shopping_results_widget`. Show one list as product cards, with a widget per batch if `show` split it. Show two to ten lists as one collection with a section per list, named after the list, when the tool offers collections and no list was split. Otherwise give each list its own widget.

## Reply

- Build the reply from the markers `shopping.resolve_results` returned. Each marker renders as a chip that shows the product's name and opens its page in Muse, so write the marker wherever you would write the name. A plain name or a pointer to the cards above can't be tapped.

- When you saved or moved products, confirm it in the first sentence with each of those products' markers and the name of the list they went to.

- Keep the reply short: any confirmation, then every product on each list as its marker, in the order `show` printed them.

- Use plain text only for a product with no marker: one you removed, or one the resolver returned no marker for.

- Mention each list's `notes`, with the product's marker in place of its name. Notes say when a price changed, a product is out of stock, or a price is still the saved one because it wasn't refreshed. Browser and Walmart prices aren't refreshed, and a catalog refresh can fail.

## Available connectors

- [Meta Catalog](/opt/hatch/connectors/meta_catalog_search/CONNECTOR.md) for catalog products.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.
