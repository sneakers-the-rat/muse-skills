## Bot detection

- JD checks automated visits often. Its verification page is titled “京东验证”
  (on cfe.m.jd.com) and may expose no controls; read the check from the
  screenshot `browser.observe` returns.
- Treat it as a bot challenge and keep the page open. Navigating back to the
  product repeatedly does not show whether it sold out.
