"""WSGI config — exposes the module-level ``application`` callable.

Production posture (DEBUG, SECRET_KEY, security headers) is driven by
environment variables in ``conf/settings.py``. See ``.env.example``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

application = get_wsgi_application()
