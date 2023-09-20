#!/bin/bash

echo "Executing init.sh script..."

# Update package list and install MySQL client without prompting
apt-get update
apt-get install python3-pip
apt-get install -y mysql-client
apt-get install -y djangorestframework


# Collect static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate
python manage.py makemigrations
python manage.py migrate

# Start the Django development server
python manage.py runserver 0.0.0.0:8080

