Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list_1 = [1, 'a']
>>> list_2 = [3, 4, 5]
>>> list_joined = list_1 + list_2
>>> print(list_joined)
[1, 'a', 3, 4, 5]
>>> 
>>> 
>>> list_1 = [1, 'a']
>>> list_2 = range(2,4)
>>> list_joined = [*list_1, *list_2]
>>> print(list_joined)
[1, 'a', 2, 3]
>>> 
>>> 
>>> list_1 = [1, 'a']
>>> list_2 = [1, 2, 3]
>>> list_joined = list(set(list_1 + list_2))
>>> print(list_joined)
[3, 1, 'a', 2]
>>> 
>>> 
>>> list_1 = [1, 'a']
>>> list_2 = [1, 2, 3]
>>> list_2.extend(list_1)
>>> print(list_2)
[1, 2, 3, 1, 'a']
