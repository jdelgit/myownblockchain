import asyncio
import uvloop
import asyncpg
import json
from aiohttp import web
from .utils.utils import utc

from .utils.response import json_success, json_error
from .models.mempool import mempool


"""
request_structure = {
    "code" : "001",
    "data" : {
        "transactions": [{
            "sender": "Bob",
            "receiver": "Lisa",
            "notes": "food",
            "record": {
            	"amount": 1.00,
            	"sender":{
            		"inputs": [],
            		"outputs":[]
            	},
            	"receiver":{
            		"output":[1.00]
            	},
            "fee": 0.01
            }
        }]
    }
}

"""


async def add_transactions_to_mempool(request):
    requestdata = await request.json()
    code = requestdata.get("code")
    data = requestdata.get("data", {})
    dbpool = request.app["dbpool"]
    timestamp = utc()
    async with dbpool.acquire() as connection:
        result = await mempool.add_transactions_to_mempool(
            connection, code, data, timestamp
        )
    if result["response"] == "success":
        return web.json_response(json_success({"data": result}))
    else:
        return web.json_response(
            json_error(400, "invalid transactions in request", {"transactions": result})
        )


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
    app.add_routes([web.post("/api/newtransaction", add_transactions_to_mempool)])
    app.add_routes([web.post("/api/addblock", addblock)])
    app.add_routes([web.get("/api/getmempool", getmempool)])
    app.add_routes([web.post("/api/getchain", getchain)])
    app.add_routes([web.post("/api/getdifficulty", getdifficulty)])
    return app

