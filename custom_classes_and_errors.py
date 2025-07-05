import argparse


class CustomHelpFormatter(
    argparse.RawTextHelpFormatter,
    argparse.ArgumentDefaultsHelpFormatter,
):
    """Custom class to fuse RawTextHelpFormatter and ArgumentDefaultsHelpFormatter"""
    
    pass


def check_min_length(length: int) -> int:
    """Function to handle minimum password length error"""

    l = int(length)
    if l < 8:
        raise argparse.ArgumentTypeError(
            "Password length should be at least 8 characters."
        )
    return l
