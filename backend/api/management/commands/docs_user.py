from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.conf import settings


class Command(BaseCommand):
    help = 'Create Super User and API key for docs'

    def handle(self, *args, **options):
        try:
            user = get_user_model().objects.get(
                email='api_admin@user.co.ke')
        except get_user_model().DoesNotExist:
            user = get_user_model().objects.create_superuser(
                email='api_admin@user.co.ke',
                first_name='API',
                last_name='ADMIN',
                password='api_1520_admin'
            )
        key = settings.SWAGGER_SETTINGS['api_key']
        Token.objects.get_or_create(user=user, key=key)
        self.stdout.write("Successfully created api user")
