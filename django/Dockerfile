FROM python:3.9.4-alpine3.12

RUN apk update
RUN apk add --no-cache \
    musl-dev \
    mariadb-dev \
    gcc \
    libffi-dev \
    python3-dev \
    openssl-dev \
    cargo

ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/
