# Price a Meta campaign budget

Use this guide to price the proposed campaign strategy, and again when the plan changes significantly; an earlier estimate that changed the plan was evidence, not its price. Everything priced is confirmed by the advertiser or settled by evidence. An existing campaign's budget questions belong to [tool routing](tool-routing.md).

`meta-ads-cli estimate-budget` prices the whole campaign in one call, with its flags in `estimate-budget --help`.

- A campaign is prospecting by default, or retargeting when its audience is people who are already engaged, such as site visitors or a customer list. The stage covers the whole campaign.

- Each ad set's own details shape its price:
  - targeting: interests, custom audiences, languages, age and gender
  - Advantage+ Audience, read as on when left out, which widens a stated age range
  - geography: countries, cities or regions
  - schedule: start and end dates, or a duration
- The plan's countries name every country the ad sets reach, including a targeted city's or region's country. The estimate prices in those markets, and without them it assumes the ad account's registered country.

- Every amount in the call is one the advertiser stated: a budget, a spending limit, a maximum cost per result or a minimum return. With no budget stated, the budget flags are left out and the estimate recommends one. Amounts are in major units, such as 25 for $25, in the currency the advertiser used.

- An advertiser's result goal that made it into the plan, counted in the unit the plan optimizes for, can shape the estimate through `--goal-value`, `--goal-result-type` and `--goal-period`. With a stated budget too, the budget holds and the gap to the goal is reported.

## Read and settle the budget

The estimate's result needs interpretation to offer the right budget for the proposed strategy. A returned amount is evidence, not the advertiser's budget: it becomes the budget when the advertiser stated it or their history supports it, and is otherwise offered as a choice. If the estimate returns no amount, say so and ask the advertiser for a budget instead of showing the plan for approval. The estimate's figures are shown as returned, since rounding or recalculating them breaks their consistency, and its API codes appear in plain words. What decided the amount:

- `budget_honored`: the advertiser's stated budget, kept exactly.

- `account_history`: the account's own recent spending.

- `target_derived`: how much the advertiser needs to spend to reach the goal used in the estimate; not required, and maybe not affordable.

- `learning_floor`: the spend estimated for each ad set to get enough events to leave the learning phase, about 50 in seven days; a recommendation, not a minimum.

- `delivery_floor`: the estimator couldn't anchor on anything, so it used the default amount; not a minimum.

- `account_minimum`: the least this account can spend, which raised any smaller amount; a hard limit.

The cost source says how much to trust the number. `account_history` is the advertiser's own measured cost, so it comes with its sample size. `peer_benchmark`, `industry_benchmark` and `forecast` are estimates. `none` means no cost could be estimated, so there's no cost to quote.

Expected results are projections. Ad-set costs show how each audience compares; the campaign cost already combines them. When the advertiser's amount is far below what the plan needs, say so early, with what each amount projects, and offer other ways to close the gap, such as a more frequent event, fewer ad sets sharing the budget or a longer run. If you quote an amount, take it from an estimate, not your own math.

In full research, call `muse.create_options` for an open budget before writing the reply, then explain the choice with the options token last. A settled budget with no other constraint goes straight to the [complete plan](campaign-planning.md#recommend-the-plan). Step by step, it ends in the budget choice in [planning](campaign-planning.md).
