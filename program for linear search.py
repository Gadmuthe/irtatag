Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def search(arr, x):
...     for i in range(len(arr)):
...         if arr[i] == x:
...             return i
...         return -1
... 
...     
>>> 
>>> 
>>> def search(arr, curr_index, key):
...     if curr_index == -1:
...         return -1
...     if arr[curr_index] == key:
...         return curr_index
...     return search(arr, curr_index-1, key)
... 
