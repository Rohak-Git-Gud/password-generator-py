from string import ascii_lowercase, ascii_uppercase, digits
from parser_gen import parser_creator
from seed_gen import seed_creator
from pass_gen import pass_creator


# Main Function
def main():
    """
    Main function that calls other subfunctions,
    deals with the input parameters dictionary for resource allocation and delocation
    and prints the generated password.
    """

    # Calling parser_creator to create parser, executing and storing arguments.
    parser = parser_creator()
    args = parser.parse_args()

    # Creating dictionary to minimize function parameter count.
    _param_dict = {
        "NAME": args.name,
        "SITE": args.site,
        "MASTER_KEY": args.master_key,
        "PASS_LEN": args.length,
        "LC_STR": ascii_lowercase,
        "UC_STR": ascii_uppercase,
        "D_STR": digits,
    }

    # Calling seed_creator to generate SEED and storing it.
    _param_dict["SEED"] = seed_creator(_param_dict)

    # Resource delocation and delayed allocation for better performance.
    del _param_dict["NAME"], _param_dict["SITE"], _param_dict["MASTER_KEY"]

    _param_dict["INC_SPC"] = args.nsp
    _param_dict["SP_STR"] = args.specialC

    # Calling pass_creator and printing generated password.
    print(
        "Hello,",
        args.name,
        "\nPassword for",
        args.site,
        "is:",
        pass_creator(_param_dict),
    )


# Entry Point
if __name__ == "__main__":
    main()
