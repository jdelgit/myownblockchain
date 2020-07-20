from utils.seedwords import SEEDWORDS, PRIVATEKEY_JOINSALT
from utils.config import SEED_LENGTH
import random
import hashlib


"""
    To Do:
    generate_digital_signature

"""

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


def generate_keypair_from_seed(wallet_seed=[]):
    """
        Generate public/private key pair from wallet seed

    Args:
        wallet_seed (list/str,optional): Seed phrase for generating private key

    Returns:
        dict: Wallet seeds along with generated public/private key pair
    """
    private_key = generate_private_key(wallet_seed)
    public_key = generate_public_key(private_key)
    return {"private": private_key, "public": public_key, "wallet_seed": wallet_seed}


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
    return {"private": private_key, "public": public_key}


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
