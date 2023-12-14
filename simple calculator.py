Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(num1, num2):
...     return num1 + num2
... 
>>> def substract(num1, num2):
...     return num1 - num2
... 
>>> def multiply(num1, num2):
...     return num1 * num2
... 
>>> def divide(num1, num2):
...     return num1 / num2
... 
>>> print("Please select operation -\n" \
...       "1. Add\n" \
...       "2. substract\n" \
...       "3. Multiply\n" \
...       "4. Divide\n")
Please select operation -
1. Add
2. substract
3. Multiply
4. Divide

>>> 
>>> select = int(input("Select operations from 1,2,3,4: "))
Select operations from 1,2,3,4: 3
>>> number_1 = int(input("Enter first number: "))
Enter first number: 150
>>> number_2 = int(input("Enter second number: "))
Enter second number: 700
>>> if select == 1:
...     print(number_1, "+", number_2, "=", add(number_1, number_2))
... elif select == 2:
...     print(number_1, "-", number_2, "=", substract(number_1, number_2))
... elif select == 3:
...     print(number_1, "*", number_2, "=", multiply(number_1, number_2))
... else:
    print("Invalid input")

    
150 * 700 = 105000
