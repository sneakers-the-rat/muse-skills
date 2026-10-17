# Health Review and Visit Preparation

## Gather the records

- Use this skill for the user's clinical records and for preparing a clinician visit. Use [Fitness Tracking](/opt/muse/skills/fitness-tracking/SKILL.md) for activity, sleep and training trends, and bring a wearable reading here once it becomes something to raise with a clinician.

- Start with the user's concern and the period to review. Retrieve the relevant labs, observations, medications, conditions and notes, and keep each result with its source, collection date, result date, units and reference range.

- Separate a recorded diagnosis from a symptom or an interpretation, and keep the user's own description of what changed.

## Check the evidence

- Report only values the records contain, and say which dates and sources you checked. Never fill a gap with a plausible value, range or interpretation.

- Compare results only when units, methods and reference ranges allow it, converting units with a valid conversion. A missing test is not a normal result.

- Look for meaningful change over time and for conflicting records. One abnormal flag or a consumer-device estimate is not a diagnosis, and a lab's interpretation flag is information, not advice.

- When the records suggest a gap, such as a condition without its usual medication, a medication without its monitoring test or a key test more than a year old, raise it as a question for the clinician, not a conclusion. If your search did not cover the full history, do not call anything missing.

## Prepare the visit

- Build a short timeline with the current concerns, relevant changes and a few prioritized questions. Mark which statements come from records, which are the user's reports and which are your interpretation.

- Name the source of each value and keep useful links. Explain a test or term with a reliable patient resource such as [MedlinePlus](https://medlineplus.gov/) or the [NHS](https://www.nhs.uk/), kept separate from the user's results.

- Give each concern a concrete next step, such as a question to ask, a test to discuss or a symptom diary to keep. Never suggest starting, stopping or changing a medicine. Put that question in the summary for the clinician instead.

- Keep the shareable summary to the requested scope, and keep clinical details out of memory and saved files unless the user asks to keep them.

- When symptoms sound urgent, advise timely care first and do not delay it to assemble a history.

## Available connectors

- [HealthEx](/opt/hatch/connectors/healthex/CONNECTOR.md) for conditions, medications, allergies, labs, vitals, immunizations and visit notes from the user's healthcare providers.

- [Function Health](/opt/hatch/connectors/function_health/CONNECTOR.md) for Function Health lab biomarkers and clinician notes.

- [Withings](/opt/hatch/connectors/withings/CONNECTOR.md) for home blood pressure, weight and ECG readings.

- [Apple Health](/opt/hatch/connectors/apple_healthkit/CONNECTOR.md) for heart rate, sleep and activity measurements from an iPhone.

- [Health Connect](/opt/hatch/connectors/google_health_connect/CONNECTOR.md) for the same measurements from an Android phone.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Zocdoc](/opt/hatch/connectors/zocdoc/CONNECTOR.md) to find a provider and open appointment times for a follow-up visit.

## Websites

- Open the user's patient or lab portal with `browser.browse` when connected records lack a result, the original report or a visit summary. Tell the task which results and dates to find and to download the official report where the portal offers one. The user signs in when the portal asks.

- [MyQuest](https://myquest.questdiagnostics.com/) for Quest Diagnostics results in the US.

- [MyLabcorp](https://patient.labcorp.com/) for Labcorp results and official report PDFs in the US.

- [NHS App](https://www.nhs.uk/nhs-app/) for GP records and test results in England.

## Alternatives for better results

- Ask for original lab reports, discharge letters or portal exports when connected records have gaps, and check conflicting values against the original report.

- For a single appointment, a focused one-page summary usually serves the user better than a complete history.

- Suggest the user bring their current medication list and recent home readings when they bear on the concern.
