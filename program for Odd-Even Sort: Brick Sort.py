Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def oddEvenSort(arr, n):
...     isSorted = 0
...     while isSorted == 0:
...         isSorted = 1
...         temp = 0
...         for i in range(1, n-1, 2):
...             if arr[i] > arr[i+1]:
...                 arr[i], arr[i+1] = arr[i+1], arr[i]
...                 isSorted = 0
...         for i in range(0, n-1, 2):
...             if arr[i] > arr[i+1]:
...                 arr[i], arr[i+1] = arr[i+1], arr[i]
...                 isSorted = 0
...         return
... 
...     
>>> arr = [34, 2, 10, -9]
>>> n = len(arr)
>>> oddEvenSort(arr, n);
>>> for i in range(0, n):
...     print(arr[i], end = " ")
... 
...     
2 34 -9 10 
