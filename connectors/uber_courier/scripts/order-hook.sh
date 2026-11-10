#!/usr/bin/env bash
set -euo pipefail

[[ ${HATCH_HOOK_ID-} =~ ^[a-z0-9][a-z0-9_-]{0,63}$ ]]
# shellcheck source=/dev/null
source "${HATCH_HOOK_RUNTIME:?Use the registered hook runtime}"
umask 077
exec 9>"${HATCH_HOOK_STATE_DIR:?}/${HATCH_HOOK_ID}.lock"
flock -x -w 5 9

result=$(hook_state_get | python3 "$(dirname "${BASH_SOURCE[0]}")/order_hook.py" "$@")
if jq -e 'has("state")' <<<"$result" >/dev/null; then
    hook_state_set "$(jq -c .state <<<"$result")"
fi
if [[ $(jq -r '.disable // false' <<<"$result") == true ]]; then
    disable_after_run
fi
reason=$(jq -r '.reason // empty' <<<"$result")
payload=$(jq -c '.payload // {}' <<<"$result")
case $(jq -r '.decision // empty' <<<"$result") in
    wake) wake "$reason" "$payload" ;;
    silent) silent "$reason" "$payload" ;;
    *) jq 'del(.state)' <<<"$result" ;;
esac
