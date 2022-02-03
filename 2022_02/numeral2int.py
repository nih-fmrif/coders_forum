def numeral2int(numeral):
    """Convert a Roman Numeral to an int"""

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
            raise ValueError('Invalid Roman Numeral "' + str(character) + '": using a numeral not contained in the dictionary')

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
