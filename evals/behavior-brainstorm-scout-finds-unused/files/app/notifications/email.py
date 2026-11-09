"""Sending mail. Tests use RecordingMailer, which keeps messages instead of sending."""
import smtplib
from email.message import EmailMessage

from app.config import SMTP_HOST, SUPPORT_FROM


class Mailer:
    def send(self, to, subject, body):
        message = EmailMessage()
        message["From"] = SUPPORT_FROM
        message["To"] = to
        message["Subject"] = subject
        message.set_content(body)
        with smtplib.SMTP(SMTP_HOST) as smtp:
            smtp.send_message(message)


class RecordingMailer:
    def __init__(self):
        self.sent = []

    def send(self, to, subject, body):
        self.sent.append({"to": to, "subject": subject, "body": body})
