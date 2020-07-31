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
    """
        Validate incoming seedwords against known valid words

    Args:
        seed_words (list): List of seedwords (str)

    Returns:
        bool: Whether the seedwords are valid or not
    """
    input_set = set(seed_words)
    master_set = set(SEEDWORDS)
    if len(input_set) < SEED_LENGTH:
        # there were duplicates i guess
        return False
    return input_set.issubset(master_set)

def record_to_dict(record):
    """

        Convert record object to dict object
    Args:
        record (asyncpg.Record): Record object

    Returns:
        dict: Record converted to dict
    """
    record_data = {}
    for fieldnames,field in record.items():
        record_data[fieldnames] = field
    return record_data