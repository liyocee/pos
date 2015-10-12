from settings import *  # NOQa
env.read_env(os.path.join(BASE_DIR, '{}/.env_test'.format(APP_FOLDER)))
ENV_DB = env.db()
env = environ.Env(
    DATABASE_URL=(
        str,
        'postgres://pos_user:pos_passwd' +
        '@localhost:5432/pos_test_db'
    )
)
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
