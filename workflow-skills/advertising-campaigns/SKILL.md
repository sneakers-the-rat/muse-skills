# Advertising Campaigns

## Start from the business result

- Identify the business, what is being advertised and the result the advertiser needs, such as sales, leads, bookings, messages, visits or awareness. Settle the destination, budget, schedule and geography before choosing any setting.

- Ask for missing facts about the offering together in one natural turn. Do not invent what the product is, what it costs or who it serves from the business category, an account name or an old campaign.

- For an existing campaign, read its current settings and recent results before proposing a change. The current request overrides older preferences, so an old budget, promotion or destination does not carry into a new campaign.

## Choose the channel and audience

- Choose the channel for where the audience is, what can be measured there and the expected cost. Search ads reach people already looking, social and video ads create demand, and professional networks reach business buyers.

- A connected ad account is not a reason to spend on that channel. Recommend the channel that fits the goal and say when another one would serve it better.

- Start from the people the advertiser actually serves. Never infer age, gender, interests or exclusions from the business type, and never assume a limit the advertiser has not stated, such as one location or a delivery radius.

- A business people visit, or one serving a local area, needs its real service area, such as the city, the neighborhood or a radius around the address. Confirm before treating a whole state, region or country as the audience.

- Check the platform's policy for regulated categories such as housing, employment, credit and financial services, and social-issue or political ads before planning targeting or copy. Classify by what is advertised, not by who the customers are.

## Explore ad ideas

- When the advertiser asks for ad ideas, they want possibilities to consider, not a finished ad. Offer a few ideas that are clearly different from each other. An idea can be a new direction or build on an ad they already run. Explain what is new about each idea and why it could be worth testing.

- Ground ideas in what you know about the business: the ads already running, how they performed, and the product details the advertiser gave or a source verified. When the grounding evidence is thin, say so and present the idea as something to try rather than a likely winner. Don't overpromise results.

- Images can help show an idea, but only once you understand what the advertiser is going for. When you don't yet know their creative direction, such as the look, what to show and what to avoid, ask before generating, because an image made on a guess is likely to miss. Preparing creative for approval and creating ads wait until the advertiser picks an idea.

## Plan the structure, creative and budget

- Give each campaign one objective. Separate ad sets only for real differences in budget, audience, geography, schedule or optimization, and use separate ads for different messages.

- Do not split a small budget into more ad sets or tests than it can support. Several ads in one ad set are not a controlled test, so use the platform's experiment tool when the advertiser needs a clean comparison.

- Check that the creative fits its placements, the landing page works and tracking can measure the result the campaign optimizes for. Do not promise purchase or application reporting when only visits can be measured.

- Every claim, price, offer and product detail in the copy traces to a fact the advertiser gave or a verified source, with their qualifiers kept. Approving a draft does not substantiate a claim.

- Take the budget amount and cadence from the advertiser or from a platform estimate they accept. Dividing a monthly total into a daily budget is a new decision, and an amount in another currency needs restating in the account's currency rather than converting from memory.

- When the advertiser's goal ends on a date, such as an event or a closing offer, settle an end date. A condition like "pause it once the flat is let" is a manual step the advertiser takes, so offer a date as a backstop.

## Get approval before anything spends

- Keep the approvals for the strategy, the creative, the paused campaign and publishing separate. Agreement to one never approves the next, and only publishing starts spending.

- Before publishing or raising a budget, state the objects, budget, schedule and audience in your own words. If a write returns an uncertain result, read the campaign before repeating anything.

- Do not set up recurring tasks or rules that change budgets, targeting, schedules or campaign status. Offer a recurring read-only report through `cron.add`, or a one-time approved change, instead.

## Evaluate results and recommend

- Use [performance analysis](references/analysis.md) to diagnose results and [presentation](references/presentation.md) to write the answer. Judge each campaign by the result its objective optimizes for, over a period long enough to mean something.

- Tie every recommendation to a figure you retrieved and to the advertiser's goal and budget, and show which changes the evidence supports and which are experiments. Stopping an unproductive expense is a valid recommendation.

- Change one meaningful factor at a time when you can, so the result stays interpretable. A competitor's public ad proves only that it ran, not that it worked.

## Available connectors

- [Meta Business Manager](/opt/hatch/connectors/meta_ads/CONNECTOR.md) for Facebook and Instagram campaigns, with account and performance reads, budget estimates, creative preparation, paused creation, policy checks and public Ad Library research.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- Use the Meta Business Manager connector by default for Meta Business backend operations. When the advertiser explicitly requests website execution for the current task, `browser.browse` may perform otherwise permitted operations, subject to the browser's privacy, security and approval requirements and any platform-specific restrictions. A connector failure is not permission to silently switch routes.

- Public web research and inspection outside the Meta Business backend, including the advertiser's landing page or checkout, remain allowed under policy, security and approval requirements.

- When connector access or a permitted capability is unavailable, explain the limitation. Unless the advertiser has explicitly requested a permitted website path, keep available, permitted reads in the connector and give instructions they can complete manually. Ground manual instructions in retrieved connector help, and say what could not be verified rather than inventing navigation steps or effects.

- Respect policy and security refusals and approval requirements. Do not achieve the blocked outcome through the browser, another connector, a script, or manual workaround instructions. Provide official recovery steps only when the service identifies them.

- If the ad account is unclear, ask the advertiser which account to use before making changes.

- When asking `browser.browse` to make an approved change, name the ad account and what to change, and pass along the advertiser's approved settings. Have it check the saved settings before you report completion.

- [Google Ads](https://ads.google.com/) for search, YouTube and shopping ads.

- [Microsoft Advertising](https://ads.microsoft.com/) for searchers on Bing and its partner sites.

- [LinkedIn Campaign Manager](https://www.linkedin.com/campaignmanager/) for professional audiences by job, industry and company.

- [TikTok Ads Manager](https://ads.tiktok.com/) for short vertical video.

- [Pinterest Ads](https://ads.pinterest.com/) for visual discovery and planning.

## Alternatives for better results

- Ask whether a better offer, a clearer landing page, outreach to existing customers or organic posting would solve the problem more cheaply than more ad spend.

- Ask for the advertiser's margin or target cost per result, so a recommendation can be judged on profit rather than on cheap clicks.

- Run a small, measured test before scaling, and decide from its results at a planned review date.

- For campaigns outside the US, check which platforms the local audience actually uses, such as LINE and Yahoo! JAPAN in Japan or Naver in South Korea.
