import re

ONES = "1"
TWOS = "2"
THREES = "3"
FOURS = "4"
FIVES = "5"
SIXES = "6"
YACHT = r"((.)\2{4})"
FULL_HOUSE = r"((.)\2((?!\2).)\3{2}|(.)\4{2}((?!\4).)\5)"
FOUR_OF_A_KIND = r"((.)\2{3})"
LITTLE_STRAIGHT = "12345"
BIG_STRAIGHT = "23456"
CHOICE = "[1-6]{5}"


def score(dice, category):
    matches = re.findall(category, "".join(map(str, sorted(dice))))
    if any(matches) and category == YACHT:
        return 50
    elif any(matches) and category in (LITTLE_STRAIGHT, BIG_STRAIGHT):
        return 30
    elif any(matches) and category in (FULL_HOUSE, CHOICE):
        return sum(dice)
    elif any(matches) and category == FOUR_OF_A_KIND:
        return sum(map(int, matches[0][0]))
    else:
        return sum(map(int, matches))
