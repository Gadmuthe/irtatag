Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> lower = 100
>>> upper = 2000
>>> for num in range(lower, upper + 1):
...     order = len(str(num))
...     sum = 0
...     temp = num
...     while temp > 0:
...         digit = temp % 10
...         sum += digit ** order
...         temp //= 10
...         if sum == num:
...             print(num)
... 
...             
125
153
216
370
371
407
729
1296
1634
