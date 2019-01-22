def distance2(first, second):
    if len(first) != len(second):
        raise ValueError("Not the same length")
    else:
        return sum(1 for i in range(len(first)) if first[i] != second[i])
