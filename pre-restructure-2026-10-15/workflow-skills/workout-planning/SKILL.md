# Workout Planning

## Start from the user

- Know the user's goal and any injury, condition or clinician restriction before writing a program, and ask once if either is unknown. If they would rather not share health details, keep to general, low-risk guidance that does not depend on them.

- Use their available time, equipment, experience and recent training. When one of these is missing, state your assumption, choose a conservative default and invite correction instead of asking a string of questions.

- Base starting loads on work the user can already do. Recent training and recovery data can inform the plan, as [Fitness Tracking](/opt/muse/skills/fitness-tracking/SKILL.md) describes, but a wearable score never decides it alone.

## Write sessions the user can follow

- Give the program a clear purpose and say how it progresses. Each session needs a warm-up, the exercises or intervals, sets and repetitions or duration, an effort target, rest and a cool-down.

- Without known recent loads, set effort with reps in reserve or a 1 to 10 effort scale instead of invented weights or percentages. Do not prescribe one-repetition-max testing to a beginner or to someone without a spotter or safety equipment.

- Leave at least 48 hours before training the same muscle group hard again, and build lighter weeks into longer programs.

- Offer a practical substitute when equipment, space or time is short. Teach an unfamiliar movement with its setup and one technique cue or a reliable demonstration, or swap in a familiar, safer movement.

## Adjust from what happened

- Decide whether to repeat, ease or progress a session from the work actually completed, the effort reported and recovery. A planned session is not a completed one, and stored data is never a live reading.

- Honor pain and restrictions by modifying, substituting or stopping, never by pushing through. A training plan cannot establish the cause of pain.

- If the user reports chest pain, dizziness, faintness or sudden sharp pain while exercising, tell them to stop and to seek urgent care if it is severe or does not settle, before any other coaching. A normal-looking heart rate or pace never overrules what they feel.

- Do not set or adjust medication doses around exercise, including insulin. That belongs with the user's care team.

## Available connectors

- [Peloton](/opt/hatch/connectors/peloton/CONNECTOR.md) to find classes that fit the plan and add, move or remove them on the user's Peloton schedule.

- [Apple Health](/opt/hatch/connectors/apple_healthkit/CONNECTOR.md) for recent workouts, heart rate and sleep from an iPhone.

- [Health Connect](/opt/hatch/connectors/google_health_connect/CONNECTOR.md) for the same data from an Android phone.

- [Withings](/opt/hatch/connectors/withings/CONNECTOR.md) for weight, body composition and sleep trends.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- Read recovery or training data from a platform without a connector with `browser.spawn_task`, giving the task the dates and measures to return. Share exercise demonstrations and guided workouts as links.

- [WHOOP](https://app.whoop.com/) for the day's Recovery and recent Strain when deciding whether to push or ease a session.

- [ACE Exercise Library](https://www.acefitness.org/resources/everyone/exercise-library/) for movement descriptions, photos and demonstration videos.

- [Nike Training Club](https://www.nike.com/ntc-app) for free guided workouts the user can follow at home or in a gym.

## Alternatives for better results

- Compare a gym session with a home, bodyweight or shorter version that serves the same goal. Favor a routine the user can repeat over a more elaborate plan they cannot fit in.

- Offer a check-in with `cron.add` after the first week or two to adjust the plan from the sessions actually completed.

- Suggest a coach or physical therapist when technique, an injury or a condition needs hands-on assessment.
