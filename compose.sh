#!/usr/bin/bash
export SECRET_KEY=`.venv/Scripts/python.exe commands/gen_secret.py`
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
