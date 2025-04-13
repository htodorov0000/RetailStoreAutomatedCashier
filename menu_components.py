from menu_classes import Menu, MenuItem
from product import Product

total_price = 0

def load_menu(menu):
    menu.start()

def start_new_menu(name, description, *items):
    new_menu = Menu(name, description, items)
    load_menu(new_menu)
    
def increment_total_price(amount):
    global total_price
    total_price += amount
    print("Total Price = " + "%.2f" % total_price)
    
def get_total_price():
    return total_price

def increment_product_quantity(product, amount):
    product.quantity += amount
    error = False
    if product.quantity < 0:
        product.quantity = 0
        error = True
        print("Amount in cart cannot be below 0.")
    if not error: 
        increment_total_price(product.price * amount)
    print(product.name + "s in cart: " + str(product.quantity))