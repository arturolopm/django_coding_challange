from django.core.mail import send_mail
from django.template.loader import render_to_string
from config.settings import DEFAULT_FROM_EMAIL
from datetime import timedelta
from django.utils import timezone
from .models import License


def send_email_notification(subject, message, recipient_list):
    """
    Sends an email notification using Django's email backend.
    """
    send_mail(subject, message, DEFAULT_FROM_EMAIL, recipient_list)

def get_licenses_to_notify():
    """
    Retrieve licenses that need to be notified based on expiration conditions.
    """
    current_date = timezone.datetime.now()
    
    # Retrieve licenses that expire in exactly 4 months
    
    licenses_4_months = License.objects.filter(
        expiration_datetime=current_date + timedelta(days=4*30)
    )
    
    # Retrieve licenses that expire within a month and today is Monday
    if current_date.weekday() == 0:  # Monday
        licenses_1_month = License.objects.filter(
            expiration_datetime__gte=current_date,
            expiration_datetime__lte=current_date + timedelta(days=30)
        )
    else:
        licenses_1_month = []
    
    # Retrieve licenses that expire within a week
    licenses_1_week = License.objects.filter(
        expiration_datetime__gte=current_date,
        expiration_datetime__lte=current_date + timedelta(days=7)
    )
    
    # Combine all licenses to be notified
    licenses_to_notify = list(licenses_4_months) + list(licenses_1_month) + list(licenses_1_week)
    
    # Extract relevant license information for notifications
    notification_data = []
    for license in licenses_to_notify:
        notification_data.append({
            'license_id': license.id,
            'license_type': license.license_type,
            'package': license.package,
            'expiration_date': license.expiration_datetime,
            'poc_name': license.client.poc_contact_name,
            'poc_email': license.client.poc_contact_email,
        })
    
    return notification_data