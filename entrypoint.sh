#!/usr/bin/env sh
set -e

# Apply database migrations (creates the sqlite file on first boot).
python manage.py migrate --noinput

# Start the production WSGI server.
exec gunicorn d05.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers "${GUNICORN_WORKERS:-3}" \
    --access-logfile - \
    --error-logfile -
