FROM python:3.10

WORKDIR /webapp

ADD . /webapp

COPY ./requirements.txt /webapp/requirements.txt


RUN pip install -r requirements.txt
RUN python3 manage.py collectstatic --noinput


COPY . /webapp/ 