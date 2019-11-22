import re
import unicodedata
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def compare(word, other):
    return similar(trim(word), trim(other)) > 0.5


def remove_digit(word):
    return re.sub(r"\d+", "", word)


def trim(word):
    return remove_accent(remove_digit(word.replace(".", "").replace(" ", "").lower()))


def remove_accent(text):
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)
