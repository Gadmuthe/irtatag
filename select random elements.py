Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> my_list = [1, 'a', 32, 'c','d', 31]
>>> print(random.choice(my_list))
32
>>> 
>>> 
>>> import secrets
>>> my_list = [1, 'a', 32, 'c', 'd', 31]
>>> print(secrets.choice(my_list))
31
