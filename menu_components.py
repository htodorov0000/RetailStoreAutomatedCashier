from menu_classes import Menu, MenuItem
from product import Product
from cash import currency_units
from collection_of_goods import robot_runtime, request_input_to_continue

"""This module contains function components for MenuItem."""

total_price = 0

def load_menu(menu):
    """Load existing menu."""
    menu.start()

def start_new_menu(name, description, *items):
    """Create and load new menu."""
    new_menu = Menu(name, description, items)
    load_menu(new_menu)
    
def increment_total_price(amount):
    """Add amount to total_price."""
    global total_price
    total_price += amount
    total_price = round(total_price, 2)
    print("Owed Amount = " + "%.2f" % total_price)

def payment_calculation(amount):
    """Handle payment and change calculations."""
    global total_price
    if total_price > 0:
        increment_total_price(amount)
    if total_price < 0:
        return_change()
        total_price = 0
    if total_price == 0: 
        robot_runtime()
        
def return_change():
    """Returns change starting from highest unit."""
    global total_price
    total_price *= -1
    print("Returning " + "%.2f" % total_price + " in change.")
    for unit in currency_units:
        while unit.value <= round(total_price, 2):
            total_price -= unit.value
            print("Returned " + unit.name + ".")
            request_input_to_continue()


def load_payment_menu(payment_menu):
    """Loads payment menu from previous menu."""
    if total_price <= 0:
        print("No items selected. Please select items to purchase.")
        return
    print("Please insert cash. Owed amount: " + "%.2f" % total_price)
    load_menu(payment_menu)

def increment_product_quantity(product, amount):
    """Increments the quantity of given product in the user's cart."""
    product.quantity += amount
    error = False
    if product.quantity < 0:
        product.quantity = 0
        error = True
        print("Amount in cart cannot be below 0.")
    if not error: 
        increment_total_price(product.price * amount)
    print(product.name + "s in cart: " + str(product.quantity))