#!/usr/bin/env bash
set -o errexit
set -x  # Debug mode

# System-wide install (bypass virtual env)
pip install --user --upgrade pip
pip install --user gunicorn==23.0.0
pip install --user -r requirements.txt

# Verify installation
echo "=== Gunicorn verification ==="
~/.local/bin/gunicorn --version || echo "Gunicorn check failed!"

# Django setup
python manage.py collectstatic --noinput
python manage.py migrate