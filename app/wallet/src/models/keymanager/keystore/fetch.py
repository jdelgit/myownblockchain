from utils.utils import record_to_dict


async def fetch_public_keys(private_key, dbconn):
    records = []
    async with dbconn.transaction():
        records = await dbconn.fetch(
            """
                SELECT public_key, nonce from keystore
                WHERE private_key=$1
            """,
            private_key,
        )
    for record in records:
        yield record_to_dict(record)
