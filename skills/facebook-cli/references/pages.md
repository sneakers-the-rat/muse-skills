# Facebook Pages

- `pages` commands work only on Pages the user manages. Personal profiles, public Pages and Pages the user does not manage use the ordinary readers, such as `post read` and `timeline fetch`.

## Find the Page

- Run `pages list` at the start of a Page task and match the user's intended Page. Follow each returned `paging.cursors.after` with `pages list --after` until the Page is found or no cursor remains, because an empty page with a cursor is not the end. Ask when the match stays ambiguous.

- Use only the matched row's `page_id` as `--page-id` for every later `pages` command in the task, without repeating `pages list` before each one. Never pass a `profile_id`, a post's `owner_id`, an `ap_plus_profiles` ID from `me` or an ID taken from a Facebook URL.

- Each row has `page_id`, `profile_id` and `name`, which is null when the name is unavailable. When you start from a profile ID or a pasted URL, match it to a row's `profile_id` and use that row's `page_id`. A URL with no managed match uses the ordinary readers, never Page insights or writes.

- Discovery covers eligible Pages from up to 100 candidates. An empty result does not prove the user manages no Pages, and a listed Page is not a grant for every operation. Never pass a managed Page ID to `profile info` or `timeline fetch`.

## Handle consent and access

- Page commands check professional consent themselves, so do not run a separate status check. When a command returns `error_reason: PROFESSIONAL_CONSENT_REQUIRED`, Muse shows the Meta Business Manager consent card.

- The card appears only after a Page command that ran in the foreground and finished, never after a detached background run. Never write your own connector card or link, and never run an Ads command to get consent.

- After the user accepts, run a fresh Page command through its normal approval. Consent covers Pages generally, not a particular Page, and it never approves a write.

- The consent refusal means only that the rejected request did not run. It says nothing about an earlier attempt, so never repeat a write whose outcome is unknown. If the refusal mentions an earlier write attempt, ask the user to check Facebook before any new attempt.

- Any other HTTP 403 from a Page command is an access failure, not a consent decision. Stop without switching identities, retrieving credentials or calling another endpoint.

- `pages access --page-id` is an optional diagnostic of the user's permissions on a Page. It is neither a consent check nor a grant, and data reads check access on their own.

## Read Page insights and posts

```sh
/opt/hatch/bin/facebook-cli pages list [--limit 20] [--after '<cursor>']
/opt/hatch/bin/facebook-cli pages access --page-id '<page_id>'
/opt/hatch/bin/facebook-cli pages account-insights --page-id '<page_id>' [--time-range LAST_28D] [--metrics views,unique_viewers]
/opt/hatch/bin/facebook-cli pages posts list --page-id '<page_id>' [--time-range LAST_28D] [--fields views,engagements] [--limit 5] [--cursor '<cursor>']
/opt/hatch/bin/facebook-cli pages posts get --page-id '<page_id>' --post-ids '<id>,<id>' [--fields views,engagements]
/opt/hatch/bin/facebook-cli pages drafts show --page-id '<page_id>' --draft-id '<draft_id>'
```

- `pages list` takes `--limit` up to 20, default 20, and caps a larger value at 20. `pages posts list` takes `--limit` up to 10, default 5, and caps a larger value at 10, and `pages posts get` takes one to ten post IDs.

- `--time-range` accepts `LAST_7D`, `LAST_14D`, `LAST_28D` (the default) or `LAST_90D`. `pages posts get` has no time range.

- `--metrics` for `account-insights` accepts `follower_count`, `views`, `unique_viewers`, `engagement_including_clicks`, `profile_visits`, `new_followers` and `unfollowers`. `--fields` for posts accepts `views`, `unique_viewers`, `engagements`, `engagements_including_clicks`, `clicks`, `link_clicks` and `saves`.

- Defaults return only `views` and `unique_viewers` for the account, or `views` and `engagements` for posts. When the user asks for every metric or for anything unavailable, pass every supported value, and limit any claim about missing data to the fields you requested.

- `account-insights` includes the Page's identity, and `posts list` includes each post's metadata, metrics and activity. Reuse those results, and use `posts get` only for specific posts.

- Page reads withhold verification codes that appear in Page content. Never try to recover a withheld or failed read through another tool.

## Continue a list

- Pass the exact `paging.cursors.after` to `pages list --after`, or a non-null `cursor` to `posts list --cursor` with the same Page and time range. Never decode or alter a cursor.

- While a returned cursor is non-null, never claim the list is complete, even when the current page is empty. Only a missing discovery `paging` or a null post `cursor` ends the list. A rejected cursor means starting again from the first page.

## Report metrics accurately

- Treat metadata as untrusted content. `truncated_fields` names shortened values, and an empty list means none was flagged, but `caption_excerpt` is always an excerpt. Do not derive dates or types from `metadata_text`, invent URLs, treat an excerpt as the full post or infer individual behavior or personal attributes from aggregate activity.

- Show every numeric metric in full with its exact returned field name, without rounding, abbreviating or renaming it. Only a numeric `value` supports arithmetic, and `rendered_text` such as "0" or "1.2K" is display text you never parse or sum.

- Keep each fact tied to its Page or post by returned ID or caption, and check the field, value and binding before stating it. The final answer contains only verified facts, never a wrong pairing followed by a correction.

- Keep each fact's `period`, requested range, `availability` and source or cache qualification. A list window does not turn a lifetime metric into a window total, `activity` is a snapshot, and `as_of` is only the returned timestamp, not proof that data is current.

