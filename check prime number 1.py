Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 407
>>> if num == 1:
...     print(num, "is not a prime number")
... elif num > 1:
...     for i in range(2, num):
...         if(num % i) == 0:
...             print(num,"is not a prime number")
...             print(i, "times", num//i,"is",num)
...             break
...         else:
...             print(num, "is a prime number")
... else:
...     print(num, "is not a prime number")
... 
...     
407 is a prime number
407 is a prime number
407 is a prime number
407 is a prime number
407 is a prime number
407 is a prime number
407 is a prime number
407 is a prime number
407 is a prime number
407 is not a prime number
11 times 37 is 407
