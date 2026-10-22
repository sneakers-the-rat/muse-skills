## Bot detection

- Bot checks are occasional here. Sign-in is where Apple most often stops
  automation: after the password it can open an “Account Repair” frame. A frame
  that keeps loading without rendering is a bot check; treat it as a bot
  challenge first. A rendered one is an account security step, not a
  successful sign-in; report it in `browser.report` instead of starting account
  recovery.
- When a check or block page replaces the store, treat it as a bot challenge.
