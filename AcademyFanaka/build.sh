#!/usr/bin/env bash
set -o errexit
set -x

# Nuclear option: Install directly to system Python
sudo apt-get update && sudo apt-get install -y python3-pip
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install gunicorn==23.0.0
sudo python3 -m pip install -r requirements.txt

# Create symlink to ensure gunicorn is in PATH
sudo ln -s /usr/local/bin/gunicorn /usr/bin/gunicorn

# Verification
echo "=== GUNICORN LOCATION ==="
which gunicorn || echo "Gunicorn not found!"
sudo find / -name gunicorn -type f -ls

# Django setup
python3 manage.py collectstatic --noinput
python3 manage.py migrate