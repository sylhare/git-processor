import re


def compare(word, other):
    return remove_digit(word) == remove_digit(other)


def remove_digit(word):
    return re.sub(r"\d+", "", word)
