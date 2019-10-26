import json


def format_transaction_for_mempool(transaction, utctime):
    transaction_record = transaction["record"]
    formated_transaction = (
        transaction["sender"],
        transaction["receiver"],
        transaction["notes"],
        transaction_record["amount"],
        json.dumps(transaction_record["sender"]["inputs"]),
        json.dumps(transaction_record["sender"]["outputs"]),
        json.dumps(transaction_record["receiver"]["outputs"]),
        json.dumps(transaction_record["fee"]),
        utctime,
    )
    return formated_transaction


def validate_datatypes(record):

    return True


def validate_transction(transaction):
    return True
