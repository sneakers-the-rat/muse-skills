# DuckDuckGo instructions

## Page setup

- **Promotions.** Close a Duck.ai or other promotion with its “Dismiss” or
  “Dismiss promotion” control if it covers the page.
- **Search mode.** The homepage switches between “Search” and “Ask AI”. Keep
  “Search” unless the task asks for Duck.ai.

## Searching

- Use “Search privately” or `/?q=<encoded query>`. The script-free version at
  `html.duckduckgo.com/html/?q=<encoded query>` also serves results.
- Open a result by its title. “Search domain …” runs another search instead.
- Region (“All regions”) and Safe Search settings change results. Keep their
  current values unless the task calls for a different search.
- Duck.ai and Search Assist answers are separate from the source links.

## Bot detection

- DuckDuckGo challenges automated searches often. Its check reads
  “Unfortunately, bots use DuckDuckGo too. Please complete the following
  challenge to confirm this search was made by a human.” followed by “Select
  all squares containing a duck:”, a grid of checkboxes and “Submit”.
- A results page that keeps the search box and filters but lists no results can
  be the same block; do not conclude that nothing matches.
- Treat either as a bot challenge.
