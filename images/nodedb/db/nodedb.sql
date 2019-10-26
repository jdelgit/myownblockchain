CREATE USER noderunner WITH PASSWORD 'capitulating';
CREATE DATABASE nodedb WITH OWNER noderunner ENCODING = 'UTF8' TABLESPACE = pg_default;
GRANT ALL on DATABASE nodedb to noderunner;