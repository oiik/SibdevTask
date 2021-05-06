#!/bin/sh

if ["DATABASE" = "postgres"]
then
  echo "Wait..."
  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
  done
  echo "Postgres started"
fi

python3 manage.py flush --no-input
python3 manage.py makemigrations
python3 manage.py migrate

exec "$@"
