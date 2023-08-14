Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
x = 1
while x < 100:
    print(x)
    x = x * 2

    
1
2
4
8
16
32
64
>>> 
>>> 
>>> x = 1
>>> i = 0
>>> while x < 100:
...     if i == 5:
...         break
...     print(i, x)
...     x = x * 2
...     i += 1
... 
...     
0 1
1 2
2 4
3 8
4 16
>>> 
>>> 
>>> i = 0
>>> while i < 10:
...     if i % 3 != 0:
...         print(i)
...         i += 1
...         continue
...     i +=1
... 
...     
1
2
4
5
7
8
>>> 
