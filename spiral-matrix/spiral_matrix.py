# import math
#
#
# def spiral(size):
#     matrix = [[0 for i in range(size)] for j in range(size)]
#     values = iter(range(1, size ** 2 + 1))
#     for frame in range(math.ceil(size / 2)):
#         for cell in range(size - 2 * frame - 1):
#             matrix[frame][frame + cell] = next(values)
#         for cell in range(size - 2 * frame - 1):
#             matrix[frame + cell][size - frame - 1] = next(values)
#         for cell in range(size - 2 * frame - 1):
#             matrix[size - frame - 1][size - frame - 1 - cell] = next(values)
#         for cell in range(size - 2 * frame - 1):
#             matrix[size - frame - 1 - cell][frame] = next(values)
#     if size % 2:
#         matrix[size // 2][size // 2] = next(values)
#     return matrix

def spiral(size):
    m = [[0] * size for i in range(size)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]           # koordynaty przemieszczeń po każdym zakręcie
    x, y, c = 0, -1, 1
    for i in range(2 * size - 1):                   # ile zakrętów
        for j in range((2 * size - i) // 2):        # ile komórek po danym zakręcie
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m


print(spiral(3))
