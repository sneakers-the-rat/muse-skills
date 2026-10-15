# Facebook saved items

## Find saved content

```sh
/opt/hatch/bin/facebook-cli saved list --limit 20
/opt/hatch/bin/facebook-cli saved list --type video --collection-id '<collection ID>'
/opt/hatch/bin/facebook-cli saved collections list
```

- `saved list` returns saved items in `data`, most recently saved first. Each item has `id` for the save itself, `savable_id` for the underlying content, `type`, `saved_time` as a Unix timestamp, `title`, `description` and `permalink`.

- `--type` filters by category and accepts the `type` values `saved list` returns, such as `post`, `post_with_photo`, `video`, `reel`, `link`, `product`, `event` and `page`. Pass a returned value unchanged.

- `--collection-id` lists one collection. A page holds at most 20 items. Pass `paging.cursors.after` as `--after` for the next page only when the user wants more, and `--cursor` is an alias.

- `saved collections list` returns each collection's `id`, `name` and `item_count`.

## Read the saved content

- Pass `savable_id` to the reader that matches the item's `type`:
  - a post goes to `post read`, `post comments read` or `post reactions read` with `--post-id`
  - a Page goes to `profile info --profile-id`
  - a product goes to `marketplace listing details --listing-id`
  - an event goes to `events details --event-id`

## Save, move or remove an item

```sh
/opt/hatch/bin/facebook-cli saved add --savable-id '<savable_id>' --type post
/opt/hatch/bin/facebook-cli saved add --savable-id '<savable_id>' --type post --collection-id '<collection ID>'
/opt/hatch/bin/facebook-cli saved remove --savable-id '<savable_id>' --type post_with_photo --collection-id '<collection ID>'
/opt/hatch/bin/facebook-cli saved collections create --name 'My Collection'
```

- A clear request authorizes these changes without another confirmation. Resolve the exact item and collection first.

- `add` and `remove` take the content's `savable_id`, never the save entry's `id`. `--type` defaults to `post`, so pass the item's returned `type` unchanged for any other content.

- `add` without a collection saves to All Saves. `remove` with a collection removes only that membership, and without one it fully unsaves the item. Neither deletes the original post, video or Page.

- A successful `add` returns `id` with `saved: true`, and `remove` returns `id` with `unsaved: true`. Collection creation returns `collection_id` and `name`. Confirm the change from the result.
