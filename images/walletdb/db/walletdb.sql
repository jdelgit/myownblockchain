CREATE USER walletuser WITH PASSWORD 'capitulating';
CREATE DATABASE walletdb WITH OWNER walletuser ENCODING = 'UTF8' TABLESPACE = pg_default;
GRANT ALL on DATABASE walletdb to walletuser;