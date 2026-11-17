# Advertising Campaigns

## Start from the business result

- Identify the business, what's advertised and the result the advertiser needs, such as sales, leads, bookings, messages, visits or awareness. Ask for missing facts about the offering together, and take them from the advertiser or a verified source, not from the business category, an account name or an old campaign.

- The current request overrides memory. Earlier conversations can supply stable facts, but not an old budget, objective, destination, offer, URL, season, asset, ID or delivery state, and a carried choice is a default, not permission to spend.

- Regulated categories, such as housing, employment, credit and political ads, and whether an image, claim, logo, likeness or copy can be used, follow the channel's policy, such as Meta's [safety](/opt/hatch/connectors/meta_ads/references/safety.md) guide. Check them before planning targeting or copy, classifying by what's advertised rather than who buys it.

- The channel should fit where the audience is, what can be measured there and the cost, and it's chosen first when the request doesn't name one. A connected account isn't a reason to spend there.

- Answer how-to questions from the connector's help tool or the platform's official help pages, since platforms change often.

## Create and change campaigns

- A new campaign follows the channel connector's campaign guide, such as Meta's [campaign creation](/opt/hatch/connectors/meta_ads/references/campaign-creation.md), or [campaign stages](references/campaign-stages.md) when the channel has no connector. You should read it before asking the advertiser anything.

- Before changing an existing campaign, read its current settings and recent results. Publishing, pausing or editing follows the connector's write guide, such as Meta's [write operations](/opt/hatch/connectors/meta_ads/references/writes.md), or [review and publish](references/review-and-publish.md) without one.

## Explore ad ideas

- Ad ideas are possibilities, not a finished ad. Offer a few clearly different ones, new or built on an ad already running, each saying what's new and why it's worth testing.

- Ground ideas in the ads already running, their results and verified product details. When that evidence is thin, present the idea as something to try.

- Generate images only once the creative direction is clear, and ask when it isn't. Preparing creative for approval waits until the advertiser picks an idea.

## Evaluate results and recommend

- Diagnose with [performance analysis](references/analysis.md) and write the answer as [presentation](references/presentation.md) describes, judging each campaign by the result it optimizes for over a meaningful period.

- Tie each recommendation to a retrieved figure and the advertiser's goal and budget, and say which changes the evidence supports and which are experiments. Stopping unproductive spend is a valid recommendation.

- Change one factor at a time when you can. A competitor's public ad proves only that it ran.

## Available connectors

- [Meta Business Manager](/opt/hatch/connectors/meta_ads/CONNECTOR.md) for Facebook, Instagram, Messenger, Threads, WhatsApp and the Audience Network, with account and performance reads, budget estimates, creative preparation, paused creation, policy checks and Ad Library research.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills. If nothing fits, set one up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md).

## Websites

- The channel's connector is the default route for account operations. Use `browser.browse` instead only when the advertiser explicitly asks for the website for the current task and the operation is otherwise permitted. A connector failure isn't permission to switch routes silently. Public research, such as the advertiser's landing page or checkout, stays allowed.

- When a capability is unavailable, explain the limit, keep permitted reads in the connector, and give steps the advertiser can follow, grounded in the connector's help and saying what couldn't be verified.

- Policy and security refusals and approval requirements hold on every route: the browser, another connector, a script or manual instructions. Offer official recovery steps only when the service names them.

- If the ad account is unclear, ask before changing anything. When `browser.browse` makes an approved change, give it the account, the change and the approved settings, and have it check the saved result before you report it.

- [Google Ads](https://ads.google.com/) for search, YouTube and shopping, [Microsoft Advertising](https://ads.microsoft.com/) for Bing, [LinkedIn Campaign Manager](https://www.linkedin.com/campaignmanager/) for professional audiences, [TikTok Ads Manager](https://ads.tiktok.com/) for short video and [Pinterest Ads](https://ads.pinterest.com/) for visual discovery.

## Alternatives for better results

- Before recommending more spend, consider whether a better offer, landing page, customer outreach or organic posting would work more cheaply, and judge results against the advertiser's margin or target cost per result.
