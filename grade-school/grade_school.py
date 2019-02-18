class School:
    def __init__(self, name):
        self.name = name
        self._db = {i: [] for i in range(1, 9)}

    def add(self, name, grade_):
        if grade_ not in range(1, 9):
            raise ValueError("You entered invalid grade number")
        self._db[grade_].append(name)

    def grade(self, grade_):
        if grade_ not in range(1, 9):
            raise ValueError("You entered invalid grade number")
        return tuple(self._db[grade_])

    def sort(self):
        return [(grade, tuple(sorted(students))) for grade, students in self._db.items() if students]
