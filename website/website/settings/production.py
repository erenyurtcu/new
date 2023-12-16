from website.settings.base import *


DEBUG = False

DATABASES  = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'guneybetulwebsite',
        'USER': 'guney_betul',
        'PASSWORD': 'bgey23',
        'HOST': 'localhost',
        'PORT': '',
    }
}

#STATICFILES_DIRS = [ BASE_DIR / 'home/static']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
