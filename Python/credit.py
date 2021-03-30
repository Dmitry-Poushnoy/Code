import re


def check_13to16(num: str) -> bool:
    """
    Check if input string consists of 13 or 15 to 16 digits.
    :param num: String which we want to check.
    :return: True if input string consists of 13 or 15 to 16 digits.
    """
    number_of_symbols = len(num)
    if number_of_symbols == 13:
        mask = re.compile('[0-9]{13}')
    elif number_of_symbols == 15:
        mask = re.compile('[0-9]{15}')
    elif number_of_symbols == 16:
        mask = re.compile('[0-9]{16}')
    else:
        return False

    match = mask.match(num)
    if match:
        return True
    else:
        return False


def str_to_list_int(num: str) -> list:
    """
    Convert string to list of integers.
    :param num: String of digits symbols.
    :return: List on integers equal to initial string symbols.
    """
    symbols_number = len(num)
    num_list = list(num)
    for i in range(symbols_number):
        num_list[i] = int(num_list[i])
    return num_list


def luhn(num: str) -> bool:
    """
    Check if algorithm of Luhn is correct with num.
    :param num: String which we check by algorithm of Luhn.
    :return: True if algorithm of Luhn is correct witn num.
    """
    num_list = str_to_list_int(num)
    # TODO: Realise algorithm of Luhn
    return True


def check_cardnum(num: str) -> str:
    """
    Check if input is a real card number. Main function.
    :param num: String which we want to check. Is it a card number?
    :return: Name of card AMEX\n or MASTERCARD\n or VISA\n or INVALID\n
    """
    name_card = 'AMEX', 'MASTERCARD', 'VISA', 'INVALID'
    if check_13to16(num):
        # Check for AMEX
        for i in {'34', '37'}:
            if num.startswith(i) and len(num) == 15 and luhn(num):
                return name_card[0]
        # Check for MASTERCARD
        for i in {'51', '52', '53', '54', '55'}:
            if num.startswith(i) and len(num) == 16 and luhn(num):
                return name_card[1]
        # Check for VISA
        if num.startswith('4') and len(num) in {13, 16} and luhn(num):
            return name_card[2]
        # Else INVALID
        return name_card[3]
    else:
        return name_card[3]


# MAIN PROGRAM
number = input("Number: ")
print(check_cardnum(number))
