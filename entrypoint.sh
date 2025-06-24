#!/bin/sh

# entrypoint.sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Wait for the PostgreSQL database to be ready
# 'db' is the service name from your docker-compose.yml
# 5432 is the default PostgreSQL port
echo "Waiting for PostgreSQL to start..."
while ! nc -z db 5432; do
  sleep 0.5 # Wait for 0.5 seconds before retrying
done
echo "PostgreSQL started"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput # --noinput prevents interactive prompts during migration

exec "$@"