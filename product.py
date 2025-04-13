class Aisle():
    def __init__(self, name: str, char: str):
        self.name = name
        self.char = char

class Product():
    def __init__(self, name:str, price:float, aisle:Aisle):
        self.name = name
        self.quantity = 0
        self.price = price
        self.aisle = aisle




