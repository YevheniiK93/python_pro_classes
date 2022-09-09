"""Implement functionality that will disable the setting
of class fields any value other than integers."""


import math


class Circle:

    def __init__(self, r: int):
        if not isinstance(r, int):
            raise TypeError()
        if r <= 0:
            raise ValueError()
        self.r = r

    def __str__(self):
        return f"Circle radius = {self.r}, diameter = {self.r * 2}, " \
               f"round length = {self.r * 2 * math.pi}"

    def __setattr__(self, attr_name, attr_value):
        if not isinstance(attr_value, int):
            raise TypeError()
        self.__dict__[attr_name] = attr_value


c = Circle(5)
print(c)
