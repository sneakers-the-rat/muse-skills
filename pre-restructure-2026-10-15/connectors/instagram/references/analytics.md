# Instagram analytics

- The analytics commands read Instagram's analytics service under the separate Access analytics permission. They support performance reviews of the user's accounts and public comparisons with other accounts.

- `--account-id` is always the user's own linked account from `accounts`. It selects the account the command runs as and is never a competitor's identifier.

## Commands

```sh
/opt/hatch/bin/instagram-cli analytics-metric-metadata --account-id <user_own_fbid> --metric-name <metric>
/opt/hatch/bin/instagram-cli analytics-account-insights --account-id <user_own_fbid> --time-range last-28d
/opt/hatch/bin/instagram-cli analytics-account-insights --account-id <user_own_fbid> --time-range last-28d --include-time-series
/opt/hatch/bin/instagram-cli analytics-top-post --account-id <user_own_fbid> --username <handle> --days 30 --include-text
/opt/hatch/bin/instagram-cli analytics-follower-count-delta --account-id <user_own_fbid> --username <handle> --days 28
/opt/hatch/bin/instagram-cli analytics-metric-cards --account-id <user_own_fbid> --username <handle> --username <handle> --days 28
```

- `analytics-metric-metadata` resolves a metric's display name and definition, and `--metric-name` can repeat. Use the returned display name and definition verbatim. Omit a metric that has no display name, and never invent a missing definition.

- `analytics-account-insights` reads metrics for the one linked account selected by `--account-id`. For several of the user's accounts, call it once per returned account and combine the results. Add `--include-time-series` only when the question needs a trend.

- `analytics-top-post` returns the most-liked post for each handle in the window. Add `--include-text` whenever a post will be named, summarized or displayed, so its label comes from returned content.

- `analytics-follower-count-delta` reports follower changes. An empty daily series means there is not enough history, not zero growth.

- `analytics-metric-cards` returns comparable metric cards. Check each account's `window.complete` and errors before comparing, keep card values and `growth_display` verbatim, and never convert that ratio to a percentage.

- `--username` can repeat, up to 10 handles per call. Put the accounts being compared in one call so they share one window.

## Read the results correctly

- Join results by the resolved handle or an echoed request identifier, never by array position.

- Keep the service's deltas, ratios and rankings as returned rather than recomputing them from rounded display values.

- `analytics-top-post` can return a post published outside the requested window. Check its returned publication date before using it.

- Account metrics describe the account, not any single post. For post-level evidence, read the posts with the commands in [read commands](read-results.md).

## Other accounts

- For accounts the user does not own, these commands return public metrics only.

- No command reads a product launch directly. Read the relevant public posts instead.
