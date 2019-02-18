def spiral(size):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    values = iter(range(1, size ** 2 + 1))
    for frame in range(size // 2):
        for cell in range(size - 2 * frame - 1):
            matrix[frame][frame + cell] = next(values)
        for cell in range(size - 2 * frame - 1):
            matrix[frame + cell][size - frame - 1] = next(values)
        for cell in range(size - 2 * frame - 1):
            matrix[size - frame - 1][size - frame - 1 - cell] = next(values)
        for cell in range(size - 2 * frame - 1):
            matrix[size - frame - 1 - cell][frame] = next(values)
    if size % 2:
        matrix[size // 2][size // 2] = next(values)
    return matrix
