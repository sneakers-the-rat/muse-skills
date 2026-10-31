# Shopify UCP checkout protocol

- Use this protocol after the user selects catalog products from one Shopify merchant whose product details carry a `checkout_token`, after a browser completion result supplies a privately captured `shopify_cart`, or when the user asks about a native order confirmed in this conversation by a successful `checkout complete` or a successful `order get` after an unclear completion.

- Every command runs as `/opt/hatch/bin/shopify-ucp-cli`, and every command except `order get` takes a JSON input file.

## Use a captured storefront cart

- After a browser completion result supplies `shopify_cart`, keep its exact `shopify_cart.browser_task_id` and currency. Skip catalog product checks and optional catalog cart commands for this source. Never request, copy or reconstruct the private cart ID, key or UCP endpoint.

- Choose the payment route and prepare buyer details below before creation. If those rules require website checkout, continue the original browser task using `shopify_cart.browser_task_id`. Tell it to continue website checkout without capturing again. The runtime releases the unused capture before preparing browser payment.

- Create the same buyer-and-currency input described below, using the currency read from checkout (ask if it is unknown), replacing the entire `items` field with `"browser_task_id": "<shopify_cart.browser_task_id>"`. Never provide both sources. One CLI invocation converts the captured cart and applies the prepared buyer and delivery details before returning its quote.

- Never recapture. Retry captured-cart creation only when the CLI reports `buyer.email must contain @`, `buyer.country_code must be a two-letter ISO country code`, or `unsupported Shopify checkout currency`, with no `create_outcome` or checkout reference. These errors occur before the cart is claimed. Correct the draft from confirmed details, asking the user if needed, and run `checkout create` once more with the same `browser_task_id`. Missing `create_outcome` alone does not permit a retry. For any other failure with neither `create_outcome` nor a checkout reference, including a corrected attempt that still fails or cannot claim the cart, stop and report the unresolved outcome without switching routes. Catalog-token refresh instructions below do not apply to a captured cart.

- When `create_outcome` is `rejected`, stop and report the rejection; if the user chooses website checkout, continue the original browser task without another capture. When `create_outcome` is `created` but `ok` is false, read `agent_state.checkout_id` with `checkout get` and address the reported issue, using `checkout update` for buyer corrections before reviewing the quote. Keep that checkout instead of reopening the original cart.

- After successful creation, use the returned checkout and the completion rules below. A continuation URL alone does not require browser checkout. If the checkout requires buyer action or review, continue at its exact returned URL without reopening the original storefront cart.

## Check the products

- Keep each selected product's exact `product_id` and storefront `url`. A product with a `checkout_token` gets a UCP checkout, and the checkout itself decides how it completes. Ignore the catalog and product-details checkout flags.

- Put products in one checkout only when their URLs clearly identify the same storefront. Matching brand names are not enough, and a checkout never mixes merchants.

- The checkout endpoint makes the final decision.

- For each selected catalog product, keep the `checkout_token` string from the product-details response that confirmed its variant. Run `/opt/hatch/bin/shopping product-details --product-id <product_id>` only for a product you have no response for. It is signed and tells the checkout which merchant and variant to use, so copy it exactly and never write or edit one yourself.

- A product whose details have no `checkout_token` cannot be checked out directly, so offer browser checkout from its product URL.

## Keep an optional cart

- Use a cart only when the basket must outlast the turn, because the user is still adding or removing items or wants to return later. `checkout create` takes items directly. Keep the opaque cart ID, which `cart create` returns as `result.id` and later cart commands echo as `agent_state.cart_id`.

```json
{"items": [{"checkout_token": "<checkout_token from product-details>", "quantity": 1}]}
```

- `cart get` and `cart cancel` take `{"cart_id": "<cart_id>"}`, and `cart update` takes the `cart_id` with the complete `items` list. An update replaces the whole basket, which is how an item is removed, so read `cart get` first when unsure and rebuild from `result.line_items`, using each line's `item.id` and `quantity`.

- A cart holds one merchant. A cart spanning two is refused with an error naming both merchants, so start a separate cart instead of retrying.

- Cart commands and `checkout create` take each catalog product as its product-details `checkout_token`, or a saved cart's product as `item_id` set to the variant ID from that cart line's `item.id`, with no `checkout_token`.

- A cart is not linked to its checkout. Cancel it once `checkout complete` returns `ok: true` or the browser confirms the order, because nothing else closes it and there is no way to list forgotten carts.

- A `warning` or `info` message, such as `quantity_adjusted`, does not fail a cart call. Report it when it changes what the user is buying.

## Choose the payment route

- Keep a payment route explicitly selected for this purchase, including Link selected by the purchase handoff. Otherwise ask with `muse.create_options` and wait, offering Shop Pay, Link and Use another method. A saved default or an existing connection alone does not select a route.

