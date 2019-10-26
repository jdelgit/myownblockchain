import asyncio
import uvloop
import asyncpg
import json
from aiohttp import web
from .utils.utils import utc

from .utils.response import json_success, json_error
from .models.mempool import mempool


async def add_transactions_to_mempool(request):
    requestdata = await request.json()
    code = requestdata.get("code")
    data = requestdata.get("data", {})

    if "transactions" in data:
        transctions = data["transactions"]
    else:
        return web.json_response(
            json_error(
                400,
                "invalid transactions in request",
                {"info": "no transactions in request"},
            )
        )
    dbpool = request.app["dbpool"]
    timestamp = utc()
    async with dbpool.acquire() as connection:
        result = await mempool.add_transactions_to_mempool(
            connection, code, transctions, timestamp
        )
    if result["response"] == "success":
        return web.json_response(json_success({"data": result}))
    else:
        return web.json_response(
            json_error(400, "invalid transactions in request", {"info": result})
        )


async def get_transactions_from_mempool(request):
    requestdata = await request.json()
    code = requestdata.get("code")
    data = requestdata.get("data")
    if "parameters" in data:
        parameters = data["parameters"]
    else:
        return web.json_response(
            json_error(400, "invalid in request", {"info": "no parameters in request"})
        )
    dbpool = request.app["dbpool"]
    async with dbpool.acquire() as connection:
        result = await mempool.get_transactions_from_mempool(
            connection, code, parameters
        )
    if result["response"] == "success":
        return web.json_response(json_success({"data": result}))
    else:
        return web.json_response(
            json_error(
                400,
                "Unable to retrieve transactions based on parameters",
                {"info": result},
            )
        )


async def append_new_block(request):
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
    app.add_routes([web.post("/api/newtransaction", add_transactions_to_mempool)])
    app.add_routes(
        [web.get("/api/get_transactions_from_mempool", get_transactions_from_mempool)]
    )
    app.add_routes([web.post("/api/append_block", append_new_block)])
    app.add_routes([web.post("/api/getchain", getchain)])
    app.add_routes([web.post("/api/getdifficulty", getdifficulty)])
    return app

