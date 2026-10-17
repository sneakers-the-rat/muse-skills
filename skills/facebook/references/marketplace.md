# Facebook Marketplace

- These commands search Marketplace listings, read items and sellers, and manage the user's own listings. Use [Marketplaces](/opt/muse/skills/marketplaces/SKILL.md) for buying, selling and coordinating a transaction, and [Shopping](/opt/muse/skills/shopping/SKILL.md) for product comparison and checkout.

- Route a pasted Marketplace item link or share link as [the connector doc](../CONNECTOR.md) describes, before any search.

## Form a search

- Turn the request into at least one search query plus any stated budget, condition, delivery preference, category and listing age, such as 7 days for listed this week. If the request is too vague to search, such as "something nice," ask for a product type or category first.

- There is no `--location`, `--city` or `--address` flag. Geocode a named place with `map.geocode` and pass `--latitude` and `--longitude` together.

- If the user named no location, use a default location and radius saved in memory and tell the user which you applied, such as San Jose within 30 miles. Without a saved default, omit the location flags.

- Quote every `--query` value, because an unquoted multiword query breaks argument parsing.

## Run the search

```sh
MARKETPLACE_RESULTS_JSON=$(mktemp "${TMPDIR:-/tmp}/facebook-marketplace-search.XXXXXX")
/opt/hatch/bin/facebook-cli marketplace search \
  --query 'road bike 51cm' --query 'road bicycle 51' --max-price 500 \
  --latitude 37.3382 --longitude=-121.8863 --radius-in-miles 20 \
  --sort-by price_ascend --allowed-item-conditions 'new,used' \
  --out "$MARKETPLACE_RESULTS_JSON"
```

- Give every search and every page its own new `--out` file. The flag truncates an existing file, which would drop results the shopping resolver still needs.

- The search flags are:
  - `--query` or `-q`, required and repeatable, with the first as the primary term
  - `--min-price` and `--max-price` in dollars
  - `--latitude` and `--longitude` for the search center, plus `--radius-in-miles` or `--radius-in-km` only when the user gave a distance or you applied a saved default, in the unit given, decimals allowed, without converting between them
  - `--max-listing-age-in-days`
  - `--sort-by` with `best_match`, `creation_time_descend`, `price_ascend`, `price_descend` or `distance_ascend`
  - `--allowed-item-conditions` as a comma-separated list, such as `new,refurbished`
  - `--delivery-method` with `local_pickup_only`, `shipping_only` or `pickup_and_shipping`
  - `--category-id`, repeatable
  - `--limit`, 20 by default and at most 20
  - `--after` with the previous page's `paging.cursors.after`

- Write negative numbers in the `--longitude=-121.8863` form so they are not read as another flag. This applies to `--latitude`, `--longitude`, `--min-price` and `--max-price`.

- For a vehicle, use `--min-year`, `--max-year`, `--min-mileage-in-miles`, `--max-mileage-in-miles` or `--transmission automatic|manual` for the requested constraints. Years start at 1900 and mileage accepts 1 to 1,000,000 miles, so convert kilometers to miles first.

- Any vehicle filter limits results to whole vehicles, so never use one for parts or accessories. Put the vehicle a part must fit in `--query` instead. If adding vehicle filters returns HTTP 400, check that no year is beyond next year and no minimum exceeds its maximum.

- Keep every filter unchanged when continuing with `--after`. When `paging` is absent, there are no more results. For a request to see more, fetch the next page instead of raising `--limit`.

## Present listings

- The listings are in the top-level `data` array of stdout. Choose results from stdout and never read the `--out` file.

- Photo URLs come back as an `image_url` object marked `withheld`, because a copied signed URL breaks. Pick only listings that have an `image_url`, since the resolver fails on a listing without a photo, and never write an image link yourself.

- Pass the `--out` files and the chosen `listing_id` values, in display order, to `shopping.resolve_results`:

```json
{
  "result_paths": ["<MARKETPLACE_RESULTS_JSON>"],
  "selected_ids": ["listing-id-1", "listing-id-2"]
}
```

- Then call `shopping.create_shopping_results_widget` with the returned `path`, which shows the listing cards with their photos and exact links. Use the returned markers as citations in your text, never as a replacement for the cards.

- Use the same resolver and widget for item details, saved listings and the user's own listings. With item details, also give the full description, price, condition, seller name and creation date.

