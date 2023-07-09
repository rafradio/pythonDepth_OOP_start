from .Animal import Animal

class Fish(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', age:int=0, count_fins: int = 0):
        super().__init__(name, breed, age)
        self.count_fins = count_fins

    def print_specific(self):
        return f'{self.count_fins}'