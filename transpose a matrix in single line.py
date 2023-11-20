Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
m = [[1,2], [3,4], [5,6]]
>>> for row in m:
...     print(row)
... 
...     
[1, 2]
[3, 4]
[5, 6]
>>> rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
>>> print("\n")


>>> for row in rez:
...     print(row)
... 
...     
[1, 3, 5]
[2, 4, 6]
>>> 
>>> 
>>> matrix = [(1,2,3), (4,5,6), (7,8,9), (10, 11, 12)]
>>> for row in matrix:
...     print(row)
... 
...     
(1, 2, 3)
(4, 5, 6)
(7, 8, 9)
(10, 11, 12)
>>> print("\n")


>>> t_matrix = zip(*matrix)
>>> for row in t_matrix:
...     print(row)
... 
...     
(1, 4, 7, 10)
(2, 5, 8, 11)
(3, 6, 9, 12)
