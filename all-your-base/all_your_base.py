def rebase(base_from, number_from, base_to):
    if int(base_from) != base_from or int(base_to) != base_to or base_from < 2 or base_to < 2:
        raise ValueError("Wrong base number, it should be integer greater than 1")
    for digit in number_from:
        if int(digit) != digit or digit >= base_from or digit < 0:
            raise ValueError("Wrong sequence of digits")
    if base_from == base_to:
        return number_from
    decimal = 0
    for i, digit in enumerate(number_from[::-1]):
        decimal += digit * base_from ** i
    number_to = []
    while decimal > 0:
        number_to.append(decimal % base_to)
        decimal //= base_to
    return number_to[::-1]
