from string import ascii_lowercase


def is_pangram(input_str):
    return not any(x for x in ascii_lowercase if x not in input_str.lower())
