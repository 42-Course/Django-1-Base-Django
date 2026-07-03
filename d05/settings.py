import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def _env_bool(name, default):
    return os.environ.get(name, str(default)).strip().lower() in ('1', 'true', 'yes', 'on')


def _env_list(name, default=''):
    return [item.strip() for item in os.environ.get(name, default).split(',') if item.strip()]


# Defaults keep the piscine dev behaviour; production overrides via env vars.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-base-django-piscine-key')
DEBUG = _env_bool('DJANGO_DEBUG', True)
ALLOWED_HOSTS = _env_list('DJANGO_ALLOWED_HOSTS', '*')

# Origins allowed to submit forms (needed for ex02 behind HTTPS in production).
CSRF_TRUSTED_ORIGINS = _env_list('DJANGO_CSRF_TRUSTED_ORIGINS')

if not DEBUG:
    # Coolify (Traefik) terminates TLS and forwards the original scheme.
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.staticfiles',
    'ex00',
    'ex01',
    'ex02',
    'ex03',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

# WhiteNoise serves static files directly from the app in production.
# Only enabled when the package is installed, so the base dev env is untouched.
try:
    import whitenoise  # noqa: F401
    MIDDLEWARE.insert(0, 'whitenoise.middleware.WhiteNoiseMiddleware')
    STORAGES = {
        'default': {'BACKEND': 'django.core.files.storage.FileSystemStorage'},
        'staticfiles': {
            'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
        },
    }
except ImportError:
    pass

ROOT_URLCONF = 'd05.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': []},
    },
]

WSGI_APPLICATION = 'd05.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # In production point this at a persistent volume, e.g. /app/data/db.sqlite3
        'NAME': os.environ.get('DJANGO_DB_PATH', BASE_DIR / 'db.sqlite3'),
    }
}

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# APPEND_SLASH lets /ex00 and /ex00/ both resolve.
APPEND_SLASH = True

# ex02: location of the input history log file.
EX02_LOG_FILE = BASE_DIR / 'ex02' / 'form_history.log'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
