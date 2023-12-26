from website.settings.base import *


DEBUG = False

ALLOWED_HOSTS = [
    'betulguney.com',
    'www.betulguney.com',
    '134.122.62.69',
]

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
