# Turo instructions

## Page setup

- Close a covering support chat with “Close chat” before using the booking
  form.
- Host accounts open in host navigation; “Switch to guest” returns to the
  renter view.

## Searching for a car

1. Enter the pickup place in “Airport, hotel, address, city” and choose its
   suggestion.
2. Open the “Start date” and “End date” calendars; the fields are read-only and
   do not accept typing. Choose dates before times: “Start time” and “End time”
   stay disabled until then.
3. Search, then recheck the dates and place in the search summary.

## Vehicles and booking

- Open the vehicle to read pickup versus delivery, the mileage allowance, trip
  conditions and the total charges. The daily rate is not the trip total.
- Keep a pending booking open during sign-in or verification. Confirm the
  resulting reservation in your booked trips (`/us/en/trips/booked`) before
  reporting the car as booked in `browser.report`.
- Messages with hosts are under `/us/en/inbox/messages`.

## Bot detection

Turo frequently blocks automated browsing, in two forms.

- **Verification page.** “Performing security verification” with a Cloudflare
  “Verify you are human” checkbox. It is interactive.
- **Block page.** “Sorry, you've been blocked” with a Cloudflare Ray ID. It is
  a bot wall with nothing to click.

Treat both as a bot challenge. Neither says anything
about a car's availability; do not reload in a loop.
