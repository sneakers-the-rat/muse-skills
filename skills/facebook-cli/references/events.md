# Facebook events

## Search events

```sh
/opt/hatch/bin/facebook-cli events search
/opt/hatch/bin/facebook-cli events search --scope discover --keywords 'music' --limit 5
/opt/hatch/bin/facebook-cli events search --scope discover --location 'Seattle' --start-date 2026-07-31 --limit 5
/opt/hatch/bin/facebook-cli events search --scope discover --latitude 37.5072 --longitude=-122.2605 --radius-in-miles 5 --limit 5
/opt/hatch/bin/facebook-cli events search --scope discover --keywords 'music' --after '<cursor>'
```

- `--scope connected`, the default, returns only events the user is going to, interested in, invited to or hosting. These can include public events. Use `--scope discover` for public event discovery in or near a place. For the user's own events in a place, use connected and keep any requested date filters. Use `--location` to match venue text, or omit it and filter the returned `location` values when the place requires geographic interpretation. Follow `paging.cursors.after` with `--after` until no cursor remains before saying none match, or say the search covered only the pages read.

- `--keywords` takes free text such as `music` or `farmers market`. `--category` takes a category name such as `MUSIC_AND_AUDIO`.

- `--start-date` and `--end-date` take `YYYY-MM-DD` dates, and the start cannot be after the end.

- `--limit` defaults to 10, up to 25. Pass `paging.cursors.after` as `--after` for the next page. A cursor belongs to its scope, so never reuse it with another scope.

## Choose the search location

- With connected scope, `--location` filters venue text. Coordinates and radius do not turn it into a nearby public event search. With discover scope, `--latitude` and `--longitude` set an exact center and must be passed together. The pair overrides `--location`, and `--radius-in-miles` needs them, defaulting to 25 miles.

- For discover, `--location` takes a place name, which the server geocodes to a city center. It cannot express a neighborhood or an address.

- For discover, when the conversation already carries the user's coordinates, such as a `message_location` tag, pass them straight to `--latitude` and `--longitude` instead of turning them into a place name.

- For discover in a named neighborhood or address, get coordinates with `map.geocode`. A city name in `--location` is enough for a city-level request.

- If nothing establishes the location, ask the user. Discovery without a location falls back to a server-side guess, and the response never says which place it used.

- Pass a negative coordinate in either form, `--longitude -122.2605` or `--longitude=-122.2605`.

## Read event details

```sh
/opt/hatch/bin/facebook-cli events details --event-id '<event ID>'
```

- `--event-id` takes the numeric `id` from search results, which is also the number in the event's `permalink_url`.

- Search returns events in `data`. Each has `id`, `name`, `permalink_url` (always `https://www.facebook.com/events/<id>/`), `description`, `start_time` and `end_time` with an offset such as `2026-08-01T11:00:00-0400`, `location`, `category`, `going_count`, `interested_count`, `timezone`, `privacy` and `is_online`. Optional fields can be null.

- Only `events details` returns `online_url`, the third-party link where an online event is hosted, and it is null when there is none. Search results omit the key entirely.

- A malformed ID returns HTTP 400. A missing event and one the account cannot see both return HTTP 404, so the response cannot tell them apart.

- Give the event's link and its local start time in the answer.
