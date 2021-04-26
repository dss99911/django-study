#!/bin/sh

set -e

#migration is managed on database. so, should migrate on runtime.
python manage.py makemigrations second_app
python manage.py migrate

set +e
#if user already exists. ignore it
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$DJANGO_ADMIN_NAME', '$DJANGO_ADMIN_EMAIL', '$DJANGO_ADMIN_PASSWORD')" | python manage.py shell || echo "admin account is not created"
set -e
if [ $DJANGO_DEBUG = "False" ]; then
  echo "Django release mode"
  #collect all static files and put them in static route
  python manage.py collectstatic --noinput
  uwsgi --socket :8000 --master --enable-threads --module sample.wsgi
else
  echo "Djang debug mode"
  python manage.py runserver 0.0.0.0:8000
fi