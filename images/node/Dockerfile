FROM nginx:alpine
RUN apk update && \
    apk upgrade


RUN apk add curl
RUN apk add python3  && \
    apk add python3-dev && \
    apk add py3-pip
RUN apk add build-base && \
    apk add python-dev && \
    apk add libffi-dev  && \
    apk add postgresql 

RUN pip3 install --upgrade pip
COPY ./config/requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
COPY ./scripts/startup.sh /startup.sh
RUN chmod +x /startup.sh
COPY ./config/server.conf /etc/nginx/conf.d/cc.conf
