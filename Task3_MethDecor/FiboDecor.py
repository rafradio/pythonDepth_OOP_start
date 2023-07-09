class FiboDecor:
    def __init__(self):
        self.count = 0
        self.x = int(input("Введите число n: "))

    def decor(func):
        def calc(self):      
            a, b = 1, 1
            for _ in func(self):
                yield a
                a, b = b, a + b
        return calc
    

    @decor
    def generator(self):
        i = 0
        while i < self.x:
            yield i
            i +=1