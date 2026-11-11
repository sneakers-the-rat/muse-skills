# Page stories

- These commands read a managed Page's live stories and their view counts, and publish or delete a story as the Page.

- Decline story text meant to deceive people or to shame or expose a person before running any command, including `pages list`, because it would be published as the Page.

- Before running any command here, choose the Page with the steps in [Facebook Pages](/opt/hatch/connectors/facebook_cli/references/pages.md), because they ask which Page the user means when more than one could match.

## Read stories

```sh
/opt/hatch/bin/facebook-cli pages stories list --page-id '<page_id>' [--limit <1 to 20, default 5>] [--cursor '<cursor from the previous result>'] [--field <views, unique_viewers, engagements, engagements_including_clicks, reactions, shares, clicks, interaction_rate, comment_rate, reaction_rate, share_rate, views_by_follower_status or post_title>]
```

- `pages stories list` shows the Page's stories from the last 24 hours. An empty list means nothing is live, not that the Page never posts stories. Pass a returned cursor as `--cursor` for the next page.

```sh
/opt/hatch/bin/facebook-cli pages stories get --page-id '<page_id>' --story-id '<story_id>' [--field <views, unique_viewers, engagements, engagements_including_clicks, reactions, shares, clicks, interaction_rate, comment_rate, reaction_rate, share_rate, views_by_follower_status or post_title>]
```

- `pages stories get` reads up to 10 specific stories, such as ones from `pages stories list`, with one `--story-id` for each. Each ID comes back in `results` or in `item_failures` with its reason.

- Repeat `--field` for each metric the user asks about. `viewer_count` and `unique_viewers` come from different sources, so report each under its own name.

## Post or delete a story

```sh
/opt/hatch/bin/facebook-cli pages stories create --page-id '<page_id>' [--text '<exact story text>'] [--file '<PNG or JPEG photo>']
```

- `pages stories create` publishes a story as the Page with text of up to 1,024 characters, one PNG or JPEG photo, or both. Video isn't supported.

```sh
/opt/hatch/bin/facebook-cli pages stories delete --page-id '<page_id>' --story-id '<story_id from pages stories list>'
```

- `pages stories delete` removes one of the Page's live stories. A deleted story can't be restored.

- Facebook doesn't let a published story be edited, and no command changes one. When the user asks to change a story, say so and offer to delete it and post the corrected story. Run neither command in that turn, because the user hasn't yet agreed to remove a live story.

- Run `stories delete` and `stories create` as two separate steps, each only after the user agrees to it, because the user may want to keep the old story or skip the new one.

## Posting guidance

- `stories create` and `stories delete` act as the Page after the user approves the exact text, photo and IDs on an approval card. Run each requested write once. Each additional story the user names is a separate write with its own approval.

- A story appears publicly under the Page's name. Write only what the user asked the Page to say.

- A null `story_url` means Facebook returned no link for the story, so give the story ID instead of a link.

- HTTP 403 on any of these means the command is unavailable for this request. Say so without guessing a cause.
