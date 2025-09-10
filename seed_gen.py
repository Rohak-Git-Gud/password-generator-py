from hashlib import sha3_256
from random import seed, choice


# Seed Generator Function
def seed_creator(param_dict: dict) -> str:
    """
    Function to generate a hash string based on name, site, master_key, pass_len.

    Returns:
        seed: A string that is deterministic.
    """

    # Generating initial seed from input parameters
    _SEED_1 = param_dict["MASTER_KEY"] + param_dict["NAME"] + param_dict["SITE"]
    seed(_SEED_1)

    # Generating salt and creating new string
    _salt_value = (
        choice(param_dict["UC_STR"])
        + choice(param_dict["D_STR"])
        + choice(param_dict["LC_STR"])
    )
    _str_to_be_hashed = (
        _salt_value
        + param_dict["SITE"]
        + _salt_value
        + param_dict["NAME"]
        + _salt_value
        + param_dict["MASTER_KEY"]
        + _salt_value
    )

    # Hashing and converting it to string
    # Returning only portion of string as seed
    return sha3_256(_str_to_be_hashed.encode()).hexdigest()[: param_dict["PASS_LEN"]]
