# Price and Stock Checks

Use this for a current price, stock or availability check on a specific product at a known store, whether the user asks once or a scheduled watch runs it.

## Read the product page first

- Find the store's page for the exact product: a link the user gave, one saved with the watch or in memory, or one returned by `browser.search`. Search results are often news or deal posts; open only the store's own product page. Never construct a URL.

- Open it with `browser.open` and set `max_age_minutes` to the oldest copy that still answers the question.

- For a one-time check that needs a page newer than 30 minutes, such as a drop the user says is happening right now, start a browser task with `browser.browse` when the page's crawl time is older than that, even though `browser.open` succeeded.

- Answer from the page when it is the product page you meant, not a robot check, access-denied page, error page or a different product, and its text states the price or stock you need. The `## Product Offer` block near the end gives the page's main price and availability; when it disagrees with the page's own buy button or stock text, the page text wins. Name the store and say you read its product page.

## Fall back to the live browser

Start a live browser task with `browser.browse` instead when:

- the read failed;
- the page is a robot check, sign-in wall, error page or the wrong product, or its text does not state the price or stock;
- the user needs a size, color, edition, quantity, location or delivery date the page text does not settle, since the offer block covers only the page's default option;
- the answer depends on a cart, a member price, a sign-in, store pickup or one store location's inventory.

When a browser task reports the store's product page URL, keep it so the next check can start with `browser.open`: while setting up a watch in chat, put it in the watch job; during a scheduled run, append it to `~/memory/YYYY-MM-DD.md`.

A failed read says nothing about the product. Do not report the item as out of stock or unavailable because of it.

## Scheduled watches

- When you set up a restock or price watch on a product page, save the page's URL with the watch and write the job's `body` so each run reads that URL with `browser.open` and a stated `max_age_minutes` first, and starts a browser task only on the fallback conditions above. Set that number to the watch's interval in minutes.

## Available connectors

- Use `muse.connector_search` to find a connector that reports this store's live stock or prices, and `muse.skill_search` to find related skills such as Deal Monitoring.
