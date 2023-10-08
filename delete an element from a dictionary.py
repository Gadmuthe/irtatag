Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_dict = {31: 'a', 21: 'b', 14: 'c'}
>>> del my_dict[31]
>>> print(my_dict)
{21: 'b', 14: 'c'}
>>> 
>>> 
>>> my_dict = {31: 'a', 21: 'b', 14: 'c'}
>>> print(my_dict.pop(31))
a
>>> print(my_dict)
{21: 'b', 14: 'c'}
