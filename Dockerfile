FROM python:3.8.0-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get install gcc -y \
  && apt-get clean


RUN mkdir /app

WORKDIR /app

ADD . /app/

RUN pip install -r requirements.txt

