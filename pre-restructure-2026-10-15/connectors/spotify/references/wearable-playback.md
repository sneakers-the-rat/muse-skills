# Wearable playback

- Use this only for a spoken request on a call to start music, a podcast, an episode or an audiobook, when the device carrying the call lists `music_fulfillment` in its device catalog. For anything else, follow the [Spotify docs](../CONNECTOR.md).

- That device plays only Spotify. If the caller asks for another service or source, such as Apple Music, Audible or music stored on the device, say that only Spotify plays there for now, offer to play it on Spotify and run no command.

## Resolve the item

```sh
/opt/hatch/bin/spotify-api wearable-play --query "<name>" --content-type <kind>
```

- Put only the requested name in `--query`. That is the title alone, the artist alone for an artist-only request, or `<title> by <artist>` when the caller gives both. Leave out words such as "album", "playlist", "podcast", "episode" and "audiobook".

- Set `--content-type` to the kind the caller asked for, one of `song`, `artist`, `album`, `playlist`, `podcast`, `episode` or `audiobook`. It defaults to `song`, so set it for every other kind. An artist-only request uses `artist`.

- When the request names nothing to play, such as "play music" or "play Spotify", run `wearable-play --content-type saved_music` with no query instead of asking what to play. For the caller's liked songs, use `--content-type liked_songs`.

- Spotify's DJ is a playlist titled "DJ". For "play my DJ" or "play DJ", run `wearable-play --query "DJ" --content-type playlist`. Play the result only when its `body.title` is exactly "DJ". If it resolved to a playlist with another title, say DJ was not found, name that playlist, and ask before playing it. A `not_found` result follows Results in the Voice playback section of the [Spotify docs](../CONNECTOR.md), like any other missing item.

- Before saying a Spotify item can't play here, run the lookup, even when an earlier turn or a memory says it can't. Only a `not_found` result shows that. If the play fails, report the failure as Results says, without saying the item can't play.

## Play on the requested device

- If the caller named no device or clearly referred to the device carrying the call, such as "here", "on this device" or "these glasses", require `body.status` to be `wearable_play_resolved`. Call `device.invoke` on the device carrying the call, with `command` set to the returned `body.node_command` and `params_json` set to the returned `body.node_params`, both unchanged.

- Call `device.invoke` exactly once. If it fails or times out, report that. Do not retry, invoke another device or switch to `spotify-api play`, because playback may already have started on the device carrying the call.

- If the caller names a device other than the one carrying the call, such as a phone, speaker, TV, computer, car or console, even without a brand or name, run `spotify-api devices`. The same applies to "there" when it refers to a device mentioned earlier. Then play the resolved item on it:

```sh
/opt/hatch/bin/spotify-api play --context-uri <partner_uri> --target-device-id <id>
```

- Ask which device to use when none clearly matches.

- For a missing item, a failure or a success, follow Results in the Voice playback section of the [Spotify docs](../CONNECTOR.md).
