from settings import *  # NOQa
import os
env.read_env(os.path.join(BASE_DIR, '{}/.env_test'.format(APP_FOLDER)))
ENV_DB = env.db()
env = environ.Env(
    DATABASE_URL=(
        str,
        'postgres://{}:{}' +
        '@localhost:5432/test'.format(os.environ.get('PG_USER'),
                                      os.environ.get('PG_PASSWORD'))
    )
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': os.environ.get('PG_USER'),
        'PASSWORD': os.environ.get('PG_PASSWORD'),
        'HOST': '127.0.0.1',
    }
}
