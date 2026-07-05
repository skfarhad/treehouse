"""Thin Replicate HTTP client — run a model, wait, return output URL(s).

Uses the official-model prediction endpoint
(`POST /v1/models/{owner}/{name}/predictions`) so callers pass a friendly slug
like ``black-forest-labs/flux-dev`` with no version hash. Sends ``Prefer: wait``
to block server-side, then polls as a fallback for long jobs.

Only depends on ``requests`` (already a project dependency).
"""
from __future__ import annotations

import time
from typing import Any

import requests

API_ROOT = "https://api.replicate.com/v1"


class ReplicateError(RuntimeError):
    pass


class ReplicateClient:
    def __init__(self, token: str, *, timeout: int = 300, poll_interval: float = 2.0):
        if not token:
            raise ReplicateError("No Replicate API token provided.")
        self._token = token
        self._timeout = timeout
        self._poll_interval = poll_interval
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        })

    def run(self, model: str, model_input: dict[str, Any]) -> Any:
        """Run ``model`` (``owner/name``) and return its ``output`` once done."""
        if "/" not in model:
            raise ReplicateError(f"Model must be 'owner/name', got: {model!r}")
        url = f"{API_ROOT}/models/{model}/predictions"
        resp = self._session.post(
            url,
            json={"input": model_input},
            headers={"Prefer": "wait"},
            timeout=self._timeout,
        )
        if resp.status_code >= 400:
            raise ReplicateError(f"{model}: HTTP {resp.status_code} — {resp.text}")
        prediction = resp.json()
        return self._await_output(prediction)

    def _await_output(self, prediction: dict[str, Any]) -> Any:
        deadline = time.monotonic() + self._timeout
        while True:
            status = prediction.get("status")
            if status == "succeeded":
                return prediction.get("output")
            if status in ("failed", "canceled"):
                raise ReplicateError(
                    f"Prediction {status}: {prediction.get('error') or prediction}"
                )
            if time.monotonic() > deadline:
                raise ReplicateError("Timed out waiting for prediction to finish.")
            get_url = (prediction.get("urls") or {}).get("get")
            if not get_url:
                raise ReplicateError(f"No poll URL on prediction: {prediction}")
            time.sleep(self._poll_interval)
            r = self._session.get(get_url, timeout=self._timeout)
            if r.status_code >= 400:
                raise ReplicateError(f"Poll HTTP {r.status_code} — {r.text}")
            prediction = r.json()


def output_urls(output: Any) -> list[str]:
    """Normalise a model's ``output`` to a flat list of URL strings."""
    if output is None:
        return []
    if isinstance(output, str):
        return [output]
    if isinstance(output, list):
        urls: list[str] = []
        for item in output:
            urls.extend(output_urls(item))
        return urls
    if isinstance(output, dict):
        # Some models wrap the file under a key (e.g. {"image": "..."}).
        for key in ("image", "images", "output", "url"):
            if key in output:
                return output_urls(output[key])
    return []
