# Instacart instructions

## Choosing a store

- Set the delivery address and retailer before searching. A search across
  “All stores” and a search inside one store cover different inventory; keep
  the requested retailer.
- Choose “Delivery” or “Pickup” and the service time. A different store or
  address can change availability, prices and the cart.

## Products and cart

- Open the item to confirm its size and unit count before adding.
- After adding, read the item's quantity in the cart (“View Cart”). Do not add
  again just because a drawer stayed open.
- Review replacement preferences, weight-based estimates, fees and tip with the
  cart. An estimated grocery total can change after the order is fulfilled.

## Past orders

- Order history is at `/store/account/orders`. Guessed paths such as `/orders`
  return “Page not found”.
- “Reorder” and “View all orders” refer to past purchases. An old delivered
  order is not confirmation of the current checkout.

## Signing in

- Enter the email in “Enter your email address” and press “Continue”, or choose
  “Phone”. Instacart then sends a code.

### Verification codes

- “Verify email” takes the 6-digit code in one “Enter code” field. The code
  expires soon after it is sent.
- “Request a new code” unlocks after a countdown. Use it only when no code
  arrived.

## Bot detection

- Bot checks appear occasionally. Treat one as a bot challenge and do not
  resubmit the cart or sign-in while it is showing.

## Checking the result

- A placed order opens its own page under `/store/orders/`, titled “Instacart |
  Post Checkout”. The cart and checkout pages are not a confirmation.
