# Facebook friends

- `me friends` searches the user's friends by name, profile details, interests or upcoming birthdays.

## Search by name or profile details

```sh
/opt/hatch/bin/facebook-cli me friends
/opt/hatch/bin/facebook-cli me friends --name 'Sarah'
/opt/hatch/bin/facebook-cli me friends --city 'New York' --work 'Google'
/opt/hatch/bin/facebook-cli me friends --city 'Seattle' --education 'Stanford' --filter-mode OR
```

- Filter with `--name` (or `-n`), `--city` for the current city, `--hometown`, `--work` for an employer or job title and `--education` for a school. Each is a case-insensitive substring match.

- Several filters must all match by default. `--filter-mode OR` returns friends who match any of them.

- Without filters, the command returns close friends first. Each friend in `data` has `friend_id`, `name`, `profile_url` and, when available, `match_context`.

- Pages hold at most 20 friends, and larger `--limit` values are capped. Pass `paging.cursors.after` back as `--after` with the same filters. A cursor from one filter set is not valid for another, and a missing cursor means the list has ended.

## Find upcoming birthdays

```sh
/opt/hatch/bin/facebook-cli me friends --birthday-within-days
/opt/hatch/bin/facebook-cli me friends --birthday-within-days 30
```

- Use this for questions such as whose birthday is coming up. The flag without a number covers the next seven days, which fits a request with no timeframe. A number covers the next 1 to 365 days.

- For a calendar period such as the rest of this month, choose a number of days that covers the period and keep only friends whose returned `birthday_date` falls inside it.

- Each friend gains `birthday_date` in `YYYY-MM-DD` form, and results are ordered by the next birthday. Follow the page cursor as needed.

- Friends who hide their birthday are excluded, so the result is not a complete birthday calendar. This mode ignores every other filter, including `--name` and `--json-query`.

## Search by interest

- Use `--json-query` with a FindPeople query for interests, sports, entertainment and similar topics. Put the user's `fb_user_id` from `me` in `friend_by`:

```sh
/opt/hatch/bin/facebook-cli me friends --json-query '{
  "intent": "FindPeople",
  "target": "users",
  "filters": {
    "friend_by": ["<fb_user_id from me>"],
    "topic": ["hiking"]
  }
}'
```

- Choose the filter key from the user's intent:
  - `topic` for interests and hobbies, such as friends who like hiking or cooking
  - `sports` for teams and sports, such as friends who play soccer
  - `company` for an employer and `job` for a job title
  - `college` for a college or university and `school` for any school
  - `location` for the current city and `hometown` for a hometown
  - `movies`, `music`, `tv_shows`, `books`, `games` or `podcasts` for entertainment, such as friends who watch a particular show

- The interest key is `topic`, never `interests`. Values are lists, such as `["seattle seahawks"]`.

- This search returns one result set of at most 20 friends. It has no paging, so `--after` has no effect, and you refine the query instead of paging.

- Do not scan friends' posts, timelines, groups or Page likes to infer interests this lookup does not establish.

## Explain a match

- `match_context` can contain `groups`, `pages` and `profile_details`. Topic matches usually come from groups and Pages, sports and entertainment from Pages, and work, school and location from profile details.

- Group context carries tagged text with `GROUP_NAME` and `GROUP_DESCRIPTION`. Page context uses `PAGE_NAME`, `PAGE_CATEGORY` and `PAGE_DESCRIPTION`, and profile details are plain text such as "Works at Acme Corp".

- Extract the readable names instead of showing tags, such as "member of the Hiking Enthusiasts group" or "follows the Home Cooking Tips Page". Describe the actual evidence, because membership in a hiking group does not show that someone hikes regularly.
