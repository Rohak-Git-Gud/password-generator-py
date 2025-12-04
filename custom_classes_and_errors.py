from argparse import (
    RawTextHelpFormatter,
    ArgumentDefaultsHelpFormatter,
    ArgumentTypeError,
)


class CustomHelpFormatter(
    RawTextHelpFormatter,
    ArgumentDefaultsHelpFormatter,
):
    """Custom class to fuse RawTextHelpFormatter and ArgumentDefaultsHelpFormatter classes."""

    pass


def check_min_length(check_value: str) -> int:
    """Function to handle minimum password length error."""

    try:
        return_length = int(check_value)
    except ValueError:
        raise ArgumentTypeError(check_value, "is not a valid integer.")
    
    if return_length < 8:
        raise ArgumentTypeError("Password length should be at least 8 characters.")
    return return_length
