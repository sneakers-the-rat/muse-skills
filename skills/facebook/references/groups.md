# Facebook groups

## Read a group's details

```sh
/opt/hatch/bin/facebook-cli groups details --group-id '<group ID or vanity name>'
```

- `--group-id` accepts a numeric group ID or the vanity name from a group URL such as `https://www.facebook.com/groups/<id-or-vanity>`. Pass only the path segment after `/groups/`, never the whole URL.

- The response has `name`, `about`, `visibility` (`OPEN`, `CLOSED` or `SECRET`), `history` with localized creation and name changes when visible, admin-selected `tags`, `rules` as title and description objects in the admins' order, and an approximate `member_count`.

- A missing group and a group the account cannot see return the same not-found error.

## Search groups

```sh
/opt/hatch/bin/facebook-cli groups search
/opt/hatch/bin/facebook-cli groups search --keywords 'hiking'
/opt/hatch/bin/facebook-cli groups search --sort-by LARGEST --limit 5
/opt/hatch/bin/facebook-cli groups search --role admin
/opt/hatch/bin/facebook-cli groups search --keywords 'hiking' --role any
/opt/hatch/bin/facebook-cli groups search --role connected --after '<cursor>'
```

- `--keywords` searches group names and topics. Omit it to list the user's own groups.

- `--role` sets the scope:
  - `connected`, the default, covers groups the user belongs to
  - `admin` covers groups the user administers
  - `admod` covers groups the user administers or moderates
  - `any` searches the user's groups, including private ones, then public groups, and requires `--keywords`

- `--sort-by` accepts `MOST_RELEVANT`, `LARGEST`, `LAST_VISITED`, `RECENT_ACTIVITY` or `ALPHABETICAL`. `--status` accepts `any`, `weekly_active`, `non_archived` (the default) or `archived`.

- `--limit` defaults to 25 with keywords and 10 without, up to 25.

- Results are in `groups`, each with `group_id`, `name`, `member_count`, `privacy` (`Public` or `Private`) and `group_url`. Use the ID for later reads and the URL in the answer.

- Only a listing without `--keywords` can page. Pass `paging.cursors.after` as `--after` with the other filters unchanged while it is present. A keyword search cannot take a cursor.

## Read group posts

```sh
/opt/hatch/bin/facebook-cli groups posts --group-id '<group ID>'
/opt/hatch/bin/facebook-cli groups posts --group-id '<group ID>' --sort-by MOST_REACTS --limit 5
/opt/hatch/bin/facebook-cli groups posts --group-id '<group ID>' --query 'recipe'
/opt/hatch/bin/facebook-cli groups posts --group-id '<group ID>' --min-timestamp 1750000000 --max-timestamp 1752000000
```

- Only `--group-id` is required, and `--query` filters posts by text. `--sort-by` accepts `MOST_RECENT_ACTIVITY` (the default), `NEW_POSTS` or `MOST_REACTS`.

- `--min-timestamp` keeps posts newer than a Unix time in seconds, and `--max-timestamp` keeps posts at or before one.

- `--limit` defaults to 10, up to 25. Paging with `--after` works only for `MOST_RECENT_ACTIVITY` and `NEW_POSTS`, with at most 20 posts per page, and `MOST_REACTS` returns no cursor. Keep the same group, filters and sort when continuing.