- For Use another method, follow `/opt/muse/skills/shopping/references/browser-checkout.md` from the selected product URLs, explain that the user will enter payment during browser takeover and do not create a UCP checkout.

- For a wallet route, call `wallet.list_payment_methods` for its provider and resolve one exact saved card as that wallet's connector docs describe. If the user declines setup or no usable card results, return to the route choice.

## Prepare buyer details

- Start from details already known in the conversation and `~/USER.md`. Before asking for a missing name, email address or phone number, call `wallet.get_user_info`, and for a missing recipient name or shipping address call `wallet.list_shipping_addresses`. Use wallet values only for matching missing fields.

- After applying known, sole or default values, ask one grouped question for every required detail still missing or ambiguous. Never guess or fill in a buyer email, recipient name or address field. Do not tell the user details are needed before these lookups finish.

- Direct completion needs the buyer email, the recipient's first and last name and a complete shipping address with street, city, state or region, postal code and two-letter country code. Direct checkout ships only to the United States, Canada, Japan, Singapore and the United Kingdom (country code `GB`), so use the browser route for another destination. Include a phone number when known, and ask for one only when the user or merchant requires it.

- Wait for those details before creating the checkout. If the user does not want to give them, use the browser route with the selected wallet from the original product URLs.

## Create the checkout

- Confirm every product, exact variant and quantity, and put the complete item set into this first call, because `checkout update` cannot add or remove products.

- Put each catalog product's product-details `checkout_token` in `items[].checkout_token`, and pass a variant ID from a cart line's `item.id` as `item_id` with no `checkout_token`. Use one entry per distinct variant and fold repeats into its `quantity`, which must be at least 1. Leave `item_id` out of an item that has `checkout_token`, and do not add a merchant field, because the CLI takes both from the token.

- Set `currency` from the products' latest catalog details, such as `CAD` for a product priced in Canadian dollars, and use `USD` only when the currency is absent. Never infer it from the shipping country. If the products' currencies differ, offer browser checkout for all of them instead.

- Leave the wallet provider and payment-method ID out of this request.

```json
{
  "buyer": {
    "email": "<buyer email>",
    "phone_number": "<phone, when known>",
    "country_code": "<two-letter country code, when known>",
    "address": {
      "first_name": "<recipient first name>",
      "last_name": "<recipient last name>",
      "street1": "<street address>",
      "street2": "<apartment or unit, when known>",
      "city": "<city>",
      "state": "<state or region>",
      "postal_code": "<postal code>",
      "country": "<two-letter country code>"
    }
  },
  "items": [
    {
      "checkout_token": "<checkout_token from product-details>",
      "quantity": 1
    }
  ],
  "currency": "<catalog currency, or USD>"
}
```

```text
/opt/hatch/bin/shopify-ucp-cli checkout create --input-file '<checkout.json>'
```

## Read the creation result

- Continue only with a usable `agent_state.checkout_id`, and save it. Read the quote from the output's `checkout` view, which the CLI validated, and treat `result` as the merchant's raw body.

- A checkout ID with `requires_escalation` or a buyer-detail message is still a created checkout. Keep the selected route and follow the completion branches below without asking the route question again.

- A merchant `error` message sets `ok` to false and adds an `error` summary, but keeps the checkout. Its `severity` decides the next step:

  - `recoverable` can be fixed with `checkout update`.

  - `requires_buyer_input` and `requires_buyer_review` continue in the browser from the checkout URL.

  - `unrecoverable` ends direct checkout, so explain it and offer browser checkout at the returned checkout URL. Only catalog checkouts may fall back to the original product URL; for a captured cart without a checkout URL, report the blocker.

- Read `requested_currency`, `checkout_currency` and `currency_changed`. Shopify may choose a supported currency for the shipping destination, which is not an error and needs no browser fallback.

- When the currency changed, use only the checkout currency and amounts from then on. Tell the user both currencies, explain that Shopify chose the market from the shipping address, and show the new item price and total.

- After the first usable quote is established, the checkout currency is fixed, and `checkout get` or `checkout update` fails if the merchant answers in another currency. Explain the failure and offer browser checkout from the checkout URL instead of retrying.

- Recheck any budget against the checkout amounts. If the budget is in another currency and no user-approved equivalent exists, ask for a limit in the checkout currency, and never compare currencies as raw numbers or invent an exchange rate. The user approves the final quote in its own currency, and a decision about the catalog price does not cover it.

- Take the checkout URL from `result.continue_url` or `result.checkout.continue_url`, or, for a catalog checkout only, use a selected product's original storefront URL. If a captured checkout needs the browser but has no continuation URL, report the blocker. Never construct one. A continuation URL alone does not require browser completion.