- For each listing in the shortlist, give the title, a prominent price, a short excerpt of the description, the location and a recommendation on value. Never put listing results, links, titles or status in a code block, so links stay clickable.

- Without the resolver, link the title to `product_url`, or to `https://www.facebook.com/marketplace/item/<listing_id>/` when it is missing, and to `url` for item details.

- Recommend on value by comparing price with similar results, distance for pickup and stated condition. Read item details and seller feedback for the finalists before recommending one, and never invent photos or seller details that are missing.

## Read listing results

- Search, `saved` and `my-listings` results have `listing_id`, `title`, a formatted `price` such as "$900", `condition`, `description`, `location` as city and state text, `seller_id`, `product_url`, `creation_date`, `listing_status` such as Available, Sold or Draft, an optional `distance` such as "11 mi" and an optional `image_url`.

- These results carry no seller name or ratings, so never show a seller name from them.

## Read items, sellers and saved listings

```sh
/opt/hatch/bin/facebook-cli marketplace listing details --listing-id '<listing_id>' --out '<new file>'
/opt/hatch/bin/facebook-cli marketplace seller-info --listing-id '<listing_id>'
/opt/hatch/bin/facebook-cli marketplace saved [--keywords '<text>'] [--limit 20] [--after '<cursor>'] --out '<new file>'
/opt/hatch/bin/facebook-cli marketplace my-listings [--status active|pending|sold|draft] [--limit 20] [--after '<cursor>'] --out '<new file>'
```

- `listing details` takes one or more `--listing-id` values or one `--url` item link, never both. It does not accept share links, and it needs no linked account.

- For several listings, repeat `--listing-id` once per listing in `listing details` and `seller-info`, as in `--listing-id '<id1>' --listing-id '<id2>'`. A comma-joined value is sent as one ID.

- Item details add `currency`, `seller_name` and `created_at`, and use `url` for the listing link. Only the primary photo is included.

- `seller-info` returns `seller_id`, `name`, `followers`, `avg_rating`, `total_ratings`, `good_attributes` and `bad_attributes`, such as "Item as described (12)". Present the name, followers, average rating with the number of ratings and the feedback breakdown. A name or a large following alone does not show that a seller is trustworthy.

- `saved` lists the user's saved listings, filtered by `--keywords` when given. `my-listings` lists the user's own listings in every state, including drafts and sold items, unless `--status` narrows it. Both page with `paging.cursors.after`, at most 20 per page.

- Use `my-listings` to find the `listing_id` for an edit, deletion or publication. The user does not need to supply a raw ID when the listing can be found from the conversation and this inventory.

## Prepare a listing

- A listing goes live only when it has all four of these, whether at creation or later through `listing publish`:
  - at least one photo, through repeated `--photo <path>`
  - a condition through `--condition`
  - a category through `--category`
  - a location through `--latitude` and `--longitude` together

- Without all four, the listing is saved as a draft, even if the user asked to post it. Title and price are required to create a listing but do not decide publication.

- Decide whether the user wants the listing live or saved as a draft. Post, publish or list it for sale means live, and save a draft or finish it later means draft. Treat an ambiguous request as live.

- Check the four fields against what you have and say plainly whether the listing will publish immediately or be saved as a draft, naming any missing fields. Never silently create a draft when the user expects it to go live, and let them choose between supplying the fields and saving the draft.

- There is no draft-only flag. When the user wants a draft but all four fields are known, do not send a complete creation request, because it would publish. Keep the proposed listing in chat instead.

- Use only details the user gave or that are unambiguous from the conversation. Never invent features, specifications, brand or model details, history, accessories, flaws or measurements, and keep the description short and factual rather than embellished.

- Set the condition only when the user stated it, choosing `new`, `used_like_new`, `used_good`, `used_fair`, `used` or `refurbished`. Never infer it from a photo or the item type, and ask when it is unknown.

- Geocode only a specific place the user gave, such as a city, neighborhood, ZIP code or address. A region such as the Bay Area is not a listing location, so ask for a city or ZIP code instead of picking a point inside it.

- `--category` accepts a category ID or the names `vehicles`, `electronics`, `home`, `furniture`, `clothing`, `apparel`, `entertainment`, `family`, `hobbies`, `specialty`, `classifieds`, `housing`, `free`, `sports`, `outdoor`, `toys`, `games`, `garden`, `pet`, `pets`, `office`, `music`, `instruments`, `bikes`, `bicycles`, `auto-parts` and `miscellaneous`.

