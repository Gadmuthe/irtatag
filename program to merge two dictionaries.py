Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict_1 = {1: 'a', 2: 'b'}
>>> dict_2 = {2: 'c', 4: 'd'}
>>> print(dict_1 | dict_2)
{1: 'a', 2: 'c', 4: 'd'}
>>> 
>>> 
>>> dict_1 = {1: 'a', 2: 'b'}
>>> dict_2 = {2: 'c', 4: 'd'}
>>> print({**dict_1, **dict_2})
{1: 'a', 2: 'c', 4: 'd'}
>>> 
>>> 
>>> dict_1 = {1: 'a', 2: 'b'}
>>> dict_2 = {2: 'c', 4: 'd'}
>>> dict_3 = dict_2.copy()
>>> dict_3.update(dict_1)
>>> print(dict_3)
{2: 'b', 4: 'd', 1: 'a'}
