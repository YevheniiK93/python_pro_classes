"""Create a decorator that will count how many
times the decorated function was called."""

count = 0


def count_decorator(f):
    def calls_count(*args, **kwargs):
        global count
        count += 1
        return f(*args, **kwargs)
    return calls_count


@count_decorator
def summa(a, b):
    return a + b


print(summa(5, 8))
print(summa(2, 7))
summa(1, 2)
summa(2, 3)


print(f"Function  called {count} times")
