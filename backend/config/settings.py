import os
import environ

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Override in production via env
env = environ.Env()
env = environ.Env(
    DATABASE_URL=(
        str,
        'postgres://pos_user:pos_passwd@localhost:5432/pos_db'
    )
)
APP_FOLDER = 'api'
env.read_env(os.path.join(BASE_DIR, '{}/.env'.format(APP_FOLDER)))
DEBUG = env('DEBUG', default=True)
SECRET_KEY = env(
    'SECRET_KEY', default='p!ci1&ni8u98vvd#%18yp)aqh+m_8o565g*@!8@1wb$j#pj4d8')
ENV_DB = env.db()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': ENV_DB['HOST'],
        'NAME': ENV_DB['NAME'],
        'PASSWORD': ENV_DB['PASSWORD'],
        'PORT': ENV_DB['PORT'],
        'USER': ENV_DB['USER'],
    }
}  # Env should have DATABASE_URL

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
EMAIL_HOST = env('EMAIL_HOST', default='localhost')
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default=487)
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='notarealpassword')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
ALLOWED_HOSTS = ['.healthix.co.ke', '.localhost']
INSTALLED_APPS = (
    'django.contrib.sites',
    'common',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.postgres',

    # libs
    'django_extensions',
    'django_filters',
    'djrill',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'oauth2_provider',
    'gunicorn',
    'corsheaders',
    'reversion',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',

    # our apps
    'api',
    'users',
    'pos',
)
LOCAL_APPS = (
    'api',
    'common',
    'users',
    'pos'
)
SITE_ID = 1
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'localhost:8012',
    '.healthix.co.ke',
    'pos-web.healthix.co.ke',
    'pos-api.healthix.co.ke',
    '52.89.181.225'
)
API_DOMAIN = 'pos-api.healthix.co.ke'
CORS_ALLOW_CREDENTIALS = True
CORS_PREFLIGHT_MAX_AGE = 172800
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)
CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'cache-control'
)
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
AUTH_USER_MODEL = 'users.User'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = 'http://localhost:9000/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False  # Turn on in production
SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': '0.1',
    'api_path': '/',
    'enabled_methods': [
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'api_key': '228b67fadab69d86a8d7e49dc03ac8e2206yre22',
    'is_authenticated': True,
    'is_superuser': True,
    'permission_denied_handler': 'api.views.permission_denied_handler',
    'resource_access_handler': None,
    'base_path': 'localhost:8000' if DEBUG else API_DOMAIN,
    'info': {
        'contact': 'developers@emanager.co',
        'description': 'Explore the POS v0.0.1 API',
        'title': 'POS V0.0.1 API',
    },
    'doc_expansion': 'none',
}
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.ScopedRateThrottle',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework_xml.parsers.XMLParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework_xml.renderers.XMLRenderer'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.PageNumberPagination'),
    'PAGE_SIZE': 3,
    'PAGINATE_BY_PARAM': 'page_size',
    # Should be able to opt in to see all wards at once
    'MAX_PAGINATE_BY': 15000,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DATETIME_FORMAT': 'iso-8601',
    'DATE_FORMAT': 'iso-8601',
    'TIME_FORMAT': 'iso-8601'

}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': os.path.join(BASE_DIR, '/common/templates/'),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# django-allauth related settings
# some of these settings take into account that the target audience
# of this system is not super-savvy
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[POS]'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = ''
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/api/v1/auth/login/'
API_LOGIN_URL = '/api/v1/auth/drf/login/'

# django_rest_auth settings
OLD_PASSWORD_FIELD_ENABLED = True
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'users.serializers.UserSerializer',
    'TOKEN_SERIALIZER': 'users.serializers.UserAuthTokenSerializer',
    'PASSWORD_RESET_SERIALIZER': (
        'users.serializers.UserPasswordResetSerializer'),
}

# Client origin to be allowed access
CLIENT_ORIGIN = 'http://localhost:8012'
DEFAULT_FROM_EMAIL = 'POS <info@pos.co.ke>'

API_ROOT = 'http://localhost:8061/api/v1'
MANDRILL_API_KEY = ''
EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
