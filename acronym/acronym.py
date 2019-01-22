import re


def abbreviate(input_str):
    outcome = re.findall(r'\b\w{1}', input_str)
    return "".join(outcome).upper()
