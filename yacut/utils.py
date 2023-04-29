import random
from string import ascii_letters, digits

SYMBOLS_CHOICE = list(ascii_letters + digits)


def get_unique_short_id():
    return ''.join(random.choices(SYMBOLS_CHOICE, k=6))


def check(custom_id):
    for elem in custom_id:
        if elem not in SYMBOLS_CHOICE:
            return False
    return True