#!/usr/bin/bash
export SECRET_KEY=`.venv/bin/python.exe commands/gen_secret.py`
export DEBUG='True'
export TIME_ZONE='America/Sao_Paulo'
export ALLOWED_HOSTS='127.0.0.1,localhost'
export LANGUAGE_CODE='pt-BR'
export DBNAME='gestao'
export DBUSER='postgres'
export DBPASSWORD='supersecretpassword'
export DBHOST='db'
export DBURL="postgres://${DBUSER}:${DBPASSWORD}@${DBHOST}:5432/${DBNAME}"
export CELERY_BROKER_URL='redis://redis:6379'
export EMAIL_HOST=""
export EMAIL_PORT=587
export EMAIL_HOST_USER=""
export EMAIL_HOST_PASSWORD=""
export EMAIL_USE_TLS=True
export EMAIL_USE_SSL=False
export CODECOV_TOKEN=""

if [ "$1" = "down" ]; then
  docker-compose $1
else
  docker-compose up --detach --build

  if [ $? -eq 0 ]; then
      echo -e "Your .env file was created!
      SECRET_KEY=${SECRET_KEY}
      DEBUG=${DEBUG}
      ALLOWED_HOSTS=${ALLOWED_HOSTS}
      LANGUAGE_CODE=${LANGUAGE_CODE}
      TIME_ZONE=${TIME_ZONE}
      DATABASE_URL=${DBURL}
      "
  fi
fi
