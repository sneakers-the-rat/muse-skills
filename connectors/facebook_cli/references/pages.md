# Facebook Pages

- `pages` commands work only on Pages the user manages. The commands allow the user to read insights, publish or schedule posts, and create or edit draft posts.

- After you find the Page and handle consent below, you can read [Page insights](/opt/hatch/connectors/facebook_cli/references/pages-insights.md) to report how the Page and its posts are performing, or [Page publishing](/opt/hatch/connectors/facebook_cli/references/pages-publishing.md) to draft, publish, schedule or delete posts.

<!-- facebook-pages-tranche2-only:start -->
- Decline a Page request meant to defraud people, forge earnings statements or payment proof, or redirect someone else's payouts. Decline before running any command, including `pages list`, and don't suggest another tool or site.

<!-- facebook-pages-tranche2-only:end -->
## Find a Page

```sh
/opt/hatch/bin/facebook-cli pages list [--limit <1 to 20, default 20>] [--after '<paging.cursors.after from the previous response>']
```

- `pages list` reads the user's managed Pages. Use this to match the user's intended Page. Follow each returned `paging.cursors.after` with `pages list --after` until the Page is found or no cursor remains, because an empty page with a cursor is not the end.

- When it's unclear which Page or Pages the user means, for example they name no Page and manage more than one, or the name they give matches more than one managed Page, list the matching Pages by name and ask which they mean before running any other command for any of them, because reading or changing each Page shows or touches data from a Page the user didn't choose.

- A request for all of the user's Pages, such as "compare views across all my Pages", selects every managed Page. Run each command with each Page's own `page_id`.

- An empty `pages list` result does not prove the user manages no Pages.

- Use only the matched row's `page_id` as `--page-id` for every later `pages` command in the task, without repeating `pages list` before each one.

- Each row has `page_id`, `profile_id` and `name`, which is null when the name is unavailable. When you start from a profile ID or a pasted URL, match it to a row's `profile_id` and use that row's `page_id`. If no managed Page matches, do not use `pages` commands for it.

## Handle consent and access

- Page commands check professional consent themselves, so do not run a separate status check. When a command returns `error_reason: PROFESSIONAL_CONSENT_REQUIRED`, Muse shows the Meta Business Manager consent card. The card appears only after a Page command that ran in the foreground and finished, not after a detached background run.

- After the user accepts, run a fresh Page command through its normal approval. Consent covers Pages generally, not a particular Page, and it does not approve a write.

- The consent refusal means only that the rejected request did not run. It says nothing about an earlier attempt, so do not repeat a write whose outcome is unknown. If the refusal mentions an earlier write attempt, ask the user to check Facebook before any new attempt.

- Any other HTTP 403 from a Page command is an access failure, not a consent decision. Stop without switching identities, retrieving credentials, or calling another endpoint.

- `pages access --page-id` is an optional diagnostic of the user's permissions on a Page. It is neither a consent check nor a grant, and data reads check access on their own.

<!-- facebook-pages-tranche2-only:start -->
## Read Page details

```sh
/opt/hatch/bin/facebook-cli pages info --page-id '<page_id>'
```

- `pages info` reads what a Page the user manages shows about itself, including its About text and bio, categories, websites, public phones and emails, location, hours, action button, products it sells, username, profile link and verification.

- Answer from the fields the user asked about.

- A null or empty field means the Page doesn't list it. A field named in `field_failures` couldn't be read, and one in `truncated_fields` was shortened or left out, so report those as unavailable rather than empty.

- Hours intervals count seconds from the start of the local day, so 32400 is 9:00 AM, and a `close` past 86400 runs past midnight. Name the returned `timezone` with the times, or say it wasn't returned.

<!-- facebook-pages-tranche2-only:end -->
## Continue a list

- Pass the exact `paging.cursors.after` to `pages list --after`, or a non-null `cursor` to `posts list --cursor` with the same Page and time range.

- While a returned cursor is non-null, do not claim the list is complete, even when the current page is empty. Only a missing discovery `paging` or a null post `cursor` ends the list. A rejected cursor means starting again from the first page.
