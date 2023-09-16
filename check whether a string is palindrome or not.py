Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_str = 'aIbohPhoBiA'
>>> my_str = my_str.casefold()
>>> rev_str = reversed(my_str)
>>> if list(my_str) == list(rev_str):
...     print("the string is a palindrome.")
... else:
...     print("the string is not a palindrome.")
... 
...     
the string is a palindrome.
