#!/bin/sh
until psql "postgresql://walletuser:capitulating@walletdb/walletdb" ; do
    echo "Postgres is unavailable - sleeping"
    sleep 15
    done

adev runserver  /srv/app/api/src/ &

tail -f /dev/null