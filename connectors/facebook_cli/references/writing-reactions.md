# Adding/changing/removing Facebook reactions

- reactions are made through the user's linked personal profile, and are currently scoped to posts, comments, and replies.

```sh
/opt/hatch/bin/facebook-cli post reactions add --id '<post or comment ID>' --reaction-type '<LIKE|LOVE|WOW|HAHA|SORRY|ANGER>'
```

```sh
/opt/hatch/bin/facebook-cli post reactions remove --id '<post or comment ID>'
```

- When the user asks to react, map clear reaction names to the supported types: Like, Love, Wow, Haha, SORRY (Sad), and ANGER (Angry). If the user's requested reaction is ambiguous or doesn't map clearly, ask for clarification based on the available options.

- To react to a specific post or comment, you'll need the right post or comment ID. Read the post or comment before reacting.

- Reacting with the current reaction writes nothing and returns `changed: false`. `add` with a different type replaces it. There's no separate edit command.

- A successful receipt contains `success`, `changed`, and `reaction_type` (`null` if reaction was removed), `previous_reaction`, `post_id`, and if reacting to a comment `comment_id`.

- If the write outcome is unknown, read the target's reactions. Report the current reaction from the output.

## References

- [Reading posts](/opt/hatch/connectors/facebook_cli/references/reading-posts.md) serves as a reference for reading posts themselves.

- [Feed](/opt/hatch/connectors/facebook_cli/references/feed.md) serves as a reference for fetching posts on the user's feed.

- [Reading comments](/opt/hatch/connectors/facebook_cli/references/reading-comments.md) serves as a reference for retrieving and reading specific comments.
