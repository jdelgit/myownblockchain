FROM postgres:11.3-alpine
RUN apk update && \
    apk upgrade

COPY ./db/walletdb.sql /docker-entrypoint-initdb.d/1.sql
COPY ./db/wallettable.sql /wallettable.sql
COPY ./scripts/startup.sh /docker-entrypoint-initdb.d/sql.sh