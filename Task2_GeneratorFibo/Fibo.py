from functools import cache

class Fibo:
    def __init__(self):
        self.count = 0
        self.x = int(input("Введите число n: "))

    @cache
    def calc(self, nn):
        self.count += 1
        return self.calc(nn - 1) + self.calc(nn - 2) if nn not in [1, 2] else 1
    

    def generator(self):
        next = 1
        while next < self.x + 1:
            next = yield self.calc(next)
            # next = self.calc(next)
            # yield next
            yield