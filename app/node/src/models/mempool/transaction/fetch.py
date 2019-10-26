from .utils import convert_transaction_from_mempool


async def get_transactions_from_mempool(connection, parameters):

    transactions = []
    orderby = parameters["orderby"]
    limit = parameters["limit"]
    records = await connection.fetch(
        f"""
            SELECT * FROM mempool
            ORDER BY {orderby}
            LIMIT {limit}
            """
    )
    return [convert_transaction_from_mempool(record) for record in records]
