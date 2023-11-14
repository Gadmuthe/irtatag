Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from itertools import chain
>>> test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]
>>> print("The original list is: "+ str(test_list))
The original list is: [(15, 3), (3, 9), (1, 10), (99, 2)]
>>> temp = map(lambda ele: str(ele), chain.from_iterable(test_list))
>>> res = set()
>>> for sub in temp:
...     for ele in sub:
...         res.add(ele)
... 
...         
>>> print("The extracted digits: "+ str(res))
The extracted digits: {'3', '2', '1', '5', '9', '0'}
>>> 
>>> 
>>> 
>>> import re
>>> test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]
>>> print("The original list is: "+str(test_list))
The original list is: [(15, 3), (3, 9), (1, 10), (99, 2)]
>>> temp = re.sub(r'[\[\]\(\), ]', '', str(test_list))
>>> res = [int(ele) for ele in set(temp)]
>>> print("The extracted digits: "+ str(res))
The extracted digits: [3, 2, 1, 5, 9, 0]
