# Publish and deliver an episode

## Deliver the episode

- Put the title as plain text above the playable link:

```text
{title}
[{title}](sandbox://workspace/podcasts/{slug}/{slug}.mp3)
```

- After delivering, offer what applies:
  - When the episode is not published and was not blocked, offer a personal podcast feed. It is an RSS feed the user can add to Apple Podcasts, Overcast, Pocket Casts or most other podcast players, and future published episodes appear there automatically. Published episodes are public, so anyone with the link can listen.

  - When no schedule exists, offer a new episode on a regular schedule, such as every morning.

- The first time a feed comes up in a conversation, explain it in a sentence as above. Use shorter wording after that.

- When the user asks to hear their podcast or asks about their episodes, read the catalog and give each relevant episode's listen link in the format above. Add the subscription links when its feed is published.

## Choose the feed

- Keep one feed unless the user asks for a separate show. Run `manifest read` before publishing: `feeds` lists every show and `feed` is the one published most recently. When either has a non-empty `feed_url`, reuse that feed's `feed_title` exactly.

- The feed title picks the show. A title that matches an existing feed adds to it and any other title creates a new feed, so reuse a title character for character and never reuse one for a different show.

- For the first feed, choose a title from the name the user gave Muse, such as "Today with Alex".

## Publish

- Publish an episode generated without `--publish`:

```sh
/opt/muse/skills/generate_podcast/scripts/podcast-helper publish \
  --slug <slug> \
  --feed-title "Today with Alex" \
  --feed-description "Daily news and tech updates"
```

- It prints `feed_url`, `episode_url` and `subscription_links`. The helper refuses an episode that is already published, because publishing appends a new entry and would duplicate the episode in every subscriber's feed.

- A publish that brings a new show cover replaces the covers of that feed's episodes in the catalog. A series show keeps its series cover, and an episode changed with `update-cover` keeps the show's existing cover when published. Other feeds keep their own artwork.

## Handle a refused publication

- Public publishing goes through a content review. A result with `"blocked": true` was not published. Relay its `error` plainly and stop, without retrying, rewording the script or trying another way to publish. The local audio and catalog entry remain, and saving to the user's own Spotify is not affected by this review.

- A result with `"retryable": true` means the review could not run. Tell the user publication can be retried later with the `publish` command above, reusing the feed's exact `feed_title`.

- When `generate --publish` returns `published: false` with `publish_error`, the audio was generated but publication failed. Relay the error and do not say the episode reached the feed.

## Present published links

- After publishing, show the listen link again. Confirm in plain words that the episode is on the user's personal feed, the RSS feed they subscribe to in a podcast app, and that published episodes are public, so anyone with the feed link can listen.

- On the first episode published to a feed, present the subscription links from the result. Skip them for later episodes in the same feed.

```text
Subscribe to your personal feed:

RSS feed URL (copy and paste into any podcast player):
`{subscription_links.rss}`

Or open directly in a podcast app:

- [Open in Apple Podcasts]({subscription_links.apple_podcasts})

- [Open in Overcast]({subscription_links.overcast})

- [Open in Pocket Casts]({subscription_links.pocket_casts})
```

- Show every published `https://` URL, such as the feed or an episode, as copyable code in backticks. Never show it as a bare URL or a `[label](https://...)` link, because native clients may fail to open it and the user should copy it. Do not offer direct episode download links.

- Only `sandbox://` listen links and the podcast-app links (`podcast://`, `overcast://`, `pktc://`) may be clickable.

## Schedule a series

- Create one job with `cron.add`, giving it a kebab-case `id`, `mode: task`, `enabled: true`, `predicted_connector_permissions` (`[]` when the run uses no connector), a recurring `schedule` and `timeout_secs: 1800` so a run has time to research, synthesize and publish. Report the effective timeout that `cron.add` returns.

- Write a body that stands on its own, because the run cannot see this conversation. Include:
  - the topic, the angle and a reminder to research live sources when the episode is produced

  - the fixed cast, with each host's name and `--speaker` voice ID

  - `--series-id` set to the job ID, and a `--cover-prompt`

  - reading `manifest read` topics first to avoid repeats, then writing and passing a `--topics-file`

  - whether to publish, and the exact feed title when publishing is authorized

```json
{
  "id": "daily-tides-podcast",
  "title": "Daily tides podcast",
  "mode": "task",
  "enabled": true,
  "predicted_connector_permissions": [],
  "timeout_secs": 1800,
  "schedule": {"kind": "daily", "time": "07:00"},
  "body": "Produce today's episode of the tides podcast with the Podcast Production skill. Research today's tide and weather news first. Keep the cast: Alex (--speaker Alex=avocado_v2:MAI_01) and Jordan (--speaker Jordan=avocado_v2:MAI_03). Run manifest read and avoid topics earlier episodes covered. Use --series-id daily-tides-podcast and --cover-prompt 'ocean tides at sunrise', and pass a short topics summary with --topics-file. Publish to the feed titled 'Tides with Alex'."
}
```

- A scheduled run follows its body. When the body says to publish, the run publishes without asking again.
