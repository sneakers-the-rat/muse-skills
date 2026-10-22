# The Home Depot instructions

## Page setup

- **Store and ZIP.** Set the store with “Open drawer to view my store” and the
  ZIP code with “Open drawer to update zip code” before comparing local prices
  or stock.
- **Sign-in tooltip.** “Sign in for the best experience” can cover the header;
  close it with “close” when it blocks a control.

## Product pages

- Search with “What can we help you find today?” and open the product.
- Select dimensions, finish, pack size and quantity before “Add to Cart”. Use
  “Decrease by 1” and “Increase by 1” to change the quantity.
- The pickup and delivery tiles are separate fulfillment choices; select the
  intended one. A “Check Nearby Stores” result is not stock at the selected
  store.
- “Protect This Item” offers a protection plan. Leave “No thanks” selected
  unless the task asks for one.

## Checkout

- Expand “Delivery Options”, “Payment Method” or billing details as needed.
  Select an address suggestion before relying on its ZIP; “Place Order” stays
  disabled until every required section is complete.
- Card expiration and security code are separate protected fields.
- Gift cards (“Apply a Gift Card”), promo codes (“Press to add a Promo code”),
  tax exemption (“Apply Tax Exempt ID”) and a PO or job name (“Have a PO/Job
  Name for This Order?”) each have their own control; do not confuse them.
- “Review Your Order” precedes the final “Place Order”. Read the delivery
  charges and current total at review.

## Signing in

- Sign-in runs on `/auth/view/signin` in two steps: “Enter Your Email Address”
  and “Continue”, then “Enter Your Password” and “Sign In”.
- “Your Password Has Expired” offers “Sign In without a Password (Suggested)”,
  which signs the account out of every other device, and “Reset Password”. Both
  change account security; report the page in `browser.report` instead of
  choosing either.

### Verification codes

- The code goes in one “Enter Code” field (“Your code must be 6 digits.”),
  followed by “Verify”.
- After a short countdown the page offers “Text me a new code”, “Email me a
  code”, “Call me with a code” and “Use my password instead”. Use them only
  when the first code did not arrive.

## Bot detection

- Bot checks are frequent. Most take the form of an “Access Denied” page (“You
  don't have permission to access … on this server.”) with a Reference number.
  It is a bot wall, not an empty catalog or an outage.
- The sign-in pages carry reCAPTCHA; a visible reCAPTCHA puzzle is the same
  kind of check.
- Treat either as a bot challenge. Do not reload in a loop or repeat searches
  to get past it.
- “Oops!! Something went wrong. Please refresh page” and “WE'RE FIXING IT.” are
  site errors, not bot checks. Use “Refresh”; if the error persists, try again
  shortly or reach the page another way before reporting it in
  `browser.report`.

## Checking the result

- An order is placed only when Home Depot shows its order record after “Place
  Order”. The review page is not a confirmation.
