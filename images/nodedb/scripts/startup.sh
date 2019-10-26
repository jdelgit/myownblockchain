#!/bin/sh
psql --set ON_ERROR_STOP=on -U noderunner -d nodedb < /nodetable.sql