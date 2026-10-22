# iCloud instructions

## Signing in

- Sign-in starts with “Email or Phone Number”. “Continue” can reveal the
  password field or a verification step; observe the page with `browser.observe`
  after each step.
- “Sign in with iPhone” is a device-assisted flow that needs the user's iPhone
  (iOS 17 or later).
- “Check the account information you entered and try again.” means the account
  or password was refused. Report it in `browser.report` instead of retrying.

### Verification codes

- Two-factor authentication sends a code to the user's Apple devices and shows
  six boxes, “Verification Code Digit 1” through “Digit 6”. They are one
  verification-code field: supply all six references in order, never the first
  box alone. Focus moves to the next box on its own.
- Observe the page with `browser.observe` after the code is entered. “Resend
  code” sends a new challenge; do not use it just because entry is slow. “Can’t
  get to your devices?” sends the code by text instead; use it when Muse cannot
  get the device code.

## Using iCloud apps

- Open only the requested app, such as Mail, Calendar or Reminders. Signing in
  does not grant permission to search Mail for codes that belong to another
  task.
- In Calendar, “Next day, week, or month” moves the view. Check the event's
  date, time and calendar before “Save”, then open the event to confirm it.

## Bot detection

- Bot checks are uncommon on iCloud. Sign-in more often stops at two-factor
  authentication, which is a verification step, not a bot check.
- If a bot check appears, treat it as a bot challenge and do not retry the
  sign-in while it is showing.
