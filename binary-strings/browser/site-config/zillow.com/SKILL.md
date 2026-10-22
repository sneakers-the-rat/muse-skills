# Zillow instructions

## Searching

- Search by city, address or ZIP with “Search” and “Submit Search”, then check
  the selected Buy or Rent mode and filters. Open a listing to read its current
  details.
- “Save” bookmarks a listing. It does not contact an agent, schedule a tour or
  apply for the property.

## Rental Manager

- Landlord tools live under `/rental-manager/properties`. Each property's
  dashboard covers tenants (“Add tenant”, “Invite to apply”), leases (“Upload a
  lease”), tours (“Set tour availability”) and the “Payments” tab.
- Tour, application and payment forms are separate. “Confirm upgrade” changes
  a paid Zillow product; it is not a listing filter.

## Signing in

1. Enter “Email Address”, then “Continue”.
2. Choose “Sign in with password”, or “Or send a secure code to your email” for
   an emailed code. Google, Apple and Facebook are separate methods.

## Bot detection

- Zillow frequently refuses pages with “Access to this page has been denied”
  and a “Press & Hold” button, often on a single listing while other listings
  still open. During sign-in the same check appears as a “Before we continue”
  panel.
- These pages can expose nothing to the accessibility tree; read them from the
  screenshot `browser.observe` returns.
- Treat it as a bot challenge.
