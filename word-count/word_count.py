import re
from collections import Counter


def word_count(input_str):
    word_list = re.findall(r"[a-z0-9]+(?:\'[a-z]+)?", str.lower(input_str))
    return dict(Counter(word_list))
