## Bot detection

- Walmart frequently redirects to a “Robot or human?” page at `/blocked` with a
  “Press & Hold Human Challenge” button that must be held until verified. It
  can replace a search or product page.
- Treat it as a bot challenge. It is not an empty search or an unavailable
  product; keep the original task and resume once it clears.
