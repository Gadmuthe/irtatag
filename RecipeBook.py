class RecipeBook:
    def __init__(self):
        self.recipes = {}
    def add_recipe(self, name, indegredients):
        self.recipes[name] = indegredients
        print(f"Recipe '{name}' added successfully.")
    def remove_recipe(self, name):
        if name in self.recipes:
            del self.recipes[name]
            print(f"Recipe '{name}' removed successfully.")
        else:
            print(f"Recipe '{name}' not found.")
    def show_recipes(self):
        if self.recipes:
            print("Your Recipes: ")
            for idx, (recipe, indegredients) in enumerate(self.recipes.items(), start = 1):
                print(f"{idx}. {recipe}: {', '.join(indegredients)}")
        else:
            print("No recipes available.")

recipe_book = RecipeBook()
recipe_book.show_recipes()
recipe_book.add_recipe("Pancakes", ["Flour", "Milk", "Eggs", "Sugar"])
recipe_book.add_recipe("Omelette", ["Eggs", "Milk", "Cheese", "Tomato"])
recipe_book.show_recipes()
recipe_book.remove_recipe("Omelette")
recipe_book.show_recipes()