from random import seed, choice, choices, randint


# Sub Function
def pass_creator(ip: dict) -> str:
    """
    Function to generate a deterministic password based on
    name, site, master_key, pass_len, inc_spc, sp_str.

    Returns:
        password: An alphanumeric string that may include special characters.
    """

    # Setting seed
    seed(ip["SEED"])

    # Generating 1st 3 characters of the password.
    __password = [choice(ip["LC_STR"]), choice(ip["D_STR"]), choice(ip["UC_STR"])]

    # Generating remainder of the password.
    MERGED_STR = ip["D_STR"] + ip["UC_STR"] + ip["LC_STR"]
    __password.extend(choices(MERGED_STR, k=ip["PASS_LEN"] - 3))

    if ip["INC_SPC"]:
        # Generating special characters count.
        spc_count = randint(1, ip["PASS_LEN"] // 6 + 1)
        for _ in range(spc_count):
            # Choosing index to be swapped (except 1st 3 characters of the password.)
            i = randint(3, ip["PASS_LEN"] - 2)
            # Swapping pre generated characters with special characters.
            __password[i] = choice(ip["SP_STR"])

    # Converting list into string and returning it.
    return "".join(__password)
