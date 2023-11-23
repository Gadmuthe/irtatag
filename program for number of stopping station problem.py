Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def stopping_station(p, n):
...     num = 1
...     dem = 1
...     s = p
...     while p != 1:
...         dem *= p
...         p-=1
...     t = n - s + 1
...     while t != (n-2 * s + 1):
...         num *= t
...         t -= 1
...     if(n-s+1)>= s:
...         return int(num/dem)
...     else:
...         return -1
... 
...     
>>> num = stopping_station(4, 12)
>>> if num != -1:
...     print(num)
... else:
...     print("Not Possible")
... 
...     
126
