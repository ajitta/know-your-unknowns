"""Publish and subscribe by event name, through the message broker at BROKER_URL.
An event that no process subscribes to is dropped."""
import json
import logging
import os
from collections import defaultdict

import redis

log = logging.getLogger(__name__)
_client = None
_handlers = defaultdict(list)


def _broker():
    global _client
    if _client is None:
        _client = redis.Redis.from_url(os.environ["BROKER_URL"])
    return _client


def publish(event_name, payload):
    _broker().publish(event_name, json.dumps(dict(payload, event=event_name)))


def subscribe(event_name, handler):
    _handlers[event_name].append(handler)


def listen():
    """Deliver events to the handlers subscribed in this process, until stopped."""
    channel = _broker().pubsub()
    channel.subscribe(*_handlers)
    for message in channel.listen():
        if message["type"] != "message":
            continue
        event_name = message["channel"].decode()
        event = json.loads(message["data"])
        for handler in _handlers[event_name]:
            try:
                handler(event)
            except Exception:
                log.exception("handler for %s failed", event_name)
