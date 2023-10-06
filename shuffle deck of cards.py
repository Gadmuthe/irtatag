Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import itertools, random
>>> deck = list(itertools.product(range(1, 14), ['spade', 'heart', 'diamond', 'club']))
>>> random.shuffle(deck)
>>> print("you got:")
you got:
>>> for i in range(5):
...     print(deck[i][0], "of", deck[i][1])
... 
...     
8 of spade
11 of heart
10 of spade
9 of heart
8 of diamond
