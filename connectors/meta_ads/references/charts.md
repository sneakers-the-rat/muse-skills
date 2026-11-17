# Meta Ads chart renderer

- `render-chart` draws a line or bar chart locally from returned figures and writes it to a file. Never write chart HTML or SVG yourself.

```sh
/opt/hatch/bin/meta-ads-cli render-chart --chart-json '<json-object>'
```

- `--out-dir` defaults to `workspace/charts`. Never set it to `workspace/your_files`, because chart widgets reject paths in the Library.

## Build the chart object

- The object accepts exactly these keys and rejects any other:
  - `type`, either `line` for a trend or `bar` for comparing periods
  - `title`, naming the object and period as a table caption would, up to 200 characters
  - `metric`, up to 40 characters, and `unit`, one of `currency`, `percent` or `number`
  - `currency`, the account's three-letter ISO code, required with `unit` `currency` and rejected otherwise
  - `x_labels`, 2 to 92 labels of up to 16 characters each
  - `series`, 1 to 8 objects of `{name, values}`, with one value per label and `name` required when there are two or more
  - `reference`, optional, as `{label, value}`

- Each value is the tool's own number as a string, copied exactly without a currency symbol, such as `"1234.50"`. A period with no data is `null`, never `0`, and a series with no values at all is left out.

- Use `reference` only for a returned value, such as the prior period or the advertiser's own target, never an invented benchmark.

## Show the chart

- The command returns a `widget` object whose `kind` is `html_file` and whose `data` holds `path` and `fallback_text`, plus a `full_view` object with its own `path`. Pass that `data` object unchanged as the arguments of `widget.create_html_file_widget`, and never put the full-view path, an image link or a second link to the chart in the answer.

- Make both calls before writing the answer, then place the returned `embed_token` on its own line where the chart belongs. An unplaced token shows nothing, so never describe a chart whose token you did not place.

- One question gets one chart with nothing beside it. When more objects qualify than eight series hold, plot the leading eight on the measure asked about and say how many you plotted out of how many.

- Correct only an input error the renderer reports. If it still fails, or the widget fails, give the figures in a list or table, say once that the chart could not be shown and do not retry.

## Performance-trend report card

- `ads_insights_performance_trend` renders its own interactive report card. On success the tool result already includes a `sandbox_link` (a `sandbox://workspace/.ads-performance/…html` path) and a `_present_ads_performance_card` directive — the report file has already been written for you.
- To show the card, place that `sandbox_link` on its own line as a Markdown link, e.g. `[Ad performance trend](sandbox://workspace/.ads-performance/…html)`. That line becomes the interactive card (the ad table that expands into per-ad metric tiles and a trend chart). Do not call `render-chart`, `widget.create_html_file_widget`, or `render-performance-trend` for the same data, and do not write the card's HTML yourself.
- The card already shows every ad's metric tiles, trend charts, status, objective and percent changes. Do not restate that data in prose — no summary table, no per-ad metric list, no repeating each percent change. Below the card, add a short takeaway (you may cite the single most important figure) and one next step.
- If the result has no `sandbox_link` (older data or a render error), fall back to the analytical-answer rules in [metrics](metrics.md): give the decisive figures in prose and do not retry the card.
