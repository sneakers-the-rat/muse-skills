# Mortgage Comparison

## Set up a fair comparison

- Use the purchase price, down payment, loan purpose, term and rate type the user supplied, and keep missing figures explicit. An advertised rate is not a personalized quote, and a calculator result is not an approval.

- Compare offers on the same loan amount, term, rate type, points and lock period, recording when each quote was given and what it assumes. For an adjustable rate, note the initial period, reset rules and caps.

- Explain any difference in assumptions before ranking the offers.

## Explain cost and tradeoffs

- Show the interest rate and APR beside lender fees, points, closing costs and the cash needed at closing. Separate principal and interest from property tax, insurance, mortgage insurance and association fees, and label estimates.

- Weigh upfront cost against how long the user expects to keep the loan, and calculate when a lower payment recovers extra points or fees. Include prepayment terms and when the rate lock expires.

- In the US, compare lenders' Loan Estimates, the standard form that makes fees and payments comparable. Elsewhere, compare what local lenders must disclose, such as a UK illustration with its early repayment charges and follow-on rate, or the prepayment penalties and term in Canada.

- Present a small comparison of the strongest offers and the tradeoffs that matter to this borrower.

## Follow through

- Request an explanation, a written estimate, a pre-approval or a call with a banker, according to what the user wants. Share financial and contact details only within that task, and keep each lender's conversation separate unless the user agrees to share.

- Confirm what the lender actually completed. A conversation or a start receipt does not establish an approval, a locked rate or a booked call.

- Use [Scheduling](/opt/muse/skills/scheduling/SKILL.md) to record a confirmed call, and [Home Search](/opt/muse/skills/home-search/SKILL.md) when the financing is part of choosing a property.

## Available connectors

- [Finances (Plaid)](/opt/hatch/connectors/plaid/CONNECTOR.md) for the income, savings and debts that shape affordability.

- [Google Calendar](/opt/hatch/connectors/google_calendar/CONNECTOR.md) for recording a confirmed call with a lender.

- [Outlook Calendar](/opt/hatch/connectors/outlook_calendar/CONNECTOR.md) for recording a confirmed call with a lender.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Rocket](/opt/hatch/connectors/rocket/CONNECTOR.md) for a conversation with Rocket Mortgage about options, a pre-approval or a banker call.

## Websites

- Use lenders' sites with `browser.browse` for published rates and quote forms. Give each the same price, down payment, term and credit range, and have the task return the rate, APR, points and fees with the date they were quoted.

- [Rocket Mortgage](https://www.rocketmortgage.com/) for published rates and an online quote. Use the Rocket connector instead for a pre-approval or banker call where it is available.

- [Bankrate](https://www.bankrate.com/) for US lender comparisons to verify with each lender.

- [Freddie Mac's weekly rate survey](https://www.freddiemac.com/pmms) for a benchmark of average US mortgage rates.

- [Consumer Financial Protection Bureau](https://www.consumerfinance.gov/) for Loan Estimate guidance and US disclosures, and [MoneyHelper](https://www.moneyhelper.org.uk/) for UK mortgage guidance.

## Alternatives for better results

- Compare a mix of lenders, such as a large national lender, the user's own bank and a local credit union. Existing-customer discounts can help, but check the complete terms.

- Show the preferred lender a competing Loan Estimate and ask whether it will match the rate or fees.

- Ask a mortgage broker to search more lenders, after asking how the broker is paid and which lenders the comparison covers.
