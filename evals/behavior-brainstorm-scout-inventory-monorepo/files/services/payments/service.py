"""Card payments for subscriptions and add-ons."""
from datetime import datetime, timedelta, timezone

from libs.events.bus import publish
from libs.scheduler import Scheduler
from services.payments.config import settings
from services.payments.models import Payment
from services.payments.processor import CardDeclined, ProcessorClient
from services.payments.repository import PaymentRepository

MAX_ATTEMPTS = settings.renewals["max_attempts"]
RETRY_DELAY = timedelta(hours=settings.renewals["retry_delay_hours"])


class PaymentService:
    def __init__(self, repository=None, processor=None, scheduler=None, subscriptions=None):
        self.repository = repository or PaymentRepository()
        self.processor = processor
        self.scheduler = scheduler
        self.subscriptions = subscriptions

    def create(self, data):
        payment = Payment.from_dict(data)
        self.repository.save(payment)
        return payment

    def get(self, payment_id):
        return self.repository.get(payment_id)

    def list(self, limit=50, offset=0):
        return self.repository.list(limit=limit, offset=offset)

    def update(self, payment_id, changes):
        payment = self.repository.get(payment_id)
        if payment is None:
            raise KeyError(payment_id)
        for name, value in changes.items():
            if name not in ("account_id", "amount", "status"):
                raise ValueError("unknown field %r" % name)
            setattr(payment, name, value)
        self.repository.save(payment)
        return payment

    def charge_due_renewals(self):
        from services.subscriptions.service import SubscriptionService
        self.subscriptions = self.subscriptions or SubscriptionService()
        for renewal in self.subscriptions.due_for_renewal():
            self.charge_renewal(renewal)

    def charge_renewal(self, renewal, attempt=1):
        """Charge one renewal. A declined charge is tried again RETRY_DELAY later, up to
        MAX_ATTEMPTS attempts in all; when the last one is declined too, the
        subscription is cancelled."""
        processor = self.processor or ProcessorClient()
        payment = Payment(account_id=renewal.account_id, amount=renewal.price)
        try:
            processor.charge(renewal.card_token, renewal.price, reference=renewal.id)
        except CardDeclined as declined:
            payment.status = "declined"
            self.repository.save(payment)
            publish("charge.declined", {"subscription_id": renewal.id,
                                        "account_id": renewal.account_id,
                                        "decline_code": declined.code,
                                        "attempt": attempt})
            if attempt < MAX_ATTEMPTS:
                scheduler = self.scheduler or Scheduler()
                scheduler.run_at(datetime.now(timezone.utc) + RETRY_DELAY, "payments.retry_due",
                                 {"subscription_id": renewal.id, "attempt": attempt + 1})
            else:
                self.subscriptions.cancel(renewal.id, reason="payment_failed")
            return payment
        payment.status = "paid"
        self.repository.save(payment)
        publish("charge.succeeded", {"subscription_id": renewal.id, "attempt": attempt})
        return payment
