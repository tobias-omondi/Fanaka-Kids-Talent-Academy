#!/usr/bin/env bash
set -o errexit
set -x  # Enable debug output

# Install directly to Render's system Python (bypass virtualenv)
python -m pip install --upgrade pip
python -m pip install gunicorn==23.0.0 --prefix=/opt/render
python -m pip install -r requirements.txt --prefix=/opt/render

# Verify installation
echo "=== GUNICORN VERIFICATION ==="
/opt/render/bin/gunicorn --version || {
    echo "Gunicorn verification FAILED!";
    find /opt/render -name gunicorn;
    exit 1;
}

# Django setup
python manage.py collectstatic --noinput
python manage.py migrate