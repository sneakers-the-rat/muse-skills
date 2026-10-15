# Map presentation

- Before creating a map, look up details for the chosen numeric place IDs as the [Places Search](/opt/hatch/connectors/places/CONNECTOR.md) connector docs describe.

- Use `widget.create_map_widget` with one `rich_place` element per place. Take `place_id`, the canonical `name` and `coordinate` from the same details record:

```json
{
  "elements": [
    {
      "kind": "rich_place",
      "place_id": "<numeric ID>",
      "name": "<name from the same record>",
      "coordinate": {"latitude": 0.0, "longitude": 0.0}
    }
  ]
}
```

- Put the places named in the text first, in the order they were named, then other relevant returned places that have an ID and coordinates. Omit any place whose details or coordinates are missing, and never infer an ID or geocode a name.

- Create one map per answer and present its returned embed once.

- If map creation fails, answer without a map. Do not retry or build an HTML or image map instead.
