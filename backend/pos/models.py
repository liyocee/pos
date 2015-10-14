import reversion
from django.db import models
from django.conf import settings
from common.models import AbstractBase


@reversion.register
class Organization(AbstractBase):
    profile = models.OneToOneField(settings.AUTH_USER_MODEL)

    class Meta:
        app_label = 'pos'


@reversion.register
class SalesAgent(AbstractBase):
    organization = models.ForeignKey(Organization)
    profile = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="sales_agent")

    class Meta:
        app_label = 'pos'


@reversion.register
class ProductTypes(AbstractBase):
    name = models.CharField(
        max_length=255, null=False, blank=False)
    organization = models.ForeignKey(Organization)

    class Meta:
        app_label = 'pos'
        unique_together = ('name', 'organization')


@reversion.register
class Sales(AbstractBase):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    product = models.ForeignKey(ProductTypes)
    customer_email = models.EmailField(
        null=True, blank=True)
    customer_id_number = models.CharField(
        null=False, blank=False, max_length=128)
    customer_phone = models.CharField(
        null=False, blank=False, max_length=128)
    customer_first_name = models.CharField(
        null=False, blank=False, max_length=128)
    customer_last_name = models.CharField(
        null=False, blank=False, max_length=128)
    customer_address = models.TextField(
        null=True, blank=True)
    follow_up_date = models.DateTimeField(null=True, blank=True)
    agent = models.ForeignKey(SalesAgent)

    class Meta:
        app_label = 'pos'
