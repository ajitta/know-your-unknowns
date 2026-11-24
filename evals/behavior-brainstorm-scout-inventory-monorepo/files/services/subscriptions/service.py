"""Subscriptions: start, pause, resume and cancel, and the renewals due each night."""
from dataclasses import dataclass

from libs.events.bus import publish
from services.payments.cards import CardStore
from services.pricing.client import PriceRuleClient
from services.subscriptions.models import Subscription
from services.subscriptions.repository import SubscriptionRepository


@dataclass
class Renewal:
    id: str
    account_id: str
    price: str
    card_token: str


class SubscriptionService:
    def __init__(self, repository=None, cards=None, pricing=None):
        self.repository = repository or SubscriptionRepository()
        self.cards = cards
        self.pricing = pricing

    def create(self, data):
        subscription = Subscription.from_dict(data)
        self.repository.save(subscription)
        publish("subscription.created", {"id": subscription.id})
        return subscription

    def get(self, subscription_id):
        return self.repository.get(subscription_id)

    def list(self, limit=50, offset=0):
        return self.repository.list(limit=limit, offset=offset)

    def update(self, subscription_id, changes):
        subscription = self.repository.get(subscription_id)
        if subscription is None:
            raise KeyError(subscription_id)
        for name, value in changes.items():
            if name not in ("account_id", "box_size", "status"):
                raise ValueError("unknown field %r" % name)
            setattr(subscription, name, value)
        self.repository.save(subscription)
        publish("subscription.updated", {"id": subscription.id})
        return subscription

    def pause(self, subscription_id):
        return self._set_status(subscription_id, "paused", "subscription.paused")

    def resume(self, subscription_id):
        return self._set_status(subscription_id, "active", "subscription.resumed")

    def cancel(self, subscription_id, reason):
        subscription = self._set_status(subscription_id, "cancelled", "subscription.cancelled")
        publish("subscription.cancelled_reason", {"id": subscription_id, "reason": reason})
        return subscription

    def due_for_renewal(self):
        for subscription in self.repository.list(limit=100000):
            if subscription.status == "active":
                yield self._renewal(subscription)

    def renewal_for(self, subscription_id):
        subscription = self.repository.get(subscription_id)
        if subscription is None or subscription.status != "active":
            return None
        return self._renewal(subscription)

    def _renewal(self, subscription):
        cards = self.cards or CardStore()
        pricing = self.pricing or PriceRuleClient()
        price = pricing.get(subscription.box_size)["price"]
        return Renewal(subscription.id, subscription.account_id, price,
                       cards.token_for(subscription.account_id))

    def _set_status(self, subscription_id, status, event_name):
        subscription = self.repository.get(subscription_id)
        if subscription is None:
            raise KeyError(subscription_id)
        subscription.status = status
        self.repository.save(subscription)
        publish(event_name, {"id": subscription_id})
        return subscription
