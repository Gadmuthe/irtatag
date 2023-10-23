Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
>>> print("The original tuple : " + str(test_tuple))
The original tuple : ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
>>> res = [{'key': sub[0], 'value': sub[1], 'id': sub[2]}
...        for sub in test_tuple]
>>> print("The converted dictionary :" +str(res))
The converted dictionary :[{'key': 4, 'value': 'Gfg', 'id': 10}, {'key': 3, 'value': 'is', 'id': 8}, {'key': 6, 'value': 'Best', 'id': 10}]
