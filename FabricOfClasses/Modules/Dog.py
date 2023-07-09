from .Animal import Animal

class Dog(Animal):
    def __init__(self, name:str=None, breed:str='unknown', age:int=0, commands: list[str] = 'unknown'):
        super().__init__(name, breed, age)
        self.commands = commands

    def print_specific(self):
        return f'{self.commands}'