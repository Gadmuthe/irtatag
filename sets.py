Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
x = set(('foo', 'bar', 'baz', 'foo'))
>>> print(x)
{'baz', 'foo', 'bar'}
>>> 
>>> x = set('foo')
>>> print(x)
{'f', 'o'}
>>> x = {'foo'}
>>> print(type(x))
<class 'set'>
>>> 
>>> set1 = {1, 2, 3, 4, 5, 6}
>>> set2 = {4, 5, 6, 7, 8, 9}
>>> print(set1.intersection(set2))
{4, 5, 6}
>>> print(set1 & set2)
{4, 5, 6}
>>> 
>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}
>>> print(x1.union(x2))
{'baz', 'foo', 'bar', 'qux', 'quux'}
>>> print(x1 | x2)
{'baz', 'foo', 'bar', 'qux', 'quux'}
>>> 
>>> set1 = {1, 2, 3, 4, 5, 6}
>>> set2 = {4, 5, 6, 7, 8, 9}
>>> print(set1.difference(set2))
{1, 2, 3}
>>> print
<built-in function print>
>>> print(set1 - set2)
{1, 2, 3}
>>> 
>>> set1 = {1, 2, 3, 4, 5, 6}
>>> set2 = {4, 5, 6, 7, 8, 9}
>>> print(set2.symmetric_difference(set1))
{1, 2, 3, 7, 8, 9}
>>> print(set2 ^ set1)
{1, 2, 3, 7, 8, 9}
