# Costco instructions

## Page setup

- **Country and location.** Check the country selector (“US, Country/Region”)
  and the warehouse or delivery location before comparing anything.
- **Shopping flows.** Costco.com, “Business Delivery” and “Grocery by
  Instacart” are different flows with different stock and prices.

## Finding items

- Use “Search Costco” for products. For a known item number, use “Order By
  Item Number”: enter each item number and quantity, “Validate Items”, then
  “Add all to Cart”.
- Member-only prices stay hidden until sign-in. Check membership-dependent
  pricing on the item page after an authorized sign-in.
- Open pages from Costco's own links. Guessed URLs lead to “Page Not Found!”.

## Cart

- Check quantities and fulfilment restrictions in the cart. Warehouse stock and
  an online offer do not establish each other's availability.

## Signing in

- Sign-in runs on signin.costco.com with “Email Address” and “Password”. The
  form also offers “Receive a Passcode” and “Sign in with a passkey”; keep the
  chosen method, since requesting a passcode changes the active challenge.
- “Keep me signed in” is ticked by default; Costco says to use it only on a
  private device.

## Bot detection

- Costco blocks automated browsing often, and usually silently: a sign-in that
  returns the same form with no error, or search results that stay on
  “Loading”.
- Submit sign-in once. If the form comes back unchanged, or results never load,
  treat it as a bot challenge rather than resubmitting.
