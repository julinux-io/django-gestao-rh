#!/usr/bin/bash
SECRET_KEY=`.venv/Scripts/python.exe commands/gen_secret.py`
DEBUG='True'
TIME_ZONE='America/Sao_Paulo'
ALLOWED_HOSTS='127.0.0.1,localhost'
LANGUAGE_CODE='pt-BR'
DBNAME='gestao'
DBUSER='postgres'
DBPASSWORD='supersecretpassword'
DBHOST='db'
DBURL="postgres://${DBUSER}:${DBPASSWORD}@${DBHOST}:5432/${DBNAME}"

DEBUG=$DEBUG DBNAME=$DBNAME DBUSER=$DBUSER DBPASSWORD=$DBPASSWORD \
DBHOST=$DBHOST DBURL=$DBURL docker-compose up --detach --build

if [ $? == 0 ]; then
    echo -e "Your .env file was created!
    SECRET_KEY=${SECRET_KEY}
    DEBUG=${DEBUG}
    ALLOWED_HOSTS=${ALLOWED_HOSTS}
    LANGUAGE_CODE=${LANGUAGE_CODE}
    TIME_ZONE=${TIME_ZONE}
    DATABASE_URL=${DBURL}
    "
fi
