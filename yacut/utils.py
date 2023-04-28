import random
import string
from string import ascii_letters, digits

SYMBOLS_CHOICE = list(ascii_letters + digits)


def get_unique_short_id():
    short = ''.join(random.choices(string.ascii_letters + digits, k=6))
    return short


def check(custom_id):
    for elem in custom_id:
        if elem not in SYMBOLS_CHOICE:
            return False
    return True