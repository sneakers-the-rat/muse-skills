# Preview the campaign before creating it

- You should show the preview only when every create tool is listed. If one is missing, you should tell the advertiser creation isn't available instead.

- `meta-ads-cli render-campaign-summary --summary-json` takes exactly these keys: `campaign_name`, `goal`, `optimization`, `destination`, `structure` (with whole numbers `ad_set_count` and `ad_count`), `budget`, `schedule`, `audience_and_geography`, `audience_description` and `placements`. The values describe the approved plan without adding or leaving out an important setting. Creative, ad category and paused state were reviewed earlier.

- `schedule` has `start` as `after_publishing` or `scheduled`, and `end` as `no_end` or `scheduled`. A scheduled start or end adds `start_time` or `end_time` as a real date or time.

- `placements` has one `mode`: `automatic`, `platform_restricted` with `platforms`, or `manual` with `positions`.

- Render the preview and pass its widget `data` unchanged to `widget.create_html_file_widget`, then call `muse.create_options` with `Yes, create paused campaign` and `No, make changes`. Make both calls before writing the reply.

- The reply places the preview's `embed_token`, then the question "Proceed with this campaign? It will be created paused. After success I'll give you a direct Ads Manager link.", then the options' `embed_token`, so the card comes first and the buttons last. The reply contains only the card, the question and the buttons.

- Tapping yes, or clearly typing yes to the same campaign, approves it. A yes to anything else doesn't. If something changes after approval, show a new preview. Once approved, create it as [execution](campaign-execution.md) describes.
