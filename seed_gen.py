from hashlib import sha3_256
from random import seed, choice


# Seed Generator Function
def seed_creator(ip: dict) -> str:
    """
    Function to generate a hash string based on name, site, master_key, pass_len.

    Returns:
        seed: A string that is deterministic.
    """

    # Generating initial seed from input parameters
    _SEED_1 = ip["MASTER_KEY"] + ip["NAME"] + ip["SITE"]
    seed(_SEED_1)

    # Generating salt and creating new string
    _salt_value = choice(ip["UC_STR"]) + choice(ip["D_STR"]) + choice(ip["LC_STR"])
    _str_to_be_hashed = (
        _salt_value
        + ip["SITE"]
        + _salt_value
        + ip["NAME"]
        + _salt_value
        + ip["MASTER_KEY"]
        + _salt_value
    )

    # Hashing and converting it to string
    # Returning only portion of string as seed
    return sha3_256(_str_to_be_hashed.encode()).hexdigest()[: ip["PASS_LEN"]]
