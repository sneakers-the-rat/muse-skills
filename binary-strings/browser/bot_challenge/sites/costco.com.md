## Bot detection

- Costco blocks automated browsing often, and usually silently: a sign-in that
  returns the same form with no error, or search results that stay on
  “Loading”.
- Submit sign-in once. If the form comes back unchanged, or results never load,
  treat it as a bot challenge rather than resubmitting.
