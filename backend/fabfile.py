
"""
    Fab tasks for workflow automation
"""
import os
from fabric.api import local, shell_env
from config import settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def manage(command, args=''):
    local('{}/manage.py {} {}'.format(BASE_DIR, command, args))


def psql(query, no_sudo=False, is_file=False):
    sudo = 'sudo -u postgres'
    if no_sudo:
        sudo = ''
    if is_file:
        local('{} psql < {}'.format(sudo, query))
    else:
        local('{} psql -c "{}"'.format(sudo, query))


def reset_migrations():
    clean_pyc()
    for app_name in settings.LOCAL_APPS:
        local('rm -rf {}/migrations/ -r'.format(app_name))
    for app_name in settings.LOCAL_APPS:
        manage('makemigrations {}'.format(app_name))
    # local('git add . --all')


def clean_pyc():
    local("find . -name '*.pyc' -delete")


def migrate():
    manage('makemigrations')
    manage('migrate')


def setup(*args, **kwargs):
    no_sudo = True if 'no-sudo' in args else False
    bootstrap_sql = kwargs['sql'] if 'sql' in kwargs else None
    db_name = kwargs['db'] if 'db' in kwargs else settings.DATABASES.get(
        'default').get('NAME')
    db_user = settings.DATABASES.get('default').get('USER')
    db_pass = settings.DATABASES.get('default').get('PASSWORD')
    psql("DROP DATABASE IF EXISTS {}".format(db_name), no_sudo)
    try:
        psql("DROP USER IF EXISTS {}".format(db_user), no_sudo)
        psql(
            "CREATE USER {0} WITH SUPERUSER CREATEDB "
            "CREATEROLE LOGIN PASSWORD '{1}'".format(
                db_user, db_pass), no_sudo)
    except:
        pass
    psql("CREATE DATABASE {}".format(db_name), no_sudo)
    if bootstrap_sql:
        psql(bootstrap_sql, no_sudo=no_sudo, is_file=True)
    else:
        manage('migrate --noinput')


def run():
    local('./manage.py  runserver 9000')


def run_tasks():
    local('./manage.py run_huey')


def supervisor():
    local('./manage.py supervisor --daemonize')


def tox_test():
    """Dev and release - run the test suite"""
    local('python setup.py check')
    local('pip install tox')
    local('tox -r -c tox.ini')


def test(*args, **kwargs):
    with shell_env(DJANGO_SETTINGS_MODULE="config.test"):
        setup(db="pos_test_db")
        local("flake8 --exclude=migrations,docs,data_bootstrap")
        local("coverage erase")
        local("coverage run -m py.test --ds=config.test {}".format(
            " ".join(settings.LOCAL_APPS)))
        local("coverage report --fail-under=100")
        local("coverage html")


def codeship_test():
    with shell_env(DJANGO_SETTINGS_MODULE="config.codeship_test"):
        manage('makemigrations')
        manage('migrate --noinput')
        local("flake8 --exclude=migrations,docs,data_bootstrap")
        local("coverage erase")
        local("coverage run -m py.test --ds=config.codeship_test {}".format(
            " ".join(settings.LOCAL_APPS)))
        # local("py.test  --cov . ")
        local("coverage report --fail-under=100")
        local("coverage html")
