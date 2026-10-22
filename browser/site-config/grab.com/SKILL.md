# Grab instructions

## Page setup

- **Service and country.** GrabFood (food.grab.com), GrabMart
  (mart.grab.com), transport and the merchant portal each have their own
  forms, and the path carries the country (such as `/sg/en`). Confirm both
  before searching.

## Searching

- Select the requested address from the location suggestions and inspect the
  resolved location with `browser.observe`. Typed text alone is not a selected
  address.
- “Login to search location” means location search needs sign-in first;
  submitting the search again will not get past it.

## Ordering and bookings

- Review the selected merchant or service, the destination and the fees before
  confirming. A search result or quote is not a completed booking.

## Signing in

- Consumers sign in through “Login/Sign Up”. Merchants sign in separately, on
  the merchant portal.

## Bot detection

- GrabMart can answer with CloudFront's “403 ERROR” page: “The request could
  not be satisfied. Request blocked.” It is a bot wall, not an empty store.
- Treat it as a bot challenge. Do not reload the search in a loop.
