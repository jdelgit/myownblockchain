import asyncio
import uvloop
import asyncpg
import json
from aiohttp import web
from models.wallet import wallet as wl

routes = web.RouteTableDef()
app = web.Application()

@routes.post('/api/setupwallet')
async def setup_wallet_from_seed(request):
    request_json = await request.json()
    input_seed = []
    if "wallet_seed" in request_json:
        input_seed = request_json["wallet_seed"]
    wallet = await wl.setup_wallet_from_seed(input_seed)
    return web.json_response(wallet)

app.add_routes(routes)


if __name__ == "__main__":
    web.run_app(app)
