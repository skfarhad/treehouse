#!/bin/bash

# Exit on error
set -e

echo "✅ Booting app now..."

# No database — this is a static personal site (content in apps/website/content.py).

# ✅ Make sure Django knows where to find settings
export DJANGO_SETTINGS_MODULE=conf.settings

# Collect static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn
echo "🚀 Starting Gunicorn server..."
gunicorn -c conf/gunicorn.conf.py conf.wsgi:application
