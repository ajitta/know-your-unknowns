"""Routing for the services' HTTP APIs, and a client for calling other services."""
import json
import os
from dataclasses import dataclass

import httpx


@dataclass
class Route:
    method: str
    path: str
    handler: object


class Router:
    def __init__(self, prefix=""):
        self.prefix = prefix
        self.routes = []

    def _add(self, method, path):
        def register(handler):
            self.routes.append(Route(method, self.prefix + path, handler))
            return handler
        return register

    def get(self, path):
        return self._add("GET", path)

    def post(self, path):
        return self._add("POST", path)

    def patch(self, path):
        return self._add("PATCH", path)


def json_response(body, status=200):
    return status, {"Content-Type": "application/json"}, json.dumps(body)


def not_found():
    return json_response({"error": "not found"}, status=404)


class HttpClient:
    def __init__(self, base_url, api_key=None, timeout=10.0):
        headers = {}
        if api_key:
            headers["Authorization"] = "Bearer " + os.environ.get(api_key, "")
        self.client = httpx.Client(base_url=base_url, headers=headers, timeout=timeout)

    def get(self, path):
        return self.client.get(path).raise_for_status().json()

    def post(self, path, body):
        return self.client.post(path, json=body).raise_for_status().json()

    def patch(self, path, body):
        return self.client.patch(path, json=body).raise_for_status().json()
