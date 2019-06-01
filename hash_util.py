import hashlib as hl
import json


def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block):
    """Hashes a block and returns a string representation of it

    :param block: the block that should be ashed
    :return: the block hashed
    """
    return hash_string_256(json.dumps(block,sort_keys=True).encode())