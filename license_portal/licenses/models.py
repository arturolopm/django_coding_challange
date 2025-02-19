""" Data model for licenses application
"""
import enum

from datetime import timedelta, datetime
from typing import Tuple, List

from django.contrib.auth.models import User
from django.db import models

LICENSE_EXPIRATION_DELTA = timedelta(days=90)


class ChoiceEnum(enum.Enum):
    """Enum for choices in a choices field"""
    @classmethod
    def get_choices(cls) -> List[Tuple[str, int]]:
        return [(a.name, a.value) for a in cls]


class Package(ChoiceEnum):
    """A Package accessible to a client with a valid license"""
    JAVASCRIPT_SDK = 'javascript_sdk'
    IOS_SDK = 'ios_sdk'
    ANDROID_SDK = 'android_sdk'


class LicenseType(ChoiceEnum):
    """A license type"""
    PRODUCTION = 'production'
    EVALUATION = 'evaluation'


def get_default_license_expiration() -> datetime:
    """Get the default expiration datetime"""
    return datetime.utcnow() + LICENSE_EXPIRATION_DELTA


class License(models.Model):
    """ Data model for a client license allowing access to a package
    """
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    package = models.CharField(max_length=20,choices=Package.get_choices())
    license_type = models.CharField(max_length=20,choices=LicenseType.get_choices())

    created_datetime = models.DateTimeField(auto_now=True)
    expiration_datetime = models.DateTimeField(default=get_default_license_expiration)


class Client(models.Model):
    """ A client who holds licenses to packages
    """
    client_name = models.CharField(max_length=120, unique=True)
    poc_contact_name = models.CharField(max_length=120)
    poc_contact_email = models.EmailField()

    admin_poc = models.ForeignKey(User, limit_choices_to={'is_staff': True}, on_delete=models.CASCADE)

class LogEmail(models.Model):
    sent_at = models.DateTimeField()
    license_id = models.IntegerField()