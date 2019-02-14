from collections import Counter


def chain(input_dominoes):
    if not input_dominoes:
        return []
    input_dominoes = input_dominoes[:]
    number_of_elements = Counter((element for domino in input_dominoes for element in domino))
    if any(value for value in number_of_elements.values() if value % 2 != 0):
        return None
    output = []
    while input_dominoes:
        first_number = output[-1][1] if output else max(number_of_elements,
                                                        key=lambda x: number_of_elements.get(x))
        neighbour_numbers = []
        for number1, number2 in input_dominoes:
            if number1 == first_number:
                neighbour_numbers.append(number2)
            if number2 == first_number:
                neighbour_numbers.append(number1)
        next_number = max(Counter(neighbour_numbers), default=False,
                          key=lambda x: Counter(neighbour_numbers).get(x))
        if not next_number:
            return None
        output.append((first_number, next_number))
        if (first_number, next_number) in input_dominoes:
            input_dominoes.remove((first_number, next_number))
        else:
            input_dominoes.remove((next_number, first_number))
    return output
