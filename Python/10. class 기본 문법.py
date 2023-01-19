def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


class Calc:
    def __init__(self, a, b):
        self.__a = a
        self.b = b

    def add(self):
        return self.__a + self.b

    def sub(self):
        return self.__a - self.b

    def div(self):
        return self.__a / self.b

    def get_a(self):
        return self.__a

    @property
    def a(self):
        return self.__a


if __name__ == "__main__":
    a, b = 20, 10
    # print(add(a, b))
    # print(sub(a, b))
    # print(div(a, b))

    c = Calc(a, b)
    # print(dir(c))
    # print(c.add())
    # print(c.sub())
    # print(c.div())
    # print(c.get_a())
    print(c.a)
