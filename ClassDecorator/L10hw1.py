"""Create a decorator that registers the
class being decorated in the class list."""


class_lst = []


def add_class_to_list(cls):
    class_lst.append(cls)
    return cls


@add_class_to_list
class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Box x = {self.x} y = {self.y} z = {self.z}"


@add_class_to_list
class Circle:
    def __init__(self, r: int | float):
        self.r = r

    def __str__(self):
        return f"Circle r = {self.r}, d = {self.r * 2}, l = {2 * 3.14 * self.r} "

print(class_lst)
