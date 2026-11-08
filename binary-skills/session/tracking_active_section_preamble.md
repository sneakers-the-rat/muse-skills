These are your currently active tracked items; close an item with `tracking.set_status` set to `completed` when user confirmation, the end of its relevant timeline, or other evidence shows that the whole responsibility has finished.
Close the tracked item proactively when the evidence shows it is finished, without waiting for the user to explicitly ask you to close it.
failed to load goals prompt snapshot; rendering empty goals sectiongoals prompt snapshot timed out; rendering empty goals sectionrelationship connection context unavailablerelationship connection context timed outmemory/people/memory/groups/md connection context unavailablefailed to load paired-device prompt snapshot; omitting devices sectionpaired-device prompt snapshot timed out; omitting devices section%Y-%m-%d %H:%Mchat.read_historybrowser/site_egresslast_auditlast_buildselect exists(select 1 from spaces.user_state
         where sharing_state is null or accessed_at_ms is not null
           or last_opened_at_ms is not null or frequency_score is not null
           or favorite_order is not null)insert into spaces.user_state (space_slug, favorite_order, is_favorite) values library on conflict (space_slug) do update set
            favorite_order = excluded.favorite_order, is_favorite = true
          where spaces.user_state.sharing_state is not null
            and spaces.user_state.accessed_at_ms is null
            and spaces.user_state.last_opened_at_ms is null
            and spaces.user_state.frequency_score is null
            and spaces.user_state.favorite_order is null, true)content-typeacceptx-typesafe-request-id
SELECT pg_advisory_xact_lock(hashtextextended(agent_id, $2))
FROM unnest($1::text[]) AS locked(agent_id)
ORDER BY agent_id
SELECT pg_advisory_xact_lock_shared(hashtextextended($1, 0))agent.volatile_context_pins.lifecycleSELECT pg_advisory_xact_lock(hashtextextended($1, 0))
WITH owners AS MATERIALIZED (
    SELECT DISTINCT agent_id COLLATE "C" AS agent_id
    FROM unnest($1::text[]) AS input(agent_id)
)
SELECT pg_advisory_xact_lock(hashtextextended($2 || agent_id, 0))
FROM owners ORDER BY agent_id COLLATE "C"
agent.volatile_context_pins:select owner_agent_id from runtime.browser_tasks where task_id = $1 and status = 'running' for updateannotation rendering worker failedrequested program frame was not retainedprogram frame has no pixelssaved image batch reader failedretained image reader failed# Dev-notice audit log — APPEND ONLY.
#
# Add a [[version]] entry only when a deploy must correct already-live sessions'
# stale/poisoned history (tool/skill/API renames, deprecated capabilities,
# incident corrections), labeled with a `notify` mode. Do not use this ledger
# for ordinary prompt wording or behavior tuning.
#
# The same machinery also delivers opt-in deploy/incident notices (set `kind`,
# omit `hash`). Full schema + semantics: 