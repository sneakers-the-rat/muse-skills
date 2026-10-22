# Temu instructions

## Page setup

- Close a covering promotion or login dialog before using the controls behind
  it, then observe again with `browser.observe`; earlier references belong to
  the replaced page.
- Signed out, the homepage and search can redirect to `/login.html`. That is a
  sign-in wall, not an empty result.

## Searching and product pages

- Search with “Search” and “Submit search”. Open the item and choose its size,
  colour and pack quantity before comparing the final offer.

## Orders

- “Confirm delivery” marks an existing order as received. It is not the control
  for choosing an address or placing a new order.
- Order help lives in the support center (“Manage orders”, “Find my order”,
  “Cancel my order”); returns and refunds are under `/return-refund-list.html`.

## Signing in

- “Sign in / Register” offers “Continue with Email”, “Continue with phone
  number”, Google, Apple and Facebook. “Use another way to sign in” switches the
  method; observe the new form with `browser.observe` before entering anything.

### Verification codes

- The code screen draws six boxes over one hidden six-digit input. Assess the
  hidden input as the single verification-code field, not the six boxes.
- If code entry is refused, follow the fix the refusal states rather than
  trying the boxes one at a time, and report only a rejection the site will not
  let you retry.

## Bot detection

- Temu frequently shows “Security Verification” (“This step confirms you are a
  real person, not a robot.”), on its own page (`/bgn_verification.html`) or in
  a dialog over the login page.
- Its puzzle is a slider, such as “Slide to complete the puzzle”, that the
  accessibility tree does not expose; it needs a current screenshot. “Refresh”
  loads a different puzzle.
- Treat it as a bot challenge.
