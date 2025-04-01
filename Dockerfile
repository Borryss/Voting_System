FROM python:3.10-alpine3.20

COPY requirements.txt /temp/requirements.txt
COPY main_service /main_service
WORKDIR /main_service
EXPOSE 8020

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password main_service-user

USER main_service-user
