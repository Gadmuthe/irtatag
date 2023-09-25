Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_list = [12, 65, 54, 39, 102, 339, 221]
>>> result = list(filter(lambda x: (x % 13 == 0), my_list))
>>> print("numbers divisible by 13 are", result)
numbers divisible by 13 are [65, 39, 221]
>>> 
