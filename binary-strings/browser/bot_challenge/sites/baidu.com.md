## Bot detection

- Baidu checks automated searches often. The check is “百度安全验证” on
  wappass.baidu.com, an image puzzle that exposes no controls to the
  accessibility tree; read it from the screenshot `browser.observe` returns.
- Treat it as a bot challenge. Do not resubmit the search while it is showing.
