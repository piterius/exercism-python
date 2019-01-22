class Matrix:
    def __init__(self, mx):
        self.matrix = [[int(position) for position in row.split(" ")] for row in mx.split("\n")]

    def row(self, number):
        return self.matrix[number]

    def column(self, number):
        return [row[number] for row in self.matrix]
