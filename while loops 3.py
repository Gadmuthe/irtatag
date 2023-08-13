Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from time import sleep
>>> mins = 10
>>> while mins >= 0:
...     if mins == 5:
...         print('place your reservation! 5 minutes remaining. ')
...     elif mins == 2:
...         print('don\'t lose your seats! 2 minutes remaining.')
...     elif mins == 0:
...         print('user timed out.')
...     else:
...         print(mins)
...     mins -= 1
...     sleep(1)
... 
...     
10
9
8
7
6
place your reservation! 5 minutes remaining. 
4
3
don't lose your seats! 2 minutes remaining.
1
user timed out.
