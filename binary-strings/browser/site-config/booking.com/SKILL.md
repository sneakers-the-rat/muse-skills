# Booking.com instructions

## Page setup

- **Sign-in prompt.** “Sign in, save money” can cover the page a moment after it
  loads. Close it with “Dismiss sign-in info”, then observe again with
  `browser.observe`; the overlay invalidates earlier references.
- **Currency.** The header shows the active currency, such as “Prices in U.S.
  Dollar USD”. Change it only when the task asks; every price on the page
  follows it.

## Searching for a stay

1. Type the destination into the main search box (some layouts label it
   “Search in your own words”) and choose a suggestion.
2. Set check-in and check-out, then “Rooms and occupancy” for adults,
   children and rooms.
3. Search, then confirm all of these on the results page; the bar can reset
   occupancy on its own.

Leave “Add flights to my search” unchecked unless the task asks for flights.

## Choosing a room

- A property's headline price is not a bookable offer. Open the property and
  compare its individual rooms.
- Before reserving, read the chosen room's cancellation policy, prepayment
  terms, breakfast and taxes, and report them with its price in
  `browser.report`.

## Existing reservations

- Signed in, use “Bookings & Trips”. Otherwise use the guest booking lookup
  with the confirmation number.
- A confirmation-number lookup can ask for an emailed verification code instead
  of the PIN; enter it as described below.

## Signing in

- Sign-in runs on account.booking.com. Enter the email address and continue
  with “Next”; Booking.com then asks for the password or emails a code.
- A security check can follow the email step (step-up authentication). Its page
  may expose no controls to the accessibility tree; read it from the screenshot
  `browser.observe` returns before deciding what it is.

### Verification codes

- Booking.com emails a six-digit code and shows six boxes, labelled “Enter
  verification code character 1 of 6” through “6 of 6”. They are one
  verification-code field: supply all six references in order, never the first
  box alone.
- The form can submit itself once the sixth digit lands. Observe the page with
  `browser.observe` before pressing “Verify email” or requesting another code.
- A resend countdown does not invalidate a code already received. If code entry
  is refused, follow the fix the refusal states rather than retrying one box at
  a time, and report only a rejection the site will not let you retry.

## Bot detection

- Booking.com runs an interactive bot check, most often a slider that asks you
  to “Drag the key to the Lock”. It can appear on search, sign-in and account
  pages. An empty page whose URL carries a `chal_t` parameter is the same check
  before it renders.
- Treat it as a bot challenge. Do not reload in a loop or resubmit the form
  while it is showing.
