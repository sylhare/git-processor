import re
import unicodedata
from difflib import SequenceMatcher


def similarity_ratio(a, b):
    return SequenceMatcher(None, a, b).ratio()


def is_similar(word, other):
    return similarity_ratio(trim(word), trim(other)) > 0.6


def remove_digit(word):
    return re.sub(r"\d+", "", word)


def trim(word):
    return remove_accent(
        remove_digit(word.replace(".", "").replace("\\", "").replace("-", "").replace(" ", "").lower()))


def remove_accent(text):
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)


if __name__ == "__main__":
    pass