- An error containing `no_ucp_descriptor` means an item's `checkout_token` was missing, expired or did not match it. Run product-details for that product once more and retry with the new `checkout_token`. If it fails again, offer browser checkout from the product URL.

- If catalog creation fails or rejects an item for any other reason, explain the result and offer browser checkout from the original product URL without retrying. If the user accepts, follow `/opt/muse/skills/shopping/references/browser-checkout.md`.

## Choose direct or browser completion

- Keep the selected wallet and card. Ask again only when the user asks to switch or the card is no longer listed, and never substitute another card.

- For a switch to another wallet, resolve its exact card with `wallet.list_payment_methods` and keep the existing checkout, without asking the user to confirm the switch they just requested. For Use another method, continue the existing checkout in the browser from its URL and explain that the user will enter payment during takeover.

- If setup for the requested wallet is declined or leaves no usable card, keep the checkout and ask the user to choose another route.

- Take the first branch that matches the selected wallet:

  - Shop Pay completes directly when creation did not report `requires_escalation` and the checkout has the recipient's name and address. Otherwise continue in the browser with Shop Pay.

  - Link continues in the browser when creation reported `requires_escalation` or a message requiring buyer input or review.

  - Link continues in the browser when the checkout lacks the recipient's name and address.

  - Otherwise Link completes directly.

- Missing delivery options or an unsettled total do not choose a browser branch. Handle them with the refresh steps below.

- On a browser branch, finish any wallet connection or card setup in the parent first, briefly acknowledge the handoff and end the reply. Do not poll the browser task, and never call `checkout complete` for that checkout.

### Continue in the browser

- Start a browser task with `browser.browse` and `task_id: "new"`. Name the wallet by provider ID and the card by its masked label in the brief, never the opaque payment-method ID. The browser task does not call wallet tools or discuss other payment routes, and the trusted checkout tool revalidates the exact selected card against a fresh wallet read before it creates the approval.

```json
{
  "task_id": "new",
  "task": "<request in the user's words>. Open <exact Shopify checkout URL> for <selected products>. Use provider <shop-pay or stripe-link> with saved card <masked label>. Use these choices for every item: <variants and quantities>. Ask only for missing required purchase choices. Complete the purchase after the payment decision. Shipping preference: <deadline, budget or speed, or none>."
}
```

- Continue the purchase as `/opt/muse/skills/shopping/references/browser-checkout.md` describes.

## Refresh buyer details, delivery, discounts and totals

- Read the offered delivery options, with their `id`, `title`, `description` and `totals`, from `result.checkout.fulfillment.methods[].groups[].options[]`, because the `checkout` view shows only the selected one.

- When the checkout offers one delivery option, select it. With several, pick the best fit when the user stated a deadline, budget or speed or the options are nearly identical, and say which you chose. Otherwise show each option's price and estimate and let the user choose.

- If different item groups need separate delivery choices, do not complete directly, and continue in the browser from the checkout URL.

```json
{"checkout_id": "<checkout_id>", "selected_delivery_option_id": "<delivery option id>"}
```

```text
/opt/hatch/bin/shopify-ucp-cli checkout update --input-file '<update.json>'
```

- When the user asks to add or change buyer contact or shipping details on an existing checkout, run `checkout update` with its saved `checkout_id` and the complete desired `buyer` object. Use known buyer details and ask together for any missing or ambiguous fields.

- Keep the shipping address nested under `buyer`, because the CLI maps it to the checkout's fulfillment destination and buyer context. Never invent a top-level fulfillment field.

- Send the whole buyer, not only newly learned fields, because a buyer update replaces the checkout's buyer state.

- Send buyer changes alone or with delivery and discount changes. The checkout stays the same, and a buyer update needs no payment method or wallet connection.

```json
{
  "checkout_id": "<checkout_id>",
  "buyer": {
    "email": "<email>",
    "phone_number": "<phone>",
    "country_code": "<country code>",
    "address": {
      "first_name": "<first name>",
      "last_name": "<last name>",
      "street1": "<street1>",
      "street2": "<street2>",
      "city": "<city>",
      "state": "<state>",
      "postal_code": "<postal code>",
      "country": "<two-letter country>"
    }
  }
}
```

- Refresh the same checkout with `checkout get` to verify the buyer update and read its delivery options. A buyer update request does not authorize completing or charging the checkout.

- Apply promo codes by passing the complete desired set in `discount_codes`, in the same call as a delivery choice or on its own with the `checkout_id`, even when the checkout offers no delivery options. Use codes the user supplied or found in a deal search they asked for, never invent codes and do not interrupt every checkout to ask for one.

