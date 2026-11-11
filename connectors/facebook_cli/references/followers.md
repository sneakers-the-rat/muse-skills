# Followers and following

- These commands list the people and Pages that follow the user or a Page they manage, and the people and Pages each of them follows. They return names and profile types, not a follower total.

- Decline to sort people in these lists by traits such as relationship status, health, beliefs or where they live, to pick people to target or contact, or to locate or contact someone who has blocked or avoided the user, before running any command.

- Before running a `pages` command here, choose the Page with the steps in [Facebook Pages](/opt/hatch/connectors/facebook_cli/references/pages.md), because they ask which Page the user means when more than one could match.

## Followers

```sh
/opt/hatch/bin/facebook-cli me followers [--limit <1 to 20, default 20>] [--cursor '<cursor from the previous result>']
```

- `me followers` lists the people and Pages that follow the user's profile.

```sh
/opt/hatch/bin/facebook-cli pages followers --page-id '<page_id>' [--limit <1 to 20, default 20>] [--cursor '<cursor from the previous result>']
```

- `pages followers` lists the people and Pages that follow a Page the user manages.

- These lists have no total. When the user asks how many people follow them, don't run a list just to count it. Say Facebook doesn't return a follower count for their profile, and offer to list who follows them. A managed Page's count comes from `pages account-insights --metrics follower_count`.

## Following

```sh
/opt/hatch/bin/facebook-cli me following [--limit <1 to 20, default 20>] [--cursor '<cursor from the previous result>']
```

- `me following` lists the people and Pages the user follows.

```sh
/opt/hatch/bin/facebook-cli pages following --page-id '<page_id>' [--limit <1 to 20, default 20>] [--cursor '<cursor from the previous result>']
```

- `pages following` lists the people and Pages that a Page the user manages follows.

## Read and present the lists

- A question about the user's own followers or following is about their profile. Read a Page's lists only when the user asks about that Page.

- A non-null `cursor` means the list continues. Pass it as `--cursor` to the same command, with the same `--limit`, for the next page, and read the whole output so the cursor isn't cut off. Read further pages only when the user asks for more or for everyone, and say the list continues when you stop.

- Summarize the people instead of pasting the list. Say how many you read, how many are people and how many are Pages, and name a few when that helps. List every name only when the user asks for the full list, and keep it in your reply rather than a saved file unless they ask you to save it.

- Rows come in Facebook's order, which is not a ranking by closeness or activity. Each row's `follower_count` counts that profile's own followers.

- `available: false` with empty `results` means Facebook returned no list for this profile, not that nobody follows the user. Share the returned `message` and give no count.

- `item_failures` lists rows Facebook couldn't read, so mention them rather than treating the page as complete.

- These lists cover only the user and the Pages they manage. For anyone else's followers, or a Page the user doesn't manage, say these commands can't list them.
