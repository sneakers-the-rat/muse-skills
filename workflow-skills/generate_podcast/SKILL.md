# Podcast Production

## Plan the episode

- Use [Spoken Audio](/opt/muse/skills/spoken-audio/SKILL.md) for a voice message, narration for an artifact or a word-for-word reading. This skill covers composed episodes, briefings and narrated summaries.

- Settle the topic, the angle and who will listen before writing. Aim for 5 to 15 minutes unless the user asks otherwise. A spoken script runs about 130 words a minute.

- Read the catalog with `/opt/muse/skills/generate_podcast/scripts/podcast-helper manifest read` and look at each recent episode's `topics`. Choose fresh material or a new angle rather than covering the same ground again, which matters most in a recurring series.

- Research facts that change, such as news, scores or prices, when you produce the episode. Build it around one clear idea or progression rather than a list of facts.

## Cast the hosts

- Choose voices from `/opt/muse/assets/voice-selector/voice_source.json` and pass each entry's exact `id`. Default to the two Meta AI voices, `avocado_v2:MAI_01` and `avocado_v2:MAI_03`, and pick another catalog voice when the topic, a character or the user's request calls for it. Any number of speakers works.

- Call them the Meta AI voices or use their catalog display names with the user. Never say "MAI", which is only an ID prefix.

- Give each host a real first name, such as Alex or Jordan, chosen separately from the voice's display name. Keep each voice's host name stable by recording the pairing in `~/MEMORY.md` (for example, host Alex uses `avocado_v2:MAI_01`) and checking it before naming a host.

- Keep the same host names and voices in every episode of a series so it sounds like the same show.

## Write and produce

- Write the script for the ear, review it and save a topics summary, following [script writing](references/script.md).

- Generate the episode with the helper's `generate` command as described in [production](references/production.md), which also covers cover art, language and failed renders. Check the returned path and duration before delivering, and never deliver a partial episode.

## Deliver, publish or schedule

- Generation is private. Publish to the public RSS feed only when the user explicitly asks, or when the catalog already has an RSS feed (a `feed` with a non-empty `feed_url`) because the user published to it before. A `feed` that carries only `spotify_show_url` comes from a personal Spotify save and does not authorize publishing.

- Deliver the episode, publish it when authorized and schedule recurring episodes as described in [publishing and delivery](references/publishing.md). For a recurring request, deliver the first episode now and offer to publish it, then create the schedule.

- Save an episode to the user's own Spotify only when they explicitly ask, following [Save to Spotify](references/save-to-spotify.md). It is separate from RSS publishing.

## Available connectors

- [Spotify](/opt/hatch/connectors/spotify/CONNECTOR.md) for listing the user's Save to Spotify shows, checking an upload's processing and deleting a show or episode.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Descript](/opt/hatch/connectors/descript_mcp/CONNECTOR.md) for editing, exporting or publishing an existing Descript audio or video project.

- [Jellypod](/opt/hatch/connectors/jellypod_mcp/CONNECTOR.md) for producing episodes in the user's Jellypod account with its voices and characters.

## Websites

- [Apple Podcasts Connect](https://podcastsconnect.apple.com/) and [Spotify for Creators](https://creators.spotify.com/) list a published RSS feed in their public podcast directories, which the helper does not do. Submitting a feed happens in the user's own account and only at their request. Give the browser task the `feed_url` and show title, and have it report whether the listing was accepted.

## Alternatives for better results

- A short briefing often works better with one voice. Use two or more voices when their roles make the explanation easier to follow, within the format the user asked for.

- Offer the script as show notes or a transcript when listeners may want to check names, numbers or links.

- Use the user's own recordings or licensed material as inputs when they ask. Using them does not authorize publishing them publicly.
