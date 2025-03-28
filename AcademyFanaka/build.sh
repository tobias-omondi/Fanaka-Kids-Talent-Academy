#!/usr/bin/env bash
set -o errexit
set -x  # Enable debug output

# System-level installation (bypasses virtualenv issues)
python -m pip install --upgrade pip
python -m pip install --prefix=/opt/render gunicorn==23.0.0
python -m pip install --prefix=/opt/render -r requirements.txt

# Verify installation
echo "=== Verifying Gunicorn ==="
/opt/render/bin/gunicorn --version || echo "Gunicorn verification failed!"

# Django setup
python manage.py collectstatic --noinput
python manage.py migrate