# Walmart instructions

## Page setup

- **Shopping assistant.** If “Ask me anything” (Sparky) covers the page, close
  it with “Close Sparky”. Its “Sign in” prompt belongs to the assistant.
- **Fulfilment.** Set the delivery address or pickup store with “Pickup or
  delivery?” first. Shipping, delivery from a store and pickup have different
  inventory and fees.

## Searching and product pages

- Search with the “Search” combobox or `/search?q=<encoded query>`.
- On the product page, check the selected size, pack count and seller, and the
  fulfilment options (“Shipping”, “Pickup”, “Delivery”), each with its own date
  or availability, before adding.

## Cart and checkout

- Read the cart after adding and confirm the line quantity and fulfilment mode.
  Grocery weight estimates and substitution choices can change the total.
- At review, check the delivery window, order minimum, fees and total. A
  membership offer is not consent to start a trial.

## Signing in

1. Enter “Phone number or email (required)”, then “Continue”.
2. Under “Choose a sign in method”, pick a texted code (“Send a verification
   code to …”, the default), an emailed code (“Email me a verification code …”)
   or “Password”. “Text me” or “Call me instead” sends the code; “Sign in with
   passkey” is a separate method.

### Verification codes

- “Enter verification code” shows six boxes, labelled “digit 1” through “digit
  6”, and focus jumps to the next box as each digit lands. They are one
  verification-code field: supply all six references in order, never the first
  box alone.
- If code entry is refused, follow the fix the refusal states rather than
  retrying one box at a time; when its result is uncertain, assess the page
  again. Report only a rejection the site will not let you retry.

## Bot detection

- Walmart frequently redirects to a “Robot or human?” page at `/blocked` with a
  “Press & Hold Human Challenge” button that must be held until verified. It
  can replace a search or product page.
- Treat it as a bot challenge. It is not an empty search or an unavailable
  product; keep the original task and resume once it clears.
