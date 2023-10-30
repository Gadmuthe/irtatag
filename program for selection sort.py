Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def selectionSort(array, size):
...     for ind in range(size):
...         min_index = ind
...         for j in range(ind + 1, size):
...             if array[j] < array[min_index]:
...                 min_index = j
...         (array[ind], array[min_index]) = (array[min_index], array[ind])
... 
...         
>>> arr = [-2, 45, 0, 11, -9, 88,-97,-202,747]
>>> size = len(arr)
>>> selectionSort(arr, size)
>>> print('The array after sorting in Ascending Order by selection sort is:')
The array after sorting in Ascending Order by selection sort is:
>>> print(arr)
[-202, -97, -9, -2, 0, 11, 45, 88, 747]
