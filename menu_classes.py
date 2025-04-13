from ctypes import Array
from pyclbr import Function




class MenuItem:
    """Objects of this class contain components in the form
    of functions with unique functionality, selectable
    in Menu system."""
    def __init__(self, name: str, function: Function, args: Array):
        self.name = name
        self.function = function
        self.args = args
        
    def execute(self):
        return self.function(self.args)
    

class Menu:
    """Objects of this class are printed as menus with
    each MenuItem assigned being selectable."""
    def __init__(self, name: str, description: str, items: MenuItem):
        self.name = name
        self.description = description
        self.items = items

    def start(self):
        print("==" + self.name.upper() + "==")
        while True:
            print(self.description)
            item_num = 0
            for item in self.items:
                item_num += 1
                print(str(item_num) + ". ", item.name)
            inp = input()
            found_item = False
            item_num = 0
            for item in self.items:
                item_num += 1
                if inp == str(item_num):
                    found_item = True
                    item.function(*item.args)
            if found_item == False:
                print("Item not found.")



#below are example objects and functions:

# def add(a,b):
#     print(a+b)

# def start_new_menu(*items):
#     new_menu = Menu(items)

# def no_arg():
#     print("works")

# item1 = MenuItem("first", add, [2,4]) #6
# item2 = MenuItem("second", add, [3,6]) #9
# item3 = MenuItem("new menu", start_new_menu, [["1", item2], ["2", item1]])
# item4 = MenuItem("no arg function", no_arg, [])
# start = Menu([["1", item1], ["2", item2], ["3", item3], ["4", item4]])

