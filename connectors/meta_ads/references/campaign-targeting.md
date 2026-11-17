# Resolve Meta targeting

Use this guide when the audience includes an interest, language or place that isn't yet a country code or a result returned in this conversation.

- One `ads_targeting_search` call covers every candidate. Interests come from the advertiser, or from a few the product, Page and matching history support, and they're only ideas until the search returns them. With weak evidence there's no interest search, and Advantage+ Audience stays broad.

- A search rejected as a restricted topic means that audience can't be targeted, and similar terms for the same people can't either. Tell the advertiser it's unavailable, and keep the audience broad or use what they can target.

- A place is searched by its real name, with its country code and the matching `location_type_hint` from the schema. A radius applies only to an address or a specific place.

- A returned place matches only when its name, type, country and region all fit.

- Only returned results are used: `targeting_results` for interests, `location_results` for places and `locale_results` for languages. Each keeps its key or ID for pricing and creation. A place inside a country you also target conflicts with it, so the audience lists one or the other. If the create schema has no slot for a place type or radius, say so.

- IDs stay out of the reply. When several places fit, choose only when the advertiser's words or business evidence point to one; otherwise ask.

- A partial result is final for that round. Search again only with new information from the advertiser.

- An unresolved place stays open rather than widening to its country. An unresolved interest or language is left out, and the plan doesn't claim it.

- Advantage+ Audience can expand interests but keeps the chosen geography. Saved and custom audiences use their own tools.
