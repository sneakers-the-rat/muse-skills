"""Bounded Uber order detector; the shell adapter owns hook state and decisions."""

import argparse
import hashlib
import json
import math
import os
import subprocess
import sys
import time
import uuid

MAX_DURATION = 3 * 60 * 60
ORDER_PREFIX = "FULFILLMENT_ORDER_STATE_"
JOB_PREFIX = "FULFILLMENT_JOB_STATE_"
TERMINAL_ORDERS = {ORDER_PREFIX + s for s in ("COMPLETED", "CANCELED", "FAILED")}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def observation(response, order_id):
    if not isinstance(response, dict) or response.get("ok") is not True:
        raise ValueError("order_read_failed")
    order = response["body"]["order"]
    if str(uuid.UUID(order["order_id"])) != order_id:
        raise ValueError("wrong_order")
    order_state = order["order_state"]
    if not isinstance(order_state, str) or not 0 < len(order_state) <= 128:
        raise ValueError("invalid_order_state")
    jobs = order.get("fulfillment_jobs", [])
    if not isinstance(jobs, list) or len(jobs) > 32:
        raise ValueError("invalid_jobs")
    compact = []
    for job in jobs:
        job_id, job_state = job["job_id"], job["job_state"]
        if not all(
            isinstance(v, str) and 0 < len(v) <= 128 for v in (job_id, job_state)
        ):
            raise ValueError("invalid_job")
        context = job.get("transport_provider_context") or {}
        provider = context.get("transport_provider") or {}
        vehicle = context.get("vehicle") or {}
        identity = [provider.get("transport_provider_id")]
        if not identity[0]:
            identity = [
                provider.get("first_name"),
                provider.get("last_name"),
                vehicle.get("license_plate"),
            ]
        if not all(
            v is None or isinstance(v, str) and len(v) <= 1024 for v in identity
        ):
            raise ValueError("invalid_provider")
        compact.append(
            {
                "job_id": job_id,
                "state": job_state,
                "courier": fingerprint(identity) if any(identity) else None,
            }
        )
    if len({j["job_id"] for j in compact}) != len(compact):
        raise ValueError("duplicate_job")
    return {
        "order_state": order_state,
        "jobs": sorted(compact, key=lambda j: j["job_id"]),
    }


def read_order(order_id):
    try:
        result = subprocess.run(
            ["/opt/hatch/bin/uber-courier", "get-order", "--order-id", order_id],
            capture_output=True,
            timeout=12,
            check=False,
        )
        if len(result.stdout) > 2 * 1024 * 1024:
            return {}
        response = json.loads(result.stdout)
        if result.returncode != 0 and isinstance(response, dict):
            response["ok"] = False
        return response
    except (OSError, subprocess.TimeoutExpired, ValueError):
        return {}


def baseline(state, hook_id, order_id, now, ttl, *, restart_expired=False):
    order_id = str(uuid.UUID(order_id))
    if not 60 <= ttl <= MAX_DURATION:
        raise ValueError("duration must be 60 through 10800 seconds")
    if state:
        validate(state, hook_id)
        if state["order_id"] != order_id:
            raise ValueError("hook already belongs to another order")
        if restart_expired:
            if now < state["expires_at"]:
                raise ValueError("monitor has not expired")
            pending = state["pending"] or {}
            if any(
                snapshot and snapshot.get("order_state") in TERMINAL_ORDERS
                for snapshot in (state["seen"], pending.get("snapshot"))
            ):
                raise ValueError("terminal order cannot be monitored again")
            state.update(
                created_at=now,
                expires_at=now + ttl,
                pending=None,
                next_wake_at=now,
                last_success_at=now,
                revision=state["revision"] + 1,
            )
            return {"ok": True, "expires_at": state["expires_at"], "state": state}
        return {
            "ok": True,
            "already_configured": True,
            "expires_at": state["expires_at"],
        }
    if restart_expired:
        raise ValueError("restart requires an existing monitor")
    return {
        "ok": True,
        "expires_at": now + ttl,
        "state": {
            "version": 1,
            "hook_id": hook_id,
            "order_id": order_id,
            "created_at": now,
            "expires_at": now + ttl,
            "seen": None,
            "pending": None,
            "next_read_at": now,
            "next_wake_at": now,
            "last_success_at": now,
            "failures": 0,
            "unavailable_reported": False,
            "revision": 0,
        },
    }


