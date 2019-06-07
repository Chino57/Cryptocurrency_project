"""Provide hasher helper methods"""

import hashlib as hl
import json

# all__ = ['hash_string_256','hash_block']


def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block):
    """Hashes a block and returns a string representation of it

    :param block: the block that should be ashed
    :return: the block hashed
    """
    hashable_block = block.__dict__.copy()
    hashable_block['transactions'] = [
        tx.to_ordered_dict() for tx in hashable_block['transactions']
    ]
    return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())
