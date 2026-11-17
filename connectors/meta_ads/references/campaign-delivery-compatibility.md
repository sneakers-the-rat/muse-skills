# Keep campaign settings compatible

Each ad set's outcome, objective, optimization goal, destination, tracking signal or promoted object, and billing event are one decision. A setting that's valid on its own can still make an invalid campaign with the others, so the decision is settled only when they all fit:

- the objective supports the optimization goal

- the destination can produce the event being optimized

- every Page, form, messaging account, dataset or pixel, and event it needs was returned for this account and fits its role

- the promoted object has exactly the fields the goal and destination need

- the billing event, budget and bid level work with the same setup

No tool lists an account's apps, so a Meta app ID, which differs from the store's numeric ID, and the store link come from the advertiser or an existing ad set's promoted object. The live schema wins when it differs from this guide. A conflict the advertiser has to choose between is a [binding constraint](campaign-planning.md#binding-constraints).

## Match the setup to the outcome

Codes stay in arguments; replies use plain names.

- Awareness or reach: `OUTCOME_AWARENESS` with `REACH`, `IMPRESSIONS` or another supported awareness goal.

- Website visits: `OUTCOME_TRAFFIC` with `LANDING_PAGE_VIEWS` or `LINK_CLICKS`, a verified website link, and only the tracking fields that goal supports.

- Website purchases or conversion value: `OUTCOME_SALES` with `OFFSITE_CONVERSIONS` or `VALUE`, a website destination, and a returned conversion source with a supported event, sent as the promoted object's `pixel_id` and `custom_event_type`.

- Website leads: `OUTCOME_LEADS` with `OFFSITE_CONVERSIONS`, a website destination, and a returned conversion source with the lead event, sent the same way.

- Instant-form leads: `OUTCOME_LEADS` with `LEAD_GENERATION` or `QUALITY_LEAD`, an on-ad destination, and a returned Page with `leadgen_tos_accepted` true as the promoted object's `page_id`, since lead ads run only on Pages that accepted the Lead Ads terms. The form belongs to the creative, not the promoted object.

- Messaging conversations: an objective matching the outcome with `CONVERSATIONS`, the ad set's `destination_type` set to Messenger, WhatsApp or Instagram Direct, and the returned account for that channel. Only WhatsApp works under `OUTCOME_LEADS`. The creative uses the channel's button and link from [message ads](campaign-execution.md#message-ads).

- Page likes: `OUTCOME_ENGAGEMENT` with `PAGE_LIKES`, the Page destination and the returned Page, usually billed on impressions.

- Post engagement: `OUTCOME_ENGAGEMENT` with `POST_ENGAGEMENT`, an on-post destination, and the returned Page and post or a supported new ad.

- Profile visits: `OUTCOME_TRAFFIC` with `VISIT_INSTAGRAM_PROFILE` or `PROFILE_VISIT` and the matching returned profile.

- Video views: `OUTCOME_AWARENESS` or `OUTCOME_ENGAGEMENT` with a supported video-view goal and destination.

- App installs or app events: `OUTCOME_APP_PROMOTION` with an app goal, an app destination, and the advertiser's app ID and store link or event.

- Calls: an objective matching the outcome with a supported call goal, a phone destination, and the returned Page and number.

A combination outside this list, or one gated by account, is settled only when current tool evidence supports the whole combination and its inputs. A field appearing in a schema doesn't prove every combination using it works.

## Rules the fields don't show

These pass every field check and are still rejected:

- Under a campaign budget with lowest-cost bidding, every ad set uses the same optimization goal, including one added later. A different goal needs its own campaign. Adding an ad set to an existing campaign starts by reading its ad sets' goal and its budget.

- A lifetime budget, on the ad set or its campaign, needs the ad set to end more than 24 hours after it starts. A lifetime budget without an end date gets one from the advertiser; it isn't switched to daily.

- An app ad targets the app's operating system: iOS for an App Store app, Android for a Google Play app, with the value from the live schema or a targeting search.

- The conversion event has to fit the objective, as the list above pairs them. When Meta rejects the event, offer one the objective supports or a new campaign with the matching objective.

- iOS 14 attribution needs a matching campaign. The ad set's `campaign_attribution` (`SKAN` or `AEM`) goes only under a campaign created here with `is_skadnetwork_attribution: true`, or one the advertiser says is an iOS 14 campaign. Reads can't show an existing campaign's iOS 14 setting, so otherwise it's left out.
