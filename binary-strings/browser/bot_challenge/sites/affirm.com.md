## Bot detection

- Affirm's sign-in sometimes fails for automated browsers with an error page:
  “This page isn't loading right now” and “We can't reach this page”, with a
  “Go back” button. It is not a puzzle and says nothing about the account.
- Treat it as a bot challenge. Do not reload the sign-in page in a loop.
