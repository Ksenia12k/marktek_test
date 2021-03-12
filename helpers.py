import random


def get_locator_with_name(locator, name):
    result = locator[0], locator[1].replace('<name>', name)
    return result


def get_random_number(min, max):
    return random.randint(min, max)
