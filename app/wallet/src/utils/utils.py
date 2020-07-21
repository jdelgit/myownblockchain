from datetime import datetime
from .config import *
from .seedwords import SEEDWORDS


def utc():
    return datetime.utcnow()


def test_true(message):

    if message.lower() in ["y", "yes", "j", "ja"]:
        return True
    else:
        return False


def validate_seed_words(seed_words):
    input_set = set(seed_words)
    master_set = set(SEEDWORDS)
    if len(input_set) < SEED_LENGTH:
        # there were duplicates i guess
        return False
    return input_set.issubset(master_set)
