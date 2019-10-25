import dj_database_url
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['mydiary666-api.herokuapp.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'myDiary_API.apps.authentication',
    'myDiary_API.apps.diary',
    'myDiary_API.apps.entry',
    'gunicorn'
]

DATABASES = {}
DB_URL = os.getenv('DATABASE_URL')
DATABASES['default'] = dj_database_url.config(
    default=DB_URL,
    engine='django.db.backends.postgresql'
)
