def numeral2int(numeral):
    """
    Convert a roman numeral as a string to an integer.

    Parameters
    ----------
    s : str
        Roman numeral to be converted to an integer


    Returns
    -------
    int
        Integer value of Roman numeral

    Raises
    ------
    ValueError
        If one of the inputs is not a valid Roman numeral.
    """
    if numeral == "":
        raise ValueError("Empty Roman numeral. For historical accuracy, we don't return 0.")

    # forcing all characters to uppercase
    numeral = numeral.upper()

    # creating a dictionary of roman numerals and their values
    numeral_dict = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
                    }

    # creating a list of the numerals in the string
    numeral_list = list(numeral)

    for character in numeral_list:
        if character not in numeral_dict.keys():
            raise ValueError(f'Invalid Roman Numeral "{str(character)}":' \
                f' using a numeral not contained in the dictionary ({numeral_dict.keys()}).')

    # reverse the list order
    numeral_list.reverse()

    # initialize the summator
    numeral_int = 0

    # iterate through the list
    for i in range(len(numeral_list)):
        # if we're at the first element, add the value to the summator
        if i == 0:
            # add the first reversed list value
            numeral_int += numeral_dict[numeral_list[i]]
        elif numeral_dict[numeral_list[i]] > numeral_dict[numeral_list[i-1]]:
            numeral_int += numeral_dict[numeral_list[i]]
        else:
            numeral_int -= numeral_dict[numeral_list[i]]
    return numeral_int
