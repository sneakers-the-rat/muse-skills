# Facebook stories

```sh
/opt/hatch/bin/facebook-cli story feed
/opt/hatch/bin/facebook-cli story feed --limit 5
```

- `story feed` reads the user's story tray, the recent stories from friends and Pages they follow. `--limit` counts story buckets, one per author, not individual cards. It defaults to 20 and allows at most 50.

- Each bucket has `owner_name`, `owner_id`, `seen` for whether the user has viewed it, and `cards`. Each card can include `story_id`, `creation_time` and `expiry_time` as Unix timestamps, `message` for any text and `story_url`.

- Describe a story from its returned text and link, and keep its author clear.
