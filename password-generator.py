import random
import hashlib
import string

# Global Variables for characters' strings
UC_STR = string.ascii_uppercase
LC_STR = string.ascii_lowercase
D_STR = string.digits

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
    salt_str = random.choice(UC_STR) + random.choice(D_STR) + random.choice(LC_STR)
    new_string = salt_str + SITE + salt_str + NAME + salt_str + MASTER_KEY + salt_str

    # Step 3: Return trimmed hex string of generated hash
    return hashlib.sha3_256(new_string.encode()).hexdigest()[:PASS_LEN]


def generate_password(
    NAME: str, SITE: str, MASTER_KEY: str, PASS_LEN: int = 16, INC_SPC: bool = False
) -> str:
    """
    Generate a deterministic password based on:
        - NAME: User's name or identifier.
        - SITE: The service or website name.
        - MASTER_KEY: Master passphrase.
        - PASS_LEN: Desired length of the generated password.
        - INC_SPC: Boolean of whether special characters are allowed or not.

    Returns:
        A password that is deterministic and may include special characters.
    """

    # Step 1: Generate randomiser and seed initiation
    random.seed(generate_randomiser(NAME, SITE, MASTER_KEY, PASS_LEN))

    # Step 2A: Generate password without special characters
    c_str = UC_STR + D_STR + LC_STR
    password_list = [
        c_str[random.randint(36, 61)],
        c_str[random.randint(26, 35)],
        c_str[random.randint(0, 25)]
    ]
    for _ in range(3, PASS_LEN):
        password_list.append(c_str[random.randint(0, 61)])

    # Step 2B: Add special characters if True
    if INC_SPC:
        spc_str = "!@#$%^&*-+_=?"
        spc_count = random.randint(1, PASS_LEN // 4)
        for k in range(spc_count):
            i = random.randint(3, PASS_LEN - 1)
            j = random.randint(0, 12)
            password_list[i] = spc_str[j]

    # Step 3: Returns generated password
    return ''.join(password_list)


print(generate_password("R", "www.R.com", "RMK", 8, True))
print(generate_password("R", "www.R.com", "RMK", 8, True))
print(generate_password("R", "www.R.com", "RMK"))
print(generate_password("R", "www.R.com", "RMK"))
