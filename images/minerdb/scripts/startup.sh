#!/bin/sh
psql --set ON_ERROR_STOP=on -U miner -d minerdb < /minertable.sql