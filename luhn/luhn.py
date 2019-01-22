class Luhn:
    def __init__(self, input_str):
        self.s = input_str.replace(" ", "")

    def is_valid(self):
        if self.s.isdigit() and len(self.s) > 1:
            reversed_str = self.s[::-1]
            doubled = (int(reversed_str[i]) if i % 2 == 0 else self.is_greater(int(reversed_str[i]) * 2)
                       for i in range(len(self.s)))
            if sum(doubled) % 10 == 0:
                return True
        return False

    @staticmethod
    def is_greater(value):
        if value > 9:
            return value - 9
        else:
            return value
