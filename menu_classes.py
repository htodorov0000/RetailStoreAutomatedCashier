"""Contains Menu and MenuItem classes."""
class MenuItem:
    """Objects of this class contain components in the form
    of functions with unique functionality, selectable
    in Menu system."""
    def __init__(self, name: str, function, args: list):
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