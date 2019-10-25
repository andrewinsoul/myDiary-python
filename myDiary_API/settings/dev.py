from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

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
]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'PORT': os.getenv('DB_PORT'),
        'HOST': os.getenv('DB_HOST'),
        'TEST': {
            'CHARSET': None,
            'COLLATION': None,
            'NAME': 'test.db',
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': 'postgres',
            'PORT': 5432,
            'USER': 'postgres',
            'MIRROR': None
        }

    }
}
