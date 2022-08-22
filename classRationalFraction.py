import math


class RationalFraction:
    """
    Create Rational Fraction class.
    Add-, sub-, mul-, simile- functions was implemented
    """
    def __init__(self, a: int, b: int):
        if not isinstance(a, int):
            raise TypeError()
        if not isinstance(b, int):
            raise TypeError()
        if not b:
            raise ZeroDivisionError()

        self.a = a
        self.b = b

        tmp = math.gcd(self.a, self.b)
        self.a //= tmp
        self.b //= tmp

    def __add__(self, other):
        if isinstance(other, RationalFraction):
            b = self.b * other.b
            a = other.b * self.a + self.b * other.a

            return RationalFraction(a, b)

    def __sub__(self, other):
        if isinstance(other, RationalFraction):
            b = self.b * other.b
            a = other.b * self.a - self.b * other.a

            return RationalFraction(a, b)

    def __mul__(self, other):
        if isinstance(other, RationalFraction):
            a = self.a * other.a
            b = self.b * other.b

            return RationalFraction(a, b)

    def __lt__(self, other):
        if isinstance(other, RationalFraction):
            return self.a / self.b < other.a / other.b

        return NotImplemented

    def __le__(self, other):
        return self.a / self.b <= other.a / other.b

    def __gt__(self, other):
        return self.a / self.b > other.a / other.b

    def __ge__(self, other):
        return self.a / self.b >= other.a / other.b

    def __eq__(self, other):
        return self.a / self.b == other.a / other.b

    def __ne__(self, other):
        return self.a / self.b != other.a / other.b

    def __str__(self):
        if self.a == 0:
            return f'0'
        elif self.b == 1:
            return f'{self.a}'
        elif self.a == self.b:
            return f'{self.a} // {self.b}'

        return f'{self.a} / {self.b}'


x = RationalFraction(1, 2)
y = RationalFraction(2, 3)


print(x+y)
print(x-y)
print(x*y)
print(x < y)
