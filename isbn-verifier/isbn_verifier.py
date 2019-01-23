import re


def verify(isbn):
    isbn = isbn.replace("-", "").upper()
    if not re.fullmatch(r"[0-9]{9}(X|[0-9])", isbn):
        return False
    result = sum(((10-i) * int(isbn[i]) for i in range(9)))
    result += 10 if isbn[-1] == 'X' else int(isbn[-1])
    return result % 11 == 0
