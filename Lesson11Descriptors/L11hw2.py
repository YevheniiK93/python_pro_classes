"""Implement functionality that will disable the setting
of class fields any value other than integers."""


class Circle:

    def __init__(self, radius: int):
        if not isinstance(radius, int):
            raise TypeError()
        if radius <= 0:
            raise ValueError()

        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, int):
            raise TypeError()
        if value <= 0:
            raise ValueError()

        self.__radius = value

    @radius.deleter
    def radius(self):
        pass


c = Circle(5)
print(c.radius)
c.radius = 10
print(c.radius)
