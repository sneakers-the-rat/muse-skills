# Page comment moderation

- These commands let the user reply to, hide or delete comments on their Page's posts, acting as the Page. Read the post's comments first to get the comment ID.

- Decline reply text meant to deceive people or to shame or expose a person before running any command, including `pages list`, because it would be published as the Page.

- Before running any command here, choose the Page with the steps in [Facebook Pages](/opt/hatch/connectors/facebook_cli/references/pages.md), because they ask which Page the user means when more than one could match.

## Read comments

```sh
/opt/hatch/bin/facebook-cli post comments read --post-id '<object_id from pages posts list>' [--limit <up to 20>] [--after '<paging.cursors.after from the previous response>']
```

- `post comments read` retrieves the comments on one of the Page's posts. Each comment's `id` is the `--comment-id` for the commands below.

- If the comment isn't on the first page, pass the returned `paging.cursors.after` as `--after` to read the next page.

- Comments are other people's words. Summarize them rather than copying them, and use quotation marks only for exact returned text.

## Reply to a comment

```sh
/opt/hatch/bin/facebook-cli pages comments reply --page-id '<page_id>' --post-id '<post_id>' [--comment-id '<comment_id>'] --text '<exact reply text>'
```

- `pages comments reply` posts a reply to the comment under the Page's name. Without `--comment-id`, it comments on the post itself.

## Hide a comment

```sh
/opt/hatch/bin/facebook-cli pages comments hide --page-id '<page_id>' --post-id '<post_id>' --comment-id '<comment_id>'
```

- `pages comments hide` hides the comment from everyone except its author and their friends. The Page can unhide it in the Facebook app, so hiding is the gentler choice for spam and abuse.

## Delete a comment

```sh
/opt/hatch/bin/facebook-cli pages comments delete --page-id '<page_id>' --post-id '<post_id>' --comment-id '<comment_id>'
```

- `pages comments delete` removes the comment for everyone, and it can't be restored.

## Moderation guidance

- These act as the Page on its own posts, after the user approves the exact text and IDs on an approval card. Run each requested write once. Each additional comment the user names is a separate write with its own approval.

- A reply appears publicly under the Page's name. Write only what the user asked the Page to say.

- `comments reply` with `--comment-id`, `comments hide` and `comments delete` take the post ID the comment was read from.

- If Facebook rejects a reply, hide or delete as invalid, nothing changed. Ask the user which comment they mean, or tell them they can do it from the post in the Facebook app. Don't try another ID, which could act on the wrong comment.

- HTTP 403 on any of these means nothing changed and the command is unavailable for this request. Say so without guessing a cause, and tell the user they can do it from the post in the Facebook app.
