
async def add_key_pair_to_database(keypair_data, dbconn):
    if all([ 1 for data in keypair_data.keys() if data in ['private', 'public','nonce']]):
        async with dbconn.transaction():
            return await dbconn.execute(
                                        "INSERT INTO keystore (public_key, private_key, nonce)  VALUES ($1),($2),($3) ",
                                        keypair_data['public'],
                                        keypair_data['private'],
                                        keypair_data['nonce']
                                    )
    return False

async def add_address_to_database(public_key, address, nonce, dbconn):
    async with dbconn.transaction():
        return await dbconn.execute(
                                    "INSERT INTO wallet_address (public_key, public_address, nonce)  VALUES ($1),($2),($3) ",
                                    public_key,
                                    address,
                                    nonce,
                                )
