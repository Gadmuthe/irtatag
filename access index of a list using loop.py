Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_list = [21, 44, 35, 11]
>>> for index, val in enumerate(my_list):
...     print(index, val)
... 
...     
0 21
1 44
2 35
3 11
>>> 
>>> 
>>> my_list = [21, 44, 35, 11]
>>> for index, val in enumerate(my_list, start = 1):
...     print(index, val)
... 
...     
1 21
2 44
3 35
4 11
>>> 
>>> 
>>> my_list = [21, 44, 35, 11]
>>> for index in range(len(my_list)):
...     value = my_list[index]
...     print(index, value)
... 
...     
0 21
1 44
2 35
3 11
