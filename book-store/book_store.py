def calculate_total(input_list):
    book_list = [0, 0, 0, 0, 0]
    total = 0
    discounts = {1: 100, 2: 95, 3: 90, 4: 80, 5: 75}
    for i in input_list:
        book_list[i-1] += 1
    book_list = [y for y in book_list if y != 0]
    start_no = len(book_list)
    if len(book_list) == 5 and book_list[3] == book_list[4] and book_list[2] > book_list[3]:
        start_no = 4
    for i in range(start_no, 0, -1):
        while len(book_list) >= i:
            book_list[:i] = [book_list[x] - 1 for x in range(i) if book_list[x] - 1 > 0]
            total += i * discounts[i] * 8
    return total
