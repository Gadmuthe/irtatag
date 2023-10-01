Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
my_list = [[1],[2,3],[4,5,6,7]]
>>> flat_list = [num for sublist in my_list for num in sublist]
>>> print(flat_list)
[1, 2, 3, 4, 5, 6, 7]
>>> 
>>> 
>>> my_list = [[1],[2,3],[4,5,6,7]]
>>> flat_list = []
>>> for sublist in my_list:
...     for num in sublist:
...         flat_list.append(num)
...         print(flat_list)
... 
...         
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
>>> import itertools
>>> my_list = [[1], [2,3],[4,5,6,7]]
>>> flat_list = list(itertools.chain(*my_list))
>>> print(flat_list)
[1, 2, 3, 4, 5, 6, 7]
>>> 
>>> 
>>> my_list = [[1],[2,3],[4,5,6,7]]
>>> flat_list = sum(my_list, [])
>>> print(flat_list)
[1, 2, 3, 4, 5, 6, 7]
>>> 
>>> 
>>> from functools import reduce
>>> my_list = [[1], [2,3], [4,5,6,7]]
>>> print(reduce(lambda x, y: x+y, my_list))
[1, 2, 3, 4, 5, 6, 7]
>>> 
>>> 
