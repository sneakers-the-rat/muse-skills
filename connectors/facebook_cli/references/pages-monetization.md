# Page earnings and payouts

- These commands read a managed Page's earnings, its standing in Facebook's monetization programs and its payouts. They only read, so they can't change a payout or the payout account.

- Decline a request to fake a payout confirmation, payment proof or earnings statement, or to use earnings or payout data to expose or target a person's money problems, such as guessing which followers are in debt or posting that someone can't pay, before running any command or search, including `pages list`, because any lookup already starts the task.

- Before running any command here, choose the Page with the steps in [Facebook Pages](/opt/hatch/connectors/facebook_cli/references/pages.md), because they ask which Page the user means when more than one could match.

## Earnings

```sh
/opt/hatch/bin/facebook-cli pages monetization earnings --page-id '<page_id>' [--question '<question>'] [--time-range <today, last_7d, last_14d, last_28d (the default), last_60d, last_90d, this_month, last_month or custom>] [--start-date <YYYY-MM-DD> --end-date <YYYY-MM-DD>]
```

- `pages monetization earnings` explains how the Page's earnings changed over a time range. Pass the user's question as `--question`, up to 300 characters, and the period they mean as `--time-range`. A `custom` range needs both `--start-date` and `--end-date`.

## Monetization programs

```sh
/opt/hatch/bin/facebook-cli pages monetization guidance --page-id '<page_id>' [--program <stars, subscriptions or facebook_content_monetization; omit for all>] [--include-criteria]
```

- `pages monetization guidance` says which programs the Page is in and what it needs to do next. Add `--include-criteria` when the user asks what a program requires.

```sh
/opt/hatch/bin/facebook-cli pages monetization invite-eligibility --page-id '<page_id>'
```

- `pages monetization invite-eligibility` says whether the Page is invited to Facebook content monetization. An invitation is not the same as monetization being on.

## Payouts

```sh
/opt/hatch/bin/facebook-cli pages monetization payout-account-state --page-id '<page_id>'
```

- `pages monetization payout-account-state` reads whether the Page's payout account is set up and any holds on it.

```sh
/opt/hatch/bin/facebook-cli pages monetization payout-report --page-id '<page_id>' [--year <YYYY, default the latest year with payouts>]
```

- `pages monetization payout-report` reads the Page's monthly payouts for one year.

```sh
/opt/hatch/bin/facebook-cli pages monetization payout-status --page-id '<page_id>'
```

- `pages monetization payout-status` reads the current payout balance, the payout schedule and recent payouts.

## Report the figures

- Report only the figures a command returned, exactly as returned. Don't add your own totals, estimates or projections, because the user would take them as Facebook's numbers.

- Payouts are set up and changed in Facebook. These commands need no bank, tax or identity details from the user, and none of them can move a payout or produce payment proof.
