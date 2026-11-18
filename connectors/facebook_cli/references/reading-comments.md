# Read comments

- `post comments` commands enable the user to read comments on Facebook posts.

```sh
/opt/hatch/bin/facebook-cli post comments read --post-id '<post_id from a timeline, feed or group posts>' [--limit <up to 20>] [--after '<paging.cursors.after from the previous response>']
```

- Results from `post comments read` return a page of at most 20 comments. If there are more comments available, the response also contains `paging.cursors.after`, the cursor that can be passed as `--after` to fetch the next page.

- Each comment in `data` contains `id`, `text`, `created_time` as a Unix timestamp, `reply_count`, and `comment_url`, a direct link to that comment. `author_id` and `author_name` appear together when Facebook returns the author. `summary.post_url` is the link to the parent Facebook post. This information can be helpful when presenting the data to the user, and referring them to the right link.

## Present comments

- Name the commenter from `author_name` each time you quote or summarize a comment, including in follow-up answers. Don't take a name from the comment text or a tagged person. When a comment has no `author_name`, say Facebook didn't return the commenter's name. When the user asks who wrote that comment, also give its `comment_url` mid-sentence and offer to look up the name in the browser, which takes a few minutes. Look it up only if the user says yes.

- Facebook post and comment links become separate cards when they end a line or fill a bullet, which splits the answer, so keep words after each link on the same line.

- Quote or summarize each comment's `text` as plain text, not as a link.

- Give the post's `summary.post_url` once, mid-sentence.

- Keep `comment_url` links out of the answer body, because each one adds a card that crowds out the answer. Put them at the end in one sentence, or give one when the user asks.

- Group comments by post when they come from several posts, with each post's `summary.post_url` once.

- Treat two comments as from the same person only when their `author_id` values match.
