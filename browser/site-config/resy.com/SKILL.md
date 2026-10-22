# Resy instructions

## Searching

- Set “Location”, the guest count and “Date” before searching. The URL carries
  them as `date=YYYY-MM-DD` and `seats=N`.
- Enter the restaurant in “Search restaurants, cuisines, etc.” and select it in
  the intended city.

## Venue pages and slots

- A venue page can first show an interstitial titled “Resy | Right This Way”
  with no content. Wait and observe again with `browser.observe` before
  concluding anything.
- Availability belongs to the selected party size and date. Each slot names its
  time and seating, such as “6:00 PM Dining Room”; check both before
  continuing.
- A spinner under the Guests/Date/Time bar that never resolves means
  availability did not load, not that the restaurant is full. Resy's bot
  restriction causes it; treat availability that stays unloaded as a bot
  challenge before reporting that it could not be read. A brief “No results.” on
  search can also mean results are still loading.
- “Notify” and “Notify for Dinner” create availability alerts, and “Join
  waitlist” joins a waitlist. Neither is a reservation.

## Booking

- Read any deposit, cancellation fee and seating terms in the booking review.
- Keep a pending slot open while signing in, and never start a second
  reservation while the first submission is unresolved.

## Signing in

- Resy signs in with a phone number and a texted code; “Log in with email &
  one-time code” is the alternative.

### Verification codes

- “Check your mobile phone!” shows six boxes, “Digit number 1 in OTP code”
  through “Digit number 6 in OTP code”. They are one verification-code field:
  supply all six references in order, never the first box alone.
- Observe the page with `browser.observe` after entry. Use “Resend Code” only
  when no code arrived.

## Bot detection

- Resy restricts automated traffic often. Besides visible bot checks, the
  restriction can leave availability unloaded, as described above.
- Treat a visible check as a bot challenge. Do not reload in a loop to force
  slots to appear.
