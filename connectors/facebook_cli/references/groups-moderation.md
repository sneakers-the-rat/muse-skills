# Facebook Group moderation

- These commands list and moderate individual items in four Facebook Group queues: pending posts, membership requests, participation requests, and spam. They are available to Group admins and moderators.

- These commands aren't available on confidential VMs and return an unavailable error there.

## List a queue

- `groups search` command can provide the numeric Group ID needed for the queue list and moderation commands.

- Public Groups use participation requests and private Groups use membership requests. When the Group's privacy is unknown, read `visibility` via the `groups details` command before choosing: `OPEN` is public, and `CLOSED` and `SECRET` are private.

- A queue mismatch returns a message identifying the applicable queue, such as "This Facebook Group is private. Use the pending membership requests workflow instead of pending participation requests."

```sh
/opt/hatch/bin/facebook-cli groups pending-posts list --group-id '<group ID>' [--limit <1–20; default: 20>] [--after '<paging.cursors.after from the previous response>']
/opt/hatch/bin/facebook-cli groups pending-membership-requests list --group-id '<group ID>' [--limit <1–20; default: 20>] [--after '<paging.cursors.after from the previous response>']
/opt/hatch/bin/facebook-cli groups pending-participation-requests list --group-id '<group ID>' [--limit <1–20; default: 20>] [--after '<paging.cursors.after from the previous response>']
/opt/hatch/bin/facebook-cli groups spam list --group-id '<group ID>' [--content-type post|comment] [--limit <1–20; default: 20>] [--after '<paging.cursors.after from the previous response>']
```

- All four queue responses return the current page of items in `data`. Nonempty `summary.warnings` indicates that some items were omitted, so the returned page is incomplete even if `data` is empty.

- Pending posts are returned in `data` with `content_id`, `type`, and `preview`. Optional fields are `author_id`, `author_name`, `author_profile_picture_url`, and `review_url`. `summary.total_count` covers the whole queue.

- Membership and participation requests are returned in `data` with `member_id` and `name`. Optional fields are `profile_picture_url`, `facebook_age_days`, `question_answers`, `rules_agreement_status`, and `review_url`. `question_answers` contains the requester's responses to the Group's screening questions.

- Spam entries are returned in `data` with `content_id` and `type` (`post` or `comment`). Optional fields are `author_id`, `author_name`, `author_profile_picture_url`, `preview`, and `review_url`. Use `--content-type post` or `--content-type comment` to filter by type.

## Link an item

- Each queue item can include a `review_url` that opens it in its moderation queue. The user can follow this link to review additional context about the item in the queue.

- After presenting a queue with at least one `review_url`, include one offer to open an item's exact returned link in Muse's cloud browser if the user has trouble opening it. For multiple items, let the user choose which item.

- The user may need to take control of Muse's cloud browser and sign into Facebook with an account that administers or moderates the Group.

- When a script picks fields out of a list, keep `review_url` for every item the user may want to open.

- Use each item's `review_url` exactly as returned. Facebook generates the link for that specific item and moderation queue. The Group or item ID alone is not enough to construct it.

- When an item has no `review_url`, say that Facebook returned no review link for it instead of linking a queue or Group page.

## Moderate the queue

```sh
/opt/hatch/bin/facebook-cli groups pending-posts moderate --group-id '<group ID>' --post-ids '<content_id>' --action <approve|decline> [--decline-feedback '<feedback; may be shown to the author; decline only; max 500 characters>']
/opt/hatch/bin/facebook-cli groups pending-membership-requests moderate --group-id '<group ID>' --user-ids '<member_id>' --action <approve|decline>
/opt/hatch/bin/facebook-cli groups pending-participation-requests moderate --group-id '<group ID>' --user-ids '<member_id>' --action <approve|decline>
/opt/hatch/bin/facebook-cli groups spam moderate --group-id '<group ID>' --content-ids '<content_id>' --action <approve|delete>
```

- Each moderation invocation takes an item ID returned in `data` by that queue's `list` command: pending posts use `content_id` as `--post-ids`, membership and participation requests use `member_id` as `--user-ids`, and spam entries use `content_id` as `--content-ids`. Despite their plural names, these flags accept exactly one ID per invocation.

- For pending posts, `approve` publishes the post and `decline` rejects it. Optional `--decline-feedback` attaches a note to the decline. It may or may not be shown to the post's author; omitting it declines without feedback.

- For membership and participation requests, `approve` grants Group membership or approved participant status for posting and commenting, respectively. `decline` rejects the request.

- For spam, `approve` publishes the post to the Group or makes the comment visible on its post. `delete` removes the held post or comment without publishing it.

- The response contains an `outcomes` array with the item's result. `processing_status` is `SUCCESS` or `FAILURE`; failures include `failure.code` and `failure.detail`. A successful CLI exit does not guarantee the moderation action succeeded.

- CLI error output may contain an error prefixed with `GROUP_MODERATION_OUTCOME_UNKNOWN:`, meaning the write may have occurred but its result could not be confirmed. The corresponding queue's `list` command provides current state for reconciliation. The CLI does not retry moderation writes; another invocation could repeat an action that already completed.
