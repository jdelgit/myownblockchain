import asyncio
import uvloop
import asyncpg
import json
from aiohttp import web
from .models.wallet import wallet as wl



loop = uvloop.new_event_loop()
loop.set_debug(True)
asyncio.set_event_loop(loop)

routes = web.RouteTableDef()


@routes.post("/api/setupwallet")
async def setup_wallet_from_seed(request):
    request_json = await request.json()
    input_seed = []
    if "wallet_seed" in request_json:
        input_seed = request_json["wallet_seed"]
    wallet = await wl.setup_wallet_from_seed(input_seed)
    return web.json_response(wallet)


async def app():
    app = web.Application()
    app.add_routes(routes)
    return app
