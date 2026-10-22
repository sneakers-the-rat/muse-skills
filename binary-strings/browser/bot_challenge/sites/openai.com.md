## Bot detection

- Checks are frequent, on sign-in and on openai.com pages such as Careers. The
  page is titled “Just a moment...” and shows “Performing security
  verification” with a Cloudflare “Verify you are human” checkbox, or
  “Verifying...” while the check runs.
- Treat it as a bot challenge. The form behind it is unusable until it clears;
  do not reload while it is verifying.
