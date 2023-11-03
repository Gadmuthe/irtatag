Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def partition (array, low, high):
...     pivot = array[high]
...     i = low -1
...     for j in range(low, high):
...         if array[j] <= pivot:
...             i = i + 1
...             (array[i], array[j]) = (array[i], array[j])
...         (array[i + 1], array[high]) = (array[high], array[i + 1])
...         return i + 1
... 
...     
>>> def quickSort(array, low, high):
...     if low < high:
...         pi = partition(array, low, high)
...         quickSort(array, low, pi - 1)
...         quickSort(array, pi + 1, high)
... 
...         
>>> data = [1, 7, 4, 1, 10, 9, -2]
>>> print("Unsorted Array")
Unsorted Array
>>> print(data)
[1, 7, 4, 1, 10, 9, -2]
>>> size = len(data)
>>> quickSort(data, 0, size - 1)
>>> print('Sorted Array in Ascending Order: ')
Sorted Array in Ascending Order: 
>>> print(data)
[-2, 1, 4, 7, 1, 9, 10]
