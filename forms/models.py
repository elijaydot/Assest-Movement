from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import RegexValidator
from phone_field import PhoneField
# Create your models here.

class Post(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    asset_description = models.TextField()
    asset_tag = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    present_location = models.CharField(max_length=100)
    new_destination = models.CharField(max_length=100)
    asset_make = models.CharField(max_length=100)
    asset_model = models.CharField(max_length=100)
    asset_serial_number = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    removal_date = models.DateTimeField(blank=True, null=True)
    return_date = models.DateTimeField(default=timezone.now)
    reason_for_movement = models.TextField()

    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    requestor_unit = models.CharField(max_length=100)
    requestor_branch = models.CharField(max_length=100)
    date_requested = models.DateTimeField(blank=True, null=True)

    collected_by = models.CharField(max_length=100)
    collector_phone_number = PhoneField(blank=True, help_text='Collector phone number')
    collector_company = models.CharField(max_length=100)
    collector_branch = models.CharField(max_length=100)
    date_collected = models.DateTimeField(blank=True, null=True)

    approved_by = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_approved = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.removal_date = timezone.now()
        self.save()

    def __str__(self):
        return self.asset_description