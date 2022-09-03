"""Write a generator function that will return prime numbers.
The upper limit of this range must be given as a parameter to this function."""


def prime_number_gen(n):
    for i in range(1, n + 1):
        for j in range(2, i):
            if not i % j:
                break
        else:
            yield i


for item in prime_number_gen(100):
    print(item, end=" ")
