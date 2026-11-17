# Create a complete Meta campaign

Use this guide to create a complete Meta Ads campaign, from planning to the created campaign. The stages below are the usual order, but you can start at whichever stage the request needs, and stages the conversation already settled stay settled. The last three, preview, creation and handoff, almost always happen. A request for a plan only stops once the strategy is approved, and an account that can't be changed goes to [manual setup](campaign-manual-setup.md) instead.

## Stages

Before each stage, you should read its guide.

1. **Account and identity:** the ad account, Page and Instagram account, as [identity](campaign-planning.md#resolve-identity) and [account scope](account-scope.md) describe.
2. **Research and planning:** the campaign brief and the recommended strategy, in [planning](campaign-planning.md), with [targeting](campaign-targeting.md) for places, interests and languages, [delivery compatibility](campaign-delivery-compatibility.md) for the objective, goal and destination, and [budget](campaign-budget.md) for pricing.
3. **Creative:** the image or video, text and buttons, in [creative](campaign-creative.md), with [creative generation](campaign-creative-generation.md) for generated media.
4. **Preview:** the campaign the advertiser approves before it's created, in [preview](campaign-preview.md).
5. **Creation:** creating the campaign paused, in [execution](campaign-execution.md).
6. **Handoff:** where the campaign stands and what the advertiser can do next, in [handoff](campaign-handoff.md).

Adding one ad or ad set to an existing campaign is a standalone change under [write operations](writes.md).

## Throughout

- Call `muse.create_options`, and any widget, before writing the message that shows them, with the options token last, as the [connector guide](../CONNECTOR.md) describes.
