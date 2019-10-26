FROM postgres:11.3-alpine
RUN apk update && \
    apk upgrade


COPY ./db/minerdb.sql /docker-entrypoint-initdb.d/1.sql
COPY ./db/minertable.sql /minertable.sql
COPY ./scripts/startup.sh /docker-entrypoint-initdb.d/sql.sh