#!/bin/sh

# Stop the script execution if any command fails
set -e

# Loop until the PostgreSQL database is up and accepting connections
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  # Print a message indicating that the script is waiting for the database to start
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
  sleep 2  # Wait for 2 seconds before checking again
done

# Notify that the PostgreSQL database has started successfully
echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

# Collect static files for the Django application (non-interactive mode)
python manage.py collectstatic --noinput

# Make migrations for the Django application (non-interactive mode)
python manage.py makemigrations --noinput

# Apply database migrations for the Django application (non-interactive mode)
python manage.py migrate --noinput

# Start the Django development server in the background, listening on all interfaces
python manage.py runserver 0.0.0.0:8000 &

# Start the cron daemon in the foreground with specific logging settings
exec sudo crond -f -l 8 -L /var/log/cron/cron.log

