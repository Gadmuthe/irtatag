def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def show_menu():
    print("Temperature Converter")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    return choice

def main():
    while True:
        choice = show_menu()

        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius} Celsius is equal to {celsius_to_fahrenheit(celsius):.2f} Fahrenheit")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit} Fahrenheit is equal to {fahrenheit_to_celsius(fahrenheit):.2f} Celsius")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()