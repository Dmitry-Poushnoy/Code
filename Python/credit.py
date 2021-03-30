import re

def check_13to16(num: str) -> bool:
    """
    Check if input string consists of 13 to 16 digits.
    :param num: String which we want to check.
    :return: True if input string consists of 13 to 16 digits.
    """
    mask_13to16 = re.compile('[0-9]{13,16}')
    match_13to16 = mask_13to16.match(num)
    mask_17 = re.compile('[0-9]{17}')
    match_17 = mask_17.match(num)
    if match_13to16 and (match_17 is None):
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
        return "May be cardnumber."
    else:
        return name_card[3]


number = input("Number: ")
print(check_cardnum(number))
