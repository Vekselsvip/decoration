functions = []


def add_functions(func):
    functions.append(func)
    return func


@add_functions
def my_sum(x, y):
    return x + y


@add_functions
def hello():
    return 'Hello World'
