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
        - NAME, SITE, MASTER_KEY, PASS_LEN:
          derived from NAME, SITE, MASTER_KEY, PASS_LEN of generate_password function, respectively.

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


# Sub Function
def generate_password(
    NAME: str, SITE: str, MASTER_KEY: str, PASS_LEN: int, INC_SPC: bool, SP_STR: str
) -> str:
    """
    Generate a deterministic password based on:
        - NAME, SITE, MASTER_KEY, PASS_LEN, INC_SPC, SP_STR:
          maps to name, site, master_key, length, nsp, specialC of main function.

    Returns:
        A password that is deterministic and may include special characters.
    """

    # Step 1: Generate randomiser and seed initiation using _generate_randomiser function
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
        spc_count = random.randint(1, 2 * (PASS_LEN // 8))
        for _ in range(spc_count):
            i = random.randint(3, PASS_LEN - 1)
            j = random.randint(0, SPC_LEN - 1)
            password_list[i] = SP_STR[j]

    # Step 3: Returns generated password
    return "".join(password_list)


# Main Function
def main():
    """
    Main executable functions that handles CLI and parameters' extraction.
    CLI parameters:
        - name: User's name or identifier.
        - site: The service or website name.
        - master_key: Master passphrase.
        - length (l): Desired length of the generated password.
        - nsp: Boolean of whether special characters are allowed or not.
        - specialC (scs): String of allowed special characters.
    """

    # Step 1: Initializing argparse's argument parser
    parser = argparse.ArgumentParser(
        prog="password-generator",
        description="Deterministic password generator CLI tool.",
        epilog="To know more, check out the README.md file or the function-wise explanation.",
        formatter_class=CustomHelpFormatter,
    )

    # Step 2A: Adding required arguments to the parser
    parser.add_argument("name", type=str, help="your name or identifier")
    site_help_str = (
        'service or website name\nNote: "www.google.com" is different from "google.com"'
    )
    parser.add_argument("site", type=str, help=site_help_str)
    master_help_str = "your master key/passphrase\nMake sure it is something you remember but not that obvious to figure out"
    parser.add_argument("master_key", type=str, help=master_help_str)

    # Step 2B: Adding optional arguments to the parser
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

    # Step 3: Execute parser and store values in dictionary called args
    args = parser.parse_args()

    # Step 4: Print password generated from generate_password
    print(
        "Hello,",
        args.name,
        "Password for",
        args.site,
        "is:",
        generate_password(
            args.name, args.site, args.master_key, args.length, args.nsp, args.specialC
        ),
    )


# Entry Point
if __name__ == "__main__":
    main()
