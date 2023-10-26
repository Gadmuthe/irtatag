Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> arr = [[4, 5, 6, 8],
...        [1, 2, 3, 1],
...        [7, 8, 9, 4],
...        [1, 8, 7, 5]]
>>> n = len(arr[0])
>>> i = 0
>>> for j in range(0, n-1):
...     print(arr[i][j], end=" ")
... 
...     
4 5 6 
>>> k = 1
>>> for i in range(0, n):
...     for j in range(n, 0, -1):
...         if(j == n-k):
...             print(arr[i][j], end=" ")
...             break
...         k += 1
... 
...         
>>> i = n-1
>>> for j in range(0, n):
...     print(arr[i][j], end=" ")
... 
...     
1 8 7 5 
