class Garden:
    flora = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}
    children = ("Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid",
                "Larry")

    def __init__(self, rows, students=children):
        self.pots = rows.split()
        self.students = students

    def plants(self, name):
        index = sorted(self.students).index(name) * 2
        return list(map(self.flora.get, [self.pots[0][index], self.pots[0][index + 1], self.pots[1][index],
                                         self.pots[1][index + 1]]))
