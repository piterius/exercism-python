def on_square(number):
    if number not in range(1, 65):
        raise ValueError("Wrong number, it should be integer from 1 to 64.")
    return 2 ** (number - 1)


def total_after(number):
    if number not in range(1, 65):
        raise ValueError("Wrong number, it should be integer from 1 to 64.")
    return sum((2 ** place for place in range(number)))
