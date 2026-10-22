# Automatic check

The page checks the browser by itself and asks you to wait. Pages say things like "Just a moment…", "Checking your browser before accessing", "Verifying you are human. This may take a few seconds" or "Pardon our interruption".

- Assess it as `managed`, then wait for it with one `wait` action, for its widget to disappear or for the page's own text to appear. Do not observe the tab again and again while it runs.
- Do not click, reload or navigate during the check; each of these starts it over. An empty box may still be loading.
- Most checks finish within a few seconds and load the page by themselves. Assess the view the wait returns.
- A check that turns into a checkbox or a puzzle has its own guide. Assess it again with `bot_challenge.assess` and read that guide with `bot_challenge.guide`.
- A check that never starts, shows an error inside its box, or asks you to turn on JavaScript or cookies failed to run. Reload the page with `bot_challenge.recover` once.
- A check that finishes and then starts over did not accept this browser. When it starts over twice in a row, request `replace_environment` with `bot_challenge.recover`.
- When the moved tab starts over the same way, report it with `browser.report`.
