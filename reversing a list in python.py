Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Reverse(lst):
...     new_lst = lst[::-1]
...     return new_lst
... 
>>> lst = [10,11,12,13,14,15]
>>> print(Reverse(lst))
[15, 14, 13, 12, 11, 10]
>>> 
>>> 
>>> 
>>> 
>>> lst = [10,11,12,13,14,15]
>>> lst.reverse()
>>> print("Using reverse() ", lst)
Using reverse()  [15, 14, 13, 12, 11, 10]
>>> print("Using reversed() ", list(reversed(lst)))
Using reversed()  [10, 11, 12, 13, 14, 15]
>>> 
>>> 
>>> 
>>> lst = [10,11,12,13,14,15]
>>> l = []
>>> for i in lst:
...     l.insert(0, i)
... 
...     
>>> print(l)
[15, 14, 13, 12, 11, 10]