def validate(state, hook_id):
    counters = (
        "created_at",
        "expires_at",
        "next_read_at",
        "next_wake_at",
        "last_success_at",
        "failures",
        "revision",
    )
    if (
        not isinstance(state, dict)
        or not all(type(state[k]) is int and state[k] >= 0 for k in counters)
        or state["version"] != 1
        or state["hook_id"] != hook_id
        or not 60 <= state["expires_at"] - state["created_at"] <= MAX_DURATION
        or type(state["unavailable_reported"]) is not bool
        or not (state["seen"] is None or isinstance(state["seen"], dict))
        or not (state["pending"] is None or isinstance(state["pending"], dict))
        or str(uuid.UUID(state["order_id"])) != state["order_id"]
    ):
        raise ValueError("invalid_monitor_state")
    if state["pending"] is not None:
        pending = state["pending"]
        if (
            not isinstance(pending["event_id"], str)
            or len(pending["event_id"]) != 64
            or not isinstance(pending["reason"], str)
            or not (
                pending["snapshot"] is None or isinstance(pending["snapshot"], dict)
            )
        ):
            raise ValueError("invalid_pending_event")


def decision(state, reason, payload=None, *, wake=False, disable=False):
    return {
        "state": state,
        "decision": "wake" if wake else "silent",
        "reason": reason,
        "payload": payload or {},
        "disable": disable,
    }


def changed(state, now, reason, snapshot=None, *, disable=False, error=None):
    pending = state["pending"]
    if not pending or pending["reason"] != reason or pending["snapshot"] != snapshot:
        state["revision"] += 1
        state["pending"] = {
            "event_id": fingerprint([state["order_id"], state["revision"]]),
            "snapshot": snapshot,
            "reason": reason,
        }
    event_id = state["pending"]["event_id"]
    if now < state["next_wake_at"] and not disable:
        return decision(state, "update_pending")
    # A rejected wake remains pending until a worker acknowledges it. Limit re-wakes
    # while a worker is running; changed observations replace the pending snapshot.
    state["next_wake_at"] = now + 120
    payload = {
        "order_id": state["order_id"],
        "event_id": event_id,
        "previous": state["seen"],
        "current": snapshot,
        "expires_at": state["expires_at"],
    }
    if state["failures"]:
        payload["read_cooldown_until"] = state["next_read_at"]
    if error:
        payload["error"] = error
    return decision(state, reason, payload, wake=True, disable=disable)


def read_snapshot(state, now, fetch):
    response = fetch(state["order_id"])
    try:
        snapshot = observation(response, state["order_id"])
    except (KeyError, TypeError, ValueError, AttributeError):
        state["failures"] = min(state["failures"] + 1, 10)
        body = response.get("body") if isinstance(response, dict) else None
        error = body.get("error") if isinstance(body, dict) else None
        if not isinstance(error, dict):
            error = {}
        cooldown = error.get("retry_after_seconds")
        delay = min(300, 30 * 2 ** (state["failures"] - 1))
        if (
            type(cooldown) is int or type(cooldown) is float and math.isfinite(cooldown)
        ) and cooldown > 0:
            delay = max(delay, math.ceil(cooldown))
        state["next_read_at"] = now + delay
        diagnostics = {k: error[k] for k in ("code", "status") if k in error}
        return None, response, diagnostics
    state.update(
        failures=0,
        next_read_at=now + 15,
        last_success_at=now,
        unavailable_reported=False,
    )
    return snapshot, response, {}


def awaiting_courier(snapshot):
    return snapshot["order_state"] in {
        ORDER_PREFIX + "CREATED",
        ORDER_PREFIX + "ACTIVE",
    } and all(
        j["courier"] is None
        and j["state"] in {JOB_PREFIX + "CREATED", JOB_PREFIX + "MATCHING"}
        for j in snapshot["jobs"]
    )


def poll(state, hook_id, now, fetch=read_order):
    try:
        validate(state, hook_id)
    except (KeyError, TypeError, ValueError, AttributeError):
        return {
            "decision": "wake",
            "reason": "monitor_state_unavailable",
            "payload": {"needs_review": True},
            "disable": True,
        }
    # Stop only after the terminal update was handled. A worker whose verification
    # read fails must not consume the last progress update by disabling its hook.
    if state["seen"] and state["seen"].get("order_state") in TERMINAL_ORDERS:
        return decision(state, "terminal_order_handled", disable=True)
    if now >= state["expires_at"]:
        return changed(state, now, "monitor_deadline_reached", disable=True)
    if now < state["next_read_at"]:
        return decision(state, "read_cooldown")
    snapshot, _, diagnostics = read_snapshot(state, now, fetch)
    if snapshot is None:
        if now - state["last_success_at"] >= 300 and not state["unavailable_reported"]:
            return changed(state, now, "tracking_unavailable", error=diagnostics)
        return decision(state, "read_unavailable")
    if state["seen"] is None and awaiting_courier(snapshot):
        state["seen"] = snapshot
    if snapshot == state["seen"]:
        state["pending"] = None
        state["next_wake_at"] = now
        return decision(state, "order_unchanged")
    return changed(state, now, "order_state_changed", snapshot)


