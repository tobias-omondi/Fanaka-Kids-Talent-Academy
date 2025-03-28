#!/usr/bin/env bash
set -o errexit
set -x

# Create virtual environment in Render's persistent storage
python -m venv /opt/render/project/src/.venv
source /opt/render/project/src/.venv/bin/activate

# Install packages with network timeout retries
pip install --upgrade pip || { echo "pip upgrade failed, retrying..." && sleep 5 && pip install --upgrade pip; }
pip install gunicorn==23.0.0 || { echo "Gunicorn install failed, retrying..." && sleep 5 && pip install gunicorn==23.0.0; }
pip install -r requirements.txt

# Critical verification
echo "=== DEPLOYMENT VALIDATION ==="
echo "Python: $(which python)"
echo "Gunicorn: $(/opt/render/project/src/.venv/bin/gunicorn --version)"
echo "Project structure:"
ls -la myproject/

# Django setup
python manage.py check --deploy
python manage.py collectstatic --noinput
python manage.py migrate