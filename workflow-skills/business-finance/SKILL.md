# Bookkeeping and Invoicing

## Establish the records

- Identify the company, currency, accounting period and whether the books use cash or accrual accounting. When a broad question leaves these open, ask for them together in one message.

- Find the records that govern each figure, such as the ledger, invoices, the payment processor and the bank. A card charge, its processor payout and the bank deposit can all describe the same sale.

## Reconcile the amounts

- Match records by ID, amount, currency and date. Account for fees, refunds, tax and settlement delays before comparing gross sales with net deposits, and use one reporting period and timezone throughout.

- Keep unmatched items visible and say what would resolve each one. Never post a balancing entry to hide an unexplained difference.

- Check that every report covers the requested period and accounting method before quoting it, and name any incomplete or paginated coverage.

## Invoice and collect

- Verify the customer, line items, unit prices, tax treatment, due date and payment terms. Creating a missing customer or product needs the user's agreement.

- Learn the app's document states before creating anything. Some apps make an invoice live the moment it is created, so for a draft-only request use a real draft state or prepare the invoice outside the books.

- Treat creating, sending, reminding, charging and refunding as separate actions, and show each one's exact recipient and content first. Read the record back after an uncertain response instead of trying again.

- For overdue payments, start from the receivables aging summary and send reminders only to the customers the user picks.

## Report the result

- Return the reconciled totals, the unresolved differences and links to the records. Say whether each invoice is created, sent, paid or still processing.

- Report what the books show, and leave tax, legal, compliance and collections decisions to the user and their accountant.

## Available connectors

- [QuickBooks](/opt/hatch/connectors/quickbooks/CONNECTOR.md) for company reports, receivables, invoices, estimates, payment links and industry benchmarks.

- [Stripe](/opt/hatch/connectors/stripe/CONNECTOR.md) for charges, payouts, fees, refunds, disputes, invoices and subscriptions on a merchant account.

- [Google Sheets](/opt/hatch/connectors/google_sheets/CONNECTOR.md) for a reconciliation worksheet or an exported ledger.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Mercury](/opt/hatch/connectors/mercury_mcp/CONNECTOR.md) for business bank balances, transactions, statements and invoices.

## Websites

- Use the business's existing accounting, processor or bank site with `browser.browse` for a report, export or statement its connector lacks. Have the task save the file and report the period it covers.

- [Xero](https://www.xero.com/) for books kept there, which is common in the UK, Australia and New Zealand.

- [Square Dashboard](https://squareup.com/dashboard/) for sales, fees and payouts from Square.

- [FreshBooks](https://www.freshbooks.com/) for small businesses that already invoice there.

## Alternatives for better results

- Use bank statements, processor exports and invoice PDFs to fill gaps or to check the ledger independently.

- Prepare a reconciliation worksheet or a draft invoice when that answers the need without changing live records, and compare any proposed correction with the original before posting it.

- Suggest an accountant's review for tax treatment or year-end adjustments.
