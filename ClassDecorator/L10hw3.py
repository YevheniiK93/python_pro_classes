"""For the Box class, write a static method that will count
the total volume of two boxes, which will be its parameters."""


class Box:
    def __init__(self, x, y, z):
        if not isinstance(x, (int, float)):
            raise TypeError()
        if not isinstance(y, (int, float)):
            raise TypeError()
        if not isinstance(z, (int, float)):
            raise TypeError()

        if x <= 0 or y <= 0 or z <= 0:
            raise ValueError()

        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Box x = {self.x} y = {self.y} z = {self.z}"

    @staticmethod
    def sum_volume(a, b):
        if not isinstance(a, Box):
            return NotImplemented
        if not isinstance(a, Box):
            return NotImplemented

        volume_a = a.x * a.y * a.z
        volume_b = b.x * b.y * b.z
        return volume_a + volume_b


box_a = Box(1, 2, 3)
box_b = Box(4, 5, 6)

print(Box.sum_volume(box_a, box_b))
