# ShopBack instructions

## Page setup

- “Login” and “Sign Up” stay disabled until the page finishes loading. Wait for
  them to become available instead of clicking early.

## Cashback offers

- Find the retailer with “Search for stores” and open it. Check the country
  and the conditions of that particular cashback offer.
- Store pages sit at short paths such as `/expedia` or `/old-navy` and show the
  rate with any boost, cap or end time. Report the rate text exactly in
  `browser.report`.
- “Log in / Sign up to shop” is an account step, not a purchase.
- Follow the retailer link with its query parameters intact, then work in the
  retailer's own cart and checkout.
- Cashback shown by ShopBack is separate from the amount the retailer charges.
  Never subtract it from the payment total.

## Bot detection

- ShopBack occasionally shows a bot check. Treat any challenge page as a bot
  challenge.
