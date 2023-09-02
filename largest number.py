Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = 51
>>> num2 = 70
>>> if(num1 >= num2):
...     largest = num1
... else:
...     largest = num2
... 
...     
>>> print("the largest number is ", largest)
the largest number is  70
>>> 
>>> 
>>> num1 = 100
>>> num2 = 140
>>> num3 = 120
>>> if(num1 >= num2) and (num1 >= num3):
...     largest = num1
... elif(num2 >= num1) and (num2 >= num3):
...     largest = num2
... else:
...     largest = num3
... 
...     
>>> print("the largest number is", largest)
the largest number is 140
