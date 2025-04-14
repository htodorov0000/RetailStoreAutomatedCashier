class Aisle():
    """Represents physical aisle at the store."""
    def __init__(self, name: str, char: str):
        self.name = name
        self.char = char #character used for visual representation on grid
        self.position = [-1,-1]

class Product():
    """Represents real product present at the store."""
    def __init__(self, name:str, price:float, aisle:Aisle):
        self.name = name
        self.quantity = 0
        self.price = price
        self.aisle = aisle

def set_aisles_and_products():
    """Creates each Aisle and Product class object used. More may be added."""
    meat_aisle = Aisle("Meat Aisle", "M")
    freezer_aisle = Aisle("Freezer Aisle", "F")
    cleaning_products_aisle = Aisle("Cleaning Products Aisle", "C")
    alcoholic_beverages_aisle = Aisle("Alcoholic Beverages Aisle", "A")
    
    ground_meat = Product("Ground Meat", 2.45, meat_aisle)
    frozen_pizza = Product("Frozen Pizza", 3.30, freezer_aisle)
    laundry_detergent = Product("Laundry Detergent", 14.79, cleaning_products_aisle)
    white_wine = Product("White Wine", 8.99, alcoholic_beverages_aisle)
    
    aisles = [meat_aisle, freezer_aisle, cleaning_products_aisle, alcoholic_beverages_aisle]
    products = [ground_meat, frozen_pizza, laundry_detergent, white_wine]
    return aisles, products


aisles, products = set_aisles_and_products()


