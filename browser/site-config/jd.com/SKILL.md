# JD.com instructions

## Page setup

- jd.com can redirect to corporate.jd.com, the English company site, which
  shows no retail inventory. Open an observed shopping or product link, or the
  mobile store at m.jd.com.
- Check the selected delivery region before relying on stock or delivery
  dates.

## Product pages

- Open the product (item.jd.com or item.m.jd.com) to select its exact variant
  and quantity.
- Keep the product price apart from coupon, membership and instalment offers.

## Cart

- The cart at cart.jd.com lists items with checkboxes, and only checked items
  go to checkout. Confirm the selection and the chosen offer again before
  “去结算” (checkout), whose count shows how many items are selected.

## Signing in

- QR-code login, account-and-password login and SMS verification are different
  methods. Use the method the task names, otherwise the account form or an SMS
  code, and inspect the resulting form with `browser.observe` before signing
  in.
- The desktop sign-in (passport.jd.com) opens on “京东APP扫码登录”, a QR code for the
  JD app. Its account form takes “账号名/手机号/邮箱” and “密码”, then “登录”; “微信登录” and
  “QQ登录” are separate methods. The page can render without controls at first, so
  observe it again with `browser.observe`.
- The mobile sign-in (plogin.m.jd.com) takes a phone number in “请输入手机号”,
  sends a code with “获取验证码” and accepts it in “请输入收到的验证码”.
  “同意协议并登录” accepts JD's terms and signs in.

## Bot detection

- JD checks automated visits often. Its verification page is titled “京东验证”
  (on cfe.m.jd.com) and may expose no controls; read the check from the
  screenshot `browser.observe` returns.
- Treat it as a bot challenge and keep the page open. Navigating back to the
  product repeatedly does not show whether it sold out.
