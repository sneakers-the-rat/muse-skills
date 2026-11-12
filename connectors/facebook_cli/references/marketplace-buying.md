# Facebook Marketplace Buying

- These commands search Marketplace listings near a place and read item details, seller ratings, and the user's saved listings.

## Search listings

```sh
/opt/hatch/bin/facebook-cli marketplace search --query '<search terms>' [--query '<alternate terms>' ...] [--min-price <dollars>] [--max-price <dollars>] [--latitude <latitude> --longitude <longitude>] [--radius-in-miles <miles> | --radius-in-km <kilometers>] [--max-listing-age-in-days <days>] [--sort-by <best_match, creation_time_descend, price_ascend, price_descend or distance_ascend>] [--allowed-item-conditions '<comma-separated, such as new,used>'] [--delivery-method <local_pickup_only, shipping_only or pickup_and_shipping>] [--category-id '<category ID>' ...] [--limit <up to 20, default 20>] [--next-page] --out '<new file>'
```

- `marketplace search` finds listings near a place. Turn the request into one or more search terms plus any stated budget, condition, delivery preference, category or listing age, such as 7 days for "listed this week." If the request is too vague to search, such as "something nice," ask for a product type first. A category alone, such as "a used road bike," is enough to search.

- Location comes from coordinates. `marketplace search` takes no place name. Geocode a named place with `map.geocode` and pass `--latitude` and `--longitude`. Without a named place, use a default location and radius saved in memory and tell the user which you applied, such as 'San Jose within 30 miles'. With neither, search without location flags instead of asking. Facebook then searches the user's country, so say so and offer to narrow it to a place.

- Pass a radius as `--radius-in-miles` or `--radius-in-km` when the user gives a distance or you applied a saved default. Use the unit the user gave, without converting between them. Without either, leave the radius flags out so the search isn't narrowed to a distance the user didn't ask for. Tell the user the area you searched, such as 'within 10 miles of Oakland' or 'near San Francisco', and any alternate terms you added, so they can widen or narrow the search.

```sh
/opt/hatch/bin/facebook-cli marketplace search --query '<vehicle>' [--min-year <1900 to next year>] [--max-year <1900 to next year>] [--min-mileage-in-miles <1 to 1,000,000>] [--max-mileage-in-miles <1 to 1,000,000>] [--transmission <automatic or manual>] [other search flags] --out '<new file>'
```

- Vehicle filters narrow results to whole vehicles, so a search for parts or accessories puts the vehicle in `--query` instead. Convert kilometers to miles for mileage.

## Read items, sellers and saved listings

```sh
/opt/hatch/bin/facebook-cli marketplace listing details (--listing-id '<listing_id>' ... | --url '<Marketplace item link>') --out '<new file>'
```

- `listing details` reads full listings by `--listing-id`, or one item link with `--url`, and needs no linked account. It adds `currency`, `seller_name`, `created_at` and the primary photo, and uses `url` for the link. Show the full description, price, condition, seller name and creation date.

```sh
/opt/hatch/bin/facebook-cli marketplace seller-info (--listing-id '<listing_id>' ... | --url '<Marketplace item link>')
```

- `seller-info` looks a seller up by the `listing_id` of any of their listings, or by one item link with `--url`. It doesn't take a `seller_id`. It returns each seller's `name`, `followers`, `avg_rating`, `total_ratings`, and `good_attributes` and `bad_attributes` such as "Item as described (12)". Show the rating with its count and the feedback breakdown, because a name or a large following alone doesn't show a seller is trustworthy. When the user asks a follow-up about the same seller, reuse that result.

```sh
/opt/hatch/bin/facebook-cli marketplace saved [--keywords '<text>'] [--limit <up to 20>] [--next-page] --out '<new file>'
```

- `saved` lists the user's saved listings, filtered by `--keywords` when given.

## See more results

- To see more results from `search` or `saved`, run the same command again with every search term and filter unchanged, a new `--out` file and `--next-page`. The CLI finds the list by its search terms and filters, and remembers where it stopped in this conversation. Without `--next-page` or `--after`, the command starts over at the first page, so it returns listings the user already saw.

- Run one `--next-page` at a time for each list, because two at once can return the same page.

- A page without `paging.cursors.after` is the last one, so when the user asks for more, tell them there are no more results.

- A script pages by passing each page's `paging.cursors.after` to `--after`. That value can be a short page code, which works for 7 days.
