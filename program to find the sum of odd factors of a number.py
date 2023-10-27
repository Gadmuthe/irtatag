Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def sumofoddFactors( n ):
...     res = 1
...     while n % 2 == 0:
...         n = n//2
...     for i in range(3, int(math.sqrt(n) + 1)):
...         count = 0
...         curr_sum = 1
...         curr_term = 1
...         while n % i == 0:
...             count += 1
...             n = n//i
...             curr_term *= i
...             curr_sum += curr_term
...         res += curr_sum
...         if n >= 2:
...             res *= (1 + n)
...             return res
...         n = 30
...         print(sumofoddFactors(n))
... 
...         