- `--currency` takes an ISO 4217 code and defaults to the user's Marketplace currency. `--delivery-type` is repeatable and accepts `public_meetup`, `door_pickup` and `door_dropoff`.

- Before creating, show the user the title, price, description, condition, category, photos, location and delivery. Mark each of the four publication fields as present or missing, label any value the user did not state as an assumption to confirm, and state whether it will go live or be a draft. Run the command only after explicit confirmation.

## Create a listing

```sh
/opt/hatch/bin/facebook-cli marketplace listing create \
  --title 'Oak desk' --price 150 --description 'Oak desk with scratches on top.' \
  --photo /path/to/desk-front.jpg --photo /path/to/desk-top.jpg \
  --condition used_good --category furniture \
  --latitude 37.3382 --longitude=-121.8863 --delivery-type public_meetup
```

- Photos upload as part of the command, with no separate upload step. The approval shows whether the listing will start live or as a draft.

- Read the response `message` and report the true status. "Listing created as draft" means it is not live, and "Listing published successfully" means it is.

- If it came back as a draft but the user wanted it live, name the missing fields and offer to add them with `listing edit` and then run `listing publish`. Give the status and the listing link as plain text.

## Check buyer messages after publication

- Once the response confirms a listing is live, run this once for the selling task, after the last result when publishing several listings:

```sh
/opt/hatch/bin/hatch_messenger_cli check
```

- [Messenger](/opt/hatch/connectors/messenger_read/CONNECTOR.md) is a separate connection from Facebook, so never claim it is connected because Facebook is. If it is not connected, run `/opt/hatch/bin/hatch_messenger_cli connect-url` and share exactly `[Connect Messenger](<connect_url>)`, without pasting the raw URL, so Muse can help with buyer inquiries.

- If Messenger is already connected, show no connection prompt. Offer briefly to help with buyer messages, but do not start monitoring or send a message unless the user asks.

- Skip this check for a draft, which cannot receive buyer inquiries, until it is published.

## Edit a listing

```sh
/opt/hatch/bin/facebook-cli marketplace listing edit --listing-id '<listing_id>' --title 'New title' --price 75
/opt/hatch/bin/facebook-cli marketplace listing edit --listing-id '<listing_id>' --photo /path/to/new1.jpg --photo /path/to/new2.jpg --category furniture --latitude 37.3382 --longitude=-121.8863 --delivery-type public_meetup
```

- Identify the listing from a create response, earlier results or `my-listings`. Show each change with its current and new value, say everything else stays the same, and edit only after explicit confirmation.

- Only the flags you pass change. Supplied photos replace the existing photo set, supplied delivery types replace the existing choices, and coordinates must be passed together. An omitted `--currency` keeps the listing's currency.

- Report the updated status and listing link as plain text.

## Publish a draft

```sh
/opt/hatch/bin/facebook-cli marketplace listing publish --listing-id '<listing_id>'
```

- Find the draft from its create response or `my-listings --status draft`. Check its stored photos, condition, category and coordinates through `my-listings` or item details before publishing.

- If a publication field is missing or you are not sure it is set, tell the user first and add it through an approved `listing edit` with values they confirm. Do not run publish just to see whether it is rejected.

- A missing field returns HTTP 400 with `missing_fields`. Explain what is missing, confirm the values with the user, add them with `listing edit`, then publish again, without guessing values.

- "Listing published successfully" means it is now live. "Listing is already published" means it was live before and nothing changed, which does not make automatic retries safe after an uncertain result.

- After either live result, run the buyer message check above. Report the true status and the listing link as plain text, and never claim publication after an error.

## Delete a listing

```sh
/opt/hatch/bin/facebook-cli marketplace listing delete --listing-id '<listing_id>'
```

- Deletion is permanent and cannot be undone. Delete only a listing the user explicitly identified, showing its title and link and getting explicit confirmation of the permanent deletion before running the command.

- Success returns the `listing_id` with the message "Listing deleted successfully." If deletion fails, for example because the listing was not found or the user does not own it, report the exact error.

## Recover from a failed write

- Never silently retry a failed create, edit, publish or delete, whether with the same command, a different method or changed values. First tell the user what you attempted, the exact error, why you think it failed and the change you propose, then wait for their review.

- A timeout or unreadable response can leave the outcome unknown. Read the listing through `my-listings` or item details before proposing another write.

- Running a failed read again needs no approval.
