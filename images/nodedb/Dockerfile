FROM postgres:11.3-alpine
RUN apk update && \
    apk upgrade

COPY ./db/nodedb.sql /docker-entrypoint-initdb.d/1.sql
COPY ./db/nodetable.sql /nodetable.sql
COPY ./scripts/startup.sh /docker-entrypoint-initdb.d/sql.sh