import itertools
import re
import unicodedata
from difflib import SequenceMatcher


def is_similar(word, other):
    return similarity_ratio(trim(word), trim(other)) > 0.59


def is_any_similar(a, in_list):
    return len(list(filter(lambda x: is_similar(a, x), in_list))) > 0


def similarity_ratio(a, b):
    return SequenceMatcher(None, a, b).ratio()


def remove_digit(word):
    return re.sub(r"\d+", "", word)


def remove_accent(text):
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)


def trim(word):
    return remove_accent(
        remove_digit(word.replace(".", "").replace("\\", "").replace("-", "").replace(" ", "").lower()))


def alias_dictionary_of(names):
    results = {}
    for a, b in itertools.combinations(names, 2):
        try:
            results[b] += [b]
        except KeyError:
            results[b] = [b]

        if is_similar(a, b):
            if a != b:
                results[b].append(a)
                if is_any_similar(a, results[b]):
                    results.pop(a, None)
        else:
            results[b].remove(b)

    return results
