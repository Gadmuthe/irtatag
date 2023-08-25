Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> zoo = {
...     'pen_1': 'penguins',
...     'pen_2': 'zebras',
...     'pen_3': 'lions',
...     }
>>> zoo['pen_2']
'zebras'
>>> zoo['pen_4'] = 'elephants'
>>> zoo
{'pen_1': 'penguins', 'pen_2': 'zebras', 'pen_3': 'lions', 'pen_4': 'elephants'}
>>> print('pen_1' in zoo)
True
>>> print('pen_7' in zoo)
False
