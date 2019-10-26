import asyncio
from .transaction import fetch, update, utils
from ...utils.utils import utc


def transaction_valid_for_pool(transaction):
    """
    To DO:
        Clean the data as process of the verification
        Check that the datatype are correct
    """
    transaction_record = transaction["record"]
    amount = transaction_record["amount"]
    sender_inputs = transaction_record["sender"]["inputs"]
    sender_outputs = transaction_record["sender"]["outputs"]
    receiver_outputs = transaction_record["sender"]["outputs"]
    fee = transaction_record["fee"]

    datatypes_valid = utils.validate_datatypes(transaction_record)
    if datatypes_valid:
        transaction_valid = utils.validate_transction(transaction_record)

        if transaction_valid:
            return True
        else:
            return False
    else:
        return False


def verify_code(code):
    if code:
        return True
    else:
        return False


async def add_transactions_to_mempool(connection, code, data, utctime):
    if not verify_code(code):
        return {"message": "Invalid code"}
    transactions = data["transactions"]
    valid_transaction = []
    invalid_transactions = []
    for transaction in transactions:
        transaction_valid = transaction_valid_for_pool(transaction)
        if transaction_valid:
            valid_transaction.append(transaction)
        else:
            invalid_transactions.append(transaction)
    all_transction_added = await update.add_transactions_to_mempool(
        connection, valid_transaction, utctime
    )

    data = {
        "added": valid_transaction,
        "invalid": invalid_transactions,
        "timestamp": f"{utc()}",
    }
    if valid_transaction and not invalid_transactions:
        return {"response": "success", "data": data}
    else:
        return {"response": "error", "data": data}

