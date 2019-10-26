CREATE USER miner WITH PASSWORD 'capitulating';
CREATE DATABASE minerdb WITH OWNER miner ENCODING = 'UTF8' TABLESPACE = pg_default;
GRANT ALL on DATABASE minerdb to miner;