class BookInventory:
    def __init__(self):
        self.books = {}
    def add_book(self, title, author):
        if title not in self.books:
            self.books[title] = author
            print(f"Book '{title}' by {author} added to the inventory.")
        else:
            print(f"Book '{title}' already exists in the inventory.")
    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"Book '{title}' removed from the inventory.")
        else:
            print(f"Book '{title}' not found in the inventory.")
    def show_books(self):
        if self.books:
            print("Book Inventory:")
            for idx, (title, author) in enumerate(self.books.items(),start = 1):
                print(f"{idx}. {title} by {author}")
        else:
            print("Book inventory is empty.")

inventory = BookInventory()
inventory.show_books()
inventory.add_book("Python Crash Course", "Eric Matthes")
inventory.add_book("Deep Learning", "Ian Goodfellow")
inventory.show_books()
inventory.remove_book("Deep Learning")
inventory.show_books()
            