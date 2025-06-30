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


def generate_password(
    NAME: str, SITE: str, MASTER_KEY: str, PASS_LEN: int = 16, INC_SP: bool = False
) -> str:
    """
    Generate a deterministic password based on:
        - NAME: User's name or identifier.
        - SITE: The service or website name.
        - MASTER_KEY: Master passphrase.
        - PASS_LEN: Desired length of the generated password.
        - INC_SP: Boolean of whether special characters are allowed or not.

    Returns:
        A password that is deterministic and may include special characters.
    """

    # Step 1: Generate randomiser and seed initiation
    random.seed(generate_randomiser(NAME, SITE, MASTER_KEY, PASS_LEN))

    # Step 2A: Generate password without special characters
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
    PASSWORD = (
        CHARACTERS[random.randint(36, 61)]
        + CHARACTERS[random.randint(26, 35)]
        + CHARACTERS[random.randint(0, 25)]
    )
    for _ in range(3, PASS_LEN):
        PASSWORD += CHARACTERS[random.randint(0, 61)]

    # Step 2B: Add special characters if True
    if INC_SP:
        SP_CHARS = "!@#$"
        SP_COUNT = random.randint(1, (PASS_LEN - 3) // 4)
        print(SP_COUNT)
        for k in range(SP_COUNT):
            i = random.randint(3, PASS_LEN)
            j = random.randint(0, 3)
            # PASSWORD[i] = SP_CHARS[j]
            print(k, " -> (", i, j, ")")

    # Step 3: Returns generated password
    return PASSWORD


print(generate_password("R", "www.R.com", "RMK", 12, True))
print(generate_password("R", "www.R.com", "RMK", 12, True))

# Convert to list for better comprehensive