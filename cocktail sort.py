Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
...     while (swapped==True):
...         swapped = False
...         for i in range(start, end):
...             if(a[i] > a[i+1]):
...                 a[i], a[i+1] = a[i+1], a[i]
...                 swapped=True
...             if(swapped==False):
...                 break
...             swapped = False
...             end = end-1
...             for i in range(end-1, start-1, -1):
...                 if(a[i] > a[i+1]):
...                     a[i], a[i+1] = a[i+1], a[i]
...                     swapped = True
...             start = start+1
... 
...             
>>> a = [5, 1, 4, 2, 8, 0, 2]
>>> cocktailSort(a)
>>> print("Sorted array is:")
Sorted array is:
>>> for i in range(len(a)):
...     print("%d" %a[i]),
... 
...     
0
(None,)
1
(None,)
2
(None,)
4
(None,)
5
(None,)
8
(None,)
2
(None,)