def acknowledge(state, hook_id, event_id):
    validate(state, hook_id)
    pending = state["pending"]
    if not pending or pending["event_id"] != event_id:
        return {"ok": True, "acknowledged": False}
    if pending["snapshot"] is not None:
        state["seen"] = pending["snapshot"]
    if pending["reason"] == "tracking_unavailable":
        state["unavailable_reported"] = True
    state.update(pending=None, next_wake_at=0)
    return {"ok": True, "acknowledged": True, "state": state}


def status_summary(snapshot, previous, response):
    if snapshot is None:
        return {}
    provider_jobs = (
        response.get("body", {}).get("order", {}).get("fulfillment_jobs", [])
    )
    names = {}
    for job in provider_jobs:
        provider = (job.get("transport_provider_context") or {}).get(
            "transport_provider"
        ) or {}
        name = provider.get("first_name")
        if isinstance(name, str) and 0 < len(name) <= 128:
            names[job["job_id"]] = name
    jobs = []
    for job in snapshot["jobs"]:
        summary = {"status": job["state"].removeprefix(JOB_PREFIX).lower()}
        if job["job_id"] in names:
            summary["courier_name"] = names[job["job_id"]]
        jobs.append(summary)
    old_couriers = {
        j["courier"] for j in (previous or {}).get("jobs", []) if j["courier"]
    }
    couriers = {j["courier"] for j in snapshot["jobs"] if j["courier"]}
    return {
        "order_status": snapshot["order_state"].removeprefix(ORDER_PREFIX).lower(),
        "jobs": jobs,
        "courier_changed": bool(old_couriers and couriers and old_couriers != couriers),
    }


def verify_event(state, hook_id, event_id, now, fetch=read_order):
    try:
        validate(state, hook_id)
    except (KeyError, TypeError, ValueError, AttributeError):
        return {
            "ok": False,
            "action": "notify",
            "reason": "monitor_state_unavailable",
            "verified": False,
            "acknowledged": False,
        }
    pending = state["pending"]
    if not pending or pending["event_id"] != event_id:
        return {
            "ok": True,
            "action": "quiet",
            "reason": "event_not_pending",
            "acknowledged": False,
        }
    reason = pending["reason"]
    notice = reason in {"tracking_unavailable", "monitor_deadline_reached"}
    backoff = state["failures"] > 0 and now < state["next_read_at"]
    snapshot, response = None, {}
    if not backoff:
        snapshot, response, _ = read_snapshot(state, now, fetch)
    if snapshot is None and not notice:
        return {
            "ok": True,
            "action": "retry",
            "reason": "read_cooldown" if backoff else "verification_failed",
            "acknowledged": False,
            "retry_after_seconds": max(0, state["next_read_at"] - now),
            "state": state,
        }
    previous = state["seen"]
    if reason == "tracking_unavailable" and snapshot is not None:
        result = acknowledge(state, hook_id, event_id)
        state["unavailable_reported"] = False
        return {
            **result,
            "action": "quiet",
            "reason": "tracking_restored",
        }
    if not notice and snapshot != pending["snapshot"]:
        # Discard the stale event without recording its unverified state as seen.
        state.update(pending=None, next_wake_at=0)
        return {
            "ok": True,
            "acknowledged": True,
            "state": state,
            "action": "quiet",
            "reason": "event_superseded",
        }
    summary = status_summary(
        snapshot or previous, previous, response if snapshot else {}
    )
    quiet = snapshot is not None and awaiting_courier(snapshot) and not notice
    return {
        **acknowledge(state, hook_id, event_id),
        "action": "quiet" if quiet else "notify",
        "reason": reason,
        "verified": snapshot is not None,
        **summary,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    setup = sub.add_parser("baseline")
    setup.add_argument("--order-id", required=True)
    setup.add_argument("--ttl-seconds", type=int, default=MAX_DURATION)
    setup.add_argument("--restart-expired", action="store_true")
    sub.add_parser("poll")
    ack = sub.add_parser("acknowledge")
    ack.add_argument("--event-id", required=True)
    verify = sub.add_parser(
        "verify-event", help="Verify and acknowledge one pending update"
    )
    verify.add_argument("--event-id", default="")
    args = parser.parse_args()
    raw = sys.stdin.read(131073)
    if len(raw) > 131072:
        raise ValueError("monitor state exceeds its bound")
    state = json.loads(raw)
    hook_id, now = os.environ["HATCH_HOOK_ID"], int(time.time())
    if args.action == "baseline":
        result = baseline(
            state,
            hook_id,
            args.order_id,
            now,
            args.ttl_seconds,
            restart_expired=args.restart_expired,
        )
    elif args.action == "acknowledge":
        result = acknowledge(state, hook_id, args.event_id)
    elif args.action == "verify-event":
        result = verify_event(state, hook_id, args.event_id, now)
    else:
        result = poll(state, hook_id, now)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
