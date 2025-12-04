from argparse import ArgumentParser
from custom_classes_and_errors import CustomHelpFormatter, check_min_length


# Argument Parser Builder Function
def parser_creator() -> ArgumentParser:
    """
    Function that handles CLI and parameters' extraction.

    CLI parameters:
        - name: User's name or identifier.
        - site: The service or website name.
        - master_key: Master passphrase.
        - length (l): Desired length of the generated password.
        - nsp: Boolean of whether special characters are allowed or not.
        - specialC (scs): String of allowed special characters.
        
    Returns:
        parser: An argument parser object.
    """

    # Initializing argparse's argument parser
    _parser = ArgumentParser(
        prog="password-generator",
        description="Deterministic password generator CLI tool.",
        epilog="To know more, check out the README.md file or the function-wise explanation.",
        formatter_class=CustomHelpFormatter,
    )

    # Adding required arguments to the parser
    _parser.add_argument("name", type=str, help="your name or identifier")
    _parser.add_argument(
        "site",
        type=str,
        help='service or website name\nNote: "www.google.com" is different from "google.com"',
    )
    _parser.add_argument(
        "master_key",
        type=str,
        help="your master key/passphrase\nMake sure it is something you remember but not that obvious to figure out",
    )

    # Adding optional arguments to the parser
    _parser.add_argument(
        "-l",
        "--length",
        metavar="",
        type=check_min_length,
        default=12,
        help="password length\nMin. 8 characters",
    )
    _parser.add_argument(
        "--nsp",
        action="store_false",
        help="flag to exclude special characters from password generation",
    )
    _parser.add_argument(
        "-scs",
        "--specialC",
        metavar="",
        type=str,
        default="!@#$%^*-+_=?",
        help="use it to change the acceptable special characters used\nNot recommended, unless you know what you're doing",
    )

    return _parser
