# Reddit instructions

## Searching and reading

- “Search Reddit” can be limited to a community or profile. A community limit
  shows “Remove r/… filter and expand search to all of Reddit”, and a profile
  search reads “Search in u/…”. Remove the limit only when the task needs a
  site-wide search.
- Sorting (“Sort by: Best”) and “Next page” change the visible posts. Open the
  thread and read its comments instead of relying on the result excerpt.
- Use the normal pages, not `.json` endpoints, which answer automated access
  with “You've been blocked by network security.”

## Signing in

- The login form takes “Email or username” and “Password”; “Log In” stays
  disabled until both are filled.
- Password login, “Email me a one-time link”, “Continue with Phone Number” and
  Google or Apple are different methods. Stay in the flow you chose as the form
  advances.

### Verification codes

- Two-factor accounts ask you to “Enter the 6-digit code from your
  authenticator app” in one “Verification code” field, then “Check code”.
- “Use a backup code” expects a different credential. Switch only when the user
  provides one.

## Bot detection

- Reddit checks automated visits often, sometimes on the first page load.
  “Prove your humanity” (“Complete the challenge below…”) is a challenge page,
  not an empty feed, and its widget can load after the heading. An “I'm not a
  robot” checkbox is the same kind of check.
- Treat either as a bot challenge. Do not reload or retry the login while it is
  showing.
