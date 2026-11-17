# Hand off the created campaign

## While paused

- After the campaign is created, and after each edit while it's still paused, show the Ads Manager card. Run `meta-ads-cli render-campaign-success --success-json` with exactly `campaign_name`, whole numbers `ad_set_count` and `ad_count`, and the returned HTTPS Ads Manager link as `ads_manager_url` when there is one. If the renderer rejects the link, leave it out and the card uses the standard link. Pass the returned widget's `data` unchanged to `widget.create_list_widget`.

- Then call `muse.create_options`, with `Publish it so it can start spending at <budget and schedule>` first, then up to three paused edits the live tools and prerequisites support. Leaving the options untouched keeps the campaign paused, so there's no option to keep it paused. Make both calls before writing the reply.

- The reply should be one short sentence that names the campaign and says it's paused, so nothing spends until it's published, or says what changed after an edit. The card goes on its own line below it, followed by the options.

## Publish

- Publishing is a new request to spend money, with its own approval, following [write operations](writes.md). The objects and the spending effect are stated before approval.

- It turns the campaign on with `ads_activate_entity`, which changes each object from paused to active. Each level is activated separately, top down: the campaign, then each ad set, then each ad.

- When every call returns `ACTIVE`, the campaign is on.
