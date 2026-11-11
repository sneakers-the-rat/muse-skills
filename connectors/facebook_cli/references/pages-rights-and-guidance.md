# Page content protection and creator guidance

- These commands check where a managed Page's content was copied and which disputes need its response, and search Facebook's official policies and help for creators, Pages and businesses.

- Decline a request to harass, expose or locate the people behind Content Protect matches, copies or disputes, or to deceive people about who owns content, before running any command.

- Before running any command here, choose the Page with the steps in [Facebook Pages](/opt/hatch/connectors/facebook_cli/references/pages.md), because they ask which Page the user means when more than one could match.

## Content protection

```sh
/opt/hatch/bin/facebook-cli pages copyright content-protection --page-id '<page_id>' [--limit <1 to 10, default 5>]
```

- `pages copyright content-protection` lists Content Protect matches, where the Page's content was copied, plus accounts that copy it repeatedly and disputes waiting for the Page's response.

- The command only reads. Say a match was taken down or a dispute resolved only when its returned status shows that. The user acts on matches and disputes in Content Protect on Facebook.

- Each dispute's `days_left` is the time the Page has left to respond. Give it for every dispute you mention.

## Creator guidance

```sh
/opt/hatch/bin/facebook-cli pages knowledge search --page-id '<page_id>' --query '<plain_text_query>'
```

- `pages knowledge search` answers how-to and policy questions about Facebook features for creators and businesses from official Help Center documents, with source URLs to cite. Pass the user's question as `--query`, up to 300 characters.

- The documents are general guidance, not a decision about this Page.

- When the search returns no documents, say Facebook's official guidance had no match. Don't present a rule from memory or a web page as Facebook's, because it may be outdated or wrong.
