# Facebook profiles

```sh
/opt/hatch/bin/facebook-cli profile info --profile-id '<profile ID from earlier output>'
```

- Use `profile info` for the directory details of a person already identified through this connector. Pass only a profile ID returned earlier in this conversation, as [the connector doc](../CONNECTOR.md) explains, and never use it to enumerate profiles.

## Read the details

- The response can include `name`, `profile_picture_url`, `vanity_url` such as `facebook.com/username`, `bio`, `current_city`, `hometown`, `birthdate`, `gender`, `languages` and `hobbies`. The city, hometown, birthdate and gender are what the person stated.

- `work` entries contain `employer` and `position`, `education` entries contain `school`, `type` and `degree`, and `life_events` entries contain `title` and `date`.

## Present a profile

- Answer the requested question from these fields with the person's profile link.

- Say "not listed" for every requested field that is null, empty or absent rather than leaving it out.

- Show every work and education entry in chronological order where dates allow, and say "not listed" for a missing part of an entry.

- Do not infer personality, lifestyle or character from profile details.
