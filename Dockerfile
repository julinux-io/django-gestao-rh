FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1

RUN pip install --upgrade pip
RUN pip install pipenv

RUN apk add --update --no-cache postgresql-client jpeg-dev zlib zlib-dev \
        libffi-dev gcc libc-dev linux-headers postgresql-dev

RUN addgroup -S djangoapp && adduser -S djangoapp -G djangoapp
RUN mkdir /app
RUN chown djangoapp:djangoapp /app

WORKDIR /app

COPY ./Pipfile* /app/
COPY ./src/ /app/

RUN chown -R djangoapp:djangoapp /app

RUN mkdir -p /etc/uwsgi/vassals
COPY ./contrib/gestao_rh.ini /etc/uwsgi/vassals/

USER djangoapp

RUN pipenv --python 3.8
RUN pipenv sync
RUN pipenv install uwsgi

RUN mkdir /app/log

EXPOSE 8000

CMD ["/app/.venv/bin/uwsgi", "--emperor", "/etc/uwsgi/vassals", "--uid", "djangoapp", "--gid", "djangoapp"]
