# Klaviyo instructions

## Page setup

- When the cookie banner covers the page, choose “Accept All” or “Cookie
  Settings”.

## Working in the account

- Lists and segments live under “Lists & Segments”. Tell global search,
  filtered lists and the selected row apart, and check the intended audience or
  object before editing.
- “Apply filters” changes the list; “Save” persists the current edit. Inspect
  the saved object with `browser.observe` before repeating an operation that
  seemed slow.
- Sending a campaign differs from saving a draft. Verify recipients, content
  and schedule before the final send.
- Delayed data can be a Klaviyo incident; status.klaviyo.com lists current
  ones.

## Signing in

- “Welcome back” takes “Email” and “Password”, then “Log in”. Google,
  “Passkey” and “SSO” are separate methods.

### Verification codes

- A sign-in from a new browser opens “New device login” and emails a code.
  Enter it in “Enter verification code”, then press “Log in”.
- “Didn’t receive an email?” opens the resend options; “Back to login” abandons
  the attempt.

## Bot detection

- Checks are frequent at sign-in. The login form carries reCAPTCHA, and a
  Cloudflare “I'm not a robot” checkbox can appear; “Verification failed”
  beneath it means the check did not pass.
- A full page reading “Sorry, you have been blocked” (“You are unable to access
  klaviyo.com”) is a bot wall, not an account refusal.
- Treat any of these as a bot challenge. Never reveal the password, and do not
  resubmit the form while a check is showing.
