#!/usr/bin/env bash
set -o errexit
set -x  # Enable debug output

# Create virtual environment in Render's preferred location
python -m venv /opt/render/project/src/.venv
source /opt/render/project/src/.venv/bin/activate

# Install gunicorn FIRST as standalone package
pip install --upgrade pip
pip install gunicorn==23.0.0 --no-cache-dir

# Then install other requirements
pip install -r requirements.txt --no-cache-dir

# Verify gunicorn installation
echo "=== Gunicorn verification ==="
/opt/render/project/src/.venv/bin/gunicorn --version

# Django setup
python manage.py collectstatic --noinput
python manage.py migrate