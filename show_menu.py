def show_menu():
    print("Simple To-Do List")
    print("1. View List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    return choice

def view_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("Your To-Do List:")
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")

def add_item(todo_list):
    item = input("Enter the item to add: ")
    todo_list.append(item)
    print(f"'{item}' added to your to-do list!")

def remove_item(todo_list):
    view_list(todo_list)
    if not todo_list:
        return
    choice = int(input("Enter the number of the item to remove: "))
    if choice > 0 and choice <= len(todo_list):
        removed_item = todo_list.pop(choice - 1)
        print(f"'{removed_item}' removed from your to-do list!")
    else:
        print("Invalid choice. Please try again.")

def main():
    todo_list = []
    while True:
        choice = show_menu()
        if choice == '1':
            view_list(todo_list)
        elif choice == '2':
            add_item(todo_list)
        elif choice == '3':
            remove_item(todo_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()