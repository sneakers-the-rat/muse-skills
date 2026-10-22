# Facebook instructions

## Page setup

- **Dialogs.** Close a covering login or composer dialog with its own “Close”
  control. Observe again with `browser.observe` after a dialog closes or sign-in
  changes the page; earlier references no longer apply.

## Searching and Marketplace

- “Search Facebook” searches the site; “Search Marketplace” searches listings.
- In Marketplace, check each listing's location, price and details.
- Signed out, Marketplace and its listings show a full-page “See more on
  Facebook” sign-in gate. That is a sign-in requirement, not a bot check.

## Posting

- Before publishing, check the composer's identity and destination. Posting as
  a personal profile, a Page or into a Group are different actions.
- “Add to your post” opens attachment choices. Verify uploaded media and text in
  the composer before the final publish action.
- Group posts awaiting approval are under the group's pending content.

## Signing in

- The homepage login fields can be labelled “email” and “pass”. The login
  service fills them from their current references; “Create new account” is
  registration.
- “Wrong Credentials” with “Invalid username or password” means the sign-in was
  rejected. Report it in `browser.report`; do not retry the same credentials.
- A saved session can fall back to a one-tap “Continue …” screen naming the
  account; it still needs sign-in.
- A login checkpoint is a sign-in step: a code goes through the login service,
  and a device or app approval is a step for the user. “Forgot password?” and
  “Find your account” start account recovery; never use them to get around a
  missing credential or a blocked login.

## Bot detection

- Checks are occasional. Treat a CAPTCHA or security check as a bot challenge; a
  login checkpoint stays with sign-in, as above.
