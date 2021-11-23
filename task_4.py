import time


def midl_time(count):
    def tim(func):
        res = []
        start = 0
        end = 0

        def wrapped(*args):
            nonlocal start, end
            for i in range(count):
                start = time.time()
                result = func(*args)
                time.sleep(1)
                end = time.time()
                res.append(end - start)
            f = open(f'{func.__name__}.txt', 'w')
            f.write(f'result- {result}\nMidl Time- {sum(res) / len(res)}')
            f.close()
            return f'result- {result}\nMidl Time- {sum(res) / len(res)}'

        return wrapped

    return tim


@midl_time(3)
def my_sum(x, y):
    return x + y


print(my_sum(15, 5))
