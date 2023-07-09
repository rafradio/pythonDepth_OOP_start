class Animal:
    def __init__(self, name:str=None, breed:str='unknown', age: int = 0):
        self.name = name
        self.breed = breed
        self.age = age

    def print_specific(self):
        return f'Специфические данные'