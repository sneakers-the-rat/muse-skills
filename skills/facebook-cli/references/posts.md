# Facebook posts

## Create a personal text post

```sh
/opt/hatch/bin/facebook-cli post create --message 'Exact post text'
/opt/hatch/bin/facebook-cli post audiences
/opt/hatch/bin/facebook-cli post create --message 'Exact post text' --privacy '<returned audience ID or exact name>'
/opt/hatch/bin/facebook-cli post crossposting [--privacy '<returned audience ID or exact name>']
```

- `post create` publishes one text post to the user's own profile. The text must not be blank and must fit on the approval card in full. If it does not fit, nothing is sent and the error states the exact character limit for this post. `--text` is an alias for `--message`. Preserve the exact text the user approved.

- Omit `--privacy` to use the current Facebook composer default. The native approval shows the linked profile, the exact text, the audience and any sharing destinations, so do not ask a separate audience question or infer the default.

- For an explicit audience request or a question about which audiences are available, refresh `post audiences`, because earlier results go stale when settings change. It returns `selected_option` and `options`, each with an `id`, `name` and `explanation`, and adds `default_audience_error` when the default is unsupported.

- Pass only a returned ID or exact name to `--privacy`. Only me, Friends and Public are supported when Facebook returns them. Custom audiences and per-person inclusions or exclusions are unavailable, so do not offer them or substitute Friends for an exclusion request.

- If the default is unsupported or the requested audience is absent or ambiguous, explain the available choices and ask the user to pick one. Never substitute another audience yourself.

- Sharing to story, Instagram and Threads follows the user's account settings unless the user asks for a change on this post. Pass `--share-to-story`, `--share-to-instagram` or `--share-to-threads` with `on` or `off` in the first creation command, and keep those choices if the user asks for a revised approval.

- An unavailable sharing destination fails before approval. Relay the returned reason, and do not add media or change the post to work around a text-only limit.

- `post crossposting` answers questions about account sharing settings. Each entry in `destinations` has a `type`, `auto_share` for the account setting and `eligible` for whether this content and audience can be shared, with `ineligible_reason` and `ineligible_detail` when it cannot. These flags never change account settings, which change in Accounts Center.

- Personal posts cannot attach media, post to a group, or edit or delete content.

## Confirm the post

- A successful receipt contains `post_id` and `post_url`. Show the confirmed `post_url` as a clickable link in your confirmation, not just the post ID, and never publish again to get a link or verify success.

- If the transport or the receipt fails, the post may still exist. Inspect it through a read and report the outcome as unconfirmed. Never retry with another audience or a test post.

- An explicit audience rejection means no post was created. Refresh `post audiences` once and request a fresh approval for an audience the user chooses.

## Read a post

```sh
/opt/hatch/bin/facebook-cli post read --post-id '<returned post ID>'
/opt/hatch/bin/facebook-cli post read --url '<canonical Facebook URL>'
```

- Supply exactly one nonblank `--post-id` or `--url`. IDs may be numeric or bare PFBIDs (`pfbid02...`). The output uses `social_posts_v1` with the post's text, permalink and available media context in `posts[]`.

## Read from a Facebook URL

- The post reader does not decode share links. Decode a `/share/<token>/` or `/share/p/<token>/` wrapper first and pass the returned `original_url` unchanged:

```sh
/opt/hatch/bin/facebook-cli link-sharing decode-url --url 'https://www.facebook.com/share/p/<share-token>/'
```

- If `original_url` is null, missing or blank, report that the link could not be resolved and stop. A decoded URL shows the content type, not that the account can read the content.

- Skip decoding for an already canonical URL. The reader accepts these paths on `facebook.com`, `www.facebook.com`, `m.facebook.com`, `mbasic.facebook.com`, `web.facebook.com` and `touch.facebook.com`:
  - posts at `/<profile>/posts/<post-id>` or `/posts/<post-id>`
  - group posts at `/groups/<group>/posts/<post-id>` or `/groups/<group>/permalink/<post-id>`
  - permalinks at `/story.php?story_fbid=<post-id>` or `/permalink.php?story_fbid=<post-id>`
  - photos at `/photo.php?fbid=<id>` or `/photo/?fbid=<id>`
  - videos and Reels at `/reel/<id>`, `/videos/<id>`, `/<profile>/videos/<id>`, `/watch/?v=<id>` or `/video.php?v=<id>`

- Pass the complete URL, including its query parameters. Do not extract an ID or resolve the media yourself, because the reader resolves a photo or video URL to its containing post.

- Standalone media may have no containing post. A failed read ends the chain, so report it without guessing an ID, retrying a media ID as a post ID or claiming the content is readable from the URL.

- A malformed or unsupported URL, including an undecoded share link, returns HTTP 400. A supported URL whose post or media is missing, private or unreadable returns HTTP 404, and the two cases look the same.

## Route other links

- Browse a group link (`/groups/<group-id>`) with `groups posts --group-id`. If the path has a name instead of a numeric ID, find the group with `groups search` first.

- Read a Marketplace item link with `marketplace listing details --url`, keeping the full URL.

- Read an event link (`/events/<id>/`) with `events details --event-id <id>`.

- Game and unrecognized URLs are unsupported, so say so. Never pass a number from another kind of URL to `post read`.

## Present posts

- Include `post_caption` and `url` when present, and never invent a link or text when they are absent.

- `post_caption` prefers the author's text and can fall back to a media summary or a provider-written story header, also returned as `header_text`. Present those fallbacks as descriptions, not as the author's words.

- Name the post's owner when browsing several people's posts. Omit it when the context already makes the author obvious.

- Ground every claim about what someone has been doing in a specific post and link it.

- `media_summary`, `media_ocr` and `video_transcript` describe media when present. They are precomputed and often missing, so never claim a post shows something unless one of them confirms it.

## Read shopping context

- `post read` returns shopping context for some videos and Reels, and list commands such as feeds and timelines never do. `shoppable_products` lists detected products, each with a `product_name` and optional `descriptive_name`, `category`, `item_type`, `brand_name`, `color`, `style`, `gender` and `prominence`, alongside `shoppability` and `shoppable_product_category`.

- Use those fields to answer what a video shows or sells instead of inferring products from the caption or transcript. They describe detected products, not verified prices or availability.

- `post read --out <new file>` also fetches recommended similar products for general Reel shopping. They are recommendations, not creator tags or confirmed identifications, and they can mix sponsored and organic products.

- With `--out`, the output adds `featured_products_status` and `ordered_featured_product_ids`. `available` means the file holds a catalog ready for `shopping.resolve_results`, and `unavailable` means no catalog was written and the ID list is empty.

- Follow [Shop a Facebook Reel](shopping-links.md) to decide whether to use `--out` and how to present the products.
