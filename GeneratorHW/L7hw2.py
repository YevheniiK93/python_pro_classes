"""Implement your analog of the range() generator function."""


def range_gen(start, stop, step):
    start = start - step
    while start <= stop - step:
        start += step
        yield start


g = range_gen(1, 100, 7)

for i in g:
    print(i)
