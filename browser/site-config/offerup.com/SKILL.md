# OfferUp instructions

## Searching

- Set the area with “Set my location”, which shows the current city and radius,
  before searching.
- “Search category” picks the scope (For sale, Services, Jobs, Rentals), and
  “Search For sale” is the search box for that scope. Use “Sort” to order the
  results.

## Listings and messages

- Open the listing to verify its condition, price, pickup or shipping, and the
  seller's stated terms.
- “Saved” bookmarks listings; it is not a cart.
- Conversations are in the inbox (`/inbox`). Contacting a seller, making an
  offer and completing a purchase are separate actions; report the state you
  actually reached in `browser.report`.

## Signing in

- “Sign up / Log in” offers Facebook, Google, Apple and “Continue with email”.
  Inspect the form that follows with `browser.observe` before entering
  credentials.

## Bot detection

- OfferUp blocks automated visits often. The block page reads “Sorry, we have
  blocked your request!” and suggests turning off a proxy or VPN; it is a bot
  wall, not an empty search.
- Treat it as a bot challenge. Do not refresh repeatedly or retry the search
  from another page.
- “Sorry, something went wrong” with “Try again” is a site error. Try again; if
  it persists, search another way on the site before reporting it in
  `browser.report`.
