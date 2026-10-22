# Naver instructions

## Page setup

- The homepage can show a Whale browser banner (“웨일 브라우저 설치 안내”).
  Close it with “배너 닫기”.
- Search with “검색어를 입력해 주세요.”; “AI 검색” is a separate AI answer mode.

## Naver services

- Mail (“메일”), Cafe (“카페”), Blog (“블로그”), Shopping (“쇼핑”) and the other
  services open separate sites. Follow the observed destination; an app-store
  link does not open the requested web service.
- Files and photos live in MYBOX (mybox.naver.com); reservations live in
  “네이버 예약” (booking.naver.com).

## Signing in

- Sign-in is a separate page (nid.naver.com) with “ID or phone number” and
  “Password”. The login service fills the fields visible on the current page.
- After a refusal for an unbound or stale field, observe the form again with
  `browser.observe`. Never switch to password recovery to get past the error.

## Bot detection

- Bot checks appear occasionally. Treat one as a bot challenge and do not retry
  the sign-in while it is showing.
