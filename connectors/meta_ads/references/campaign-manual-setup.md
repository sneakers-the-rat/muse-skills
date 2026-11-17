# Set up the campaign in Ads Manager

Use this guide when the account can't be written to, or when the advertiser wants to build the campaign themselves. The account can't be written to when `ads_get_ad_accounts` lists it with `is_ads_mcp_write_disabled: true`, or when a write was rejected as unavailable for this ad account, whether a tool returned that here or the advertiser quotes it from an earlier attempt. This guide replaces creation, not planning: you still get the plan right while they do the clicking.

## When the account isn't eligible

This applies to the write-disabled flag or an account-level rejection, not to an advertiser who simply chose to build it themselves.

- Say it once, and lead with what you can do. Some ad accounts aren't yet eligible for Muse to create or change ads, and this is one of them. It's decided automatically, so there's nothing for them to fix, and you can still plan the whole campaign, write the ads, walk them through Ads Manager and read their account.

- Business verification, payment methods, admin roles and reconnecting don't change eligibility, and there's no onboarding step to complete. A missing payment method still stops delivery once they publish, so it's named as that, not as the cause.

- It isn't a failed request, and the plan isn't put on hold waiting for access.

## Plan in full, create nothing

- How the account is treated depends on how you got here:
  - With `is_ads_mcp_write_disabled: true` in the listing, say so before the plan, and treat the account as plan-only from the start.
  - After a tool returned the account-level rejection in this conversation, the account is plan-only for the rest of it: no writes and no creation approval.
  - When the advertiser quotes the rejection from an earlier attempt, it was true then, but eligibility can change and it may have been another account. It still applies only when this account's listing shows `is_ads_mcp_write_disabled: true`, not when the field is missing. Plan in full and offer both the setup guide and creating it here; if they choose creation, follow [preview](campaign-preview.md) and [execution](campaign-execution.md), where the first write either works or returns the rejection.
  - When the advertiser chose to build it themselves, the account can still be written to. No write is made for this campaign unless they ask, and any other write follows [write operations](writes.md).
- Reads still work, so the [campaign creation](campaign-creation.md) stages run as usual through the creative, and stop where the preview would begin. Nothing is described as created, staged or paused, because nothing exists until they publish it.

- If the rejection came at creation, the plan is already complete, and the setup guide follows in the same reply without replanning.

## Creative they can upload

- Each ad gets its finished main text, headline, description and button. A generated image is an asset they upload themselves, so say which ad it belongs to.

- Existing Page posts or account media are named with where to find them, not by ID.

## The setup guide

- One section per level, in the order Ads Manager builds a campaign: **Campaign**, then each **Ad set**, then each **Ad**. Each lists only the settings the plan decided, as the advertiser will see them, with the value to choose:
  - the campaign: its objective, name, any Special Ad Category, and whether the budget sits on the campaign
  - each ad set: its conversion location and performance goal, budget and schedule, locations, age, interests and languages by name, and placements
  - each ad: its Facebook Page and Instagram account, format, media, copy, destination link, and the dataset or pixel when the plan tracks conversions
- Settings use the names Ads Manager shows, as [metrics](metrics.md) describes, not API values or IDs. The guide gives setting names and values, not screens, menus or button positions you haven't seen.

- Spending starts when they publish, and accepting the Advantage+ defaults Ads Manager offers can change what the plan chose.

- Call `muse.create_options` before writing the reply, with what you can still do from here. Creating it for them is one of the options unless a write to this account was rejected in this conversation or the listing shows `is_ads_mcp_write_disabled: true`. The options token comes last.
