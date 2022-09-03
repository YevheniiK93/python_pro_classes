"""Implement a generator function that will return one member
of a geometric progression with the specified multiplier. The
generator must stop its work or upon reaching the specified
boundaries, or when sending a command to stop."""


def geom_gen(start, stop, step):
    while start <= stop:
        yield start
        start *= step


x = geom_gen(1, 1000, 2)

for num in x:
    print(num)
    if num * 2 > 200:  # Number greater than the specified number will not be displayed
        x.close()
