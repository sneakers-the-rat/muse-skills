# Yahoo instructions

## Searching

- The homepage web search is labelled “Search Query for Search the web”.
  “Search with Yahoo Scout” switches to the answer assistant instead of web
  results.
- In Mail, “Search box. Find messages, documents, photos or people” searches
  that account's mailbox, not the web.

## Finance

- Quote pages sit at `/quote/<SYMBOL>/` on finance.yahoo.com. Report a price in
  `browser.report` with the time the page gives for it.

## Account settings

- Subscriptions (login.yahoo.com/myaccount/subscriptions) and payment methods
  are separate settings. “Add new payment method” does not settle an
  outstanding purchase.

## Signing in

1. Enter “Username, email or phone number”, then “Next”.
2. Observe the next page with `browser.observe` for the method Yahoo selected:
   password, a code or a passkey.

A passkey prompt (“Sign in using passkey”) needs the user; “Try signing in
another way” lists the other methods.

## Bot detection

- Yahoo occasionally shows a bot check. Treat any challenge page as a bot
  challenge.
