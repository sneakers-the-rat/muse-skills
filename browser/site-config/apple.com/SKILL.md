# Apple instructions

## Store and country

- The store, Apple Account and support pages are separate areas. The store
  country, shown in the path (such as `/uk/`), sets availability, currency
  and pickup locations.
- “Find a Store” searches by location, postcode or store name. Each store page
  lists that store's hours.

## Buying a product

1. Open the product's buy page and select the exact model and configuration.
2. Compare delivery or store pickup only after the configuration is final;
   availability is checked per configuration and postcode.
3. Check the final bag before checkout, and the order record after it.

## Sessions at a store

- “Shop with a Specialist” books an in-store session: choose the store first,
  then a date and time.

## Signing in

- Apple Account sign-in starts with “Email or Phone Number”, then “Continue”.
  “Sign in with iPhone” selects a device-assisted method instead.
- The sign-in form lives in a frame (“Sign In to your AppleAccount”) that can
  load after the page and be replaced between steps. Observe again with
  `browser.observe` after each step before using field references.
- “Forgot password?” opens a new window and starts account recovery; it is not
  a sign-in step.
- A two-factor code prompt can follow the password.

## Bot detection

- Bot checks are occasional here. Sign-in is where Apple most often stops
  automation: after the password it can open an “Account Repair” frame. A frame
  that keeps loading without rendering is a bot check; treat it as a bot
  challenge first. A rendered one is an account security step, not a
  successful sign-in; report it in `browser.report` instead of starting account
  recovery.
- When a check or block page replaces the store, treat it as a bot challenge.
