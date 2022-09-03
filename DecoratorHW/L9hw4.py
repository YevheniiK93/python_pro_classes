import time


def timing_to_file(number, filename):
    start = time.time()
    i = 0
    while i < number:
        def wrapper(f):
            def inner(*args):
                return f(*args)
            return inner
        end = time.time()
        file = open(filename, "w")
        file.write(f"Function passed {number} times per {end - start} s.")
        file.close()
        i = i + 1
    return wrapper


@timing_to_file(1000, "timing.txt")
def greetings():
    return 'Hello World!'

print(greetings)


