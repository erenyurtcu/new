from website.settings.base import *
import os
PROJECT_DIR = os.path.dirname(__file__)


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ALLOWED_HOSTS = [
]


STATICFILES_DIRS=[os.path.join(BASE_DIR,'static'),]
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')