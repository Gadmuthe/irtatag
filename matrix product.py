Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> test_list = [[1,4,5], [7,3], [4], [46, 7,3]]
>>> print("The original list")
The original list
>>> print(str(test_list))
[[1, 4, 5], [7, 3], [4], [46, 7, 3]]
>>> res = 1
>>> for i in test_list:
...     for j in i:
...         res *= j
... 
...         
>>> print("The total element product in lists is: " + str(res))
The total element product in lists is: 1622880
