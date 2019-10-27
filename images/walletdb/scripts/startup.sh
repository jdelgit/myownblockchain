#!/bin/sh
psql --set ON_ERROR_STOP=on -U walletuser -d walletdb < /wallettable.sql