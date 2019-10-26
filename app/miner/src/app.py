import requests
import asyncio
import asyncpg
import json


async def broadcast_block(request):
    pass


async def validate_transaction(request):
    pass


async def calculate_block_hash(request):
    pass


async def get_mempool(request):
    pass


async def validate_chain(request):
    pass


async def get_chain(request):
    pass


async def get_difficulty(request):
    pass


async def main():
    async def init_connections(connection):
        await connection.set_type_codec(
            "jsonb", schema="pg_catalog", encoder=json.dumps, decoder=json.loads
        )

    dbpool = await asyncpg.create_pool(
        host="miner_db",
        database="minerdb",
        user="miner",
        password="capitulating",
        init=init_connections,
    )


asyncio.run(main())
