import sys
import os
import asyncpg

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.utils import validate_seed_words
from utils.config import SEED_LENGTH
from models.keymanager import keymanager as km
from models.transact import transact as tr
import re


async def setup_wallet_from_seed(input_seed="", dbconn=None):
    """
        Get generated private/public key pair

    Args:
        input_seed (list/str, optional): Seed to generate private key. Defaults to "".

    Returns:
        dict: Wallet seed along with private/public key pair
    """
    wallet = []
    wallet_seed = []
    if input_seed:
        if isinstance(input_seed, str):
            wallet_seed = re.findall(r"[a-zA-z]+", input_seed)
        elif isinstance(input_seed, list):
            wallet_seed = input_seed
        seed_length_difference = SEED_LENGTH - len(wallet_seed)
        if seed_length_difference != 0:
            return {
                "error": f"The seed has too {'few' if seed_length_difference > 0  else 'many'} entries"
            }
    if not wallet_seed:
        wallet_seed = km.generate_new_seed()
    if validate_seed_words(wallet_seed):
        wallet = await km.generate_keypair_from_seed(wallet_seed, dbconn)
    return wallet


async def get_pubkeys_from_seed(input_seed="", dbconn=None):
    pubkeys = []
    if input_seed:
        if isinstance(input_seed, str):
            wallet_seed = re.findall(r"[a-zA-z]+", input_seed)
        elif isinstance(input_seed, list):
            wallet_seed = input_seed
        if validate_seed_words(wallet_seed):
            pubkeys = await km.get_publickeys_with_seed(wallet_seed, dbconn)
    return pubkeys


async def get_pubkeys_from_privatekey(private_key="", dbconn=None):
    pubkeys = []
    if private_key:
        pubkeys = await km.get_publickeys_with_privatekey(private_key, dbconn)
    return pubkeys


async def create_wallet_address(pubkey, dbconn):
    """
        Generate a wallet address and save it to the database
    Args:
        pubkey (str) : Public key
        dbconn (asyncpg.pool): Database connection

    Return:
        address (str): Newly generated wallet address
    """
    pubkey_addresses = tr.get_address_list(pubkey, dbconn)
    used_nonces = [record["nonce"] async for record in pubkey_addresses]
    new_nonce = 0
    if used_nonces:
        last_nonce = max(used_nonces)
        new_nonce = last_nonce + 1
    return await km.generate_new_address(pubkey, new_nonce, dbconn)


async def get_wallet_transactions(address, dbconn):
    """
        Get all transactions for a given wallet address
    Args:
        address (str): wallet address
        dbconn (asyncpg.pool): Database connection
    Return:
        transactions (list): list of dictionaries of transaction infornation
    """
    transactions = await tr.get_transactactions(address, dbconn)
    return transactions


async def create_transaction(address, receiver, amount):
    pass
