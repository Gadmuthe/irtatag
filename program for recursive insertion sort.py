Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def insertionSortRecursive(arr, n):
...     if n <= 1:
...         return
...     insertionSortRecursive(arr, n-1)
...     last = arr[n-1]
...     j = n-2
...     while(j >= 0 and arr[j] > last):
...         arr[j+1] = arr[j]
...         j = j-1
...     arr[j+1] = last
... 
...     
>>> if __name__ == '__main__':
...     A = [-7, 11, 6, 0, -3, 5, 10, 2]
...     n = len(A)
...     insertionSortRecursive(A, n)
...     print(A)
... 
...     
[-7, -3, 0, 2, 5, 6, 10, 11]
