from random import seed, choice, choices, randint


# Sub Function
def pass_creator(param_dict: dict) -> str:
    """
    Function to generate a deterministic password based on
    name, site, master_key, pass_len, inc_spc, sp_str.

    Returns:
        password: An alphanumeric string that may include special characters.
    """

    # Setting seed
    seed(param_dict["SEED"])

    # Generating 1st 3 characters of the password.
    __password = [
        choice(param_dict["LC_STR"]),
        choice(param_dict["D_STR"]),
        choice(param_dict["UC_STR"]),
    ]
    # List is used instead of string for better performance and allows list comprehension and mutability.

    # Generating remainder of the password.
    _MERGED_STR = param_dict["D_STR"] + param_dict["UC_STR"] + param_dict["LC_STR"]
    __password.extend(choices(_MERGED_STR, k=param_dict["PASS_LEN"] - 3))

    if param_dict["INC_SPC"]:
        # Generating special characters count.
        spc_count = randint(1, param_dict["PASS_LEN"] // 6 + 1)
        for _ in range(spc_count):
            # Choosing index to be swapped (except 1st 3 characters of the password.)
            i = randint(3, param_dict["PASS_LEN"] - 2)
            # Swapping pre generated characters with special characters.
            __password[i] = choice(param_dict["SP_STR"])

    # Converting list into string and returning it.
    return "".join(__password)
