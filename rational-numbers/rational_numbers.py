from math import gcd


class Rational:
    def __init__(self, numerator, denominator):
        if denominator:
            result = gcd(numerator, denominator)
            self.numerator = int(numerator / result)
            self.denominator = int(denominator / result)
        else:
            raise ValueError("Denominator can't be zero")

    def __eq__(self, other):
        return self.numerator * self.denominator == other.numerator * other.denominator

    def __add__(self, other):
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Rational(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def __truediv__(self, other):
        if other.numerator:
            return Rational(self.numerator * other.denominator,
                            other.numerator * self.denominator)
        else:
            raise ZeroDivisionError()

    def __abs__(self):
        return Rational(abs(self.numerator), abs(self.denominator))

    def __pow__(self, power, modulo=None):
        if int(power) == power:
            return Rational(pow(self.numerator, power), pow(self.denominator, power)) if power >= 0 else Rational(
                pow(self.denominator, abs(power)), pow(self.numerator, abs(power)))
        else:
            return pow(self.numerator, power) / pow(self.denominator, power)

    def __rpow__(self, other):
        return pow(other, self.numerator / self.denominator)
