import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import random
import hashlib
from utils.config import SEED_LENGTH
from utils.seedwords import SEEDWORDS, PRIVATEKEY_JOINSALT
from models.keymanager.keystore.update import (
    add_address_to_database,
    add_key_pair_to_database,
)
from models.keymanager.keystore.fetch import fetch_public_keys

"""
    To Do:
    generate_digital_signature

"""


async def generate_keypair_from_seed(seed, dbconn=None):
    """
        Generate public/private key pair from wallet seed

    Args:
        seed (list/str,optional): Seed phrase for generating private key

    Returns:
        dict: Wallet seeds along with generated public/private key pair
    """
    if not seed:
        seed = ""
    result = {"wallet_seed": seed}
    private_key = generate_private_key(seed)
    keypair = generate_keypair_from_privatekey(private_key)
    result.update(keypair)
    success = False
    if dbconn:
        success = await add_key_pair_to_database(result, dbconn)
    return result


async def get_publickeys_with_seed(seed, dbonn):
    """

        Convert the seed to a privatekey
        Then use the private key to get the previously generated publickeys
    Args:
        seed (list/str): Seed phrase for generating private key
        dbconn (asyncpg.pool): Database connection

    Returns:
        [list]: List of all available public key related to a given private key
    """
    private_key = generate_private_key(seed)
    pubkeys = await get_publickeys_with_privatekey(private_key)

    return pubkeys


async def get_publickeys_with_privatekey(private_key, dbonn):
    """
        Use the private key to get the previously generated publickeys
    Args:
        private_key (str):  Hex representation of sha256 encoded seed
        dbconn (asyncpg.pool): Database connection

    Returns:
        [list]: List of all available public key related to a given private key
    """

    pubkeys = await fetch_public_keys(private_key, dbonn)
    return pubkeys


def generate_private_key(seed=[]):
    """
        Generate a sha256 private key using PRIVATEKEY_JOINSALT as salt

    Args:
        seed (list, optional): Seed of words to be encrypted. Defaults to [].

    Returns:
        str: Hex string of sha256 encrypted seed
    """
    data = PRIVATEKEY_JOINSALT.join(seed)
    seed_bytes = str.encode(data)
    return hashlib.sha256(seed_bytes).hexdigest()


def generate_public_key(private_key="", nonce=0):
    """
        Generate a public key given a private key and nonce

    Args:
        private_key (str,optional): Hex representation of sha256 encoded seed. Defaults to ''
        nonce (int, optional): Nonce for generating publickey. Defaults to 0.

    Returns:
        str: Hex string of sha256 encrypted seed
    """
    nonced_private_key = f"{private_key}{nonce}"
    nonced_private_key_bytes = str.encode(nonced_private_key)
    return hashlib.sha256(nonced_private_key_bytes).hexdigest()


def generate_keypair_from_privatekey(private_key, nonce=0):
    """
        Generate public/private key pair from private key

    Args:
        private_key (str): Hex string of private key
        nonce (int): Nonce to generate public key
    Returns:
        dict: Generated public key pair
    """
    public_key = generate_public_key(private_key, nonce)
    return {"private": private_key, "public": public_key, "nonce": nonce}


def generate_new_seed():
    """
        Generate new valid seed

    Returns:
        list: Valid seed phrase
    """
    wallet_seed = []
    seeds = SEEDWORDS.copy()
    while len(wallet_seed) < SEED_LENGTH:
        number_of_seeds = len(seeds)
        seed_word_index = random.randint(0, number_of_seeds - 1)
        seed_word = seeds.pop(seed_word_index)
        wallet_seed.append(seed_word)
    return wallet_seed


async def generate_new_address(public_key, nonce, dbconn):
    """
        Generate a new address based on a public key
        Then add it to the wallet database

    Args:
        public_key (str): Hex string public private key
        nonce (int): Nonce to generate new address for the public keyu
    """

    nonced_pub_key = f"{public_key}{nonce}"
    nonced_pub_key_bytes = str.encode(nonced_pub_key)
    address = hashlib.sha256(nonced_pub_key_bytes).hexdigest()
    success = await add_address_to_database(public_key, address, nonce, dbconn)
    if success:
        return address
    else:
        return ""


async def get_address_list(public_key, dbconn):
    pass
