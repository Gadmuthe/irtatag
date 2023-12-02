Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def splitArr(arr, n, k):
...     for i in range(0, k):
...         x = arr[0]
...         for j in range(0, n-1):
...             arr[j] = arr[j+1]
...         arr[n-1] = x
... 
...         
>>> arr= [12, 10, 5, 6, 52, 36]
>>> n = len(arr)
>>> position = 2
>>> splitArr(arr, n, position)
>>> for i in range(0, n):
...     print(arr[i], end= ' ')
... 
...     
5 6 52 36 12 10 
>>> 
...  
>>> 
>>> 
>>> def splitArr(a, n, k):
...     b = a[:k]
...     return (a[k::]+b[::])
... 
>>> arr = [12, 10, 5, 6, 52, 36]
>>> n = len(arr)
>>> position = 2
>>> arr = splitArr(arr, n, position)
>>> for i in range(0, n):
...     print(arr[i], end=' ')
... 
...     
5 6 52 36 12 10 
