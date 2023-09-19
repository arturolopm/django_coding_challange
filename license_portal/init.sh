#!/bin/bash

echo "Executing init.sh script..."

# Update package list and install MySQL client without prompting
apt-get update
apt-get install -y mysql-client

# Collect static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate
python manage.py makemigrations
python manage.py migrate

# Start the Django development server
python manage.py runserver 0.0.0.0:8080

