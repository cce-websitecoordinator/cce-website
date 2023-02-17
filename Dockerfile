FROM python:3.10

WORKDIR /webapp

ADD . /webapp

COPY ./requirements.txt /webapp/requirements.txt

RUN apt install build-base linux-headers
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /webapp/

RUN adduser --disabled-password --no-create-home django

USER django

CMD ["uwsgi", "--socket", ":9000", "--workers", "4", "--master", "--enable-threads", "--module", "app.wsgi"]