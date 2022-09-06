class Rectangle:

    def __init__(self, a: int | float, b: int | float):
        if not isinstance(a, (int, float)):
            raise TypeError()
        if not isinstance(b, (int, float)):
            raise TypeError()

        if a <= 0 or b <= 0:
            raise ValueError()

        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return self.square() < other.square()
        tmp = self.square() + other.square()
        return Rectangle(1, tmp)

    def __mul__(self, other: int | float):
        if not isinstance(other, (int, float)):
            return NotImplemented
        tmp = self.square() * other
        return Rectangle(1, tmp)

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.square() < other.square()

        return NotImplemented

    def __le__(self, other):
        return self.square() <= other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __ge__(self, other):
        return self.square() >= other.square()

    def __eq__(self, other):
        return self.square() == other.square()

    def __ne__(self, other):
        return self.square() != other.square()

    def __str__(self):
        return f'{self.a} x {self.b}'


rect_1 = Rectangle(1, 3)
rect_2 = Rectangle(2, 4)

x = rect_1 + rect_2

print(rect_1 < rect_2)
print(x)
print(rect_2 * 4)

