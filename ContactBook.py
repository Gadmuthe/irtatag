class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"Contact '{name}' added successfully.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' removed successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def show_contacts(self):
        if self.contacts:
            print("Your Contacts:")
            for name, number in self.contacts.items():
                print(f"{name}: {number}")
        else:
            print("No contacts available.")

# Example usage:
contact_book = ContactBook()
contact_book.show_contacts()
contact_book.add_contact("Alice", "8355812242")
contact_book.add_contact("Bob", "9653113964")
contact_book.show_contacts()
contact_book.remove_contact("Bob")
contact_book.show_contacts()