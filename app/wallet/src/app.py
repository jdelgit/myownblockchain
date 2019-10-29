import asyncio
import json
import argparse
from .models.wallet import wallet


async def main():

    parser = argparse.ArgumentParser(prog="WalletImplementation")
    parser.add_argument("--new_wallet", action="store_true")
    parser.add_argument("--new_address", action="store_true")
    parser.add_argument("--receive_funds", action="store_true")
    parser.add_argument("--send_funds", action="store_true")

    args = parser.parse_args()
    if args.new_wallet:
        result = await wallet.wallet_creation()
    elif args.new_address:
        pass
    elif args.receive_funds:
        pass
    elif args.send_funds:
        pass
    else:
        print("No valid argument passed")


asyncio.run(main())
