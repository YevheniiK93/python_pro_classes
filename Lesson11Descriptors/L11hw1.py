"""Create a descriptor that will make class fields managed by it
read-only."""


class MyDescriptor:
    def __init__(self):
        pass

    def __get__(self, instance_self, instance_class):
        return instance_self.p

    def __set__(self, instance_self, value):
        raise AttributeError("Field is read-only")

    def __delete__(self, instance_self):
        raise AttributeError("You can't delete field")


class Box:

    def __init__(self, x, y, z):
        self.p = x*y*z

    value = MyDescriptor()



b1 = Box(2,3,4)
print(b1.value)

