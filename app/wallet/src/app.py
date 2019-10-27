import requests
import asyncio
import asyncpg
import json


async def main():
    async def init_connections(connection):
        await connection.set_type_codec(
            "jsonb", schema="pg_catalog", encoder=json.dumps, decoder=json.loads
        )

    dbpool = await asyncpg.create_pool(
        host="wallet_db",
        database="walletdb",
        user="wallet",
        password="capitulating",
        init=init_connections,
    )


asyncio.run(main())
