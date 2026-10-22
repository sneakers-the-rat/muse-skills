## Bot detection

- Zillow frequently refuses pages with “Access to this page has been denied”
  and a “Press & Hold” button, often on a single listing while other listings
  still open. During sign-in the same check appears as a “Before we continue”
  panel.
- These pages can expose nothing to the accessibility tree; read them from the
  screenshot `browser.observe` returns.
- Treat it as a bot challenge.
