import asyncio
import uvloop
from aiohttp import web
import asyncpg
import json


async def add_transaction_to_mempool(request):
    pass


async def addblock(request):
    pass


async def getmempool(request):
    pass


async def getchain(request):
    pass


async def getdifficulty(request):
    pass


loop = uvloop.new_event_loop()
loop.set_debug(True)
asyncio.set_event_loop(loop)


async def create_app():
    app = web.Application()

    async def init_connections(connection):
        await connection.set_type_codec(
            "jsonb", schema="pg_catalog", encoder=json.dumps, decoder=json.loads
        )

    app["dbpool"] = await asyncpg.create_pool(
        host="nodedb",
        database="nodedb",
        user="noderunner",
        password="capitulating",
        init=init_connections,
    )
    app.add_routes([web.get("/api/addtransaction", add_transaction_to_mempool)])
    app.add_routes([web.post("/api/addblock", addblock)])
    app.add_routes([web.get("/api/getmempool", getmempool)])
    app.add_routes([web.post("/api/getchain", getchain)])
    app.add_routes([web.post("/api/getdifficulty", getdifficulty)])
    return app

