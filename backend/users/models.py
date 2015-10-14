import reversion
from django.core.validators import validate_email
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.contrib.auth.models import make_password
from django.db import models
from django.utils import timezone


class MyUserManager(BaseUserManager):
    def create(self, email, first_name,
               password=None, **extra_fields):
        now = timezone.now()
        validate_email(email)
        p = make_password(password)
        email = MyUserManager.normalize_email(email)
        user = self.model(email=email, first_name=first_name, password=p,
                          is_staff=False, is_active=True, is_superuser=False,
                          date_joined=now, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name,
                         password, **extra_fields):
        user = self.create(email, first_name,
                           password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


@reversion.register
class User(AbstractBaseUser):
    """
        Most Acquired from AbstractUser
    """
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    """
    Fields specific to Healthix User -- add them here
    """

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    @property
    def get_organization(self):
        from pos.models import Organization, SalesAgent
        try:
            # first, fetch from organization
            organization = Organization.objects.get(profile=self)
            details = {
                "id": organization.id,
                "is_creator": True
            }
        except Organization.DoesNotExist:
            # then, default to organizaiton's sales agent
            try:
                agent = SalesAgent.objects.get(profile=self)
                details = {
                    "id": agent.organization.id,
                    "is_creator": False
                }
            except SalesAgent.DoesNotExist:
                details = {}
        return details

    @property
    def get_agent(self):
        from pos.models import SalesAgent
        try:
            agent = SalesAgent.objects.get(profile=self)
            details = {
                "id": agent.id,
                "is_creator": False
            }
        except SalesAgent.DoesNotExist:
            details = {}

        return details

    class Meta:
        app_label = 'users'
