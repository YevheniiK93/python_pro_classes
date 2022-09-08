"""Create a class decorator with a parameter. The parameter should be
a string that should be added (on the left) to the result of the method
__str__."""


def add_str_left(text):
    def wrapper(cls):
        def inner(*args, **kwargs):
            new_instance = cls(*args, **kwargs)
            return text + new_instance.__str__()
        return inner
    return wrapper


class Circle:
    def __init__(self, r: int | float):
        self.r = r

    @add_str_left("Class result: ")
    def __str__(self):
        return f"r = {self.r}, d = {self.r * 2}, l = {2 * 3.14 * self.r}"


c_1 = Circle(5)
print(c_1)
