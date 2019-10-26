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
CREATE TABLE node_chain (
    previous_block_hash text,
    block_hash text,
    transactions text
  );
CREATE TABLE mempool (
    sender text,
    receiver text,
    notes text,
    transacted_amount numeric,
    sender_inputs text,
    sender_ouputs text,
    receiver_outputs text,
    transaction_fee numeric,
    time_added timestamp
  );