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
    _input_params = {
        "NAME": args.name,
        "SITE": args.site,
        "MASTER_KEY": args.master_key,
        "PASS_LEN": args.length,
        "LC_STR": ascii_lowercase,
        "UC_STR": ascii_uppercase,
        "D_STR": digits,
    }

    # Calling seed_creator to generate SEED and storing it.
    _input_params["SEED"] = seed_creator(_input_params)

    # Resource delocation and allocation for better performance.
    del _input_params["NAME"]
    del _input_params["SITE"]
    del _input_params["MASTER_KEY"]

    _input_params["INC_SPC"] = args.nsp
    _input_params["SP_STR"] = args.specialC

    # Calling pass_creator and printing generated password.
    print(
        "Hello,",
        args.name,
        "\nPassword for",
        args.site,
        "is:",
        pass_creator(_input_params),
    )


# Entry Point
if __name__ == "__main__":
    main()
