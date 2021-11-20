def count_calls(f):
    count = 0

    def num(x, y):
        nonlocal count
        count += 1
        return f'res: {f(x, y)}\nnumber of calls- {count}'

    return num


@count_calls
def mul(x, y):
    return x + y


@count_calls
def prod(x, y):
    return x * y


print(mul(2, 3))
print(mul(2, 3))
print(prod(2, 3))