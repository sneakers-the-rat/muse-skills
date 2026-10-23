# Facebook timelines

```sh
/opt/hatch/bin/facebook-cli timeline fetch --profile-id '<profile ID from earlier output>'
/opt/hatch/bin/facebook-cli timeline fetch --profile-id '<profile ID from earlier output>' --limit 10 --after '<next_cursor>'
```

- `timeline fetch` reads the posts on an identified person's timeline. Pass only a profile ID returned earlier in this conversation, as [the connector doc](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) explains. For the user's own timeline, use `fb_user_id` from `me`.

- A page holds 20 posts by default, and larger `--limit` values are capped at 20. When `has_next_page` is true, pass `next_cursor` unchanged as `--after` for the same profile. `--cursor` is an alias.

## Read the response

- The output is a `social_posts_v1` collection. Read `posts[]` directly, without guessing another path or piping it through `jq`.

```json
{
  "format": "social_posts_v1",
  "count": 1,
  "posts": [{
    "rank": 1,
    "post_id": "pfbid02...",
    "url": "https://www.facebook.com/...",
    "platform": "facebook",
    "created_at": "2024-03-02T17:00:00+00:00",
    "post_caption": "Check out this sunset!",
    "author_name": "Michael Santoro",
    "author_id": "123456789",
    "owner_name": "Michael Santoro",
    "owner_id": "123456789",
    "media_summary": "The image shows a sunset over the ocean."
  }],
  "next_cursor": "...",
  "has_next_page": true
}
```

- Posts also carry `post_created_at` with the time in the user's timezone, plus media fields such as `media_summary`, `media_ocr` and `video_transcript` when available.

## Separate the author from the owner

- A timeline holds posts the owner wrote and posts other people wrote on the owner's wall. `author_id` equal to `owner_id` marks the owner's own post.

- When `author_id` differs from `owner_id`, say that `author_name` posted on `owner_name`'s wall. That post is not by the timeline owner.

- For "what has Alex posted" or "show me posts from Alex," report only posts where `author_id` equals `owner_id`. If there are none, say Alex hasn't posted recently, then mention separately that friends have posted on Alex's wall when they have.

- For "what's on Alex's timeline," show every post and label each one, such as "Posted by Alex" or "Sam posted on Alex's wall."

## Present the posts

- Present captions, media fields and activity summaries as [Reading posts](/opt/hatch/connectors/facebook_cli/references/reading-posts.md) describes, linking the specific posts behind each claim.

- If a page shows no posts by the person, say so for the period you inspected. A partial page does not establish that the person has stopped posting.
