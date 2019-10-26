import json
from ....utils.config import MAX_TRANSACTIONS_IN_BLOCK


def format_transaction_for_mempool(transaction, utctime):
    transaction_record = transaction["record"]
    formated_transaction = (
        transaction["sender_address"],
        transaction["receiver_address"],
        transaction["notes"],
        transaction_record["amount"],
        json.dumps(transaction_record["sender"]["inputs"]),
        json.dumps(transaction_record["sender"]["outputs"]),
        json.dumps(transaction_record["receiver"]["outputs"]),
        json.dumps(transaction_record["fee"]),
        utctime,
    )
    return formated_transaction


def convert_transaction_from_mempool(record):
    transaction = {key: str(val) for key, val in record.items()}

    return transaction


def validate_datatypes(record):

    return True


def validate_transction(transaction):
    return True


def clean_parameters(parameters):
    orderby = "time_added"
    limit = MAX_TRANSACTIONS_IN_BLOCK
    return {"orderby": orderby, "limit": limit}
