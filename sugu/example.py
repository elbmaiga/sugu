from .settings import *

# Toujours à TRUE en mode développement
DEBUG = True

ALLOWED_HOSTS = []

if not DEBUG:
    ALLOWED_HOSTS = ['localhost']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Connect to the mysql database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'db_host',
    }
}

# Connect to the sqlite3 database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}