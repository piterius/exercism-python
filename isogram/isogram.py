import re


def is_isogram(word):
    return not any(re.findall(r"([a-z]).*\1", word.lower()))
