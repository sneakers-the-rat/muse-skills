# Remember Products

- Save products the user asks you to remember in named lists, and show them again as product cards without a new search. Each command below runs `/opt/hatch/bin/product-lists`, which indexes the lists in `~/memory/products/INDEX.md`.

## Save products

- Save only the products the user chose, to a matching list from `INDEX.md` or a new one named in their words, or "wishlist". Save each as listed, even when they want another size or color; they choose that when buying.

- Run `product-lists save --list "<list>" --results <file> <ID>...` with the results file and IDs you gave `shopping.resolve_results`. When it prints `not saved`, explain why in plain words and whether a new search can help.

- Remove any `MEMORY.md` line about a product you save. Confirm what you saved and where.

## Show saved products

- When the user asks what you remembered, run `product-lists show --list "<list>"` for each matching list. Resolve its `selected_ids`, in order, from its `result_paths` with `shopping.resolve_results`, present them with `shopping.create_shopping_results_widget`, and mention its `notes`.

## Change a list

- Run `product-lists` alone for its `remove`, `move` and `delete` commands.

## Available connectors

- [Meta Catalog](/opt/hatch/connectors/meta_catalog_search/CONNECTOR.md) for catalog products.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.
