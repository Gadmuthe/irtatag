Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def rotateArray(arr, n, d):
...     temp = []
...     i = 0
...     while(i<d):
...         temp.append(arr[i])
...         i = i+1
...     i = 0
...     while(d<n):
...         arr[i] = arr[d]
...         i = i + 1
...         d = d + 1
...     arr[:] = arr[: i] + temp
...     return arr
... 
>>> arr = [1,2,3,4,5,6,7]
>>> print("Array after left rotation is: ", end=' ')
Array after left rotation is:  
>>> print(rotateArray(arr, len(arr), 2))
[3, 4, 5, 6, 7, 1, 2]
>>> 
>>> 
>>> def rotateList(arr,d,n):
...     arr[:] = arr[d:n]+arr[0:d]
...     return arr
... 
>>> arr = [1,2,3,4,5,6]
>>> print(arr)
[1, 2, 3, 4, 5, 6]
>>> print("Rotated list is")
Rotated list is
>>> print(rotateList(arr,2,len(arr)))
[3, 4, 5, 6, 1, 2]
