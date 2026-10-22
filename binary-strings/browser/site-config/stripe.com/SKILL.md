# Stripe instructions

## Telling the surfaces apart

- Hosted checkout, the customer billing portal (billing.stripe.com/p/session/…)
  and the Stripe Dashboard (dashboard.stripe.com) are different products.
  Dashboard sign-in is never a checkout requirement.

## Checkout

- Read the merchant, currency, total and whether the charge recurs. Address or
  tax changes can update the total.
- Payment fields can sit inside separate secure frames. The payment service
  fills the observed card fields; never guess selectors or type secret values.
- After the final payment action, wait for its result and read the merchant's
  confirmation. A button still showing a loading state is an unresolved
  payment.

## Billing portal

- The portal changes or cancels a subscription. Its confirm button shows a
  loading state while the change is processed; wait for it to finish and read
  the updated plan with `browser.observe` before reporting the change in
  `browser.report`.

## Signing in

- Dashboard sign-in (dashboard.stripe.com/login) takes an email and password,
  or Google, “Passkey” or “SSO”.

## Careers

- Search open roles at `/careers/search`.

## Bot detection

- The Dashboard sign-in page frequently shows an hCaptcha image challenge with
  “Verify Answers” and “Refresh Challenge.” controls.
- Treat it as a bot challenge. Do not submit the sign-in form while it is
  showing.
