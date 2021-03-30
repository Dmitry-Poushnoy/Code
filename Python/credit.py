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


def check_cardnum(num: str) -> str:
    """
    Check if input is a real card number. Main function.
    :param num: String which we want to check. Is it a card number?
    :return: Name of card AMEX\n or MASTERCARD\n or VISA\n or INVALID\n
    """
    name_card = 'AMEX', 'MASTERCARD', 'VISA', 'INVALID'
    if check_13to16(num):
        for i in {'34', '37'}:
            if num.startswith(i):
                return "May be " + name_card[0]
        for i in {'51', '52', '53', '54', '55'}:
            if num.startswith(i):
                return "May be " + name_card[1]
        if num.startswith('4'):
            return "May be " + name_card[2]
        return "May be cardnumber."
    else:
        return name_card[3]


# MAIN PROGRAM
number = input("Number: ")
print(check_cardnum(number))
