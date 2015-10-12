import os

from .settings import *  # NOQA

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": "localhost",
        "PORT": 5432,
    }
}
STATIC_ROOT = os.getenv("STATIC_ROOT")
MEDIA_ROOT = os.getenv("MEDIA_ROOT")
MEDIA_URL = os.getenv("MEDIA_URL")
DEBUG = TEMPLATE_DEBUG = os.getenv("DEBUG", "false") == "true"
DEBUG = True
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
CLIENT_ORIGIN = os.getenv("CLIENT_ORIGIN")
SESSION_COOKIE_DOMAIN = os.getenv("SESSION_COOKIE_DOMAIN")
CSRF_COOKIE_DOMAIN = os.getenv("CSRF_COOKIE_DOMAIN")
