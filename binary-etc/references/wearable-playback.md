`: those where the device carrying the call lists
`music_fulfillment` and the caller simply asks to play something by name, asks for a mood,
genre or activity, leaves the pick to you, or just asks for music, on that device, either on
Spotify or with no service named. For those requests, send
`device.invoke` with `music_fulfillment` to that device without reading the docs, passing only
`content_type`, `query` and, only when the caller gives both a title and an artist, `artist`
in `params_json`:

- Put only the requested name in `query`: the title alone, or just the artist for an
  artist-only request. When the caller gives both a title and an artist, put the artist in
  `artist`. Leave out words such as "album", "playlist", "podcast", "episode" and "audiobook".
- Set `content_type` to the kind the caller asked for, one of `song`, `artist`, `album`,
  `playlist`, `podcast`, `episode` or `audiobook`. It defaults to `song`, so set it for every
  other kind.
  An artist-only request sets `content_type` to `artist`, puts the artist in `query` and omits
  the `artist` field.
- When the caller just asks for music, such as "play music" or "play Spotify", set
  `content_type` to `saved_music` and omit `query`. For the caller's liked songs, set
  `content_type` to `liked_songs`. When `liked_songs_start.status` in the `device.invoke`
  result reports a failure, report it as a play failure, without retrying or switching
  devices.
- A request for a mood, genre or activity, such as "something mellow", "some jazz" or "music for
  my run", or an open one that leaves the pick to you, such as "something fresh", is also a named
  play: set `content_type` to `playlist` and put the few words that describe it in `query`, such
  as `mellow`, `jazz`, `running` or `fresh`. If that returns `not_found`, this is the one exception
  to the docs' rule to stop: pick a fitting playlist from the caller's library or one search, then
  play it with `wearable-play` and `device.invoke` as the docs describe, or say nothing fit and
  play nothing.
- For the latest episode of a named show or the latest album of a named artist, set
  `content_type` to `latest_episode` or `latest_album` and `query` to the show or the artist.
- Spotify's DJ is a playlist. For "play my DJ", "play DJ" or "play AI DJ", set `content_type`
  to `playlist` and `query` to `DJ`. A `not_found` result means the caller's Spotify account
  doesn't have DJ: relay its `message` and play nothing else.

Leave out the catalog's otherwise-required `action_name`, `partner_name` and `interaction_id`:
on this call the host supplies them, resolves the item and starts playback. A simple play needs
no other lookup, such as a memory search: send its `device.invoke` alone, as the only tool call
in its message.

That device plays only Spotify. If the caller asks for another service or source, such as Apple
Music, Audible or music stored on the device, say that only Spotify plays there for now, offer
to play it on Spotify and run no command.

For every other request, even one like a request you handled earlier in this conversation,
don't use the named play: an episode picked by its number, new releases with no show or artist
named (such as "the latest drop"), a request with conditions such as length,
tempo or no explicit songs, anything identifiable only from
memory or earlier conversation, or multiple actions in one request. For those, read the Spotify
connector doc's Voice playback section and follow it before running any playback command. For
each of these that starts new music, a podcast or an audiobook, if the device carrying the call
lists `music_fulfillment`, read `