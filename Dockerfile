FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /home_db

WORKDIR /home_db

COPY requirements.txt /home_db/

RUN pip install -r requirements.txt

COPY home_db /home_db/