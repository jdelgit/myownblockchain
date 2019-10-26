#!/bin/sh
until psql "postgresql://noderunner:capitulating@nodedb/nodedb" ; do
    echo "Postgres is unavailable - sleeping"
    sleep 15
    done
adev runserver /srv/app/api/src &

tail -f /dev/null