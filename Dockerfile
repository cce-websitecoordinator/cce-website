FROM python:3.10-alpine3.16

WORKDIR /webapp

ADD . /webapp

COPY ./requirements.txt /webapp/requirements.txt


RUN apk add --upgrade --no-cache build-base linux-headers && \
    pip install --upgrade pip && \
    pip install -r /requirements.txt

COPY . /webapp/

RUN adduser --disabled-password --no-create-home django

USER django

CMD ["uwsgi", "--socket", ":9000", "--workers", "4", "--master", "--enable-threads", "--module", "app.wsgi"]