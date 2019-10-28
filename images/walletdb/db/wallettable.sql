SET
  statement_timeout = 0;
SET
  lock_timeout = 0;
SET
  idle_in_transaction_session_timeout = 0;
SET
  client_encoding = 'UTF8';
SET
  standard_conforming_strings = on;
SET
  check_function_bodies = false;
SET
  xmloption = content;
SET
  client_min_messages = warning;
SET
  row_security = off;
CREATE TABLE keystore (private_key text, public_key text);
CREATE TABLE wallet_transactions (
    transaction_id text,
    transaction_inputs text,
    transaction_outputs text
  );
CREATE TABLE wallet_address (
    public_key text,
    public_address text,
    transaction_id text
  );