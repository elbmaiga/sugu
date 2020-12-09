# coding=utf-8
from .settings import *

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
        'NAME': 'sugu',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
    }
}