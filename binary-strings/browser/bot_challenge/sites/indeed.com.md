## Bot detection

- Indeed checks visitors often, on job, search and sign-in pages. The page is
  titled “Just a moment...” or “Security Check - Indeed.com” and shows
  “Additional Verification Required” with a Cloudflare “Verify you are human”
  checkbox.
- Treat it as a bot challenge. Do not reload in a loop or reopen the job while
  it is showing; the challenge page is not the job posting.
