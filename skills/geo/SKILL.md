# Place Discovery

## Find places that fit

- Establish the area the task concerns, which is the trip destination when the user is planning travel. Then settle the travel range, timing and the needs that decide the choice, using known context for simple assumptions.

- Search for candidates with a place search, following the [Places Search](/opt/hatch/connectors/places/CONNECTOR.md) connector docs. `map.geocode` turns an address into coordinates, `map.reverse_geocode` names a coordinate and `map.navigation` plans a route, but none of them chooses a suitable place or establishes its hours.

- Judge the results instead of following their rank. Set aside wrong-category, wrong-area and closed places unless the user asked about them, and search again with an exact name, a narrower type or clearer area when the set is weak.

- Name only places that came back from a tool. Identify each branch by its exact address.

- Check current hours, services and any important accessibility feature in the place's details or on its own site. Opening hours do not establish that a table can be booked, and a high rating does not establish suitability.

## Present a useful choice

- For a recommendation, name two or three places. For a broad request, name a few as a starting point. Open with one short framing line, then put each place on its own line as the bold name followed by a sentence on why it fits. When every named place has a comparable `avg_rating`, order them highest first.

- Show one map whenever a chosen place has a place ID and coordinates, even for a single named place, following [map presentation](references/map-presentation.md). The map card carries each place's address, rating, price level and photos, so keep those, IDs and coordinates out of the text, and do not narrate the map. Send the answer as one message with nothing after the map.

- When no map can be shown, give each place's verified address and only a link a tool returned for it, such as its website or a returned maps URL. Never build a link or write your own turn-by-turn directions.

- For directions, routes or travel times, use `map.navigation` instead of a place map, and never estimate a distance or travel time.

- After a recommendation, mention that more options exist. After a broad answer, offer to narrow it down. If the user wants a reservation, pass the place and their constraints to the relevant booking skill.

## Available connectors

- [Places Search](/opt/hatch/connectors/places/CONNECTOR.md) for place search results, rich details, photos and identifying a place from a photo.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [HasData](/opt/hatch/connectors/hasdata_mcp/CONNECTOR.md) for Google Maps, Yelp and Yellow Pages listings and reviews as data.

## Websites

- Use `browser.browse` to check a place's own site for current hours, menus, services or booking options when the decision depends on them.

- [Google Maps](https://maps.google.com/), [Apple Maps](https://maps.apple.com/) and [Tripadvisor](https://www.tripadvisor.com/) add details and reviews almost everywhere. [Yelp](https://www.yelp.com/) is useful where it has local coverage, such as the US and Canada.

- Use the platforms locals use where global maps are thin, such as [Naver Map](https://map.naver.com/) in South Korea, [Baidu Maps](https://map.baidu.com/) in mainland China and [Tabelog](https://tabelog.com/en/) for restaurants in Japan.

## Alternatives for better results

- Search with local place names and in the local language when it improves coverage.

- Consider a neighboring area or another type of place when it meets the need better, weighing the journey, likely spend and the experience the user wants.

- Read recent reviews for noise, crowds or accessibility when they matter, while relying on the place itself for current hours.
