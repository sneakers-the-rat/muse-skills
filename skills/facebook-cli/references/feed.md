# Facebook feeds

```sh
/opt/hatch/bin/facebook-cli feed newsfeed
/opt/hatch/bin/facebook-cli feed newsfeed --limit 10 --after '<next_cursor>'
/opt/hatch/bin/facebook-cli feed friends --limit 5
```

- `feed newsfeed` returns the ranked newsfeed of organic stories, without ads. `feed friends` returns ranked stories from friends only.

- Both return 10 stories by default and at most 10. Pass a returned `next_cursor` as `--after` for the next page, and `--cursor` is an alias.

## Read the stories

- Both commands return a `social_posts_v1` collection with `posts`, `next_cursor` and `has_next_page`. Read `posts[]` directly rather than guessing a nested path or piping the command through `jq`. A schema mismatch fails with an error instead of returning an empty list.

- Each story has `post_id`, `url`, `platform`, `created_at`, `post_created_at`, `username`, `post_caption`, `header_text` and the media and engagement fields that are available.

- Present captions as [Posts](posts.md) describes. A feed caption that matches `header_text` is the provider-written story header, not the author's words.

## Present a feed

- Present stories in the returned order, because the feed ranks them by relevance. Include each story's `url`.

- When `next_cursor` is present, more stories are available, so offer to fetch the next page.

- Use a story's `post_id` for `post comments read` and `post reactions read`.

- Keep a feed browse faithful to the stories. For a requested analysis, keep your interpretation separate from what the posts actually say.
