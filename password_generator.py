import random
import hashlib
import string
import argparse
from custom_classes_and_errors import CustomHelpFormatter, check_min_length

# Global Variables for characters' strings
UC_STR = string.ascii_uppercase
LC_STR = string.ascii_lowercase
D_STR = string.digits


# Helper Function
def _generate_randomiser(NAME: str, SITE: str, MASTER_KEY: str, PASS_LEN: int) -> str:
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
    """
    Explanation:
        - String of MASTER_KEY + NAME + SITE, in that order becomes the initial seed
          on which python's random function works.
        - A 3 character string of Uppercase + Digit + Lowercase is created
          which acts as a salt.
        - A new string is created such as, salt + SITE + salt + NAME + salt + MASTER_KEY + salt.
          (The location swapping is deliberate and not a mere overlook)
        - A SHA3 (256 BIT) hash is created of the new encoded string 
          and then converted to hexadecimal string format.
        - Only the beginning PASS_LEN characters of it is returned.
    """


# Sub Function
def generate_password(
    NAME: str, SITE: str, MASTER_KEY: str, PASS_LEN: int, INC_SPC: bool, SP_STR: str
) -> str:
    """
    Generate a deterministic password based on:
        - NAME: User's name or identifier.
        - SITE: The service or website name.
        - MASTER_KEY: Master passphrase.
        - PASS_LEN: Desired length of the generated password.
        - INC_SPC: Boolean of whether special characters are allowed or not.
        - SP_STR: String of allowed special characters.

    Returns:
        A password that is deterministic and may include special characters.
    """

    # Step 1: Generate randomiser and seed initiation
    random.seed(_generate_randomiser(NAME, SITE, MASTER_KEY, PASS_LEN))

    # Step 2A: Generate password without special characters
    c_str = UC_STR + D_STR + LC_STR
    password_list = [
        c_str[random.randint(36, 61)],
        c_str[random.randint(26, 35)],
        c_str[random.randint(0, 25)],
    ]
    for _ in range(3, PASS_LEN):
        password_list.append(c_str[random.randint(0, 61)])

    # Step 2B: Add special characters if True
    if INC_SPC:
        SPC_LEN = len(SP_STR)
        spc_count = random.randint(1, PASS_LEN // 4)
        for _ in range(spc_count):
            i = random.randint(3, PASS_LEN - 1)
            j = random.randint(0, SPC_LEN - 1)
            password_list[i] = SP_STR[j]

    # Step 3: Returns generated password
    return "".join(password_list)
    """
    Explanation:
    - A seed is generated using generate_randomiser function,
      and NAME, SITE, MASTER_KEY, PASS_LEN as parameters.
      (This is important for the underlying math.
      We want the passwords that are generated to be random but deterministic.
      This is because, we want the same password, each time the exact same parameters are received.)
    - Each password will have at least 1 lowercase, digit, uppercase.
    - Remaining characters will be pseudo-randomly generated
      from the alphanumeric ranges - A-Z, a-z, 0-9.
    - If Special Characters are to be included in the password,
      a few characters after the 3 character will be swapped with a special character.
    - Return the password as a string.
      (Lists are used for better performance and allows list comprehension.)
    """


# Main Function
def main():

    # Argparse Init
    parser = argparse.ArgumentParser(
        prog="password-generator",
        description="Deterministic password generator CLI tool.",
        epilog="To know more, check out the README.md file or the function-wise explanation.",
        formatter_class=CustomHelpFormatter,
    )

    # Required Arguments
    parser.add_argument("name", type=str, help="your name")
    site_help_str = 'site name\nNote: "www.google.com" is different from "google.com"'
    parser.add_argument("site", type=str, help=site_help_str)
    master_help_str = "your master key/passphrase\nMake sure it is something you remember but not that obvious to figure out"
    parser.add_argument("master_key", type=str, help=master_help_str)

    # Optional Arguments
    parser.add_argument(
        "-l",
        "--length",
        metavar="",
        type=check_min_length,
        default=12,
        help="password length\nMin. 8 characters",
    )
    parser.add_argument(
        "--nsp",
        action="store_false",
        help="flag to exclude special characters from password generation",
    )
    parser.add_argument(
        "-scs",
        "--specialC",
        metavar="",
        type=str,
        default="!@#$&*-+_.?",
        help="use it to change the acceptable special characters used\nNot recommended, unless you know what you're doing",
    )

    # Execute Parser
    args = parser.parse_args()

    # Generate and print password
    print(
        "Password:",
        generate_password(
            args.name, args.site, args.master_key, args.length, args.nsp, args.specialC
        ),
    )


# Entry Point
if __name__ == "__main__":
    main()

# print(generate_password("R", "www.R.com", "RMK", 8, True))
# print(generate_password("R", "www.R.com", "RMK", 8, True))
# print(generate_password("R", "www.R.com", "RMK"))
# print(generate_password("R", "www.R.com", "RMK"))
