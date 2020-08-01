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
CREATE TABLE keystore (
    public_key text  NOT NULL,
    private_key text  NOT NULL,
    nonce integer  NOT NULL,
    PRIMARY KEY (public_key)
  );
CREATE TABLE wallet_transactions (
    transaction_id int  GENERATED ALWAYS AS IDENTITY,
    transaction_inputs text,
    transaction_outputs text,
    PRIMARY KEY (transaction_id)
  );
CREATE TABLE wallet_address (
    address_id int  GENERATED ALWAYS AS IDENTITY,
    public_key text NOT NULL,
    public_address text  NOT NULL,
    nonce integer  NOT NULL,
    PRIMARY KEY (address_id),
    CONSTRAINT fk_pubkey
      FOREIGN KEY(public_key)
        REFERENCES keystore(public_key)
  );