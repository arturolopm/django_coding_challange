from datetime import timezone
from typing import List, Any

from django.core.mail import send_mail
from django.template import Template
from django.template.loader import get_template
from .models import LogEmail
from .utils import send_email_notification
from django.template.loader import render_to_string

DEFAULT_FROM_EMAIL = 'noreply@email.com'


class EmailNotification:
    """ A convenience class to send email notifications
    """
    subject = "License Expiration Notification"  # type: str
    from_email = DEFAULT_FROM_EMAIL  # type: str
    template_path = "email_template.html"  # type: str

    @classmethod
    def load_template(cls) -> Template:
        """Load the configured template path"""
        return get_template(cls.template_path)

    @classmethod
    def send_notification(cls, recipients: List[str], context: Any):
        """Send the notification using the given context"""
        template = cls.load_template()
        message_body = template.render(context=context)
        LogEmail.objects.create(
            sent_at=timezone.now(),  # Import timezone
            license_id=context.get('license_id')  # Adjust this based on your context
        )
        send_mail(cls.subject, message_body, cls.from_email, recipients, fail_silently=False)