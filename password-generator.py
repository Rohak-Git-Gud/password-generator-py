import random
import hashlib


def generate_randomiser(NAME: str, SITE: str, MASTER_KEY, PASS_LEN: int) -> str:
    """
    Generate a hash string based on:
        - NAME: User's name or identifier.
        - SITE: The service or website name.
        - MASTER_KEY: Master passphrase.
        - PASS_LEN: Desired length of the generated password.

    Returns:
        A randomiser that is deterministic of fixed length.
    """

    # Step 1: Combine strings to create a seed
    init_string = MASTER_KEY + NAME + SITE
    random.seed(init_string)

    # Step 2: Create new string based on seed and salted digits
    mid = str(random.randint(0, 9))
    new_string = mid + SITE + mid + NAME + mid + MASTER_KEY + mid

    # Step 3: Return trimmed hex string of generated hash
    return hashlib.sha3_256(new_string.encode()).hexdigest()[:PASS_LEN]
