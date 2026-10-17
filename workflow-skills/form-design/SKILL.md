# Form Design

## Start with the purpose

- This skill covers what to ask, how to ask it and how to read the answers. The tool that holds the form, whether a form service or a Muse artifact, builds it.

- Find out who will answer, how the responses will be used and which answers are essential. Ask only for what that purpose needs.

- Choose where the form lives from who answers it:
  - A form service such as Google Forms or Typeform collects answers from other people and keeps their responses.
  - A Muse app (`artifact.create_web_fullstack`) saves entries privately for the user, so it suits a personal log, tracker or check-in.
  - A shared Muse page saves nothing visitors enter, so it cannot collect responses.

- Keep contact details separate from anonymous feedback whenever combining them would break the privacy the form promises.

## Write the questions

- Ask one thing per question in neutral wording that does not suggest an answer.

- Use single choice for mutually exclusive answers, multiple choice for independent options and free text when a fixed list would miss useful information.

- Label both ends of a rating scale and keep its direction consistent across the form. Include "not applicable" when it is an honest answer.

- Make a question required only when the purpose cannot work without it. Put easy questions first and sensitive or demographic ones near the end.

## Build and test the respondent's path

- Group related questions and use branching to skip the ones that do not apply.

- Test required fields, validation and branching with representative answers, including an incomplete response. Preview the introduction, the questions and the completion message as a respondent.

- Before editing an existing form, read its structure and responses. Keep question IDs when a question's meaning stays the same.

- Tell the user when a change makes new answers incomparable with earlier ones. Rewording a question does not change what earlier respondents answered.

## Share it and read the results

- Distinguish the editable draft from the link respondents use. After an authorized publication, check that the link opens and the form accepts responses.

- Map each answer to its question's label before reporting it. Report how many people responded and how many answered each question, and keep missing answers visible.

- Do not present a self-selected sample as representative of a wider population.

- Treat respondents' names, contact details and free-text answers as private, and share only what the user's purpose needs.

## Available connectors

- [Google Forms](/opt/hatch/connectors/google_forms/CONNECTOR.md) for building, editing and publishing a form and reading its responses.

- [Google Sheets](/opt/hatch/connectors/google_sheets/CONNECTOR.md) for storing or analyzing responses in a spreadsheet.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Typeform](/opt/hatch/connectors/typeform_mcp/CONNECTOR.md) for conversational forms with logic, publishing, automations and response insights.

## Websites

- Use `browser.browse` to build or edit a form in a service the user already uses that has no connector here. Give the task the account, the form's purpose and the exact questions, and have it return the respondent link and confirm the form accepts responses.

- [Microsoft Forms](https://forms.office.com/) suits users who work in Microsoft 365.

- [Jotform](https://www.jotform.com/) suits forms that take payments or file uploads.

- [SurveyMonkey](https://www.surveymonkey.com/) suits longer surveys and recruiting respondents outside the user's own contacts.

## Alternatives for better results

- A quick poll, an email reply or a shared spreadsheet may be enough. Use a form when repeated collection, validation or branching earns the extra structure.

- Pilot the form with one or two people before sending it widely, and fix whatever confused them.

- Keep the form short and tell respondents roughly how long it takes. Fewer, sharper questions get more complete answers.

- When collecting the same information again, reuse the earlier questions unchanged so the results stay comparable.
