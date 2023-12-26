def generate_receipt(items):
    total_cost = 0
    print("Shopping List:")
    for item, cost in items.items():
        print(f"{item}: ${cost}")
        total_cost += cost
    print(f"Total: ${total_cost:.2f}")

def main():
    shopping_list = {
        "Apple": 1.5,
        "Banana": 0.75,
        "Milk": 2.0,
        "Bread": 1.8,
        "Eggs": 2.5
    }
    generate_receipt(shopping_list)

if __name__ == "__main__":
    main()