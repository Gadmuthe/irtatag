Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [[12,7],
...      [4,5],
...      [3,8]]
>>> result = [[0,0,0],
...           [0,0,0]]
>>> for i in range(len(x)):
...     for j in range(len(x[0])):
...         result[j][i] = x[i][j]
...         for r in result:
...             print(r)
... 
...             
[12, 0, 0]
[0, 0, 0]
[12, 0, 0]
[7, 0, 0]
[12, 4, 0]
[7, 0, 0]
[12, 4, 0]
[7, 5, 0]
[12, 4, 3]
[7, 5, 0]
[12, 4, 3]
[7, 5, 8]
>>> 
>>> 
>>> x = [[12,7],
...      [4,5],
...      [3,8]]
>>> result = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
>>> for r in result:
...     print(r)
... 
...     
[12, 4, 3]
[7, 5, 8]
