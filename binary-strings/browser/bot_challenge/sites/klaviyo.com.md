## Bot detection

- Checks are frequent at sign-in. The login form carries reCAPTCHA, and a
  Cloudflare “I'm not a robot” checkbox can appear; “Verification failed”
  beneath it means the check did not pass.
- A full page reading “Sorry, you have been blocked” (“You are unable to access
  klaviyo.com”) is a bot wall, not an account refusal.
- Treat any of these as a bot challenge. Never reveal the password, and do not
  resubmit the form while a check is showing.
