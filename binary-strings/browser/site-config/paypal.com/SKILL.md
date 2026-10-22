# PayPal instructions

## Page setup

- When the cookie banner covers the page, choose “Accept” or “Manage cookies
  and learn more”.

## Checkout

- Verify the merchant, amount, currency and funding source. Choosing a funding
  source is not the final payment confirmation.
- Keep the PayPal window open while the outcome is unresolved. Do not restart
  payment from the merchant tab because the return is slow; after payment,
  check the order state the merchant shows.

## Account and developer pages

- “Save Changes” on an account, payment-method or developer app page saves
  settings; it never pays a merchant.
- App credentials, features and webhooks are on developer.paypal.com under
  apps and credentials.

## Signing in

- `/signin` starts with “Email or mobile number” and “Next”. The next page
  shows the password or the verification method PayPal selected.

## Bot detection

- Checks are frequent at sign-in. PayPal shows a DataDome device check:
  “Confirm you’re human” with a slider (“Move the slider all the way to the
  right”). “Switch to the visual verification” returns to the slider from the
  audio option, and “Try the challenge again.” starts a new attempt.
- Treat it as a bot challenge. Do not resubmit the email while it is showing.
