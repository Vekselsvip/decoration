def write_f(func):
    """
    function decorator
    :param func: function reference
    :return: result decorating function and add result in text.txt
    """
    def wrapper(*args):
        f = open('text.txt', 'w')
        f.write(func(*args))
        f.close()
        return f'{func(*args)}'
    return wrapper


class Cat:
    """
    class a cat in home
    """
    def __init__(self, name: str, voice: str, sex: str):
        self.name = name
        self.voice = voice
        self.sex = sex

    @write_f
    def __str__(self):
        return f"it's a {self.name} and {self.sex} say {self.voice}!"


cat = Cat('Barsik', 'may', 'he')
print(cat)
