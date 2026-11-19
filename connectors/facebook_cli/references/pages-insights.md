# Facebook Pages Insights

- These commands show how a Page the user manages is performing, from the whole Page's trend over a time window down to individual posts, so you can answer with Facebook's own numbers.

## Read Page insights and posts

```sh
/opt/hatch/bin/facebook-cli pages account-insights --page-id '<page_id>' [--time-range <LAST_7D, LAST_14D, LAST_28D (the default) or LAST_90D>] [--metrics <follower_count,views,unique_viewers,engagement_including_clicks,profile_visits,new_followers,unfollowers<!-- facebook-creators-metrics-only:start -->,net_followers,engagement<!-- facebook-creators-metrics-only:end --><!-- facebook-pages-tranche2-monetization-only:start -->,earnings<!-- facebook-pages-tranche2-monetization-only:end --><!-- facebook-creators-metrics-only:start -->,views_by_follower_status,messaging_conversations,published_content,one_minute_video_views,top_hashtag_count,top_post_format,top_reel_length,top_fans,followers_by_age,followers_by_gender,followers_by_country,followers_by_city,followers_by_age_and_gender,audience_interests,audience_format_preferences,published_content_by_type,video_views_by_upload_type<!-- facebook-creators-metrics-only:end --> (default: views,unique_viewers)>]
```

- `pages account-insights` reads the whole Page's metrics over a time window, along with the Page's name. It's the best starting point for "how is my Page doing," because it shows the overall trend before you look at individual posts.

```sh
/opt/hatch/bin/facebook-cli pages posts list --page-id '<page_id>' [--time-range LAST_28D] [--fields <views,unique_viewers,engagements,engagements_including_clicks,clicks,link_clicks,saves<!-- facebook-pages-tranche2-monetization-only:start -->,qualified_views<!-- facebook-pages-tranche2-monetization-only:end --><!-- facebook-creators-metrics-only:start -->,net_follows,negative_feedback,private_shares,interaction_rate,comment_rate,reaction_rate,share_rate,save_rate,video_view_rate,video_watch_time,video_average_watch_time,video_average_percentage_viewed,video_effective_watch_rate,video_completion_rate,video_hide_rate,video_like_through_rate,video_retention_graph,video_relative_retention_graph,views_by_country,views_by_paid_organic,views_by_follower_status,engagement_by_follower_status,views_by_audio_language,views_by_traffic_source,video_views_by_age_and_gender_bucket,share_breakdown<!-- facebook-creators-metrics-only:end --><!-- facebook-pages-tranche2-monetization-only:start -->,earnings,earnings_by_program,stars_earnings,unified_program_earnings<!-- facebook-pages-tranche2-monetization-only:end --><!-- facebook-creators-metrics-only:start -->,quality_signals<!-- facebook-creators-metrics-only:end --> (default: views,engagements)>] [--limit <1 to 10>] [--cursor '<cursor>']
```

- `pages posts list` reads the Page's recent posts in the time window, each with its metrics and activity, in one call. Most post questions can be answered from this one response, including finding a post the user describes by its caption.

```sh
/opt/hatch/bin/facebook-cli pages posts get --page-id '<page_id>' --post-ids '<up to 10 IDs>' [--fields <views,unique_viewers,engagements,engagements_including_clicks,clicks,link_clicks,saves<!-- facebook-pages-tranche2-monetization-only:start -->,qualified_views<!-- facebook-pages-tranche2-monetization-only:end --><!-- facebook-creators-metrics-only:start -->,net_follows,negative_feedback,private_shares,interaction_rate,comment_rate,reaction_rate,share_rate,save_rate,video_view_rate,video_watch_time,video_average_watch_time,video_average_percentage_viewed,video_effective_watch_rate,video_completion_rate,video_hide_rate,video_like_through_rate,video_retention_graph,video_relative_retention_graph,views_by_country,views_by_paid_organic,views_by_follower_status,engagement_by_follower_status,views_by_audio_language,views_by_traffic_source,video_views_by_age_and_gender_bucket,share_breakdown<!-- facebook-creators-metrics-only:end --><!-- facebook-pages-tranche2-monetization-only:start -->,earnings,earnings_by_program,stars_earnings,unified_program_earnings<!-- facebook-pages-tranche2-monetization-only:end --><!-- facebook-creators-metrics-only:start -->,quality_signals<!-- facebook-creators-metrics-only:end --> (default: views,engagements)>]
```

- `pages posts get` reads up to 10 posts you already know, with their lifetime metrics. Use it to compare posts the user named, or to fetch metrics `posts list` didn't include, without listing the Page's posts again.

- Each command returns only its default metrics unless you pass `--metrics` or `--fields`. Pass the ones the user asks about, such as `follower_count`, and pass every supported value when the user asks for all of them. Limit any claim about missing data to what you requested.
