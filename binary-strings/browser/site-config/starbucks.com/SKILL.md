# Starbucks instructions

## Page setup

- **Cookie banner.** “This site uses cookies, but not the kind you eat” offers
  “Agree” and “Change cookie settings”. For essential cookies only, open
  “Change cookie settings”, choose “Strictly Necessary and Functional Cookies”
  and save.
- Ordering, the account pages and careers are separate areas. “Search jobs”
  searches careers, not the menu.

## Ordering

1. Choose the café (`/store-locator`) and the service mode, “Pickup” or
   “Delivery”, before anything else.
2. Choose the drink's size, temperature and customizations before adding it.
3. Review `/menu/cart` before checkout. Guest checkout is available.

## Account and orders

- Past orders are under `/account/history`.
- “Partner Login” and “Candidate Login” are employee and job-applicant
  accounts, separate from the customer account.
- shop.starbucks.com shows only a sign-in wall until you sign in.

## Careers

- Enter the title or keywords and the location, choose the matching location
  suggestion, then use “Search jobs”.

## Signing in

- A sign-in form can be replaced after continuing or after a challenge. Observe
  its current fields with `browser.observe` before the login service fills
  them.
- Partner single sign-on (id.starbucks.com) can load with no controls in the
  accessibility tree; read it from the screenshot `browser.observe` returns. It
  may then ask for an SMS code.

## Bot detection

- Starbucks occasionally shows a bot check. Treat any challenge page as a bot
  challenge.
