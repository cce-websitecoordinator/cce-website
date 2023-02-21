FROM python:3.10

WORKDIR /webapp

ADD . /webapp

COPY ./requirements.txt /webapp/requirements.txt


RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /webapp/