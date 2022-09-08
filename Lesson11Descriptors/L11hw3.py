"""Implement a class property that has the following
functionality: when setting the value of this property to a file with
a certain name should save the time (when set
property value) and the set value."""

from datetime import datetime


class MyDescriptor:
    def __init__(self, n):
        self.n = n

    def __get__(self, instance_self, instance_class):
        with open("start_time.txt", 'a') as g:
            print(f"Descr. started at: {datetime.now()}, Value = {self.n}", file=g)
        return self.n * instance_self.p


class Box:
    def __init__(self, x, y, z):
        self.p = x*y*z

    volume = MyDescriptor(4)


box1 = Box(1, 2, 3)
print(box1.volume)
