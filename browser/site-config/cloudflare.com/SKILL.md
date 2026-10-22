# Cloudflare instructions

## Dashboard

- cloudflare.com and its dashboard are Cloudflare's own product, not the
  Cloudflare challenge that other websites display.
- Select the intended account and zone before editing anything. A control under
  “Delivery & performance” changes the site's configuration, not browser
  routing.
- Inspect the saved configuration with `browser.observe` after an edit.
- A plan or payment screen is a separate purchase flow.

## Registering domains

- Search for a domain on the registrar pages, then complete checkout with the
  registrant address.
- The checkout's agreement boxes accept the Domain Registration Agreement and
  authorize the registration fee and annual renewals. They are purchase
  consent; never tick them outside an authorized purchase.

## Signing in

- Choose the method the task names: “Continue with Google”, “Continue with
  Apple”, “Continue with GitHub”, “Continue with SSO”, or Email and Password.
  Inspect the resulting form with `browser.observe` before the login service
  fills it.
- “Sign in” can stay disabled even after both fields are filled; do not force
  it. “Save email and login method on this device” is ticked by default.

## Bot detection

- Cloudflare challenges automated visits to its own site often, on marketing
  pages and the dashboard alike. The page is titled “Just a moment...” (or its
  translation, such as “Un momento…”) and shows little else.
- Treat it as a bot challenge. Do not reload the page while the check is
  running.
