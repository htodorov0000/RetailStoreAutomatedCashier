from menu_classes import Menu, MenuItem
from product import Product, Aisle, aisles, products
from cash import currency_units
import menu_components


def currency_menu_items():
    menu_items = []
    for unit in currency_units:
        menu_items.append(MenuItem(unit.name, menu_components.payment_calculation, [unit.value * -1]))
    return menu_items

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
                                           [product.name, "Select Desired Amount. Price = " + "%.2f" % product.price, add_to_cart, remove_from_cart, back_to_selection_menu]))
    go_to_payment_menu_item = MenuItem("To Payment", menu_components.load_payment_menu, [payment_menu])
    product_menu_items.append(go_to_payment_menu_item)
    selection_menu.items = product_menu_items

create_product_selection_menu_items(products)
selection_menu.start()