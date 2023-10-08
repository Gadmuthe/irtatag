Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> index = [1,2,3]
>>> languages = ['python', 'c', 'c++']
>>> dictionary = dict(zip(index, languages))
>>> print(dictionary)
{1: 'python', 2: 'c', 3: 'c++'}
>>> 
>>> 
>>> index = [1,2,3]
>>> languages = ['python', 'c', 'c++']
>>> dictionary = {k: v for k, v in zip(index, languages)}
>>> print(dictionary)
{1: 'python', 2: 'c', 3: 'c++'}
