Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> year = 2023
>>> if (year % 400 == 0) and (year % 100 == 0):
...     print("{0} is a leap year ".format(year))
... elif (year % 4 == 0) and (year % 100 != 0):
...     print("{0} is a leap year". format(year))
... else:
...     print("{0} is not a leap year".format(year))
... 
...     
2023 is not a leap year
