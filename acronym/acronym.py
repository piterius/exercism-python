import re


def abbreviate(input_str):
    outcome = re.findall(r'\b\w', input_str)
    return "".join(outcome).upper()
