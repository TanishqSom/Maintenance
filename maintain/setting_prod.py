from .settings import *
import os

DEBUG = False
ALLOWED_HOSTS = ['nixstay.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Test',
        'USER': 'root',
        'PASSWORD': 'Hello@84',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
