## Bot detection

- Temu frequently shows “Security Verification” (“This step confirms you are a
  real person, not a robot.”), on its own page (`/bgn_verification.html`) or in
  a dialog over the login page.
- Its puzzle is a slider, such as “Slide to complete the puzzle”, that the
  accessibility tree does not expose; it needs a current screenshot. “Refresh”
  loads a different puzzle.
- Treat it as a bot challenge.
