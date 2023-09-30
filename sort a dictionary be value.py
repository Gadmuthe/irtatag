Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> dt = {5:4, 1:6, 6:3}
>>> sorted_dt = {key: value for key, value in sorted(dt.items(), key=lambda item: item[1])}
>>> print(sorted_dt)
{6: 3, 5: 4, 1: 6}
>>> 
>>> 
>>> dt = {5:4, 1:6, 6:3}
>>> sorted_dt_value = sorted(dt.values())
>>> print(sorted_dt_value)
[3, 4, 6]
