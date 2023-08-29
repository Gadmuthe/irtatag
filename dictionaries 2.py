Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> valid_dict = {'numbers': [1, 2, 3]}
>>> print(valid_dict)
{'numbers': [1, 2, 3]}
>>> 
>>> my_dict = { 'nums': [1, 2, 3],
...             'abc': ['a', 'b', 'c']
...             }
>>> print(my_dict['nums'])
[1, 2, 3]
>>> 
>>> my_dict = {'nums': [1, 2, 3],
...            'abc': ['a', 'b', 'c']
...            }
>>> print(my_dict.values())
dict_values([[1, 2, 3], ['a', 'b', 'c']])
>>> 
>>> my_dict = {'nums': [1, 2, 3],
...            'abc': ['a', 'b', 'c']
...            }
>>> my_dict['floats'] = [1.0, 2.0, 3.0]
>>> print(my_dict)
{'nums': [1, 2, 3], 'abc': ['a', 'b', 'c'], 'floats': [1.0, 2.0, 3.0]}
>>> 
>>> smallest_countries = {'africa': 'seychelles',
...                       'asia': 'maldives',
...                       'europe': 'vatican city',
...                       'oceania': 'nauru',
...                       'north america': 'st. kitts and nevis',
...                       'south america': 'suriname'
...                       }
>>> print('africa' in smallest_countries)
True
>>> print('asia' not in smallest_countries)
False
