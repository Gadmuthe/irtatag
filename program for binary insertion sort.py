Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import bisect
>>> def binary_search(arr, val, start, end):
...     idx = bisect.bisect_left(arr[start:end+1], val)
...     return start + idx
... 
>>> def insertion_sort(arr):
...     for i in range(1, len(arr)):
...         val = arr[i]
...         j = binary_search(arr, val, 0, i-1)
...         arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
...     return arr
... 
>>> print("Sorted array:")
Sorted array:
>>> print(insertion_sort([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]))
[0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
