Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> date = datetime.date(1977, 5, 8)
>>> print(date)
1977-05-08
>>> print(date.year)
1977
>>> delta = datetime.timedelta(days=30)
>>> print(date - delta)
1977-04-08
>>> print(date + delta)
1977-06-07
>>> 
>>> 
>>> import math
>>> print(math.exp(0))
1.0
>>> print(math.log(1))
0.0
>>> print(math.factorial(4))
24
>>> print(math.sqrt(100))
10.0
>>> 
>>> import random
>>> print(random.random())
0.06607294993389667
>>> print(random.choice([1,2,3]))
1
>>> print(random.randint(1,10))
9
