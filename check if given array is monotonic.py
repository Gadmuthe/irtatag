Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def isMontonic(A):
...     x, y = [], []
...     x.extend(A)
...     y.extend(A)
...     x.sort()
...     y.sort(reverse=True)
...     if(x == A or y == A):
...         return True
...     return False
... 
>>> A = [6, 5, 4, 4]
>>> print(isMontonic(A))
True
>>> 
>>> 
>>> 
>>> def isMonotonic(A):
...     return (all(A[i] <= A[i+1] for i in range(len(A)-1)) or
...             all(A[i] >= A[i+1] for i in range(len(A)-1)))
... 
>>> A = [6,5,4,4]
>>> print(isMonotonic(A))
True
>>> 
