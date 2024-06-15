FROM python:3.11-rc-slim-buster

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    pip install -r requirements.txt