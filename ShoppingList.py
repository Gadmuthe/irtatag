class ShoppingList:
    def __init__(self):
        self.items = []
    def add_items(self, item):
        self.items.append(item)
        print(f"Item '{item}' added to the shopping list.")
    def remove_items(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Items '{item}' removed from the shopping list.")
        else:
            print(f"Item '{item}' not found in the shopping list.")
    def show_list(self):
        if self.items:
            print("Shopping List:")
            for idx, item in enumerate(self.items, start = 1):
                print(f"{idx}. {item}")
        else:
            print("Shopping list is empty.")
shopping_list = ShoppingList()
shopping_list.show_list()
shopping_list.add_items("Eggs")
shopping_list.add_items("Bread")
shopping_list.show_list()
shopping_list.remove_items("Eggs")
shopping_list.show_list()