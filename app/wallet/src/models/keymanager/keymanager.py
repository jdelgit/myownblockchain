from ...utils.seedwords import SEEDWORDS
from ...utils.config import SEED_LENGTH
import random

# import asyncpg


async def generate_private_key(seed=None):
    private_key = None

    return private_key


async def generate_public_key(private_key):
    public_key = None

    return public_key


async def generate_keypair_from_seed(wallet_seed):
    # these whill be saved to the wallets database
    private_key = await generate_private_key(wallet_seed)
    public_key = await generate_public_key(private_key)
    return {"private": private_key, "public": public_key}


async def generate_keypair_from_privatekey(private_key):
    public_key = await generate_public_key(private_key)
    return {"private": private_key, "public": public_key}


async def generate_digital_signature(public_key, message):
    pass


async def generate_new_seed(seed=None):
    wallet_seed = []
    seeds = SEEDWORDS.copy()
    while len(wallet_seed) < SEED_LENGTH:
        number_of_seeds = len(seeds)
        seed_word_index = random.randint(0, number_of_seeds - 1)
        seed_word = seeds.pop(seed_word_index)
        wallet_seed.append(seed_word)

    return wallet_seed

