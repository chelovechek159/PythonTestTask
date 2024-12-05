import os


def get_random_hex_string(length=6):
    return os.urandom(length).hex()