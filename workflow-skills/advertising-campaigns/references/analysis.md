# Advertising performance analysis

## Give the answer substance

- Reporting a value is not interpreting it. A useful answer has four properties, established in this order and delivered as one continuous argument:
  - a concrete number from this account paired with a comparator, such as a prior period, a peer or the advertiser's target
  - the mechanism behind it, tied to another value observed for the same object, such as "cost per result rose because CTR fell from 1.4% to 0.6% while CPM held flat"
  - what it means for the user's exact question, in the user's own KPI
  - one action on a named object that traces to a value stated in the same answer

- Never write `Observation`, `Interpretation`, `Analysis`, `Recommendation` or a synonym as a heading or label. These are how you think, not how the page is laid out, and one paragraph carrying all four is the ideal answer.

- When nothing moved, interpret the level instead of a change. Relate two values from the same row, such as CPM against CPC and CTR, or relate the values to what the objective optimizes for.

- Say each fact once. Do not restate a number, verdict or scope the reader already has, and keep retrieval out of the answer, with no "I pulled", "I checked" or account of your attempts.

- Match the shape to the question:
  - a name, a yes or no, or "that does not exist in this account" gets the answer, then the one action worth taking
  - one object whose metric moved gets one paragraph with the value, the driver and the action
  - a diagnosis with a real cause chain gets continuous prose with at most one bold lead-in
  - a multi-object comparison gets a table plus short prose

## Report what the platform returned

- Use the exact account, campaign or ad, period, timezone and attribution window. State the object and period once, where the reader first needs them, not after every value.

- Report only figures the platform returned. Do not average, sum, rebase, annualize or project a metric, and do not emit a ratio the platform did not return, such as a frequency from Reach and impressions. Set the two values side by side instead.

- A percentage change is a derived figure, so state it with both values, as in "cost per result is $63.40, up 37% from $46.28". Re-express a change of 500% or more as the before and after values, or describe it in words.

- Missing values stay missing, and a zero baseline has no finite percentage increase. Never carry a value into a period or object it was not returned for.

- When the user asserts a value that contradicts the retrieved one, restate the retrieved figure and its period. Do not adopt their number or rework the analysis to fit it.

## Rank only on enough volume

- A rate is only as good as the count underneath it. Before ranking or naming a winner on cost per result, CTR, conversion rate or ROAS, read the matching count in the same row. When the outcome count is in the low single digits, one more conversion reverses the order.

- On counts that low, do not rank objects, call one an underperformer, read a trend or recommend pausing, scaling or editing. This depends on the count, not the age. An ad with four results over ninety days is as unrankable as one launched yesterday.

- Age disqualifies in one direction. Do not recommend pausing, cutting or replacing an object in its first days or its learning period, even in a plan for later weeks. Schedule a first review and decide from the counts available then.

- Being unable to rank is not being unable to answer. Say which object is ahead and that the margin will not hold, such as "Summer Sale is at $12 per result and Retargeting at $18, but on 3 and 2 results one conversion reverses that", then answer from spend, impressions, reach, link clicks and the creative.

## Explain only what the evidence supports

- Judge each object on the metric its objective optimizes for. CTR is a primary success measure only for traffic objectives, sales and leads are judged on cost per result, ROAS or volume, and CPM leads only for awareness. Always report a metric the user asked for.

- Never rank or compare campaigns with different objectives on one shared metric. Compare their contribution to the business goal instead.

- Find the bottleneck among delivery, creative, audience, landing page, checkout, offer and measurement. Read the actual creative before recommending new copy, format or a call to action, and inspect the destination when its behavior may explain the result.

- A falling CTR alone is not fatigue. Pair it with frequency, conversion or cost movement before recommending a refresh or a pause.

- Attribute a difference to audience, placement, bid, budget, schedule or creative only after reading that setting for every object compared. Otherwise read it, or say the cause is not known yet.

- Before calling a child object or segment the driver of a parent result, check that the returned children account for the parent total. If they do not, describe only the comparison among the returned rows.

- Keep every figure in one list, table or paragraph at one analysis level, the level the question named. Account, campaign and ad totals do not reconcile, so never set an account total beside campaign results or assume a parent equals the sum of its children.

- For a why, trend or ranking question, use a comparator and one candidate driver from successful results. If the first read lacks them, make one targeted follow-up read, then interpret the levels you have. Never present a comparison as the requested trend, and say when the driver cannot be identified.

- Do not use bare labels such as "strong", "healthy", "low" or "expected". A label needs the value and a comparator in the same sentence, otherwise describe the relationship between values, as in "CPM $7.35 across 611,940 impressions produced 512 link clicks".

- State a blocking status, such as learning, a payment error or a spend limit, in one line of its own. Lead with what the retrieved numbers show, and make resolving the status the recommendation rather than generic tips.

## Recommend for the advertiser

- Tie the action to the observed problem and the advertiser's constraints. Options include improving the offer or landing page, changing creative, reallocating, reducing or pausing spend, and keeping the current plan.

- Take the stance the data supports. Do not fall back on "run an A/B test" or "split it into more ad sets" to avoid a call the numbers make.

- A recommendation to pause names the replacement ad, or the ad set or campaign that absorbs the budget and why, and a budget cut names where the money goes instead. Move budget at the levels the platform budgets, never by individual ad.

- Before recommending more spend, check that no account restriction, prepaid balance, spending limit, under-pacing budget or broken tracking blocks it. Lead with any blocker, and say which ones you could not confirm.

- Do not narrow an audience because of noisy segment costs or low volume. Follow the platform's own audience guidance in its connector docs.

- Use an experiment when uncertainty warrants one, with a hypothesis, an outcome and enough budget to learn.

## Include a plan in an account review

- A full account review helps the advertiser understand what is contributing to their business goal, what is holding it back, and where to focus and what actions to take next.

- A useful plan connects the account's evidence with the advertiser's priorities, strategy and constraints.

- The plan should clearly identify which recommendations are supported by evidence and where uncertainty remains (and what actions lead to further learning).

- A good plan starts with the conclusion and then the supporting findings explain the reasoning and uncertainty.

- Match the depth and scope of the review and plan to what the advertiser asked.

## Keep verdicts consistent

- Group the answer by object and give at most one verdict per object and metric. Resolve a contradiction before writing rather than calling the same ad a top performer in one place and weak in another.

- For a platform's field definitions, levels and coverage, read its connector docs, such as Meta's [evidence](/opt/hatch/connectors/meta_ads/references/evidence.md) and [metrics](/opt/hatch/connectors/meta_ads/references/metrics.md).
