FROM python:3.10-alpine3.16

WORKDIR /webapp

ADD . /webapp

COPY ./requirements.txt /webapp/requirements.txt

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps \
    && apk add jpeg-dev \
    && apk add libjpeg \
    && apk add zlib-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /webapp/

RUN adduser --disabled-password --no-create-home django

USER django

CMD ["uwsgi", "--socket", ":9000", "--workers", "4", "--master", "--enable-threads", "--module", "app.wsgi"]