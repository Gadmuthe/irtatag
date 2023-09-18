Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 7
>>> factorial = 1
>>> if num < 0:
...     print("sorry, factorial does not exist for negative numbers")
... elif num == 0:
...     print("the factorial of 0 is 1")
... else:
...     for i in range(1, num+1):
...         factorial = factorial * i
...     print("the factorial of", num, "is",factorial)
... 
...     
the factorial of 7 is 5040
