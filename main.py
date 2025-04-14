from menu_classes import Menu, MenuItem
from product import Product, Aisle
from cash import currency_units
import menu_components


def currency_menu_items():
    menu_items = []
    for unit in currency_units:
        menu_items.append(MenuItem(unit.name, menu_components.payment_calculation, [unit.value * -1]))
    return menu_items
        

def set_aisles_and_products():
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

selection_menu = Menu("Product Selection", "Please select your desired product." , [])
payment_menu = Menu("Payment", "" , currency_menu_items())

def create_product_selection_menu_items(products: list[Product]):
    product_menu_items = []
    item_num = 0
    for product in products:
        add_to_cart = MenuItem("Add One", menu_components.increment_product_quantity, [product,1])
        remove_from_cart = MenuItem("Remove One", menu_components.increment_product_quantity, [product,-1])
        back_to_selection_menu = MenuItem("Back", menu_components.load_menu, [selection_menu])
        item_num += 1
        product_menu_items.append(MenuItem(product.name, menu_components.start_new_menu, \
                                           [product.name, "Select Desired Amount. Price = " + str(product.price), add_to_cart, remove_from_cart, back_to_selection_menu]))
    go_to_payment_menu_item = MenuItem("To Payment", menu_components.load_payment_menu, [payment_menu])
    product_menu_items.append(go_to_payment_menu_item)
    selection_menu.items = product_menu_items

create_product_selection_menu_items(products)
selection_menu.start()