# Best Buy instructions

## Searching

- Use “Go to Product Search” or the search field (“What can we help you
  find?”), then “Submit search”.
- On the product page, check the exact model, capacity, colour and condition.
  A disabled “Add to cart” or “Sold Out” means the item cannot be bought now.

## Pickup and shipping

- Choose “Pickup” or “Shipping” before adding, then verify the pickup store or
  delivery destination and the date for that choice.

## Offers and cart

- Keep new and open-box offers separate. Trade-in value, membership pricing and
  financing are conditional offers, not the item's ordinary price.
- Decline optional protection or accessory offers deliberately, then inspect the
  cart with `browser.observe`. “Save” adds to a saved list, not to the cart.

## Signing in

1. Enter “Phone number or email address” and “Continue”.
2. On “Choose a sign-in method”, pick the method the task can complete. “Email
   a sign-in link” is selected by default and sends a link, not a code; choose
   “Use password”, or a code option such as “Text a code to my account phone
   number” or “Send a code to my email”, when that is the available route.
3. “Sign in another way” lists other methods, such as a passkey, Apple or
   Google.

## Bot detection

- Best Buy blocks automated browsing often. On sign-in the block can look like
  a broken page: “Best Buy: Something Went Wrong”, or a form that stays
  disabled after “Continue” with a “Failed to fetch” error.
- Treat either as a bot challenge. Do not resubmit the sign-in or reload in a
  loop.