- Omit `discount_codes` to keep the existing codes, and pass an empty list to clear them. Report the applied discounts, any `result.checkout.rejected_discount_codes` and the refreshed total, because rejected codes can appear even when `ok` is true.

## Review and complete

- Show the completed quote with the masked card, items, final total and delivery choice, as the checkout review in `~/docs/chat/payments-and-purchases.md` describes. A wallet connection or an earlier request to buy does not approve this quote.

- For Link, ask for the user's explicit approval and wait. For Shop Pay, do not ask in chat, because `checkout complete` requests the wallet approval that serves as final confirmation.

- Write the completion input with only the checkout ID, the wallet provider, the exact payment-method ID from `wallet.list_payment_methods` and the selected delivery option when there is one. `wallet_provider` is `stripe_link` or `shop_pay`, spelled with an underscore here.

```json
{
  "checkout_id": "<checkout_id>",
  "wallet_provider": "<stripe_link or shop_pay>",
  "payment_method_id": "<exact payment-method id>",
  "selected_delivery_option_id": "<delivery option id, when one exists>"
}
```

```text
/opt/hatch/bin/shopify-ucp-cli checkout complete --input-file '<complete.json>'
```

- Direct Shop Pay completion pays with a one-time Shop Pay token and never exposes card details. When direct Shop Pay completion is unavailable, use the browser route rather than producing card details.

## After completion

- `ok: true` from `checkout complete` confirms the order.

- An `escalation.continue_url` from `checkout complete` means the merchant placed no order and needs the buyer to finish the checkout in the browser. Tell the user the store needs them to finish there, then start a browser task right away as **Continue in the browser** describes, opening that URL with the same wallet and card, and name the merchant's message from `result.checkout.messages` in the brief as the step to resolve. The direct payment may not carry over to that page, so when the page asks for payment the browser task pays with that wallet and card through its own payment approval; never tell it a payment was already submitted or to avoid entering payment. Do not run `order get` or retry `checkout complete`.

- Any other failure after the wallet approval, or an unknown outcome, does not prove that no order was placed, so check `order get` before saying so, and never retry or switch to the browser automatically.

```text
/opt/hatch/bin/shopify-ucp-cli order get --checkout-id '<checkout_id>'
```

- Summarize the order status, products, merchant, final amount, delivery estimate and the returned confirmation link, without raw JSON, internal IDs, buyer contact details or the shipping address.

- After a successful native completion, follow **Check order status** below to read the placed order and include its merchant order link in the completion summary. If that read fails, the successful completion still confirms the purchase: summarize its available fields, keep any returned confirmation link, and explain that current order details could not be read. Never repeat checkout to recover order details or a missing link.

- For a captured checkout, once `checkout complete` or `order get` confirms the purchase, call `browser.browse` with the original `shopify_cart.browser_task_id` to display its confirmation. Open the exact returned merchant order, confirmation or status URL for that purchase; if none was returned, refresh the existing checkout tab once. Tell the browser the purchase completed through UCP and this task is display-only: do not fill forms, prepare checkout or pay again. Failure to display confirmation does not undo the confirmed purchase.

- For a later status question about a native order confirmed in this conversation by successful `checkout complete` or `order get`, follow **Check order status** below. Keep a browser-completed Shop Pay or Link order on the browser-owned path.

- Cancel a placed order with `checkout cancel` and `{"checkout_id": "<checkout_id>"}` only when the user explicitly asks, then confirm the new state with `order get`.

## Check order status

- Use the saved `agent_state.checkout_id` from native `checkout create`, `checkout complete`, or the confirming `order get` result for that same checkout. Creation supplies an ID without confirming a purchase. Keep this ID internal.

```text
/opt/hatch/bin/shopify-ucp-cli order get --checkout-id '<checkout_id>'
```

- Read the top-level `ok` before describing the order. On success, summarize `.order.status`, the merchant's order number in `label`, `line_items`, `totals` and available fulfillment or tracking details.

- Include one clickable `[View order](<order_url>)` link by default when a merchant order, confirmation, or status URL is available from a successful native checkout result or order read for that same confirmed purchase, even when the user asked only for status. Prefer the merchant's permanent order page when available; otherwise use its confirmation URL, then its status URL. Copy the complete URL verbatim. Never invent or shorten a link or expose a checkout or order ID.

- Prefer `fulfillment.events[].tracking_url` for a shipped package's tracking link. Relay important `messages` and relevant `adjustments`, such as refunds, returns, credits, disputes or cancellations. Reads add UTC and user-local forms of provider times; an order-status message time is not a delivery time.

- If the read fails, explain the failure and keep any order link already returned for that same confirmed purchase. Never run checkout again or place another order to recover details or a link.
