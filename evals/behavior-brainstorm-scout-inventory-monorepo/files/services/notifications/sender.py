"""Send one email or SMS to an account, through the mail relay and the sms service."""
from services.accounts.client import AccountClient
from services.sms.client import SmsMessageClient
from libs.http import HttpClient

_mail = HttpClient("http://mail-relay.internal:2525")


def send_email(account_id, subject, html):
    account = AccountClient().get(account_id)
    if account.get("status") != "active":
        return None
    return _mail.post("/send", {"to": account["email"], "subject": subject, "html": html})


def send_sms(account_id, text):
    account = AccountClient().get(account_id)
    if not account.get("phone"):
        return None
    return SmsMessageClient().create({"to_number": account["phone"], "body": text})
