Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Sort_Tuple(tup):
...     lst = len(tup)
...     for i in range(0, lst):
...         for j in range(0, lst-i-1):
...             if(tup[j][1] > tup[j+1][1]):
...                 temp = tup[j]
...                 tup[j] = tup[j + 1]
...                 tup[j + 1] = temp
...     return tup
... 
>>> tup = [('for', 24), ('is', 10), ('Geeks', 28),
...        ('Geeksforgeeks', 5), ('portal', 20), ('a', 15)]
>>> print(Sort_Tuple(tup))
[('Geeksforgeeks', 5), ('is', 10), ('a', 15), ('portal', 20), ('for', 24), ('Geeks', 28)]
>>> 
>>> 
>>> 
>>> def Sort_Tuple(tup):
...     tup.sort(key = lambda x: x[1])
...     return tup
... 
>>> tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]
>>> print(Sort_Tuple(tup))
[('akash', 5), ('rishav', 10), ('gaurav', 15), ('ram', 20)]
>>> 
>>> 
>>> 
>>> def Sort_Tuple(tup):
...     return(sorted(tup, key = lambda x: x[1]))
... 
>>> tup = [('rishav', 10), ('akash', 5), ('ram',20), ('gaurav', 15)]
>>> print(Sort_Tuple(tup))
[('akash', 5), ('rishav', 10), ('gaurav', 15), ('ram', 20)]
