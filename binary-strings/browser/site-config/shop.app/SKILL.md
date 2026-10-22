# Shop instructions

## Page setup

- shop.app opens the Shop marketplace on shop.com. Search products with
  “Search products and stores”; “Orders” lists tracked orders after sign-in.

## Merchant checkout

- Shop search and a merchant's Shop Pay checkout are different surfaces. When
  sign-in opens over a checkout, keep that checkout and return to it.
- “Shipping” and “Payment” open checkout sections. Read the address, delivery
  option, payment method and total before the final “Pay now”.
- “Check out as guest”, when offered, skips Shop sign-in. It does not skip the
  purchase approval that payment requires.
- Enter a promotion in “Discount code or gift card” and apply it with “Apply
  Discount Code”, then read the updated total.
- After returning from a payment provider, read the merchant's order state.
  “Back to finalize order” means a checkout step remains.

## Signing in

- Sign-in starts at `/accounts/login` with an email address. Shop then emails a
  six-digit sign-in code, or offers a remembered account to continue as.
- If “Continue” lands on a signed-out shop.com page instead of the code screen,
  the sign-in has looped. Report it in `browser.report` rather than repeating
  the loop.

## Bot detection

- Interactive checks are rare on Shop, but it often blocks a page outright
  with an “HTTP ERROR 403” page, order pages included. That is a bot wall, not
  a missing order.
- Treat it as a bot challenge. Do not reload it in a loop.
