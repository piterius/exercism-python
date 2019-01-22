def sum_of_multiples(border, values):
    return sum(set(n for i in values for n in range(i, border, i)))
