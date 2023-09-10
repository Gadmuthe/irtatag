Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = int(input("enter a number: "))
enter a number: 407
>>> sum = 0
>>> temp = num
>>> while temp > 0:
...     digit = temp % 10
...     sum += digit ** 3
...     temp //= 10
... 
...     
>>> if num == sum:
...     print(num, "is an armstrong number")
... else:
...     print(num, "is not an armstrong number")
... 
...     
407 is an armstrong number
>>> 
>>> 
>>> num = 1634
>>> order = len(str(num))
>>> sum = 0
>>> temp = num
>>> while temp > 0:
...     digit = temp % 10
...     sum += digit ** order
...     temp //= 10
... 
...     
>>> if num == sum:
...     print(num, "is an armstrong number")
... else:
...     print(num, "is not an armstrong number")
... 
...     
1634 is an armstrong number
