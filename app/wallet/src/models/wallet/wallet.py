import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.utils import validate_seed_words
from utils.config import SEED_LENGTH
from models.keymanager import keymanager as km
import re


async def setup_wallet_from_seed(input_seed=""):
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
    wallet = km.generate_keypair_from_seed(wallet_seed=wallet_seed)
    return wallet
