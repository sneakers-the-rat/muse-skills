# Music

## Find the right recording

- For an exact request, search by title and artist. Tell the original recording apart from a cover, live version, remaster or karaoke track, and respect the user's preference about explicit content.

- If the requested recording is unavailable, say so and offer a useful link or a clearly labeled alternative. Never substitute a cover or a different recording silently.

## Recommend music

- Start from the user's examples, mood or activity and explore a few directions. Explain the differences through actual tracks rather than genre labels.

- Mix familiar picks with a few adjacent styles rather than filling the list with near-duplicates.

## Build a playlist

- Read the existing playlist before adding to it, so you do not add duplicates. Keep the exact track IDs.

- Order the tracks for the mood, progression or activity the user described, such as a workout that builds or a dinner set that stays even.

- Read the playlist back after changing it and tell the user what was added.

## Start playback

- Play where the user is listening, using the playback route the connector docs give for this conversation and device, including calls and wearables.

- Confirm the track from the playback result or a check of what is playing. Do not send a second play command to verify the first.

- After an uncertain timeout, check what is playing before reporting a failure or repeating the action. Let the user choose another device rather than switching on their behalf.

## Available connectors

- [Spotify](/opt/hatch/connectors/spotify/CONNECTOR.md) for searching the catalog, editing the user's library and playlists and controlling playback on their devices.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [Apple Music](https://music.apple.com/), [YouTube Music](https://music.youtube.com/) and [Bandcamp](https://bandcamp.com/) carry recordings Spotify may lack. Bandcamp is strong for independent artists and for buying music directly from them.

- Regional services carry local releases that global catalogs miss, such as [Deezer](https://www.deezer.com/) in Europe and Latin America, [JioSaavn](https://www.jiosaavn.com/) in India and [Anghami](https://www.anghami.com/) in the Middle East.

- Ask the browser task for the exact version, its link and whether it plays in the user's region. A playable web link lets the user listen, but it does not let you control their speakers or edit their account on that service.

## Alternatives for better results

- Check the artist's official site or release notes when the version matters, such as a live recording versus the studio album.

- When playback cannot reach the intended device, offer a playable link or let the user choose an available device.
