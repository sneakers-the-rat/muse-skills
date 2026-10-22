# Indeed instructions

## Searching

- Enter the role in “search: Job title, keywords, or company” and the place in
  “Edit location”, replacing a prefilled location with “Clear location input”,
  then “Search”.
- Check the location and filters on the results page before comparing jobs.

## Applying

- “Apply now” starts Indeed's own application. “Apply on company site” opens
  the employer's form; continue on that destination.
- “Save job” is not an application.
- Before submitting, confirm the attached résumé and every required answer, and
  read inline validation. A login or challenge screen is not an application
  acknowledgement.

## Signing in

- Sign-in runs on secure.indeed.com: “Email address” and “Continue”, then a
  password or an emailed code. “Sign in with a code instead” switches to the
  code.
- Indeed can send a flagged anonymous visit straight to sign-in; that URL
  carries `from=bot-detection-anonymous`. When the task needs no account, treat
  that redirect as a bot challenge.

### Verification codes

- “Check your email for a code” takes the code in one “Enter code” field. The
  code expires after 10 minutes, and “Sign in” stays disabled until it is
  entered.
- Observe the page with `browser.observe` after entering the code. Use “Send new
  code” only when no code arrived; “Use a different email” changes the account.

## Bot detection

- Indeed checks visitors often, on job, search and sign-in pages. The page is
  titled “Just a moment...” or “Security Check - Indeed.com” and shows
  “Additional Verification Required” with a Cloudflare “Verify you are human”
  checkbox.
- Treat it as a bot challenge. Do not reload in a loop or reopen the job while
  it is showing; the challenge page is not the job posting.
