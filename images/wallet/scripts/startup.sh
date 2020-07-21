#!/bin/sh
until psql "postgresql://walletuser:capitulating@walletdb/walletdb" ; do
    echo "Postgres is unavailable - sleeping"
    sleep 8
    done

adev runserver  /srv/app/api/src/ &

tail -f /dev/null