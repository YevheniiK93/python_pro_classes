"""Create a decorator that will register the function to be
decorated in list of functions to process the sequence."""

f_list = []


def add_function(f):
    f_list.append(f)
    return f


@add_function
def summa(a, b):
    return a + b


@add_function
def mul(a, b):
    return a * b


@add_function
def div(a, b):
    return a / b


print(f_list)
