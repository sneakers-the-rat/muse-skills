# Facebook comments

## Read comments

```sh
/opt/hatch/bin/facebook-cli post comments read --post-id '<post ID>'
/opt/hatch/bin/facebook-cli post comments read --post-id '<post ID>' --limit 20 --after '<cursor>'
```

- `--post-id` is required. A page holds at most 20 comments, and larger `--limit` values are capped.

- `paging.cursors.after` appears only when more comments exist. Pass it unchanged as `--after` for the next page, and stop when it is absent. Follow pages only as far as the request needs.

- Each comment in `data` has `id`, `author_name`, `text`, `created_time` as a Unix timestamp, `reply_count` and `comment_url`, the direct link to that comment. `summary.post_url` links to the parent post.

## Present comments

- Group comments by post when they come from several posts, with each post's `summary.post_url`.

- When finding people who commented on several posts, name only commenters who actually appear in more than one returned thread. Never invent names or relationships.

## Add a comment or reply

```sh
/opt/hatch/bin/facebook-cli post comments add --post-id '<post ID>' --text 'Exact comment text'
/opt/hatch/bin/facebook-cli post comments add --post-id '<post ID>' --parent-comment-id '<comment ID>' --text 'Exact reply text'
```

- `--reply-to` is an alias for `--parent-comment-id`.

- Read the target with `post read` before commenting, even when the user supplies an ID, and decode a share link first. Before replying, read the comments to find the parent comment's ID. Reuse successful reads from this request.

- The post ID may be numeric or a PFBID, and the parent comment ID must be numeric. The text must not be blank and must fit on the approval card in full. If it does not fit, nothing is sent and the error states the exact character limit for this comment. `--message` is an alias for `--text`.

- The native approval shows the post link, the parent comment link for a reply and the exact text before the single write attempt. Each comment needs its own fresh approval.

- A successful receipt contains `comment_id` and `comment_url`. Return the `comment_url` as a clickable link, and never repeat the write to get a link, to verify success or to handle a later confirmation of the same request.

- After an uncertain outcome, check the comments with a read instead of writing again. Comments cannot be edited or deleted through this connector.
