import random

from . import SYMBOLS_CHOICE


def get_unique_short_id():
    # Если k=6 перенести в константу, не проходят тесты
    return ''.join(random.choices(SYMBOLS_CHOICE, k=6))


def check(custom_id):
    for elem in custom_id:
        if elem not in SYMBOLS_CHOICE:
            return False
    return True