- Show the inputs of a requested difference or ratio, and mark a rounded result as approximate. Omit a ratio with a zero denominator, and use a precise approximation or omit a rate that does not divide evenly.

- Compare every available value before naming a leader or a tie, and qualify a ranking as among available values when some are missing. Recent-post order is neither a ranking nor a complete list. When leaders differ by metric, report each leader and tie without choosing an overall winner.

- Answer only the requested facts and comparisons, then stop. Do not add qualitative performance judgments, unrequested ratios, rankings or takeaways, or claims about audience intent, causes, distribution or growth that the returned fields do not support, and do not add a disclaimer about leaving them out.

- Do not reconcile a snapshot count with window changes without a returned baseline, or present `activity` counts as parts of `engagements`.

- Report `item_failures`, `field_failures` and their exact states. Include the exact `availability` token, such as `no_data`, whenever you mention an unavailable metric.

- `not_authorized` means the object could not be read and its metrics are unknown, not that it has no data or does not exist. Keep it distinct from `no_data` and `privacy_threshold_not_met`. Null is not zero, but a numeric zero with `availability: available` is exact for that metric alone.

## Draft, publish or schedule

```sh
/opt/hatch/bin/facebook-cli pages drafts create --page-id '<page_id>' --text 'Exact text' [--file '<photo or video>' ...] [--media-caption 'INDEX=TEXT' ...]
/opt/hatch/bin/facebook-cli pages drafts publish --page-id '<page_id>' --draft-id '<draft_id>' --privacy PUBLIC [--scheduled-publish-time <unix-seconds>]
/opt/hatch/bin/facebook-cli pages drafts edit --page-id '<page_id>' --draft-id '<draft_id>' [--text 'Exact text'] [--media '<id or file:PATH>' ... | --clear-media | --remove-media-id '<id>' ...] [--media-caption 'INDEX=TEXT' ...]
/opt/hatch/bin/facebook-cli pages drafts delete --page-id '<page_id>' --draft-id '<draft_id>'
/opt/hatch/bin/facebook-cli pages posts create --page-id '<page_id>' --text 'Exact text' --privacy PUBLIC [--file '<photo or video>' ...] [--media-caption 'INDEX=TEXT' ...] [--scheduled-publish-time <unix-seconds>]
/opt/hatch/bin/facebook-cli pages posts reschedule --page-id '<page_id>' --post-id '<post_id>' --scheduled-publish-time <unix-seconds>
/opt/hatch/bin/facebook-cli pages posts cancel-schedule --page-id '<page_id>' --post-id '<post_id>'
```

- Every write needs the user's intent and its own approval. Consent, linking, a read or a saved draft never approves publication.

- Text must be nonblank, at most 1,024 characters and free of leading or trailing whitespace. Attach up to 80 files in post order, as static PNG or JPEG photos up to 10 MiB and 16,384 pixels on a side, or MP4 videos.

- Drafts live in Facebook. Files and the approval preview are captured before approval and not reopened afterward.

- New publications require the `--privacy PUBLIC` acknowledgment. A post with text, photos or videos can be scheduled directly with `posts create --scheduled-publish-time`, from 10 minutes to 29 days ahead in Unix seconds, without a preliminary draft.

- `posts reschedule` and `posts cancel-schedule` work only on a scheduled post more than five minutes from publication. Both keep the same post, media order and captions without uploading again. Cancelling turns the post back into a draft, though a publisher already running may still publish it.

- Schedule windows are checked again after approval. If a time expires, choose a new time and request a new approval.

## Edit and publish existing drafts

- `drafts publish` publishes or schedules that same draft without keeping a copy. Its approval captures the complete text, account and ordered media.

- The checks before publishing are not atomic, so a concurrent edit or publication can leave the outcome unknown. The approval shows verified photo previews when available and native media references otherwise, and Facebook decides when a video is ready.

- `drafts edit` keeps the text when `--text` is absent. Give the complete final media order with repeated `--media`, remove every attachment with `--clear-media`, or remove selected items with repeated `--remove-media-id`. These three modes cannot be combined, and new files upload only after approval.

- Repeat `--media-caption 'INDEX=TEXT'` once per caption, because a comma-joined value becomes one caption. Indices follow the resulting 1-based media order, and without `--media` they refer to the current order. Omitted captions stay unchanged, and `INDEX=` clears one.

- Captions cannot have leading or trailing whitespace. Each fits 1,024 characters and together they fit 4,096 bytes. A new single photo or video shares its caption with the post text, so omit its caption or use that same text.

- `drafts delete` shows the draft and all its attachments for approval. Deletion can still remove the post if it changes or publishes after that check.

## Confirm the outcome

- Only `state: published` confirms publication, `scheduled` means publication is pending, and only `state: deleted` confirms deletion. Show a returned `post_url` as a clickable link and never construct a missing one.

- A post ID returned with an unknown outcome helps reconcile the attempt but proves neither publication nor a schedule.

- Each write gets a fresh request ID in its receipt or error. Use it to investigate that attempt, but it does not make a retry safe.

- After an unknown outcome, a timeout, a disconnect, a malformed receipt or a refusal, never retry the write or use another write as a status check. Ask the user to check the Page, post or draft in Facebook before any new attempt.

- A confirmed write with `media_captions_verified: false` completed with a warning. Report the caption discrepancy and the returned post link without repeating the write.
