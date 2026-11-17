# Plan a complete Meta campaign

Planning turns the request into a strategy the advertiser approves.

- Use this full-research path by default. If the advertiser asks to go step by step, ask about one setting per turn with your recommendation, and price the whole plan once, at the end, as [campaign budget](campaign-budget.md) describes. Planning then ends in a budget choice rather than the complete plan: `Use <amount>` (or `Keep <amount>` when it's their amount) and `Change the budget`. The checks below still apply. [Account scope](account-scope.md) and [evidence](evidence.md) apply throughout.

- A plan-only request still gets the full research; it just doesn't create anything.

- Facts about the offering come from the advertiser or a verified source, not from the business category, an account name, an old campaign or memory. When some are missing, you should ask for them together before recommending a strategy.

- The strategy rests on what the Ads tools return. Before you recommend it, these results come back:
  1. the ad account, the Page and the Instagram account
  2. the account context and the matching past campaigns
  3. the tracking sources from `ads_get_datasets`
  4. the targeting search results for each location, interest or audience in the plan
  5. the `ads_policy_tool` result for each Special Ad Category or regulated topic in the plan
  6. the budget estimate for the final structure

## Resolve identity

The campaign uses one ad account and one Page returned for this advertiser, plus their Instagram account if they have one.

- The ad account is chosen as [account scope](account-scope.md) describes. With none available, the plan continues without Ads Manager creation and says so.

- The Page is the advertiser's choice or the one clear match among the account's Pages; several plausible ones are the advertiser's choice. Tools: `ads_get_ad_account_pages`.

- A Page name that differs materially from the destination brand is confirmed with the advertiser, with options to use that Page or choose another; cosmetic differences pass.

- The account's list holds its promoted Pages, not every Page the advertiser can use, since a creative accepts any Page they hold advertising rights to. An empty or unmatched list widens to `ads_get_user_pages`, or `ads_get_pages_for_business` with a returned business ID, and isn't something for the advertiser to fix.

- Instagram ads should use an account `ads_get_ig_accounts` returns for this ad account. If none comes back, they can still run under the Page's name and picture.

## Settle the strategy

The three groups below are settled in order, each narrowing the next.

- Account context comes first: `ads_insights_advertiser_context` when available, and `ads_get_ad_entities` history when that summary is absent, misses a fact that could change a decision, or the request names an object. You look at past campaigns that match the product, objective, destination, audience type and season.

- Conflicts resolve by compliance first, then the advertiser's explicit preference, compatible first-party evidence and safe Advantage+ defaults.

### What the campaign gets

#### Destination

Where people go after tapping the ad: a website, an app, an instant form, a messaging app, a phone call, or a Meta Page, profile, post or video.

- What it needs exists for this account: a verified URL, a Page that accepted lead terms, a connected Instagram or WhatsApp account, a phone number, or the app ID and store link. Tools: `ads_get_ad_account_pages`, `ads_get_ig_accounts`.

- Messaging can span several apps.

#### Signals and tracking

- Lead forms, messaging, calls, engagement, profile visits and video views are measured on Meta.

- A website or app result is measurable when a conversion source has received that event recently. If none has, that's a [binding constraint](#binding-constraints), and you can offer something Meta does measure instead, such as page visits. Tools: `ads_get_datasets`, `ads_get_dataset_details`, `ads_get_dataset_stats`, `ads_get_customconversions`.

- Quality-lead optimization depends on CRM outcomes reaching Meta.

#### Objective and optimization

The objective is the campaign's business goal: awareness, traffic, engagement, leads, app promotion or sales. The optimization goal is the result each ad set asks Meta to get the most of.

- Each campaign has one objective. Under a campaign budget, the optimization goal is fixed once ads run.

The whole combination passes [delivery compatibility](campaign-delivery-compatibility.md) before it's priced or recommended.

### Who sees it

The audience is the people the advertiser actually serves, in the places they serve, within any Special Ad Category's limits.

#### Compliance

The campaign's Special Ad Category matches what is advertised, judged by the offer, not the customers.

- The categories are housing (including mortgages and home loans), employment, financial products and services, social issues, elections or politics, and online gambling and gaming, scoped as [safety](safety.md) describes. A financial offer needs its category when the advertiser or audience is in the United States.

- The category applies to every country the ads target.

- Social issues, elections or politics needs the advertiser and Page authorized in each country, runs in its own campaign and is unavailable in the European Union.

- Other regulated topics, such as alcohol, healthcare or pharmaceuticals, follow Meta's policy, checked with `ads_policy_tool` when a planned setting depends on it.

- When a category applies, the plan names it and what it changes; otherwise the campaign declares none without mentioning it.

#### Geography and audience

- A business people visit, or one serving a local area, targets its real service area: a city with a 10–50 mile radius, a neighborhood, or a radius of about 1–50 miles around the address. A whole state, region or country is confirmed with the advertiser. Location targeting reaches people who live in or were recently in the area.

- Advantage+ Audience is on by default: location, a minimum age up to 25, language and exclusions stay fixed, while age, gender, interests and custom audiences are suggestions Meta can go beyond, so two or three interests the business supports are enough. Turning it off, for a stricter age range or narrowing the advertiser asks for, makes those settings limits; housing, employment and financial products and services restrict them further, as [safety](safety.md) describes.

- Places, interests and languages come from one [targeting](campaign-targeting.md) search, and country codes can be used as they are. If the search finds only some of the places, keep those and ask the advertiser about the rest. Hold off on the estimate until they answer, since pricing only what was found assumes the missing place is dropped. A missing place shouldn't be swapped for a nearby one, widened or dropped.

- An existing custom audience fits when the request or account points to it and it's ready to use; Meta blocks flagged audiences and expires ones unused for two years. Tools: `ads_get_ad_account_custom_audiences`, `ads_get_custom_audience`.

- The plan describes the audience only as its targeting encodes it; personas shape the creative, not the targeting.

### How it delivers and spends

Structure, placements, budget and schedule depend on each other: the budget decides how many campaigns and ad sets can learn, and the budget level and placements decide whether the campaign runs as Advantage+. Sales, app and leads campaigns run as Advantage+ when Advantage+ Audience, a campaign budget and automatic placements are all on, unless an advertiser constraint rules one out.

#### Structure and placements

The campaign uses only as many campaigns, ad sets and ads as real differences and the budget call for, delivering on placements that fit the creative and destination.

- Campaigns differ by objective, ad sets by delivery mechanics such as budget, audience, geography, schedule, placement or optimization, and ads by message. Several ads in one ad set aren't a controlled test; that takes an experiment.

- Each campaign or ad set has enough budget to learn, so fewer, larger ones beat many small ones. Under a campaign budget, ad sets share one bid strategy and one optimization goal.

- Placements are automatic by default, which keeps Advantage+ placements on. Which placements exist depends on the objective. Restricting them on any ad set turns Advantage+ placements off for the whole campaign, so a restricted set reflects a stated need and the plan calls it restricted. Choosing Threads means Instagram Feed has to be chosen too.

#### Budget and schedule

- By default the plan uses auction buying, a campaign-level daily budget, no end date, bidding for the most results and billing that fits the optimization goal. A daily budget is an average: days with better opportunities can spend more, within seven daily budgets per week. A lifetime budget is paced over the whole run and needs an end date.

- Cost-per-result, return-on-ad-spend and bid-cap goals reflect a target the advertiser stated, and each can leave budget unspent. A return goal needs value optimization with purchase values reaching Meta, and on iOS app campaigns, cost and return goals run at least three days.

- An end date reflects a real end to the goal, such as an event, a closing offer or a let unit, and is the only stop this connector can set. A condition like "pause once it's leased" is a manual step, with a date offered as a backstop.

- Hours-of-day scheduling serves a goal that needs it, uses a lifetime budget, and runs in the viewer's or the account's time zone. Budget increases for known peak periods can be scheduled ahead, and unpaced delivery suits flash sales and live events.

- The amount comes from the advertiser or compatible account history; otherwise pricing with `meta-ads-cli estimate-budget` offers choices, as [campaign budget](campaign-budget.md) describes. A missing amount alone isn't a reason to ask.

- An event whose recent volume or cost doesn't fit the advertiser's target or limit is a [binding constraint](#binding-constraints).

## Binding constraints

Sometimes the evidence shows the request can't be built as asked, or that it could go in clearly different directions. That's a question for the advertiser, and their answer can change the plan, so ask it before you show one.

Explain what you found and why it matters. Then offer the paths as options. Put your recommendation first, then what they asked for if it can still be built. Add any other change that would solve the problem. Don't show a plan or ask for approval in the same message.

Once they choose, do the research their answer affects, then price the final plan once.

## Recommend the plan

- The plan should lead with your recommendation, in business language for a beginner and setting names for an experienced advertiser. Each setting gets its value and a short basis, with the two to four findings that changed a decision. Mention only the assumptions or gaps that limit the plan.

- It asks "Proceed with this strategy?" with the options `Approve this strategy` and `No, make changes`. Approval goes to [creative](campaign-creative.md) without redoing research. A revision should rerun only the research it affects, reprice once if needed and show the whole revised plan.
