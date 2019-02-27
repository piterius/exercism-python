ALLERGENS = {1: "eggs", 2: "peanuts", 4: "shellfish", 8: "strawberries", 16: "tomatoes", 32: "chocolate", 64: "pollen",
             128: "cats"}


class Allergies:
    def __init__(self, score):
        self.lst = [ALLERGENS[i] for i in ALLERGENS if i & score]

    def is_allergic_to(self, product):
        return product in self.lst
