from website.settings.base import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [ BASE_DIR / 'home/static']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')