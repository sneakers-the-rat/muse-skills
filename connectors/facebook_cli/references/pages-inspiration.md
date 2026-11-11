# Page posting inspiration

- These commands recommend when a Page the user manages should post and what it could post, from Facebook's data on its audience and niche.

- Decline a request to pass off another creator's post as the Page's own or to pose as that creator, to strip copyright or attribution from a track or post, to promote the Page with a disaster or death, or to make fake news from a trend, before running any command or search, including `pages list`, because any lookup already starts the task.

- Before running any command here, choose the Page with the steps in [Facebook Pages](/opt/hatch/connectors/facebook_cli/references/pages.md), because they ask which Page the user means when more than one could match.

- Run these commands yourself when the user asks about the Page's best time to post, content ideas, trends or examples from its niche, because `social.search`, `browser.search` and subagents return public posts or web advice instead.

## Commands

```sh
/opt/hatch/bin/facebook-cli pages inspiration best-time --page-id '<page_id>'
```

- `pages inspiration best-time` recommends when the Page should post, from when its audience is most active or when its past posts got more views.

```sh
/opt/hatch/bin/facebook-cli pages inspiration content-ideas --page-id '<page_id>' [--limit <1 to 10, default 5>]
```

- `pages inspiration content-ideas` suggests post ideas, drawn from recent posts by similar creators.

```sh
/opt/hatch/bin/facebook-cli pages inspiration trending-topics --page-id '<page_id>'
```

- `pages inspiration trending-topics` lists topics trending on Facebook, ranked for the Page's niche when Facebook has a niche for it.

```sh
/opt/hatch/bin/facebook-cli pages inspiration trending-audio --page-id '<page_id>'
```

- `pages inspiration trending-audio` lists audio tracks trending on Facebook.

```sh
/opt/hatch/bin/facebook-cli pages inspiration niche --page-id '<page_id>' --recommendation-type <top_content or top_creators> [--limit <1 to 10 for top_content, 1 to 5 for top_creators, default 5>]
```

- `pages inspiration niche` shows top posts (`top_content`) or top creators (`top_creators`) in the Page's niche, as examples to learn from.

## Read the results

- `best-time` returns `recommended_time`, `timezone`, `effective_window` and `source`. Give the time with its timezone and window, and say in plain words what it's based on. `ml_fan_activity` means when the audience is most active, and `past_post_performance` means when past posts got more views.

- An unavailable `best-time` carries a `reason`, which takes the place of a recommended time.

- Run `best-time` once per Page for each request, because a second run returns the same recommendation.

- `content-ideas`, `trending-topics`, `trending-audio` and `niche` return a plain-language answer in `text` or structured results in `data`.

- Content ideas and niche results come from other creators, not from the Page's own posts.

- `niche --recommendation-type top_content` returns only `post_ids`, with no post text, creators, counts or links. Report how many posts Facebook recommended and give their IDs. Don't describe the posts or name creators, follower counts or links, because nothing returned says who made them or what they show.

- When the user asks for more ideas, posts or creators than a command's `--limit` allows, run it once at the maximum. Report how many Facebook returned and that it returns no more per request, and don't pad the list with results from other commands or ideas of your own, because the user asked for Facebook's results.

- Name trending tracks and artists exactly as returned.
