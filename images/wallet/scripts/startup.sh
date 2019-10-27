#!/bin/sh
until psql "postgresql://walletuser:capitulating@walletdb/walletdb" ; do
    echo "Postgres is unavailable - sleeping"
    sleep 15
    done

python3  /srv/app/api/src/app.py &

tail -f /dev/null