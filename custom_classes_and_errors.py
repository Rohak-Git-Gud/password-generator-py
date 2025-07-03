import argparse


class CustomHelpFormatter(
    argparse.RawTextHelpFormatter,
    argparse.ArgumentDefaultsHelpFormatter,
):
    pass
    """Custom class to fuse RawTextHelpFormatter and ArgumentDefaultsHelpFormatter"""


def check_min_length(length: int) -> int:
    l = int(length)
    if l < 8:
        raise argparse.ArgumentTypeError(
            "Password length should be at least 8 characters."
        )
    return l
    """Function to handle minimum password length error"""
