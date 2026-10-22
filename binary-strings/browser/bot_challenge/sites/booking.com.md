## Bot detection

- Booking.com runs an interactive bot check, most often a slider that asks you
  to “Drag the key to the Lock”. It can appear on search, sign-in and account
  pages. An empty page whose URL carries a `chal_t` parameter is the same check
  before it renders.
- Treat it as a bot challenge. Do not reload in a loop or resubmit the form
  while it is showing.
