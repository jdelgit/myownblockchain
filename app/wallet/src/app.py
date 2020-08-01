import asyncio
import asyncpg
from uvloop import new_event_loop
from aiohttp import web
from .models.wallet import wallet as wl
from os import environ

loop = new_event_loop()
loop.set_debug(True)
asyncio.set_event_loop(loop)
routes = web.RouteTableDef()


@routes.post("/api/setupwallet")
async def setup_wallet_from_seed(request):
    request_json = await request.json()
    input_seed = []
    if "wallet_seed" in request_json:
        input_seed = request_json["wallet_seed"]
    pool = request.app["pool"]
    async with pool.acquire() as dbconnection:
        wallet = await wl.setup_wallet_from_seed(input_seed, dbconnection)
    return web.json_response(wallet)


@routes.post("/api/getpublickeys")
async def get_wallet_transactions(request):
    response = []
    private_key = ""
    request_json = await request.json()
    pool = request.app["pool"]
    async with pool.acquire() as dbconnection:
        if "private_key" in request_json:
            private_key = request_json["private_key"]
            response = await wl.get_pubkeys_from_privatekey(private_key, dbconnection)
        elif "seed" in request_json:
            seed = request_json["seed"]
            response = await wl.get_pubkeys_from_seed(seed, dbconnection)
    return web.json_response(response)


@routes.post("/api/createaddress")
async def create_wallet_address(request):
    request_json = await request.json()
    pool = request.app["pool"]
    pubkey = ""
    if "pubkey" in request_json:
        pubkey = request_json["pubkey"]
    async with pool.acquire() as dbconnection:
        wl.create_wallet_address(pubkey, dbconnection)


@routes.post("/api/gettransactions")
async def get_wallet_transactions(request):
    response = []
    address = ""
    request_json = await request.json()
    if "address" in request_json:
        address = request_json["address"]
    pool = request.app["pool"]
    async with pool.acquire() as dbconnection:
        response = await wl.get_wallet_transactions(address, dbconnection)
    return web.json_response(response)


async def app():
    app = web.Application()
    app["pool"] = await asyncpg.create_pool(
        database="walletdb",
        user="walletuser",
        host="wallet_db",
        password="capitulating",
    )
    app.add_routes(routes)
    return app
