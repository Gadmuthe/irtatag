Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def binary_search(arr, low, high, x):
...     if high >= low:
...         mid = (high + low) // 2
...         if arr[mid] == x:
...             return mid
...         elif arr[mid] > x:
...             return binary_search(arr, low, mid - 1, x)
...         else:
...             return binary_search(arr, mid+1, high, x)
...     else:
...         return -1
...     arr = [2,3,4,10,40]
...     x = 10
...     result = binary_search(arr, 0, len(arr)-1, x)
...     if result != -1:
...         print("elements is present at index", str(result))
...     else:
...         print("element is not present in array")
... 
...         
>>> 
