from dataclasses import dataclass

from services.payments.processor import CardDeclined
from services.payments.service import PaymentService


@dataclass
class Renewal:
    id: str = "sub-1"
    account_id: str = "acc-1"
    price: str = "39.99"
    card_token: str = "tok-1"


class DecliningProcessor:
    def charge(self, card_token, amount, reference):
        raise CardDeclined("insufficient_funds")


class Recorder:
    def __init__(self):
        self.calls = []

    def run_at(self, when, task_name, payload):
        self.calls.append((task_name, payload))

    def cancel(self, subscription_id, reason):
        self.calls.append(("cancel", subscription_id, reason))


class MemoryRepository:
    def save(self, item):
        pass


def test_first_decline_schedules_one_retry():
    recorder = Recorder()
    service = PaymentService(MemoryRepository(), DecliningProcessor(), recorder, recorder)
    service.charge_renewal(Renewal(), attempt=1)
    assert recorder.calls == [("payments.retry_due", {"subscription_id": "sub-1", "attempt": 2})]


def test_second_decline_cancels_the_subscription():
    recorder = Recorder()
    service = PaymentService(MemoryRepository(), DecliningProcessor(), recorder, recorder)
    service.charge_renewal(Renewal(), attempt=2)
    assert recorder.calls == [("cancel", "sub-1", "payment_failed")]
