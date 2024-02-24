Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 300
>>> def myfunc():
...     global x
...     x = 200
... 
...     
>>> myfunc()
>>> print(x)
200
>>> 
>>> 
>>> 
>>> def myfunc():
...     global x
...     x = 300
... 
...     
>>> myfunc()
>>> print(x)
300
>>> 
>>> 
>>> 
>>> x = 300
>>> def myfunc():
...     x = 200
...     print(x)
... 
...     
>>> myfunc()
200
>>> print(x)
300
