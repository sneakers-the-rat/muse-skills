# Financial Planning

## Understand the decision

- Start with the decision the user faces, such as how much to save, whether a purchase is affordable or which debt to pay down first. Establish the period, currency and accounts involved.

- Read connected accounts or supplied statements, and name any missing information that could change the answer.

- Keep posted transactions, pending charges and balances separate. A balance is a snapshot, not a measure of income.

## Reconcile spending and cash

- Exclude transfers between the user's own accounts and payments to their own cards from income and spending, matching both sides so each purchase counts once. A payment labeled as a transfer can still be real spending when it goes to another person or business.

- Keep fees, interest, refunds and reimbursements in the right period.

- Check the cash each account needs on each date. An own-account transfer is not spending but still leaves its source account, and a card payment settles spending already counted while using cash this month. Include pending withdrawals and any minimum balance the user keeps.

- Separate regular bills, occasional expenses and discretionary spending. Confirm a recurring charge against recent transactions before treating it as a current bill, and distinguish a card's statement balance from payments made since.

- Treat missing amounts as unknown and say which accounts and dates the picture covers. Connected data can lag the institution, and one recent transaction does not prove an account is current.

## Build a practical plan

- Show the current position, the proposed changes and what they leave available. Check that every bill can be paid when it is due, rather than relying on a monthly average.

- Compare a few plausible scenarios when income or timing is uncertain, and say which assumption changes the answer.

- Lay out the options, the arithmetic and the tradeoffs, and leave the decision to the user. For debt, show what each repayment order costs in interest and time.

- Do not tell the user to buy or sell an investment, refinance or move money, and never promise returns or outcomes. For tax, legal or personal investment decisions, explain the general considerations and suggest a qualified professional, such as a tax adviser or a fee-only financial planner.

- This skill reads and plans. Moving money, trading or applying for credit happens only when the user explicitly asks, through a supported action with its own approval.

## Available connectors

- [Finances (Plaid)](/opt/hatch/connectors/plaid/CONNECTOR.md) for balances, transactions, recurring bills, liabilities and investment holdings across linked institutions.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Robinhood](/opt/hatch/connectors/robinhood_mcp/CONNECTOR.md) for brokerage positions, quotes and orders.

- [Coinbase](/opt/hatch/connectors/coinbase_mcp/CONNECTOR.md) for crypto balances, prices and orders.

- [Trust & Will](/opt/hatch/connectors/trustandwill_mcp/CONNECTOR.md) for where the user's estate plan stands.

## Websites

- Use the bank's or card issuer's own site with `browser.spawn_task` for a statement, payoff amount or rate that the connector does not return. Have the task report the figure with its date.

- [Consumer Financial Protection Bureau](https://www.consumerfinance.gov/) for US guidance on budgeting, debt and credit.

- [Bankrate](https://www.bankrate.com/) and [NerdWallet](https://www.nerdwallet.com/) for US savings, loan and card comparisons to verify with the provider.

- [MoneyHelper](https://www.moneyhelper.org.uk/) in the UK, the [Financial Consumer Agency of Canada](https://www.canada.ca/en/financial-consumer-agency.html) and [Moneysmart](https://moneysmart.gov.au/) in Australia for free, impartial money guidance.

## Alternatives for better results

- Work from statements, CSV exports and a simple worksheet when the user would rather not connect accounts, or to check connected data.

- For a loan, savings account or major purchase, compare the total cost, access to cash and the time to recover any switching cost, and include keeping the current arrangement. A lower monthly payment can cost more overall.

- Revisit the plan after a month of real spending and adjust the categories that drifted.
