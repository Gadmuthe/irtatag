Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}
>>> for key, value in dt.items():
...     print(key, value)
... 
...     
a juice
b grill
c corn
>>> 
>>> 
>>> dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}
>>> for key in dt:
...     print(key, dt[key])
... 
...     
a juice
b grill
c corn
>>> 
>>> 
>>> dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}
>>> for key in dt.keys():
...     print(key)
...     for value in dt.values():
...         print(value)
... 
...         
a
juice
grill
corn
b
juice
grill
corn
c
juice
grill
corn
