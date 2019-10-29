from ...utils.utils import *
from ..keymanager import keymanager as km
from ...utils.config import SEED_LENGTH


async def wallet_seed_request_loop():
    ERROR_MESSAGES = {
        "long": "To many words entered",
        "short": "To few words entered",
        "incorrect": "Invalid seed words",
    }
    while True:
        error = None
        wallet_seed_input = input(
            f"Please enter your {SEED_LENGTH} word seed separated by space"
        )
        wallet_seed = wallet_seed_input.split(" ")
        if len(wallet_seed) > SEED_LENGTH:
            if wallet_seed[-1] == "":
                # trailing space
                wallet_seed.pop()
                seeds_valid = validate_seed_words(wallet_seed)
                if not seeds_valid:
                    error = "incorrect"
                else:
                    break
            else:
                error = "long"
        elif len(wallet_seed) < SEED_LENGTH:
            error = "short"
        else:
            seeds_valid = validate_seed_words(wallet_seed)
            if not seeds_valid:
                error = "incorrect"
            else:
                break
        if error:
            print(ERROR_MESSAGES[error])

    return wallet_seed


async def wallet_creation():
    # wallet from new seed or existing seed
    restore_wallet = input("Restore from existing seed?\n")
    if validate_input_bool(restore_wallet):
        wallet_seed = await wallet_seed_request_loop()
    else:
        wallet_seed = await km.generate_new_seed()
    keypair = await km.generate_keypair_from_seed(wallet_seed)

    return {"seed": wallet_seed}

