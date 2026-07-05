import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Core security settings (environment-driven, secure by default) ---------

# DEBUG is OFF unless explicitly enabled. For local dev: set DJANGO_DEBUG=1.
DEBUG = os.environ.get('DJANGO_DEBUG', '').lower() in ('1', 'true', 'yes', 'on')

# SECRET_KEY must be provided via the environment in production.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
if not SECRET_KEY:
    if DEBUG:
        SECRET_KEY = 'django-insecure-dev-only-key-do-not-use-in-production'
    else:
        raise ImproperlyConfigured(
            "DJANGO_SECRET_KEY environment variable must be set when DEBUG is off."
        )

# Hosts allowed to serve the site. Override with DJANGO_ALLOWED_HOSTS
# (comma-separated). Defaults cover the custom domain + Railway.
ALLOWED_HOSTS = [
    h.strip() for h in os.environ.get(
        'DJANGO_ALLOWED_HOSTS',
        'skfarhad.com,www.skfarhad.com,.railway.app,.up.railway.app,localhost,127.0.0.1',
    ).split(',') if h.strip()
]


# This is a static personal site: no database, no admin, no auth, no sessions.
# Content lives in apps/website/content.py, not in a database.
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'apps.website',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'

# No database. The ORM is unused; site content is in apps/website/content.py.
DATABASES = {}


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
WHITENOISE_MAX_AGE = 31536000

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# --- HTTP security headers ---------------------------------------------------

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'same-origin'
X_FRAME_OPTIONS = 'DENY'

# The site has no Django-handled forms (the contact form posts to an external
# service), so CSRF middleware is intentionally omitted — silence its warning.
SILENCED_SYSTEM_CHECKS = ['security.W003']

if not DEBUG:
    # Railway terminates TLS and forwards the original scheme in this header.
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True


# Log request errors to the console.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
