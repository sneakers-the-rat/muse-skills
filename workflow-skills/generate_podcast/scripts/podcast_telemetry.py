"""Content-free, best-effort observations of one podcast helper attempt."""

import json
import os
import time
import uuid


def _request_id(attempt_id):
    try:
        trace_context = json.loads(os.environ.get("JARVIS_TRACE_CONTEXT", ""))
    except (ValueError, RecursionError):
        trace_context = None
    if isinstance(trace_context, dict):
        request_id = trace_context.get("request_id")
        if isinstance(request_id, str) and request_id.strip():
            return request_id.strip()

    tool_call_id = os.environ.get("JARVIS_TOOL_CALL_ID", "").strip()
    if tool_call_id:
        return f"tool:{tool_call_id}"
    return os.environ.get("JARVIS_REQUEST_ID", "").strip() or attempt_id


class GenerationTelemetry:
    def __init__(self, retry_generation, send):
        self.generation_id = str(retry_generation or uuid.uuid4())
        self.attempt_id = str(uuid.uuid4())
        self.retry = retry_generation is not None
        self.request_id = _request_id(self.attempt_id)
        self.stage = "prepare"
        self._send = send
        self._started = time.monotonic()
        self._finished = False
        self._emit({"event": "start"})

    def result_fields(self):
        return {
            "generation_trace_id": self.generation_id,
            "generation_attempt_id": self.attempt_id,
        }

    def finish(self, outcome):
        if self._finished:
            return
        self._finished = True
        self._emit({
            "event": "end",
            "outcome": outcome,
            "stage": self.stage,
            "elapsed_ms": min(2**32 - 1, max(0, int(
                (time.monotonic() - self._started) * 1000
            ))),
        })

    def _emit(self, observation):
        try:
            self._send(
                {
                    "generation_id": self.generation_id,
                    "attempt_id": self.attempt_id,
                    "retry": self.retry,
                    "observation": observation,
                },
                self.request_id,
            )
        except Exception:
            # Telemetry outages must not change synthesis or the helper result.
            pass
