Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(x, y):
...     return x + y
...     def substract(x, y):
...         return x - y
...         def multiply(x, y):
...             return x * y
...             def divide(x, y):
...                 return x / y
...                 print("select operation.")
...                 print("1. add")
...                 print("2. substract")
...                 print("3. multiply")
...                 print("4. divide")
...                 while True:
...                     choice = input("enter choice(1/2/3/4): ")
...                     if choice in ('1', '2', '3', '4'):
...                         try:
...                             num1 = float(input("enter first number: "))
...                             num2 = float(input("enter second number: "))
...                         except ValueError:
...                             print("invalid input. please enter a number. ")
...                             continue
...                         if choice == '1':
...                             print(num1, "+", num2, "=", add(num1, num2))
...                         elif choice == '2':
...                             print(num1, "-", num2, "=", substract(num1, num2))
...                         elif choice == '3':
...                             print(num1, "*", num2, "=", multiply(num1, num2))
...                         elif choice == '4':
...                             print(num1, "/", num2, "=", divide(num1, num2))
...                         next_calculation = input("lets do next calculation? (yes/no):")
...                         if next_calculation == "no":
...                             break
...                         else:
...                             print("Invalid Input")
... 
...                             
