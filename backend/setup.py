from __future__ import print_function

import io
import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

with open('README.md') as readme:
    description = readme.read()

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')
version = '0.0.1a'


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)


setup(
    name='pos_api',
    version=version,
    license='Private',
    author='Liyosi Collins',
    author_email='collinskivale@gmail.com',
    description="POS API-Server",
    long_description=long_description,
    url='git@github.com:liyocee/pos.git',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Private',
        'Operating System :: POSIX :: Linux',
        'Framework :: Django :: 1.8'
    ],
    tests_require=['tox'],
    cmdclass={'test': Tox},
    install_requires=[
        "model_mommy==1.2.4",
        "Fabric>=1.10",
        "coverage>=3.7",
        "psycopg2>=2.5",
        "djangorestframework==3.1",
        "django-filter>=0.9",
        'dj_database_url>=0.3.0,<=0.4.0',
        "flake8>=2.3",
        "django-cors-headers>=1.0",
        "virtualenv>=12.0",
        "pip>=6.0",
        "tox>=1.9",
        "djangorestframework-xml>=1.0",
        "djangorestframework-csv>=1.3",
        "django-rest-swagger>=0.2",
        "Markdown>=2.5.1",
        "django>=1.8",
        'sqlparse>=0.1',
        "pytest>=2.7",
        "pytest-django>=2.8",
        "pytest-xdist>=1.11",
        "six>=1.9",
        "pytest-cov>=1.8.0",
        "django-reversion>=1.8.6",
        "wheel>=0.24.0",
        "pytz>=2015.2",
        "werkzeug>=0.10.4",
        "gunicorn>=19.3.0",
        "apache-libcloud>=0.17.0",
        "django-environ>=0.3.0",
        "python-coveralls>=2.5.0",
        "djangorestframework-gis>=0.8.1",
        "django-debug-toolbar>=1.3.0",
        "django-rest-auth>=0.4.0",
        "django-allauth>=0.19.1",
        "django-oauth-toolkit>=0.8.1",
        "drf-extensions>=0.2.7",
        "xlsxwriter>=0.7.2",
        "mock>=1.0.1",
        "recommonmark>=0.1.1",
        "django-redis>=4.0.0",
        "djrill==1.3.0",
        "django-registration",
        "django-extensions==1.5.2",
        "huey==0.4.8",
        "redis==2.10.3",
        "django_hstore>=1.3.0"
    ],
)
