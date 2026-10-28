# Facebook saved items

- `saved` commands let Muse find previously saved items, add or remove saved items, and organize saved items in collections.

## Find saved content

```sh
/opt/hatch/bin/facebook-cli saved list [--type <post, post_with_photo, video, reel, link, page, product, event, or another returned type>] [--collection-id '<id from saved collections list>'] [--limit <up to 20>] [--after '<paging.cursors.after from the previous response>']
```

- `saved list` returns the user's saved items, with most recently saved first. A page holds at most 20 items.

- Each item's `collection_ids` lists the collections that hold it, by the IDs `saved collections list` returns. An empty list means the item is in no collection. It lists every collection that holds the item, even when `--collection-id` narrows the read.

- Fetch the next page of saved items only when the user asks for more.

```sh
/opt/hatch/bin/facebook-cli saved collections list [--limit <up to 20>] [--after '<paging.cursors.after from the previous response>']
```

- `saved collections list` returns each saved collection. A page holds at most 20 collections.
- Read every page of collections before creating a collection or choosing among them. To file into a named collection, stop once it appears.

- For both `saved collections list` and `saved list`, to see more results, pass the previous response's `paging.cursors.after` as `--after` with the same query and filters. A missing `paging` means there are no more results.

## Read the saved content

- `saved list` already shows each item's title, description and link. To open one in more detail, use the reader for its `type`:
  - `post`, `post_with_photo`, `video` and `reel`: pass the item's returned `permalink` unchanged to `post read --url`. Its `id` and `savable_id` are not post IDs. For comments or reactions, use `posts[0].post_id` from a successful post read with `post comments read --post-id` or `post reactions read --post-id`.
  - `page`: pass its `savable_id` to `profile info --profile-id`
  - `product`: pass its `savable_id` to `marketplace listing details --listing-id`
  - `event`: pass its `savable_id` to `events details --event-id`

## Save or remove an item

- A clear request authorizes these changes without another confirmation because saves are private and easy to undo. Resolve the exact item and collection first. When several saved items match, show each one's title and link and ask which one before changing anything.

- Each item has an `id` for the save itself and a `savable_id` for the content. `add` and `remove` take `savable_id`. Both assume `post` when `--type` is omitted, so for anything else pass the item's returned `type` unchanged.

```sh
/opt/hatch/bin/facebook-cli saved add --savable-id '<savable_id from saved list or another read>' [--type <post (the default), post_with_photo, video, reel, link, page, product, event, or another returned type>] [--collection-id '<id from saved collections list>']
```

- `saved add` saves an item. Without a collection, it saves to 'All Saves'.

```sh
/opt/hatch/bin/facebook-cli saved remove --savable-id '<savable_id from saved list>' [--type <post (the default), post_with_photo, video, reel, link, page, product, event, or another returned type>] [--collection-id '<collection to remove it from; omit to unsave completely>']
```

- `saved remove` removes a saved item. With a collection passed in, it removes only that membership. Without a collection, it fully unsaves the item.

- A successful `add` returns `saved: true` and `remove` returns `unsaved: true`. Confirm the change from that result instead of listing again.

```sh
/opt/hatch/bin/facebook-cli saved collections create --name '<collection name>'
```

- `saved collections create` creates a new saved collection.
