Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> matrix1 = [[1,2], [3,4]]
>>> matrix2 = [[4,5], [6,7]]
>>> print("Printing elements of first matrix")
Printing elements of first matrix
>>> for row in matrix1:
...     for element in row:
...         print(element, end=" ")
...     print()
... 
...     
1 2 
3 4 
>>> print("Printing elements of second martix")
Printing elements of second martix
>>> for row in matrix2:
...     for element in row:
...         print(element, end=" ")
...     print()
... 
...     
4 5 
6 7 
>>> result = [[0,0], [0,0]]
>>> for i in range(len(matrix1)):
...     for j in range(len(matrix1[0])):
...         result[i][j] = matrix1[i][j] - matrix2[i][j]
... 
...         
>>> print("Substraction of two matrix")
Substraction of two matrix
>>> for row in result:
...     for element in row:
...         print(element, end=" ")
...     print()
... 
...     
-3 -3 
-3 -3 
