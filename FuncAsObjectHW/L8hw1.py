"""Implement a generator function that will return one at a time member
of a numerical sequence whose law is given by custom function. In addition,
the parameter of the generator function must be the value of the
 first member of the progression and the number of sequence members (n)."""


def ariph_seq(start, n, step=3):
    i = 0
    while i < n:
        yield start
        start += step
        i += 1


def gen(start, n, f):
    x = f(start, n)

    for num in x:
        yield num


for num in gen(1, 10, ariph_seq):
    print(num)
