# Fitness Tracking

## Scope the question

- Use this skill to understand activity, training, sleep, recovery and body measurements over time. Use [Workout Planning](/opt/muse/skills/workout-planning/SKILL.md) to design or change sessions, and [Health Review and Visit Preparation](/opt/muse/skills/health-review/SKILL.md) for clinical records or a summary for a clinician.

- Start from the user's question and a local date range. When they ask about recent trends without dates, use the last seven days.

## Gather comparable data

- Read phone-synced data from Apple Health on an iPhone or Health Connect on Android, plus Withings or another connected app the user relies on. Check which days and measurements each source covers before reading, and distinguish when an activity happened from when it was uploaded. Missing days are unknown, not zero.

- Use consistent units and definitions. Active, total and workout calories measure different things and must not be added together. For sleep, separate time in bed from time asleep and check which date the source assigns to an overnight session.

- When several devices record the same workout, match the records before combining totals. Prefer one consistent source with good coverage, and compare sources only when their disagreement could change the answer.

- If the user would rather not connect an app, work from the screenshots, exports or numbers they share.

## Explain the pattern

- Compare the period with a useful baseline, and note changes in devices, wear habits or routine that could explain a difference. Look for a sustained trend before drawing a conclusion from one score.

- Relate the findings to the user's goal and how they feel. Device estimates help explain training and recovery, but they do not diagnose anything.

- When a reading looks implausible or concerning, such as a very high blood pressure, an irregular-rhythm alert or a sudden jump in resting heart rate, first rule out a sync or wear error. Then report what the reading shows and when it is worth raising with a clinician. Symptoms such as chest pain or fainting need urgent care, not a trend review.

- Keep health history out of reusable skills and files. Save explicit preferences, such as goals or preferred units, where they help later.

## Available connectors

- [Apple Health](/opt/hatch/connectors/apple_healthkit/CONNECTOR.md) for steps, workouts, sleep, heart rate and other metrics from an iPhone, including data other apps share into Apple Health.

- [Health Connect](/opt/hatch/connectors/google_health_connect/CONNECTOR.md) for the same kinds of data from an Android phone.

- [Withings](/opt/hatch/connectors/withings/CONNECTOR.md) for weight, body composition, blood pressure, sleep and workouts from Withings devices.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [FORM](/opt/hatch/connectors/form_mcp/CONNECTOR.md) for workouts, weight history, training plans and nutrition trends the user logs in FORM.

## Websites

- Open the user's account on a platform without a connector with `browser.browse`. Give the task the dates and measures needed, have it read or export those records, and ask for each figure with its date, unit and the platform's definition.

- [WHOOP](https://app.whoop.com/) for WHOOP's Recovery and Strain scores, which stay in WHOOP. The WHOOP app's Data Export also emails CSV files the user can share.

- [Garmin Connect](https://connect.garmin.com/) for Garmin activities, sleep and training history.

- [Strava](https://www.strava.com/) for recorded runs, rides and other activities.

## Alternatives for better results

- Many wearable apps can share their data into Apple Health or Health Connect once the user turns that on in the app, which lets you read it directly.

- Training logs and the user's own sense of effort, recovery and symptoms add context a wearable misses.

- When measurements disagree, check wear time, definitions and recording conditions. Keep the disagreement visible when there is no sound reason to prefer one reading.
