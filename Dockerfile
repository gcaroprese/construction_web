FROM python:2.7
MAINTAINER Joni Bekenstein <jonibekenstein@gmail.com>

RUN apt-get update && apt-get install -yq gettext

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

WORKDIR /app
VOLUME /app/src
VOLUME /app/media
VOLUME /app/static
EXPOSE 8000

COPY . /app/
