# Facebook reactions

```sh
/opt/hatch/bin/facebook-cli post reactions read --post-id '<post ID>'
```

- This command returns a post's current reaction totals only. `summary.total_count` is the total, and `summary.reaction_counts` lists `reaction_type` and `count` pairs such as Like, Love, Wow, Haha, Sad, Angry, Thankful and Care.

- `data` is always empty because the command does not return the people who reacted. If the user asks who reacted or who liked a post, say that list is not available and offer the counts by type.

## Present reactions

- Compare posts with their actual numbers and a link to each post. Do not call a post very popular or viral without the numbers that support it.

- There is no filter by reaction time. Selecting posts from the past week still returns each post's current totals, so state the period used to select the posts and keep that distinction clear.

- Map common words to reaction types without an extra question. Funny or laughing means Haha, sad means Sad, angry or mad means Angry, and hearts or love means Love. Ask only when the intended type remains unclear.
