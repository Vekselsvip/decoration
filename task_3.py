def write_n(x):
    def write_f(func):

        """
        function decorator
        :param func: function reference
        :return: result decorating function and add result in text.txt
        """
        def wrapper(*args):
            f = open(f'{x}.txt', 'w')
            f.write(func(*args))
            f.close()
            return f'{func(*args)}'
        return wrapper
    return write_f


class Cat(object):
    """
    class a cat in home
    """
    def __init__(self, name: str, voice: str, sex: str):
        self.name = name
        self.voice = voice
        self.sex = sex


    @write_n('Cat')
    def __str__(self):
        return f"it's a {self.name} and {self.sex} say {self.voice}!"


cat = Cat('Barsik', 'may', 'he')
print(cat)
print()
