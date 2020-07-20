FROM python:3.7-alpine3.9
ENV PYTHONUNBUFFERED 1
RUN apk update && \
    apk upgrade

RUN apk add build-base && \
    apk add postgresql && \
    apk add python-dev && \
    apk add build-base && \
    apk add libffi-dev

COPY ./config/requirements.txt /requirements.txt

RUN pip3 install --upgrade pip && \
    pip3 install -r /requirements.txt

COPY ./scripts/startup.sh /startup.sh
RUN chmod +x /startup.sh
