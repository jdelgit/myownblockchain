import asyncio
from .utils import format_transaction_for_mempool


async def add_transactions_to_mempool(connection, valid_transactions, utctime):
    result = False
    transactions = [
        format_transaction_for_mempool(transaction, utctime)
        for transaction in valid_transactions
    ]
    async with connection.transaction():
        result = await connection.executemany(
            f"""
                INSERT INTO mempool(
                   sender_address
                  ,receiver_address
                  ,notes
                  ,transacted_amount
                  ,sender_inputs
                  ,sender_ouputs
                  ,receiver_outputs
                  ,transaction_fee
                  ,time_added 
                ) VALUES (
                    $1,$2,$3,$4,$5,$6,$7,$8,$9
                )
            """,
            transactions,
        )
    return result

