import models.transact.transactions


async def create_transaction(receiver_address, value):
    pass


async def broadcast_transaction(transaction):
    pass


async def get_transactactions(address,dbconn):
    return await dbconn.fetch('SELECT *  from  wallet_transactions')

async def save_transaction(dbconn):
    return await dbconn.execute("INSERT INTO wallet_transactions  (transaction_id, transaction_inputs, transaction_outputs)  VALUES ('3123123','hallo','hola')")
