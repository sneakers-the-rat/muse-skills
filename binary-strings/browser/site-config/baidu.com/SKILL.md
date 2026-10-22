# Baidu instructions

## Searching

- The homepage search box can have no accessible name. Type into it and
  submit with “百度一下”, or open `/s?wd=<encoded query>` directly.
- Open a result's destination to verify it. A result about a login page is not
  that site's login form.

## Signing in

- “登录” means sign in and “立即注册” means create an account; choose the
  operation the task asks for. Sign-in runs on passport.baidu.com
  (“登录百度账号”).
- Baidu Netdisk (pan.baidu.com) shows its file list, “全部文件”, only after
  sign-in.

### Verification codes

- “发送验证码” sends a code. Keep that challenge open; the login service fills
  “验证码”, and another send can change which code the form expects.

## Bot detection

- Baidu checks automated searches often. The check is “百度安全验证” on
  wappass.baidu.com, an image puzzle that exposes no controls to the
  accessibility tree; read it from the screenshot `browser.observe` returns.
- Treat it as a bot challenge. Do not resubmit the search while it is showing.
