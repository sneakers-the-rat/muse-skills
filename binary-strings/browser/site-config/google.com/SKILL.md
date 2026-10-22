# Google instructions

## Searching

- Use the “Search” box or `/search?q=<encoded query>`. Open the result's
  destination to verify a claim; a snippet or generated answer is not the
  source page.
- AI answers can still be generating (“Thinking”, a “Generating” progress
  bar). Rely on the web results below, not on a partial answer.
- Apply region, date or result-type filters only when the task needs them. The
  location shown on the page (for example “Location·United States”, set “From
  your IP address”) describes this search's context; “Update location” changes
  it.

## Other Google products

- Google Flights, Maps, Gemini and Google Ads also live on this site, each
  with its own controls.

## Signing in

- Google account sign-in is separate from Search. It starts at an account
  chooser or an email field, then shows the password (“Enter your password”) on
  a new page; observe again with `browser.observe` after “Next” before using
  field references.
- “Verify it’s you” can ask the user to tap “Yes” on a phone prompt and then
  tap a number shown on the page. It needs the user's phone; “More ways to
  verify” lists other methods.
- A two-step verification code goes in a single field.

## Bot detection

- Google Search often answers automated queries with its “unusual traffic” page:
  “Our systems have detected unusual traffic from your computer network”, with
  the network's IP address and “Why did this happen?”. The page can carry an
  “I'm not a robot” checkbox.
- It is a challenge, not zero results. Keep the query and treat it as a bot
  challenge.
