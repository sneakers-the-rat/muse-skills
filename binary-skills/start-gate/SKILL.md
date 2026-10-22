# Start gate

One button opens a challenge or lets you through. It reads like "Begin", "Start puzzle" or "Continue".

- Click the button by its reference, or describe it in `look` with the widget's reference in `within` when it has none.
- What follows is usually another challenge with its own guide. Assess it again with `bot_challenge.assess`, including that guide's name.
- A button that does nothing may still be loading. Wait for the widget to change with a `wait` action before you click again.
