FROM python:3.5-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk add --no-cache --virtual .build-deps gcc musl-dev linux-headers pkgconf \
    autoconf automake libtool make postgresql-dev postgresql-client openssl-dev && \
    apk add postgresql-libs postgresql-client && \
    # Предотвращаем неудачную компиляцию uWSGI внутри Docker, см. https://git.io/v1ve3
    (while true; do pip --no-cache-dir install uwsgi==2.0.14 && break; done)

COPY ./requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
RUN SECRET_KEY=build ./manage.py collectstatic --noinput && \
    ./manage.py makemessages && \
    apk del .build-deps